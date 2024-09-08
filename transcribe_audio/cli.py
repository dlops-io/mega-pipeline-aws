"""
Module that contains the command line app.
"""
import os
import io
import argparse
import shutil
import ffmpeg
from tempfile import TemporaryDirectory
import boto3
import csv
import time
import speech_recognition as sr
from pydub import AudioSegment

bucket_name = 'megapipeline-s3bucket'
input_audios = "input_audios"
text_prompts = "text_prompts"

def makedirs():
    os.makedirs(input_audios, exist_ok=True)
    os.makedirs(text_prompts, exist_ok=True)

# Path to your CSV file
csv_file_path = os.getenv('AWS_APPLICATION_CREDENTIALS')

# Read the CSV file
with open(csv_file_path, mode='r',  encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    credentials = next(reader)  # Assuming the CSV has only one row of credentials

# Extract the access key and secret key
access_key = credentials['Access key ID']
secret_key = credentials['Secret access key']

def download():
    print("download")

    # Clear
    shutil.rmtree(input_audios, ignore_errors=True, onerror=None)
    makedirs()

    # Create a boto3 session
    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
    )
    s3_client = session.client('s3')

    # List files in the specified folder
    folder_name = 'input_audios/'  # Replace with your folder name in S3
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

def transcribe():
    print("transcribe")
    makedirs()

    # Get the list of audio files
    audio_files = os.listdir(input_audios)
    # Create a boto3 session
    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
    )
    transcribe_client = session.client('transcribe', region_name='us-east-1')

    for audio_path in audio_files:
        uuid = audio_path.replace(".mp3", "")
        audio_path = os.path.join(input_audios, audio_path)
        text_file = os.path.join(text_prompts, uuid + ".txt")

        if os.path.exists(text_file):
            continue

        print("Transcribing:", audio_path)

        r = sr.Recognizer()

        # convert mp3 file to wav                                                       
        audio_file = AudioSegment.from_mp3(audio_path)
        audio_file.export("transcript.wav", format="wav")

        # Use sr.AudioFile for the context manager
        with sr.AudioFile("transcript.wav") as source:
            audio = r.record(source)

        text = r.recognize_google(audio)
        print(text)

        uuid = audio_path.replace(".mp3", "").split("/")[-1]
        # audio_path = os.path.join(input_audios, audio_path.split("/")[-1])
        text_file = os.path.join(text_prompts, uuid + ".txt")
        # Save the transcription
        with open(text_file, "w") as f:
            f.write(text)

def upload():
    print("upload")
    makedirs()

    # Get the list of text file
    text_files = os.listdir(text_prompts)
    print(text_files)

    # Create a boto3 session
    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
    )
    s3_client = session.client('s3')

    folder_name = text_prompts
    for text_file in text_files:
        file_path = os.path.join(text_prompts, text_file)
        object_name = f'{folder_name}/{text_file}'  # The name of the file in the bucket, including the folder

        # Upload the file
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"File {file_path} uploaded to {bucket_name}/{object_name}")

# Generate the inputs arguments parser
parser = argparse.ArgumentParser(description="Command description.")

def main(args=None):
    print("Args:", args)

    if args.download:
        download()
    if args.transcribe:
        transcribe()
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
        help="Download audio files from GCS bucket",
    )

    parser.add_argument(
        "-t", "--transcribe", action="store_true", help="Transcribe audio files to text"
    )

    parser.add_argument(
        "-u",
        "--upload",
        action="store_true",
        help="Upload transcribed text to GCS bucket",
    )

    args = parser.parse_args()

    main(args)

# """
# Module that contains the command line app.
# """
# import os
# import io
# import argparse
# import shutil
# # from google.cloud import storage
# # from google.cloud import speech
# import ffmpeg
# from tempfile import TemporaryDirectory
# import boto3
# import os
# from os import path
# import csv
# import time
# import speech_recognition as sr
# from pydub import AudioSegment



# # bucket_name = 'awsbedrockbucket1' 
# bucket_name = 'mptest3'
# bucket_name = 'megapipeline-s3bucket'
# input_audios = "input_audios"
# text_prompts = "text_prompts"


# def makedirs():
#     os.makedirs(input_audios, exist_ok=True)
#     os.makedirs(text_prompts, exist_ok=True)


# # Path to your CSV file
# # csv_file_path = 'megapipeline-serviceaccount_accessKeys.csv'
# csv_file_path = os.getenv('AWS_APPLICATION_CREDENTIALS')
# print(csv_file_path)

# # Read the CSV file
# with open(csv_file_path, mode='r',  encoding='utf-8-sig') as file:
#     reader = csv.DictReader(file)
#     credentials = next(reader)  # Assuming the CSV has only one row of credentials

# # Extract the access key and secret key
# access_key = credentials['Access key ID']
# secret_key = credentials['Secret access key']


# def download():
#     print("download")

#     # Clear
#     shutil.rmtree(input_audios, ignore_errors=True, onerror=None)
#     makedirs()

#     # Create a boto3 session
#     session = boto3.Session(
#         aws_access_key_id=access_key,
#         aws_secret_access_key=secret_key,
#     )
#     s3_client = session.client('s3')

#     # List files in the specified folder
#     folder_name = 'input_audios/'  # Replace with your folder name in S3
#     response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=folder_name)

#     blobs = []
#     if 'Contents' in response:
#         for obj in response['Contents']:
#             blobs.append(obj['Key'])
#     else:
#         print(f"No files found in folder {folder_name}")
    
    
#     for blob in blobs:
#         if not blob.endswith("/"):
#             # Download the file
#             local_file_path = os.path.join(folder_name, blob.split("/")[-1])
#             s3_client.download_file(bucket_name, blob, local_file_path)
#             print(f"File {blob} downloaded to {local_file_path}")



# def transcribe():
#     print("transcribe")
#     makedirs()

#     # Get the list of audio files
#     audio_files = os.listdir(input_audios)
#     # Create a boto3 session
#     session = boto3.Session(
#         aws_access_key_id=access_key,
#         aws_secret_access_key=secret_key,
#     )
#     transcribe_client = session.client('transcribe', region_name='us-east-1')

#     for audio_path in audio_files:
#         uuid = audio_path.replace(".mp3", "")
#         audio_path = os.path.join(input_audios, audio_path)
#         text_file = os.path.join(text_prompts, uuid + ".txt")

#         if os.path.exists(text_file):
#             continue

#         print("Transcribing:", audio_path)

#         r = sr.Recognizer()

#         # convert mp3 file to wav                                                       
#         audio_file = AudioSegment.from_mp3(audio_path)
#         audio_file.export("transcript.wav", format="wav")

#         # Use sr.AudioFile for the context manager
#         with sr.AudioFile("transcript.wav") as source:
#             audio = r.record(source)

#         text = r.recognize_google(audio)
#         print(text)

#         uuid = audio_path.replace(".mp3", "").split("/")[-1]
#         # audio_path = os.path.join(input_audios, audio_path.split("/")[-1])
#         text_file = os.path.join(text_prompts, uuid + ".txt")
#         # Save the transcription
#         with open(text_file, "w") as f:
#             f.write(text)

# def upload():
#     print("upload")
#     makedirs()


# #     # Get the list of text file
#     text_files = os.listdir(text_prompts)
#     print(text_files)

#     # Create a boto3 session
#     session = boto3.Session(
#         aws_access_key_id=access_key,
#         aws_secret_access_key=secret_key,
#     )
#     s3_client = session.client('s3')

#     folder_name = text_prompts
#     for text_file in text_files:
#         file_path = os.path.join(text_prompts, text_file)
#         object_name = f'{folder_name}/{text_file}'  # The name of the file in the bucket, including the folder

#         # Upload the file
#         s3_client.upload_file(file_path, bucket_name, object_name)
#         print(f"File {file_path} uploaded to {bucket_name}/{object_name}")


# # Generate the inputs arguments parser
# parser = argparse.ArgumentParser(description="Command description.")

# def main(args=None):
#     print("Args:", args)

#     if args.download:
#         download()
#     if args.transcribe:
#         transcribe()
#     if args.upload:
#         upload()



# if __name__ == "__main__":
#     # Generate the inputs arguments parser
#     # if you type into the terminal 'python cli.py --help', it will provide the description
#     parser = argparse.ArgumentParser(description="Transcribe audio file to text")

#     parser.add_argument(
#         "-d",
#         "--download",
#         action="store_true",
#         help="Download audio files from GCS bucket",
#     )

#     parser.add_argument(
#         "-t", "--transcribe", action="store_true", help="Transcribe audio files to text"
#     )

#     parser.add_argument(
#         "-u",
#         "--upload",
#         action="store_true",
#         help="Upload transcribed text to GCS bucket",
#     )

#     args = parser.parse_args()

#     main(args)



# # """
# # Module that contains the command line app.
# # """
# # import os
# # import io
# # import argparse
# # import shutil
# # from google.cloud import storage
# # from google.cloud import speech
# # import ffmpeg
# # from tempfile import TemporaryDirectory

# # # Generate the inputs arguments parser
# # parser = argparse.ArgumentParser(description="Command description.")

# # gcp_project = "ac215-project"
# # bucket_name = "mega-pipeline-bucket"
# # input_audios = "input_audios"
# # text_prompts = "text_prompts"


# # def makedirs():
# #     os.makedirs(input_audios, exist_ok=True)
# #     os.makedirs(text_prompts, exist_ok=True)


# # def download():
# #     print("download")

# #     # Clear
# #     shutil.rmtree(input_audios, ignore_errors=True, onerror=None)
# #     makedirs()

# #     client = storage.Client()
# #     bucket = client.get_bucket(bucket_name)
# #     # bucket = client.bucket(bucket_name)

# #     storage_client = storage.Client(project=gcp_project)
# #     bucket = storage_client.bucket(bucket_name)

# #     blobs = bucket.list_blobs(prefix=input_audios+"/")
# #     for blob in blobs:
# #         print(blob.name)
# #         if not blob.name.endswith("/"):
# #             blob.download_to_filename(blob.name)


# # def transcribe():
# #     print("transcribe")
# #     makedirs()

# #     # Speech client
# #     client = speech.SpeechClient()

# #     # Get the list of audio file
# #     audio_files = os.listdir(input_audios)

# #     for audio_path in audio_files:
# #         uuid = audio_path.replace(".mp3", "")
# #         audio_path = os.path.join(input_audios, audio_path)
# #         text_file = os.path.join(text_prompts, uuid + ".txt")

# #         if os.path.exists(text_file):
# #             continue

# #         print("Transcribing:", audio_path)
# #         with TemporaryDirectory() as audio_dir:
# #             flac_path = os.path.join(audio_dir, "audio.flac")
# #             stream = ffmpeg.input(audio_path)
# #             stream = ffmpeg.output(stream, flac_path)
# #             ffmpeg.run(stream)

# #             with io.open(flac_path, "rb") as audio_file:
# #                 content = audio_file.read()

# #             # Transcribe
# #             audio = speech.RecognitionAudio(content=content)
# #             config = speech.RecognitionConfig(language_code="en-US")
# #             operation = client.long_running_recognize(config=config, audio=audio)
# #             response = operation.result(timeout=90)
# #             print("response:", response)
# #             text = "None"
# #             if len(response.results) > 0:
# #                 text = response.results[0].alternatives[0].transcript
# #                 print(text)

# #             # Save the transcription
# #             with open(text_file, "w") as f:
# #                 f.write(text)


# # def upload():
# #     print("upload")
# #     makedirs()

# #     # Upload to bucket
# #     storage_client = storage.Client()
# #     bucket = storage_client.bucket(bucket_name)

# #     # Get the list of text file
# #     text_files = os.listdir(text_prompts)
# #     print(text_files)

# #     for text_file in text_files:
# #         file_path = os.path.join(text_prompts, text_file)

# #         destination_blob_name = file_path
# #         blob = bucket.blob(destination_blob_name)

# #         blob.upload_from_filename(file_path)


# # def main(args=None):
# #     print("Args:", args)

# #     if args.download:
# #         download()
# #     if args.transcribe:
# #         transcribe()
# #     if args.upload:
# #         upload()


# # if __name__ == "__main__":
# #     # Generate the inputs arguments parser
# #     # if you type into the terminal 'python cli.py --help', it will provide the description
# #     parser = argparse.ArgumentParser(description="Transcribe audio file to text")

# #     parser.add_argument(
# #         "-d",
# #         "--download",
# #         action="store_true",
# #         help="Download audio files from GCS bucket",
# #     )

# #     parser.add_argument(
# #         "-t", "--transcribe", action="store_true", help="Transcribe audio files to text"
# #     )

# #     parser.add_argument(
# #         "-u",
# #         "--upload",
# #         action="store_true",
# #         help="Upload transcribed text to GCS bucket",
# #     )

# #     args = parser.parse_args()

# #     main(args)
