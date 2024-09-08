"""
Module that contains the command line app.
"""
import os
import argparse
import shutil
import boto3
import csv

bucket_name = 'megapipeline-s3bucket'
text_paragraphs = "text_paragraphs"
text_audios = "text_audios"

def makedirs():
    os.makedirs(text_paragraphs, exist_ok=True)
    os.makedirs(text_audios, exist_ok=True)
    
# Path to your CSV file
csv_file_path = os.getenv('AWS_APPLICATION_CREDENTIALS')

# Read the CSV file
with open(csv_file_path, mode='r',  encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    credentials = next(reader)  # Assuming the CSV has only one row of credentials

# Extract the access key and secret key
access_key = credentials['Access key ID']
secret_key = credentials['Secret access key']

# Create a Polly client
#polly_client = boto3.client('polly', region_name='us-east-1')
polly_client = boto3.client(
    'polly',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name='us-east-1'
)

def download():
    print("download")

    # Clear
    shutil.rmtree(text_paragraphs, ignore_errors=True, onerror=None)
    makedirs()
    
    # Create a boto3 session
    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
    )
    s3_client = session.client('s3')

    # List files in the specified folder
    folder_name = 'text_paragraphs/'  # Replace with your folder name in S3
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
            local_file_path = os.path.join(folder_name, blob.split("/")[-1])
            s3_client.download_file(bucket_name, blob, local_file_path)
            print(f"File {blob} downloaded to {local_file_path}")


def synthesis():
    print("synthesis")
    makedirs()

    # Get the list of text file
    text_files = os.listdir(text_paragraphs)
    # Create a boto3 session
    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
    )
    s3_client = session.client('s3')


    for text_file in text_files:
        uuid = text_file.replace(".txt", "")
        file_path = os.path.join(text_paragraphs, text_file)
        audio_file = os.path.join(text_audios, uuid + ".mp3")

        if os.path.exists(audio_file):
            continue

        with open(file_path) as f:
            input_text = f.read()

        # Call the Polly API to synthesize speech
        response = polly_client.synthesize_speech(
            Text=input_text,
            OutputFormat="mp3", 
            VoiceId="Joanna",    # Select the voice you'd like to use (e.g., "Joanna", "Matthew", etc.)
        )

        # Save the audio file
        with open(audio_file, "wb") as out:
            # Write the response to the output file.
            out.write(response["AudioStream"].read())


def upload():
    print("upload")
    makedirs()

    # Create a boto3 session
    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
    )
    s3_client = session.client('s3')

    folder_name = text_audios
    # Get the list of files
    audio_files = os.listdir(text_audios)

    for audio_file in audio_files:
        file_path = os.path.join(text_audios, audio_file)
        object_name = f'{folder_name}/{audio_file}'
        
        # Upload the file
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"File {file_path} uploaded to {bucket_name}/{object_name}")

# Generate the inputs arguments parser
parser = argparse.ArgumentParser(description="Command description.")

def main(args=None):
    print("Args:", args)

    if args.download:
        download()
    if args.synthesis:
        synthesis()
    if args.upload:
        upload()


if __name__ == "__main__":
    # Generate the inputs arguments parser
    # if you type into the terminal 'python cli.py --help', it will provide the description
    parser = argparse.ArgumentParser(description="Synthesis audio from text")

    parser.add_argument(
        "-d",
        "--download",
        action="store_true",
        help="Download paragraph of text from AWS",
    )

    parser.add_argument(
        "-s", "--synthesis", action="store_true", help="Synthesis audio"
    )

    parser.add_argument(
        "-u", "--upload", action="store_true", help="Upload audio file to AWS"
    )

    args = parser.parse_args()

    main(args)
