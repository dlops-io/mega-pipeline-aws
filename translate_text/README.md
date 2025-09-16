# Translate Text

🗒️ &rightarrow; 🇫🇷

In this container, you will implement the following:
* Read the text from the S3 bucket and folder `text_paragraphs`
* Use `googletrans` to translate the text from English to French (or any other language)
* Save the translated text as a text file in S3 bucket and folder `text_translated` (use the same file name)

### Project Setup

* Create a folder `translate_text` or clone this repo

### AWS Credentials File
* Create a CSV file with your AWS credentials and save it inside a folder called `secrets` inside `translate_text`
* The CSV file should contain:
```
Access key ID,Secret access key
AKIA...,your-secret-key-here
```
* Set the environment variable `AWS_APPLICATION_CREDENTIALS` to point to this file

### Create pyproject.toml
* Inside the `translate_text` folder create:
* Add `pyproject.toml` with the following contents:
```
[project]
name = "app"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12,<3.13"
dependencies = [
]
```

### Create Dockerfile
* Inside the `translate_text` folder
* Create a `Dockerfile` and base it from `python:3.12-slim-bookworm` the official Debian-hosted Python 3.12 image
* Set the following environment variables:
```
ENV UV_LINK_MODE=copy
ENV UV_PROJECT_ENVIRONMENT=/home/app/.venv
```

* Ensure we have an up-to-date baseline and install dependencies by running
```
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
```

* Install uv
```
RUN pip install --no-cache-dir --upgrade pip && \
    pip install uv
```

* Create a `app` folder by running `mkdir -p /app`
* Set the working directory as `/app`

* Copy source files to the `/app` folder
* Run `uv sync`

* Add Entry point to `/bin/bash`
* Add a command to get into the virtual environment shell `source /home/app/.venv/bin/activate && exec bash`

* Example dockerfile can be found in the main [README](../README.md#sample-dockerfile)

### Docker Build & Run
* Build your docker image and give your image the name `translate_text`

* You should be able to run your docker image by using:
```
docker run --rm -ti -v "$(pwd)":/app translate_text
```

* The `-v "(pwd)":/app` option mounts your current working directory into the `/app` directory inside the container as a volume. This helps us during app development, so when you change a source code file using VSCode from your host machine, the files are automatically changed inside the container.

### Python packages required
* `uv add` the following:
  - `boto3`
  - `googletrans==4.0.0rc1`

Note: This implementation uses the googletrans library, which provides free translation functionality through Google's translation service without requiring additional API keys.

* If you exit your container at this point, in order to get the latest environment from the pyproject.toml file, make sure to re-build your docker image again

### CLI to interact with your code
* Use the given Python file [`cli.py`](cli.py)
* Assign your group-number to the `group_name` variable in `cli.py`
* Update the bucket name to your S3 bucket name
* The CLI should have the following command line argument options
```
python cli.py --help
usage: cli.py [-h] [-d] [-t] [-u]

Translate English to French

optional arguments:
  -h, --help       show this help message and exit
  -d, --download   Download text paragraphs from S3 bucket
  -t, --translate  Translate text
  -u, --upload     Upload translated text to S3 bucket
```

### Testing your code locally
* Inside your docker shell, make sure you run the following commands:
* `python cli.py -d` - Should download all the required data from the S3 bucket
* `python cli.py -t` - Should translate text from English to French and save it locally
* `python cli.py -u` - Should upload the French text to the remote S3 bucket

### OPTIONAL: Push Container to Docker Hub
* Sign up in Docker Hub and create an [Access Token](https://hub.docker.com/settings/security)
* Login to the Hub: `docker login -u <USER NAME> -p <ACCESS TOKEN>`
* Tag the Docker Image: `docker tag translate_text <USER NAME>/translate_text`
* Push to Docker Hub: `docker push <USER NAME>/translate_text`
