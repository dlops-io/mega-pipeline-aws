"""
Module that contains the command line app.
"""
import os
import argparse
import shutil
import boto3
import csv
from googletrans import Translator

# Generate the inputs arguments parser
parser = argparse.ArgumentParser(description="Command description.")

bucket_name = 'megapipeline-s3bucket'
text_paragraphs = "text_paragraphs"
text_translated = "text_translated"
group_name = "group-01" # This needs to be your Group name e.g: group-01, group-02, group-03, group-04, group-05, ...

translator = Translator()

# Path to your CSV file
csv_file_path = os.getenv('AWS_APPLICATION_CREDENTIALS')

# Read the CSV file
with open(csv_file_path, mode='r',  encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    credentials = next(reader)  # Assuming the CSV has only one row of credentials

# Extract the access key and secret key
access_key = credentials['Access key ID']
secret_key = credentials['Secret access key']


def makedirs():
    os.makedirs(os.path.join(text_paragraphs, group_name), exist_ok=True)
    os.makedirs(os.path.join(text_translated, group_name), exist_ok=True)


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

    # List files matching the pattern text_paragraphs/{group_name}/input-*.txt
    prefix = f"{text_paragraphs}/{group_name}/"
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


def translate():
    print("translate")
    makedirs()

    # Get the list of text files matching input-*.txt pattern in the group folder
    group_text_dir = os.path.join(text_paragraphs, group_name)
    if os.path.exists(group_text_dir):
        text_files = [f for f in os.listdir(group_text_dir) if f.startswith("input-") and f.endswith(".txt")]
    else:
        text_files = []

    for text_file in text_files:
        uuid = os.path.basename(text_file).replace(".txt", "")
        file_path = os.path.join(text_paragraphs, group_name, text_file)
        translated_file = os.path.join(text_translated, group_name, uuid + ".txt")

        if os.path.exists(translated_file):
            continue

        with open(file_path) as f:
            input_text = f.read()

        results = translator.translate(input_text, src="en", dest="fr")
        print(results.text)

        # Save the translation
        with open(translated_file, "w") as f:
            f.write(results.text)


def upload():
    print("upload")
    makedirs()

    # Create a boto3 session
    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
    )
    s3_client = session.client('s3')

    # Get the list of text files matching input-*.txt pattern in the group folder
    group_translated_dir = os.path.join(text_translated, group_name)
    if os.path.exists(group_translated_dir):
        text_files = [f for f in os.listdir(group_translated_dir) if f.startswith("input-") and f.endswith(".txt")]
    else:
        text_files = []
    print(text_files)

    for text_file in text_files:
        file_path = os.path.join(text_translated, group_name, text_file)
        object_name = f'{text_translated}/{group_name}/{text_file}'

        # Upload the file
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"Uploading: {object_name} from {file_path}")


def main(args=None):
    print("Args:", args)

    if args.download:
        download()
    if args.translate:
        translate()
    if args.upload:
        upload()


if __name__ == "__main__":
    # Generate the inputs arguments parser
    # if you type into the terminal 'python cli.py --help', it will provide the description
    parser = argparse.ArgumentParser(description="Translate English to French")

    parser.add_argument(
        "-d",
        "--download",
        action="store_true",
        help="Download text paragraphs from S3 bucket",
    )

    parser.add_argument("-t", "--translate", action="store_true", help="Translate text")

    parser.add_argument(
        "-u",
        "--upload",
        action="store_true",
        help="Upload translated text to S3 bucket",
    )

    args = parser.parse_args()

    main(args)
