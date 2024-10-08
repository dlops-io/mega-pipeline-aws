# Synthesis Audio

🗒️  &rightarrow; 🔊

In this container you will implement the following:
* Read the paragraphs of text from the S3 bucket `megapipeline-s3bucket` and folder `text_paragraphs`
* Use Cloud Text-to-Speech API to generate an audio file in English
* Save the audio mp3 file in bucket `megapipeline-s3bucket` and folder `text_audios` (use the same file name and change extension to .mp3)


### Project Setup

* Create a folder `synthesis_audio_en` or clone this repo

### AWS Credentials File
* Download the `megapipeline-serviceaccount_accessKeys.csv` and save it inside a folder called `secrets` inside  `synthesis_audio_en`
<a href="Todo on Ed" download>megapipeline-serviceaccount_accessKeys.csv</a>

### Create Pipfile & Pipfile.lock files
* Add `Pipfile` with a the following contents:
```
[[source]]
name = "pypi"
url = "https://pypi.org/simple"
verify_ssl = true

[dev-packages]

[packages]
boto3 = "1.35.10"

[requires]
python_version = "3.11"

```

* Add `Pipfile.lock` with a the following contents:
```
{
    "_meta": {
        "hash": {
            "sha256": "99fb04bb4c8d8102fd69dcd67f7deda8a27fe4745516940953576911bc377591"
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
                "sha256:7bc78d7140c353b10a637927fe4bc4c4d95a464d1b8f515d5844def2ee52cbd5",
                "sha256:c3e138e9041d59cd34cdc28a587dfdc899dba02ea26ebc3e10fb4bc88e5cf31b"
            ],
            "index": "pypi",
            "markers": "python_version >= '3.8'",
            "version": "==1.35.14"
        },
        "botocore": {
            "hashes": [
                "sha256:24823135232f88266b66ae8e1d0f3d40872c14cd976781f7fe52b8f0d79035a0",
                "sha256:8515a2fc7ca5bcf0b10016ba05ccf2d642b7cb77d8773026ff2fa5aa3bf38d2e"
            ],
            "markers": "python_version >= '3.8'",
            "version": "==1.35.14"
        },
        "cachetools": {
            "hashes": [
                "sha256:02134e8439cdc2ffb62023ce1debca2944c3f289d66bb17ead3ab3dede74b292",
                "sha256:2cc24fb4cbe39633fb7badd9db9ca6295d766d9c2995f245725a46715d050f2a"
            ],
            "markers": "python_version >= '3.7'",
            "version": "==5.5.0"
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
        "google-api-core": {
            "extras": [
                "grpc"
            ],
            "hashes": [
                "sha256:53ec0258f2837dd53bbd3d3df50f5359281b3cc13f800c941dd15a9b5a415af4",
                "sha256:ca07de7e8aa1c98a8bfca9321890ad2340ef7f2eb136e558cee68f24b94b0a8f"
            ],
            "markers": "python_version >= '3.7'",
            "version": "==2.19.2"
        },
        "google-auth": {
            "hashes": [
                "sha256:72fd4733b80b6d777dcde515628a9eb4a577339437012874ea286bca7261ee65",
                "sha256:8eb87396435c19b20d32abd2f984e31c191a15284af72eb922f10e5bde9c04cc"
            ],
            "markers": "python_version >= '3.7'",
            "version": "==2.34.0"
        },
        "google-cloud-core": {
            "hashes": [
                "sha256:9b7749272a812bde58fff28868d0c5e2f585b82f37e09a1f6ed2d4d10f134073",
                "sha256:a9e6a4422b9ac5c29f79a0ede9485473338e2ce78d91f2370c01e730eab22e61"
            ],
            "markers": "python_version >= '3.7'",
            "version": "==2.4.1"
        },
        "google-cloud-storage": {
            "hashes": [
                "sha256:97a4d45c368b7d401ed48c4fdfe86e1e1cb96401c9e199e419d289e2c0370166",
                "sha256:aaf7acd70cdad9f274d29332673fcab98708d0e1f4dceb5a5356aaef06af4d99"
            ],
            "index": "pypi",
            "markers": "python_version >= '3.7'",
            "version": "==2.18.2"
        },
        "google-cloud-texttospeech": {
            "hashes": [
                "sha256:0a16138978277cc257b8e19ce5d285986a979cd91ffa4cae4518579c17db538e",
                "sha256:851cc3e3a32a500fde773784061e9cea5e9960ac576883a2775f70d61359850a"
            ],
            "index": "pypi",
            "markers": "python_version >= '3.7'",
            "version": "==2.17.2"
        },
        "google-crc32c": {
            "hashes": [
                "sha256:05e2d8c9a2f853ff116db9706b4a27350587f341eda835f46db3c0a8c8ce2f24",
                "sha256:18e311c64008f1f1379158158bb3f0c8d72635b9eb4f9545f8cf990c5668e59d",
                "sha256:236c87a46cdf06384f614e9092b82c05f81bd34b80248021f729396a78e55d7e",
                "sha256:35834855408429cecf495cac67ccbab802de269e948e27478b1e47dfb6465e57",
                "sha256:386122eeaaa76951a8196310432c5b0ef3b53590ef4c317ec7588ec554fec5d2",
                "sha256:40b05ab32a5067525670880eb5d169529089a26fe35dce8891127aeddc1950e8",
                "sha256:48abd62ca76a2cbe034542ed1b6aee851b6f28aaca4e6551b5599b6f3ef175cc",
                "sha256:50cf2a96da226dcbff8671233ecf37bf6e95de98b2a2ebadbfdf455e6d05df42",
                "sha256:51c4f54dd8c6dfeb58d1df5e4f7f97df8abf17a36626a217f169893d1d7f3e9f",
                "sha256:5bcc90b34df28a4b38653c36bb5ada35671ad105c99cfe915fb5bed7ad6924aa",
                "sha256:62f6d4a29fea082ac4a3c9be5e415218255cf11684ac6ef5488eea0c9132689b",
                "sha256:6eceb6ad197656a1ff49ebfbbfa870678c75be4344feb35ac1edf694309413dc",
                "sha256:7aec8e88a3583515f9e0957fe4f5f6d8d4997e36d0f61624e70469771584c760",
                "sha256:91ca8145b060679ec9176e6de4f89b07363d6805bd4760631ef254905503598d",
                "sha256:a184243544811e4a50d345838a883733461e67578959ac59964e43cca2c791e7",
                "sha256:a9e4b426c3702f3cd23b933436487eb34e01e00327fac20c9aebb68ccf34117d",
                "sha256:bb0966e1c50d0ef5bc743312cc730b533491d60585a9a08f897274e57c3f70e0",
                "sha256:bb8b3c75bd157010459b15222c3fd30577042a7060e29d42dabce449c087f2b3",
                "sha256:bd5e7d2445d1a958c266bfa5d04c39932dc54093fa391736dbfdb0f1929c1fb3",
                "sha256:c87d98c7c4a69066fd31701c4e10d178a648c2cac3452e62c6b24dc51f9fcc00",
                "sha256:d2952396dc604544ea7476b33fe87faedc24d666fb0c2d5ac971a2b9576ab871",
                "sha256:d8797406499f28b5ef791f339594b0b5fdedf54e203b5066675c406ba69d705c",
                "sha256:d9e9913f7bd69e093b81da4535ce27af842e7bf371cde42d1ae9e9bd382dc0e9",
                "sha256:e2806553238cd076f0a55bddab37a532b53580e699ed8e5606d0de1f856b5205",
                "sha256:ebab974b1687509e5c973b5c4b8b146683e101e102e17a86bd196ecaa4d099fc",
                "sha256:ed767bf4ba90104c1216b68111613f0d5926fb3780660ea1198fc469af410e9d",
                "sha256:f7a1fc29803712f80879b0806cb83ab24ce62fc8daf0569f2204a0cfd7f68ed4"
            ],
            "markers": "python_version >= '3.9'",
            "version": "==1.6.0"
        },
        "google-resumable-media": {
            "hashes": [
                "sha256:3ce7551e9fe6d99e9a126101d2536612bb73486721951e9562fee0f90c6ababa",
                "sha256:5280aed4629f2b60b847b0d42f9857fd4935c11af266744df33d8074cae92fe0"
            ],
            "markers": "python_version >= '3.7'",
            "version": "==2.7.2"
        },
        "googleapis-common-protos": {
            "hashes": [
                "sha256:2972e6c496f435b92590fd54045060867f3fe9be2c82ab148fc8885035479a63",
                "sha256:334a29d07cddc3aa01dee4988f9afd9b2916ee2ff49d6b757155dc0d197852c0"
            ],
            "markers": "python_version >= '3.7'",
            "version": "==1.65.0"
        },
        "grpcio": {
            "hashes": [
                "sha256:0e6c9b42ded5d02b6b1fea3a25f036a2236eeb75d0579bfd43c0018c88bf0a3e",
                "sha256:161d5c535c2bdf61b95080e7f0f017a1dfcb812bf54093e71e5562b16225b4ce",
                "sha256:17663598aadbedc3cacd7bbde432f541c8e07d2496564e22b214b22c7523dac8",
                "sha256:1c17ebcec157cfb8dd445890a03e20caf6209a5bd4ac5b040ae9dbc59eef091d",
                "sha256:292a846b92cdcd40ecca46e694997dd6b9be6c4c01a94a0dfb3fcb75d20da858",
                "sha256:2ca2559692d8e7e245d456877a85ee41525f3ed425aa97eb7a70fc9a79df91a0",
                "sha256:307b1d538140f19ccbd3aed7a93d8f71103c5d525f3c96f8616111614b14bf2a",
                "sha256:30a1c2cf9390c894c90bbc70147f2372130ad189cffef161f0432d0157973f45",
                "sha256:31a049daa428f928f21090403e5d18ea02670e3d5d172581670be006100db9ef",
                "sha256:35334f9c9745add3e357e3372756fd32d925bd52c41da97f4dfdafbde0bf0ee2",
                "sha256:3750c5a00bd644c75f4507f77a804d0189d97a107eb1481945a0cf3af3e7a5ac",
                "sha256:3885f037eb11f1cacc41f207b705f38a44b69478086f40608959bf5ad85826dd",
                "sha256:4573608e23f7e091acfbe3e84ac2045680b69751d8d67685ffa193a4429fedb1",
                "sha256:4825a3aa5648010842e1c9d35a082187746aa0cdbf1b7a2a930595a94fb10fce",
                "sha256:4877ba180591acdf127afe21ec1c7ff8a5ecf0fe2600f0d3c50e8c4a1cbc6492",
                "sha256:48b0d92d45ce3be2084b92fb5bae2f64c208fea8ceed7fccf6a7b524d3c4942e",
                "sha256:4d813316d1a752be6f5c4360c49f55b06d4fe212d7df03253dfdae90c8a402bb",
                "sha256:5dd67ed9da78e5121efc5c510f0122a972216808d6de70953a740560c572eb44",
                "sha256:6f914386e52cbdeb5d2a7ce3bf1fdfacbe9d818dd81b6099a05b741aaf3848bb",
                "sha256:7101db1bd4cd9b880294dec41a93fcdce465bdbb602cd8dc5bd2d6362b618759",
                "sha256:7e06aa1f764ec8265b19d8f00140b8c4b6ca179a6dc67aa9413867c47e1fb04e",
                "sha256:84ca1be089fb4446490dd1135828bd42a7c7f8421e74fa581611f7afdf7ab761",
                "sha256:8a1e224ce6f740dbb6b24c58f885422deebd7eb724aff0671a847f8951857c26",
                "sha256:97ae7edd3f3f91480e48ede5d3e7d431ad6005bfdbd65c1b56913799ec79e791",
                "sha256:9c9bebc6627873ec27a70fc800f6083a13c70b23a5564788754b9ee52c5aef6c",
                "sha256:a013c5fbb12bfb5f927444b477a26f1080755a931d5d362e6a9a720ca7dbae60",
                "sha256:a66fe4dc35d2330c185cfbb42959f57ad36f257e0cc4557d11d9f0a3f14311df",
                "sha256:a92c4f58c01c77205df6ff999faa008540475c39b835277fb8883b11cada127a",
                "sha256:aa8ba945c96e73de29d25331b26f3e416e0c0f621e984a3ebdb2d0d0b596a3b3",
                "sha256:b0aa03d240b5539648d996cc60438f128c7f46050989e35b25f5c18286c86734",
                "sha256:b1b24c23d51a1e8790b25514157d43f0a4dce1ac12b3f0b8e9f66a5e2c4c132f",
                "sha256:b7ffb8ea674d68de4cac6f57d2498fef477cef582f1fa849e9f844863af50083",
                "sha256:b9feb4e5ec8dc2d15709f4d5fc367794d69277f5d680baf1910fc9915c633524",
                "sha256:bff2096bdba686019fb32d2dde45b95981f0d1490e054400f70fc9a8af34b49d",
                "sha256:c30aeceeaff11cd5ddbc348f37c58bcb96da8d5aa93fed78ab329de5f37a0d7a",
                "sha256:c9f80f9fad93a8cf71c7f161778ba47fd730d13a343a46258065c4deb4b550c0",
                "sha256:cfd349de4158d797db2bd82d2020554a121674e98fbe6b15328456b3bf2495bb",
                "sha256:d0cd7050397b3609ea51727b1811e663ffda8bda39c6a5bb69525ef12414b503",
                "sha256:d639c939ad7c440c7b2819a28d559179a4508783f7e5b991166f8d7a34b52815",
                "sha256:e3ba04659e4fce609de2658fe4dbf7d6ed21987a94460f5f92df7579fd5d0e22",
                "sha256:ecfe735e7a59e5a98208447293ff8580e9db1e890e232b8b292dc8bd15afc0d2",
                "sha256:ef82d361ed5849d34cf09105d00b94b6728d289d6b9235513cb2fcc79f7c432c",
                "sha256:f03a5884c56256e08fd9e262e11b5cfacf1af96e2ce78dc095d2c41ccae2c80d",
                "sha256:f1fe60d0772831d96d263b53d83fb9a3d050a94b0e94b6d004a5ad111faa5b5b",
                "sha256:f517fd7259fe823ef3bd21e508b653d5492e706e9f0ef82c16ce3347a8a5620c",
                "sha256:fdb14bad0835914f325349ed34a51940bc2ad965142eb3090081593c6e347be9"
            ],
            "version": "==1.66.1"
        },
        "grpcio-status": {
            "hashes": [
                "sha256:b3f7d34ccc46d83fea5261eea3786174459f763c31f6e34f1d24eba6d515d024",
                "sha256:cf9ed0b4a83adbe9297211c95cb5488b0cd065707e812145b842c85c4782ff02"
            ],
            "version": "==1.66.1"
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
        "proto-plus": {
            "hashes": [
                "sha256:30b72a5ecafe4406b0d339db35b56c4059064e69227b8c3bda7462397f966445",
                "sha256:402576830425e5f6ce4c2a6702400ac79897dab0b4343821aa5188b0fab81a12"
            ],
            "markers": "python_version >= '3.7'",
            "version": "==1.24.0"
        },
        "protobuf": {
            "hashes": [
                "sha256:018db9056b9d75eb93d12a9d35120f97a84d9a919bcab11ed56ad2d399d6e8dd",
                "sha256:510ed78cd0980f6d3218099e874714cdf0d8a95582e7b059b06cabad855ed0a0",
                "sha256:532627e8fdd825cf8767a2d2b94d77e874d5ddb0adefb04b237f7cc296748681",
                "sha256:6206afcb2d90181ae8722798dcb56dc76675ab67458ac24c0dd7d75d632ac9bd",
                "sha256:66c3edeedb774a3508ae70d87b3a19786445fe9a068dd3585e0cefa8a77b83d0",
                "sha256:6d7cc9e60f976cf3e873acb9a40fed04afb5d224608ed5c1a105db4a3f09c5b6",
                "sha256:853db610214e77ee817ecf0514e0d1d052dff7f63a0c157aa6eabae98db8a8de",
                "sha256:d001a73c8bc2bf5b5c1360d59dd7573744e163b3607fa92788b7f3d5fefbd9a5",
                "sha256:dde74af0fa774fa98892209992295adbfb91da3fa98c8f67a88afe8f5a349add",
                "sha256:dde9fcaa24e7a9654f4baf2a55250b13a5ea701493d904c54069776b99a8216b",
                "sha256:eef7a8a2f4318e2cb2dee8666d26e58eaf437c14788f3a2911d0c3da40405ae8"
            ],
            "markers": "python_version >= '3.8'",
            "version": "==5.28.0"
        },
        "pyasn1": {
            "hashes": [
                "sha256:3a35ab2c4b5ef98e17dfdec8ab074046fbda76e281c5a706ccd82328cfc8f64c",
                "sha256:cca4bb0f2df5504f02f6f8a775b6e416ff9b0b3b16f7ee80b5a3153d9b804473"
            ],
            "markers": "python_version >= '3.8'",
            "version": "==0.6.0"
        },
        "pyasn1-modules": {
            "hashes": [
                "sha256:831dbcea1b177b28c9baddf4c6d1013c24c3accd14a1873fffaa6a2e905f17b6",
                "sha256:be04f15b66c206eed667e0bb5ab27e2b1855ea54a842e5037738099e8ca4ae0b"
            ],
            "markers": "python_version >= '3.8'",
            "version": "==0.4.0"
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
        "rsa": {
            "hashes": [
                "sha256:90260d9058e514786967344d0ef75fa8727eed8a7d2e43ce9f4bcf1b536174f7",
                "sha256:e38464a49c6c85d7f1351b0126661487a7e0a14a50f1675ec50eb34d4f20ef21"
            ],
            "markers": "python_version >= '3.6' and python_version < '4'",
            "version": "==4.9"
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

### Create a .env file for AWS credentials
* Create a `.env` file and add the following:
```
AWS_APPLICATION_CREDENTIALS="secrets/megapipeline-serviceaccount_accessKeys.csv"
```

### Create Dockerfile
* Create a `Dockerfile` and base it from `python:3.8-slim-buster` the official Debian-hosted Python 3.11 image
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
* Build your docker image and give your image the name `synthesis_audio_en`

* You should be able to run your docker image by using:
```
docker run --rm -ti -v "$(pwd)":/app --env-file .env synthesis_audio_en
```

* The `-v "(pwd)":/app` option is to mount your current working directory into the `/app` directory inside the container as a volume. This helps us during development of the app so when you change a source code file using VSCode from your host machine the files are automatically changed inside the container.

* The `--env-file .env` option is to pass the environment variables to the container from the `.env` file

### Python packages required
* `pipenv install` the following:
  - `boto3`

* If you exit your container at this point, in order to get the latest environment from the pipenv file. Make sure to re-build your docker image again

### CLI to interact with your code
* Use the given python file [`cli.py`](https://github.com/dlops-io/mega-pipeline-aws/blob/main/transcribe_audio/cli.py)
* The CLI should have the following command line argument options
```
python cli.py --help
usage: cli.py [-h] [-d] [-s] [-u]

Synthesis audio from text

optional arguments:
  -h, --help       show this help message and exit
  -d, --download   Download paragraph of text from S3 bucket
  -s, --synthesis  Synthesis audio
  -u, --upload     Upload audio file to S3 bucket

```

### Testing your code locally
* Inside your docker shell make sure you run the following commands:
* `python cli.py -d` - Should download all the required data from S3 bucket
* `python cli.py -s` - Should synthesis audio from text and save it locally
* `python cli.py -u` - Should upload the audio files to the S3 bucket
* Verify that your uploaded data shows up in the [Mega Pipeline App](https://ai5-mega-pipeline.dlops.io/)

### OPTIONAL: Push Container to Docker Hub
* Sign up in Docker Hub and create an [Access Token](https://hub.docker.com/settings/security)
* Login to the Hub: `docker login -u <USER NAME> -p <ACCESS TOKEN>`
* Tag the Docker Image: `docker tag synthesis_audio_en <USER NAME>/synthesis_audio_en`
* Push to Docker Hub: `docker push <USER NAME>/synthesis_audio_en`