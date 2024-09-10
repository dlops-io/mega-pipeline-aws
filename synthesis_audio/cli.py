"""
Module that contains the command line app.
"""
import os
import argparse
import shutil
import json
import csv
import boto3
import requests 
# Generate the inputs arguments parser
parser = argparse.ArgumentParser(description="Command description.")


bucket_name = 'megapipeline-s3bucket'
output_audios = "output_audios_pp"
text_translated = "text_translated"


# Path to your CSV file
csv_file_path = os.getenv('AWS_APPLICATION_CREDENTIALS')

# Read the CSV file
with open(csv_file_path, mode='r',  encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    credentials = next(reader)  # Assuming the CSV has only one row of credentials

# Extract the access key and secret key
access_key = credentials['Access key ID']
secret_key = credentials['Secret access key']

CHUNK_SIZE = 1024

# Pavlos Voice id


VOICE_ID = "TG3keNw5JZvsEiTtWt7t"
#Define the path to the secrets file
secrets_file_path = 'secrets/11lab_api_key.txt'

# Read the file and set the environment variable
with open(secrets_file_path) as f:
    for line in f:
        if 'XI_API_KEY' in line:
            key, value = line.strip().split('=')
            os.environ[key] = value

XI_API_KEY = os.environ['XI_API_KEY']  

def makedirs():
    os.makedirs(output_audios, exist_ok=True)
    os.makedirs(text_translated, exist_ok=True)


def download():
    print("download")

    # Clear
    shutil.rmtree(text_translated, ignore_errors=True, onerror=None)
    makedirs()

    # Create a boto3 session
    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
    )
    s3_client = session.client('s3')

    # List objects in the bucket with the specified prefix
    response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=text_translated + "/")

    for obj in response.get('Contents', []):
        print(obj['Key'])
        if obj['Key'].endswith(".txt"):
            local_file_name = os.path.join(text_translated, os.path.basename(obj['Key']))
            print("local_file_name:", local_file_name)
            s3_client.download_file(bucket_name, obj['Key'], local_file_name)

    

def synthesis():
    print("synthesis")
    makedirs()

    language_code = "es-ES" #"fr-FR"

    # Get the list of text file
    text_files = os.listdir(text_translated)

    for text_file in text_files:
        uuid = text_file.replace(".txt", "")
        print("uuid:", uuid)
        file_path = os.path.join(text_translated, text_file)
        audio_file = os.path.join(output_audios, uuid + ".mp3")
    
        if os.path.exists(audio_file):
            continue
        
        with open(file_path) as f:
            TEXT_TO_SPEAK = f.read()
    
        OUTPUT_PATH = audio_file
    
        # Construct the URL for the Text-to-Speech API request
        tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream"
    
        # Set up headers for the API request, including the API key for authentication
        headers = {
            "Accept": "application/json",
            "xi-api-key": XI_API_KEY
        }
    
        # Set up the data payload for the API request, including the text and voice settings
        data = {
            "text": TEXT_TO_SPEAK,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.8,
                "style": 0.0,
                "use_speaker_boost": True
            }
        }
    
        # Make the POST request to the TTS API with headers and data, enabling streaming response
        response = requests.post(tts_url, headers=headers, json=data, stream=True)
    
        # Check if the request was successful
        if response.ok:
            # Open the output file in write-binary mode
            with open(OUTPUT_PATH, "wb") as f:
                # Read the response in chunks and write to the file
                for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                    f.write(chunk)
            # Inform the user of success
            print("Audio stream saved successfully.")
        else:
            # Print the error message if the request was not successful
            print(response.text)

def upload():
    ## reads from output_audios_pp folder and uploads to s3 bucket output_audios folder
    print("upload")
    makedirs()

    # Create a boto3 session
    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
    )
    s3_client = session.client('s3')

    # Get the list of files
    audio_files = os.listdir(output_audios)

    for audio_file in audio_files:
        file_path = os.path.join(output_audios, audio_file)

        # The key is the path in the S3 bucket where the file will be stored
        s3_key = os.path.join("output_audios", audio_file)

        print("s3_key:", s3_key)
        print("file_path:", file_path)

        # Upload the file
        s3_client.upload_file(file_path, bucket_name, s3_key)

    print("Upload completed.")
    


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
    parser = argparse.ArgumentParser(description="Transcribe audio file to text")

    parser.add_argument(
        "-d",
        "--download",
        action="store_true",
        help="Download translated text from GCS bucket",
    )

    parser.add_argument(
        "-s", "--synthesis", action="store_true", help="Synthesis audio"
    )

    parser.add_argument(
        "-u", "--upload", action="store_true", help="Upload audio file to GCS bucket"
    )

    args = parser.parse_args()

    main(args)

