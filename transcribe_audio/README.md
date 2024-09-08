
# Transcribe Audio

🎙️ &rightarrow; 📝 

In this container you will implement the following:
* Read audio files from the S3 bucket `megapipeline-s3bucket` and folder `input_audios`
* Use the SpeechRecognition API for transcribing text
* Save the transcribed text as text file in bucket `megapipeline-s3bucket` and folder `text_prompts` (use the same file name and change extension to .txt)


### Project Setup

* Create a folder `transcribe_audio` or clone this repo

### AWS Credentials File
* Download the `megapipeline-serviceaccount_accessKeys.csv` and save it inside a folder called `secrets` inside `transcribe_audio`
<a href="Todo on Ed" download>megapipeline-serviceaccount_accessKeys.csv</a>

### Create Pipfile & Pipfile.lock files
* Inside the `transcribe_audio` folder create:
* Add `Pipfile` with a the following contents:
```
[[source]]
name = "pypi"
url = "https://pypi.org/simple"
verify_ssl = true

[dev-packages]

[packages]
boto3 = "1.35.10"
ffmpeg-python = "*"
SpeechRecognition = "3.10.4"
pydub = "0.25.1"

[requires]
python_version = "3.11"

```

* Add `Pipfile.lock` with a the following contents:
```
{
    "_meta": {
        "hash": {
            "sha256": "f6a33581e70900918858e719431ac947d0d301634cee97346cfc9d1d9c123609"
        },
        "pipfile-spec": 6,
        "requires": {
            "python_version": "3.11"
        },
        "sources": [
            {
                "name": "pypi",
                "url": "https://pypi.org/simple",
                "verify_ssl": true
            }
        ]
    },
    "default": {
        "boto3": {
            "hashes": [
                "sha256:189ab1e2b4cd86df56f82438d89b4040eb140c92683f1bda7cb2e62624f20ea5",
                "sha256:add26dd58e076dfd387013da4704716d5cff215cf14f6d4347c4b9b7fc1f0b8e"
            ],
            "index": "pypi",
            "markers": "python_version >= '3.8'",
            "version": "==1.35.10"
        },
        "botocore": {
            "hashes": [
                "sha256:e9b647b6cf1f63fd701c27433802d1c4342838a37fd152b40fe53b967fd19af4",
                "sha256:f5f671f8f9566f28bed496017ea94d275ca5c253e9e4f91cd56cb7a293e37d0c"
            ],
            "markers": "python_version >= '3.8'",
            "version": "==1.35.11"
        },
        "certifi": {
            "hashes": [
                "sha256:922820b53db7a7257ffbda3f597266d435245903d80737e34f8a45ff3e3230d8",
                "sha256:bec941d2aa8195e248a60b31ff9f0558284cf01a52591ceda73ea9afffd69fd9"
            ],
            "markers": "python_version >= '3.6'",
            "version": "==2024.8.30"
        },
        "charset-normalizer": {
            "hashes": [
                "sha256:06435b539f889b1f6f4ac1758871aae42dc3a8c0e24ac9e60c2384973ad73027",
                "sha256:06a81e93cd441c56a9b65d8e1d043daeb97a3d0856d177d5c90ba85acb3db087",
                "sha256:0a55554a2fa0d408816b3b5cedf0045f4b8e1a6065aec45849de2d6f3f8e9786",
                "sha256:0b2b64d2bb6d3fb9112bafa732def486049e63de9618b5843bcdd081d8144cd8",
                "sha256:10955842570876604d404661fbccbc9c7e684caf432c09c715ec38fbae45ae09",
                "sha256:122c7fa62b130ed55f8f285bfd56d5f4b4a5b503609d181f9ad85e55c89f4185",
                "sha256:1ceae2f17a9c33cb48e3263960dc5fc8005351ee19db217e9b1bb15d28c02574",
                "sha256:1d3193f4a680c64b4b6a9115943538edb896edc190f0b222e73761716519268e",
                "sha256:1f79682fbe303db92bc2b1136016a38a42e835d932bab5b3b1bfcfbf0640e519",
                "sha256:2127566c664442652f024c837091890cb1942c30937add288223dc895793f898",
                "sha256:22afcb9f253dac0696b5a4be4a1c0f8762f8239e21b99680099abd9b2b1b2269",
                "sha256:25baf083bf6f6b341f4121c2f3c548875ee6f5339300e08be3f2b2ba1721cdd3",
                "sha256:2e81c7b9c8979ce92ed306c249d46894776a909505d8f5a4ba55b14206e3222f",
                "sha256:3287761bc4ee9e33561a7e058c72ac0938c4f57fe49a09eae428fd88aafe7bb6",
                "sha256:34d1c8da1e78d2e001f363791c98a272bb734000fcef47a491c1e3b0505657a8",
                "sha256:37e55c8e51c236f95b033f6fb391d7d7970ba5fe7ff453dad675e88cf303377a",
                "sha256:3d47fa203a7bd9c5b6cee4736ee84ca03b8ef23193c0d1ca99b5089f72645c73",
                "sha256:3e4d1f6587322d2788836a99c69062fbb091331ec940e02d12d179c1d53e25fc",
                "sha256:42cb296636fcc8b0644486d15c12376cb9fa75443e00fb25de0b8602e64c1714",
                "sha256:45485e01ff4d3630ec0d9617310448a8702f70e9c01906b0d0118bdf9d124cf2",
                "sha256:4a78b2b446bd7c934f5dcedc588903fb2f5eec172f3d29e52a9096a43722adfc",
                "sha256:4ab2fe47fae9e0f9dee8c04187ce5d09f48eabe611be8259444906793ab7cbce",
                "sha256:4d0d1650369165a14e14e1e47b372cfcb31d6ab44e6e33cb2d4e57265290044d",
                "sha256:549a3a73da901d5bc3ce8d24e0600d1fa85524c10287f6004fbab87672bf3e1e",
                "sha256:55086ee1064215781fff39a1af09518bc9255b50d6333f2e4c74ca09fac6a8f6",
                "sha256:572c3763a264ba47b3cf708a44ce965d98555f618ca42c926a9c1616d8f34269",
                "sha256:573f6eac48f4769d667c4442081b1794f52919e7edada77495aaed9236d13a96",
                "sha256:5b4c145409bef602a690e7cfad0a15a55c13320ff7a3ad7ca59c13bb8ba4d45d",
                "sha256:6463effa3186ea09411d50efc7d85360b38d5f09b870c48e4600f63af490e56a",
                "sha256:65f6f63034100ead094b8744b3b97965785388f308a64cf8d7c34f2f2e5be0c4",
                "sha256:663946639d296df6a2bb2aa51b60a2454ca1cb29835324c640dafb5ff2131a77",
                "sha256:6897af51655e3691ff853668779c7bad41579facacf5fd7253b0133308cf000d",
                "sha256:68d1f8a9e9e37c1223b656399be5d6b448dea850bed7d0f87a8311f1ff3dabb0",
                "sha256:6ac7ffc7ad6d040517be39eb591cac5ff87416c2537df6ba3cba3bae290c0fed",
                "sha256:6b3251890fff30ee142c44144871185dbe13b11bab478a88887a639655be1068",
                "sha256:6c4caeef8fa63d06bd437cd4bdcf3ffefe6738fb1b25951440d80dc7df8c03ac",
                "sha256:6ef1d82a3af9d3eecdba2321dc1b3c238245d890843e040e41e470ffa64c3e25",
                "sha256:753f10e867343b4511128c6ed8c82f7bec3bd026875576dfd88483c5c73b2fd8",
                "sha256:7cd13a2e3ddeed6913a65e66e94b51d80a041145a026c27e6bb76c31a853c6ab",
                "sha256:7ed9e526742851e8d5cc9e6cf41427dfc6068d4f5a3bb03659444b4cabf6bc26",
                "sha256:7f04c839ed0b6b98b1a7501a002144b76c18fb1c1850c8b98d458ac269e26ed2",
                "sha256:802fe99cca7457642125a8a88a084cef28ff0cf9407060f7b93dca5aa25480db",
                "sha256:80402cd6ee291dcb72644d6eac93785fe2c8b9cb30893c1af5b8fdd753b9d40f",
                "sha256:8465322196c8b4d7ab6d1e049e4c5cb460d0394da4a27d23cc242fbf0034b6b5",
                "sha256:86216b5cee4b06df986d214f664305142d9c76df9b6512be2738aa72a2048f99",
                "sha256:87d1351268731db79e0f8e745d92493ee2841c974128ef629dc518b937d9194c",
                "sha256:8bdb58ff7ba23002a4c5808d608e4e6c687175724f54a5dade5fa8c67b604e4d",
                "sha256:8c622a5fe39a48f78944a87d4fb8a53ee07344641b0562c540d840748571b811",
                "sha256:8d756e44e94489e49571086ef83b2bb8ce311e730092d2c34ca8f7d925cb20aa",
                "sha256:8f4a014bc36d3c57402e2977dada34f9c12300af536839dc38c0beab8878f38a",
                "sha256:9063e24fdb1e498ab71cb7419e24622516c4a04476b17a2dab57e8baa30d6e03",
                "sha256:90d558489962fd4918143277a773316e56c72da56ec7aa3dc3dbbe20fdfed15b",
                "sha256:923c0c831b7cfcb071580d3f46c4baf50f174be571576556269530f4bbd79d04",
                "sha256:95f2a5796329323b8f0512e09dbb7a1860c46a39da62ecb2324f116fa8fdc85c",
                "sha256:96b02a3dc4381e5494fad39be677abcb5e6634bf7b4fa83a6dd3112607547001",
                "sha256:9f96df6923e21816da7e0ad3fd47dd8f94b2a5ce594e00677c0013018b813458",
                "sha256:a10af20b82360ab00827f916a6058451b723b4e65030c5a18577c8b2de5b3389",
                "sha256:a50aebfa173e157099939b17f18600f72f84eed3049e743b68ad15bd69b6bf99",
                "sha256:a981a536974bbc7a512cf44ed14938cf01030a99e9b3a06dd59578882f06f985",
                "sha256:a9a8e9031d613fd2009c182b69c7b2c1ef8239a0efb1df3f7c8da66d5dd3d537",
                "sha256:ae5f4161f18c61806f411a13b0310bea87f987c7d2ecdbdaad0e94eb2e404238",
                "sha256:aed38f6e4fb3f5d6bf81bfa990a07806be9d83cf7bacef998ab1a9bd660a581f",
                "sha256:b01b88d45a6fcb69667cd6d2f7a9aeb4bf53760d7fc536bf679ec94fe9f3ff3d",
                "sha256:b261ccdec7821281dade748d088bb6e9b69e6d15b30652b74cbbac25e280b796",
                "sha256:b2b0a0c0517616b6869869f8c581d4eb2dd83a4d79e0ebcb7d373ef9956aeb0a",
                "sha256:b4a23f61ce87adf89be746c8a8974fe1c823c891d8f86eb218bb957c924bb143",
                "sha256:bd8f7df7d12c2db9fab40bdd87a7c09b1530128315d047a086fa3ae3435cb3a8",
                "sha256:beb58fe5cdb101e3a055192ac291b7a21e3b7ef4f67fa1d74e331a7f2124341c",
                "sha256:c002b4ffc0be611f0d9da932eb0f704fe2602a9a949d1f738e4c34c75b0863d5",
                "sha256:c083af607d2515612056a31f0a8d9e0fcb5876b7bfc0abad3ecd275bc4ebc2d5",
                "sha256:c180f51afb394e165eafe4ac2936a14bee3eb10debc9d9e4db8958fe36afe711",
                "sha256:c235ebd9baae02f1b77bcea61bce332cb4331dc3617d254df3323aa01ab47bd4",
                "sha256:cd70574b12bb8a4d2aaa0094515df2463cb429d8536cfb6c7ce983246983e5a6",
                "sha256:d0eccceffcb53201b5bfebb52600a5fb483a20b61da9dbc885f8b103cbe7598c",
                "sha256:d965bba47ddeec8cd560687584e88cf699fd28f192ceb452d1d7ee807c5597b7",
                "sha256:db364eca23f876da6f9e16c9da0df51aa4f104a972735574842618b8c6d999d4",
                "sha256:ddbb2551d7e0102e7252db79ba445cdab71b26640817ab1e3e3648dad515003b",
                "sha256:deb6be0ac38ece9ba87dea880e438f25ca3eddfac8b002a2ec3d9183a454e8ae",
                "sha256:e06ed3eb3218bc64786f7db41917d4e686cc4856944f53d5bdf83a6884432e12",
                "sha256:e27ad930a842b4c5eb8ac0016b0a54f5aebbe679340c26101df33424142c143c",
                "sha256:e537484df0d8f426ce2afb2d0f8e1c3d0b114b83f8850e5f2fbea0e797bd82ae",
                "sha256:eb00ed941194665c332bf8e078baf037d6c35d7c4f3102ea2d4f16ca94a26dc8",
                "sha256:eb6904c354526e758fda7167b33005998fb68c46fbc10e013ca97f21ca5c8887",
                "sha256:eb8821e09e916165e160797a6c17edda0679379a4be5c716c260e836e122f54b",
                "sha256:efcb3f6676480691518c177e3b465bcddf57cea040302f9f4e6e191af91174d4",
                "sha256:f27273b60488abe721a075bcca6d7f3964f9f6f067c8c4c605743023d7d3944f",
                "sha256:f30c3cb33b24454a82faecaf01b19c18562b1e89558fb6c56de4d9118a032fd5",
                "sha256:fb69256e180cb6c8a894fee62b3afebae785babc1ee98b81cdf68bbca1987f33",
                "sha256:fd1abc0d89e30cc4e02e4064dc67fcc51bd941eb395c502aac3ec19fab46b519",
                "sha256:ff8fa367d09b717b2a17a052544193ad76cd49979c805768879cb63d9ca50561"
            ],
            "markers": "python_full_version >= '3.7.0'",
            "version": "==3.3.2"
        },
        "ffmpeg-python": {
            "hashes": [
                "sha256:65225db34627c578ef0e11c8b1eb528bb35e024752f6f10b78c011f6f64c4127",
                "sha256:ac441a0404e053f8b6a1113a77c0f452f1cfc62f6344a769475ffdc0f56c23c5"
            ],
            "index": "pypi",
            "version": "==0.2.0"
        },
        "future": {
            "hashes": [
                "sha256:929292d34f5872e70396626ef385ec22355a1fae8ad29e1a734c3e43f9fbc216",
                "sha256:bd2968309307861edae1458a4f8a4f3598c03be43b97521076aebf5d94c07b05"
            ],
            "markers": "python_version >= '2.6' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "version": "==1.0.0"
        },
        "idna": {
            "hashes": [
                "sha256:050b4e5baadcd44d760cedbd2b8e639f2ff89bbc7a5730fcc662954303377aac",
                "sha256:d838c2c0ed6fced7693d5e8ab8e734d5f8fda53a039c0164afb0b82e771e3603"
            ],
            "markers": "python_version >= '3.6'",
            "version": "==3.8"
        },
        "jmespath": {
            "hashes": [
                "sha256:02e2e4cc71b5bcab88332eebf907519190dd9e6e82107fa7f83b1003a6252980",
                "sha256:90261b206d6defd58fdd5e85f478bf633a2901798906be2ad389150c5c60edbe"
            ],
            "markers": "python_version >= '3.7'",
            "version": "==1.0.1"
        },
        "pydub": {
            "hashes": [
                "sha256:65617e33033874b59d87db603aa1ed450633288aefead953b30bded59cb599a6",
                "sha256:980a33ce9949cab2a569606b65674d748ecbca4f0796887fd6f46173a7b0d30f"
            ],
            "index": "pypi",
            "version": "==0.25.1"
        },
        "python-dateutil": {
            "hashes": [
                "sha256:37dd54208da7e1cd875388217d5e00ebd4179249f90fb72437e91a35459a0ad3",
                "sha256:a8b2bc7bffae282281c8140a97d3aa9c14da0b136dfe83f850eea9a5f7470427"
            ],
            "markers": "python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "version": "==2.9.0.post0"
        },
        "requests": {
            "hashes": [
                "sha256:55365417734eb18255590a9ff9eb97e9e1da868d4ccd6402399eaf68af20a760",
                "sha256:70761cfe03c773ceb22aa2f671b4757976145175cdfca038c02654d061d6dcc6"
            ],
            "markers": "python_version >= '3.8'",
            "version": "==2.32.3"
        },
        "s3transfer": {
            "hashes": [
                "sha256:0711534e9356d3cc692fdde846b4a1e4b0cb6519971860796e6bc4c7aea00ef6",
                "sha256:eca1c20de70a39daee580aef4986996620f365c4e0fda6a86100231d62f1bf69"
            ],
            "markers": "python_version >= '3.8'",
            "version": "==0.10.2"
        },
        "six": {
            "hashes": [
                "sha256:1e61c37477a1626458e36f7b1d82aa5c9b094fa4802892072e49de9c60c4c926",
                "sha256:8abb2f1d86890a2dfb989f9a77cfcfd3e47c2a354b01111771326f8aa26e0254"
            ],
            "markers": "python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
            "version": "==1.16.0"
        },
        "speechrecognition": {
            "hashes": [
                "sha256:723b8155692a8ed11a30013f15f89a3e57c5dc8bc73c8cb024bf9bd14c21fba5",
                "sha256:986bafcf61f14625c2f3cea6a471838edd379ed68aeed7b8f3c0fb41e21f1125"
            ],
            "index": "pypi",
            "markers": "python_version >= '3.8'",
            "version": "==3.10.4"
        },
        "typing-extensions": {
            "hashes": [
                "sha256:04e5ca0351e0f3f85c6853954072df659d0d13fac324d0072316b67d7794700d",
                "sha256:1a7ead55c7e559dd4dee8856e3a88b41225abfe1ce8df57b7c13915fe121ffb8"
            ],
            "markers": "python_version >= '3.8'",
            "version": "==4.12.2"
        },
        "urllib3": {
            "hashes": [
                "sha256:a448b2f64d686155468037e1ace9f2d2199776e17f0a46610480d311f73e3472",
                "sha256:dd505485549a7a552833da5e6063639d0d177c04f23bc3864e41e5dc5f612168"
            ],
            "markers": "python_version >= '3.10'",
            "version": "==2.2.2"
        }
    },
    "develop": {}
}
```

### Create Dockerfile
* Inside the `transcribe_audio` folder
* Create a `Dockerfile` and base it from `python:3.11-slim-buster` the official Debian-hosted Python 3.11 image
* Set the following environment variables:
```
ENV PYENV_SHELL=/bin/bash

```

* Ensure we have an up to date baseline, install dependencies by running
```
apt-get update
apt-get upgrade -y
apt-get install -y --no-install-recommends build-essential ffmpeg flac
```

* Install pipenv
```
pip install --no-cache-dir --upgrade pip
pip install pipenv
```

* Create a `app` folder by running `mkdir -p /app`

* Set the working directory as `/app`
* Add `Pipfile`, `Pipfile.lock` to the `/app/` folder
* Run `pipenv sync`

* Add the rest of your files to the `/app` folder
* Add Entry point to `/bin/bash`
* Add a command to get into the `pipenv shell`

* Example dockerfile can be found [here](https://github.com/dlops-io/mega-pipeline#sample-dockerfile) ## TODO

### Docker Build & Run
* Build your docker image and give your image the name `transcribe_audio`

* You should be able to run your docker image by using:
```
docker run --rm -ti -v "$(pwd)":/app transcribe_audio
```

* The `-v "(pwd)":/app` option is to mount your current working directory into the `/app` directory inside the container as a volume. This helps us during development of the app so when you change a source code file using VSCode from your host machine the files are automatically changed inside the container.

### Python packages required
* `pipenv install` the following:
  - `boto3`
  - `SpeechRecognition`
  - `pydub`
  - `ffmpeg-python`

* If you exit your container at this point, in order to get the latest environment from the pipenv file. Make sure to re-build your docker image again

### CLI to interact with your code
* Use the given python file [`cli.py`](https://github.com/dlops-io/mega-pipeline-aws/blob/main/transcribe_audio/cli.py)
* The CLI should have the following command line argument options
```
python cli.py --help
usage: cli.py [-h] [-d] [-t] [-u]

Transcribe audio file to text

optional arguments:
  -h, --help        show this help message and exit
  -d, --download    Download audio files from GCS bucket
  -t, --transcribe  Transcribe audio files to text
  -u, --upload      Upload transcribed text to GCS bucket
```

### Testing your code locally
* Inside your docker shell make sure you run the following commands:
* `python cli.py -d` - Should download all the required data from S3 bucket
* `python cli.py -t` - Should transcribe audio to text and save it locally
* `python cli.py -u` - Should upload the transcribed text to the remote S3 bucket
* Verify that your uploaded data shows up in the [Mega Pipeline App](https://ai5-mega-pipeline.dlops.io/) TODO

### OPTIONAL: Push Container to Docker Hub
* Sign up in Docker Hub and create an [Access Token](https://hub.docker.com/settings/security)
* Login to the Hub: `docker login -u <USER NAME> -p <ACCESS TOKEN>`
* Tag the Docker Image: `docker tag transcribe_audio <USER NAME>/transcribe_audio`
* Push to Docker Hub: `docker push <USER NAME>/transcribe_audio`
