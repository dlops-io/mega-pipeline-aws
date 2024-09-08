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
text_prompts = "text_prompts"
text_paragraphs = "text_paragraphs"


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
    os.makedirs(text_paragraphs, exist_ok=True)
    os.makedirs(text_prompts, exist_ok=True)


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

    # List files in the specified folder
    folder_name = 'text_prompts/'  # Replace with your folder name in S3
    response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=folder_name)

    blobs = []
    if 'Contents' in response:
        for obj in response['Contents']:
            blobs.append(obj['Key'])
    else:
        print(f"No files found in folder {folder_name}")
    
    for blob in blobs:
        if not blob.endswith("/"):
            # Download the file

            if blob.endswith(".txt"):
                local_file_path = os.path.join(folder_name, blob.split("/")[-1])
                s3_client.download_file(bucket_name, blob, local_file_path)
                print(f"File {blob} downloaded to {local_file_path}")


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

    # Get the list of text file
    text_files = os.listdir(text_prompts)

    # Get the list of text file
    text_files = os.listdir(text_prompts)

    for text_file in text_files:
        uuid = text_file.replace(".txt", "")
        file_path = os.path.join(text_prompts, text_file)
        paragraph_file = os.path.join(text_paragraphs, uuid + ".txt")

        if os.path.exists(paragraph_file):
            continue

        with open(file_path) as f:
            input_text = f.read()

        # Generate output
        input_prompt = f"""
            Create a transcript for the podcast about cheese with 1000 or more words.
            Use the below text as a starting point for the cheese podcast.
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

    # Get the list of text file
    text_files = os.listdir(text_paragraphs)
    print(text_files)

    # Create a boto3 session
    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
    )
    s3_client = session.client('s3')

    folder_name = text_paragraphs
    for text_file in text_files:
        file_path = os.path.join(text_paragraphs, text_file)
        object_name = f'{folder_name}/{text_file}'  # The name of the file in the bucket, including the folder

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
        help="Download text prompts from GCS bucket",
    )

    parser.add_argument(
        "-g", "--generate", action="store_true", help="Generate a text paragraph"
    )

    parser.add_argument(
        "-u",
        "--upload",
        action="store_true",
        help="Upload paragraph text to GCS bucket",
    )

    args = parser.parse_args()

    main(args)
