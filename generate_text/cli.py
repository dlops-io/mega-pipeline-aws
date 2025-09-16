"""
Module that contains the command line app.
"""
# to run local no docker
# export AWS_APPLICATION_CREDENTIALS=secrets/megapipeline-serviceaccount_accessKeys.csv ; export OPENAI_API_KEY_FILE=secrets/openaikey.json; python cli.py

import os
import io
import argparse
import shutil
import boto3
import csv
import json
from openai import OpenAI
import numpy as np

# Generate the inputs arguments parser
parser = argparse.ArgumentParser(description="Command description.")

bucket_name = 'megapipeline-s3bucket'
text_prompts = "text_prompts"  # THIS IS THE TRANSCRIBED TEXT 
text_paragraphs = "text_paragraphs" # THIS IS THE LLM GENERATED TEXT
group_name = "group-01" # This needs to be your Group name e.g: group-01, group-02, group-03, group-04, group-05, ...


# Path to your CSV file
csv_file_path = os.getenv('AWS_APPLICATION_CREDENTIALS')

# Read the CSV file
with open(csv_file_path, mode='r',  encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    credentials = next(reader)  # Assuming the CSV has only one row of credentials

# Extract the access key and secret key
access_key = credentials['Access key ID']
secret_key = credentials['Secret access key']


openai_key_file = os.environ.get('OPENAI_API_KEY_FILE')
with open(openai_key_file, 'r') as f:
    openai_key = json.load(f)['OPENAI_API_TOKEN']


def makedirs():
    os.makedirs(os.path.join(text_paragraphs, group_name), exist_ok=True)
    os.makedirs(os.path.join(text_prompts, group_name), exist_ok=True)


def download():
    print("download")

    # Clear
    shutil.rmtree(text_prompts, ignore_errors=True, onerror=None)
    makedirs()

    # Create a boto3 session
    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
    )
    s3_client = session.client('s3')

    # List files matching the pattern text_prompts/{group_name}/input-*.txt
    prefix = f"{text_prompts}/{group_name}/"
    response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

    if 'Contents' in response:
        for obj in response['Contents']:
            if obj['Key'].endswith('.txt') and 'input-' in obj['Key']:
                # Create local directory structure
                local_file_path = obj['Key']
                os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
                s3_client.download_file(bucket_name, obj['Key'], local_file_path)
                print(f"File {obj['Key']} downloaded to {local_file_path}")
    else:
        print(f"No files found matching pattern {prefix}input-*.txt")


def genResponse(text, system_message="You are a helpful assistant."):
    openai_client = OpenAI(api_key=openai_key)

    response = openai_client.chat.completions.create( #openai.chat.completions.create( #openai.Completion.create(
        model= "gpt-3.5-turbo",   #"gpt-4-1106-preview", #"gpt-4-0314",  
        messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": text}
            ],
        temperature=np.random.choice([0.9,0.95,0.85,0.87,0.92,0.97]),
        max_tokens=700,
        top_p=1,
        frequency_penalty=1.1,
        presence_penalty=1,
        n = 1
    )
    return response.choices[0].message.content

def generate():
    print("generate")
    makedirs()

    # Get the list of text files matching input-*.txt pattern in the group folder
    group_text_dir = os.path.join(text_prompts, group_name)
    if os.path.exists(group_text_dir):
        text_files = [f for f in os.listdir(group_text_dir) if f.startswith("input-") and f.endswith(".txt")]
    else:
        text_files = []

    for text_file in text_files:
        uuid = os.path.basename(text_file).replace(".txt", "")
        file_path = os.path.join(text_prompts, group_name, text_file)
        paragraph_file = os.path.join(text_paragraphs, group_name, uuid + ".txt")

        if os.path.exists(paragraph_file):
            continue

        with open(file_path) as f:
            input_text = f.read()

        # Generate output
        input_prompt = f"""
            Create a transcript for the podcast about cheese with 1000 or more words.
            Use the below text as a starting point for the cheese podcast.
            Output the transcript as paragraphs and not with who is talking or any "Sound" or any other extra information.
            Do not highlight or make words bold.
            The host's name is Pavlos Protopapas.
            {input_text}
        """
        print(input_prompt,"\n\n\n")
        
        paragraph = genResponse(input_prompt)
        
        print("Generated text:")
        print(paragraph)

        # Save the transcription
        with open(paragraph_file, "w") as f:
            f.write(paragraph)


def upload():
    print("upload")
    makedirs()

    # Get the list of text files matching input-*.txt pattern in the group folder
    group_paragraphs_dir = os.path.join(text_paragraphs, group_name)
    if os.path.exists(group_paragraphs_dir):
        text_files = [f for f in os.listdir(group_paragraphs_dir) if f.startswith("input-") and f.endswith(".txt")]
    else:
        text_files = []
    print(text_files)

    # Create a boto3 session
    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
    )
    s3_client = session.client('s3')

    for text_file in text_files:
        file_path = os.path.join(text_paragraphs, group_name, text_file)
        object_name = f'{text_paragraphs}/{group_name}/{text_file}'

        # Upload the file
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"File {file_path} uploaded to {bucket_name}/{object_name}")


    # # Upload to bucket
    # storage_client = storage.Client()
    # bucket = storage_client.bucket(bucket_name)

    # # Get the list of text file
    # text_files = os.listdir(text_paragraphs)

    # for text_file in text_files:
    #     file_path = os.path.join(text_paragraphs, text_file)

    #     destination_blob_name = file_path
    #     blob = bucket.blob(destination_blob_name)

    #     blob.upload_from_filename(file_path)



def main(args=None):
    print("Args:", args)

    if args.download:
        download()
    if args.generate:
        generate()
    if args.upload:
        upload()



if __name__ == "__main__":
    # Generate the inputs arguments parser
    # if you type into the terminal 'python cli.py --help', it will provide the description
    parser = argparse.ArgumentParser(description="Generate text from prompt")

    parser.add_argument(
        "-d",
        "--download",
        action="store_true",
        help="Download text prompts from S3 bucket",
    )

    parser.add_argument(
        "-g", "--generate", action="store_true", help="Generate a text paragraph"
    )

    parser.add_argument(
        "-u",
        "--upload",
        action="store_true",
        help="Upload paragraph text to S3 bucket",
    )

    args = parser.parse_args()

    main(args)
