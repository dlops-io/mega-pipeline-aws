# Generate Text

📝 &rightarrow; 🗒️ 

In this container you will implement the following:
* Read the text prompt from the AWS  S3 bucket `megapipeline-s3bucket` and folder `text_prompts`
* Use OpenAI API to generate text (About 100 words), (You will need your own Open AI API key - https://platform.openai.com/docs/quickstart - Create an API Key in the Dashboard)
* Save the paragraph of text as a text file in bucket `megapipeline-s3bucket` and folder `text_paragraphs` (use the same file name)


### Project Setup

* Create a folder `generate_text` or clone this repo

### AWS Credentials File
* Download the `megapipeline-serviceaccount_accessKeys.csv` and save it inside a folder called `secrets` inside `transcribe_audio`
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
transformers = "4.40.1"
openai = "1.43.1"
boto3 = "1.35.10"

[requires]
python_version = "3.11"

```

* Add `Pipfile.lock` with a the following contents:
```
{
    "_meta": {
        "hash": {
            "sha256": "00eb35b0c6c5b4b9ad2280898996abc64434e817c6a72f0c5b554a7eb2e3f6b5"
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
        "annotated-types": {
            "hashes": [
                "sha256:1f02e8b43a8fbbc3f3e0d4f0f4bfc8131bcb4eebe8849b8e5c773f3a1c582a53",
                "sha256:aff07c09a53a08bc8cfccb9c85b05f1aa9a2a6f23728d790723543408344ce89"
            ],
            "markers": "python_version >= '3.8'",
            "version": "==0.7.0"
        },
        "anyio": {
            "hashes": [
                "sha256:5aadc6a1bbb7cdb0bede386cac5e2940f5e2ff3aa20277e991cf028e0585ce94",
                "sha256:c1b2d8f46a8a812513012e1107cb0e68c17159a7a594208005a57dc776e1bdc7"
            ],
            "markers": "python_version >= '3.8'",
            "version": "==4.4.0"
        },
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
                "sha256:24823135232f88266b66ae8e1d0f3d40872c14cd976781f7fe52b8f0d79035a0",
                "sha256:8515a2fc7ca5bcf0b10016ba05ccf2d642b7cb77d8773026ff2fa5aa3bf38d2e"
            ],
            "markers": "python_version >= '3.8'",
            "version": "==1.35.14"
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
        "distro": {
            "hashes": [
                "sha256:2fa77c6fd8940f116ee1d6b94a2f90b13b5ea8d019b98bc8bafdcabcdd9bdbed",
                "sha256:7bffd925d65168f85027d8da9af6bddab658135b840670a223589bc0c8ef02b2"
            ],
            "markers": "python_version >= '3.6'",
            "version": "==1.9.0"
        },
        "filelock": {
            "hashes": [
                "sha256:81de9eb8453c769b63369f87f11131a7ab04e367f8d97ad39dc230daa07e3bec",
                "sha256:f6ed4c963184f4c84dd5557ce8fece759a3724b37b80c6c4f20a2f63a4dc6609"
            ],
            "markers": "python_version >= '3.8'",
            "version": "==3.16.0"
        },
        "fsspec": {
            "hashes": [
                "sha256:4b0afb90c2f21832df142f292649035d80b421f60a9e1c027802e5a0da2b04e8",
                "sha256:a0947d552d8a6efa72cc2c730b12c41d043509156966cca4fb157b0f2a0c574b"
            ],
            "markers": "python_version >= '3.8'",
            "version": "==2024.9.0"
        },
        "h11": {
            "hashes": [
                "sha256:8f19fbbe99e72420ff35c00b27a34cb9937e902a8b810e2c88300c6f0a3b699d",
                "sha256:e3fe4ac4b851c468cc8363d500db52c2ead036020723024a109d37346efaa761"
            ],
            "markers": "python_version >= '3.7'",
            "version": "==0.14.0"
        },
        "httpcore": {
            "hashes": [
                "sha256:34a38e2f9291467ee3b44e89dd52615370e152954ba21721378a87b2960f7a61",
                "sha256:421f18bac248b25d310f3cacd198d55b8e6125c107797b609ff9b7a6ba7991b5"
            ],
            "markers": "python_version >= '3.8'",
            "version": "==1.0.5"
        },
        "httpx": {
            "hashes": [
                "sha256:7bb2708e112d8fdd7829cd4243970f0c223274051cb35ee80c03301ee29a3df0",
                "sha256:f7c2be1d2f3c3c3160d441802406b206c2b76f5947b11115e6df10c6c65e66c2"
            ],
            "markers": "python_version >= '3.8'",
            "version": "==0.27.2"
        },
        "huggingface-hub": {
            "hashes": [
                "sha256:a990f3232aa985fe749bc9474060cbad75e8b2f115f6665a9fda5b9c97818970",
                "sha256:cc2579e761d070713eaa9c323e3debe39d5b464ae3a7261c39a9195b27bb8000"
            ],
            "markers": "python_full_version >= '3.8.0'",
            "version": "==0.24.6"
        },
        "idna": {
            "hashes": [
                "sha256:050b4e5baadcd44d760cedbd2b8e639f2ff89bbc7a5730fcc662954303377aac",
                "sha256:d838c2c0ed6fced7693d5e8ab8e734d5f8fda53a039c0164afb0b82e771e3603"
            ],
            "markers": "python_version >= '3.6'",
            "version": "==3.8"
        },
        "jiter": {
            "hashes": [
                "sha256:044f2f1148b5248ad2c8c3afb43430dccf676c5a5834d2f5089a4e6c5bbd64df",
                "sha256:04d461ad0aebf696f8da13c99bc1b3e06f66ecf6cfd56254cc402f6385231c06",
                "sha256:0af3838cfb7e6afee3f00dc66fa24695199e20ba87df26e942820345b0afc566",
                "sha256:1c834133e59a8521bc87ebcad773608c6fa6ab5c7a022df24a45030826cf10bc",
                "sha256:1d916ba875bcab5c5f7d927df998c4cb694d27dceddf3392e58beaf10563368a",
                "sha256:1ece0a115c05efca597c6d938f88c9357c843f8c245dbbb53361a1c01afd7148",
                "sha256:26351cc14507bdf466b5f99aba3df3143a59da75799bf64a53a3ad3155ecded9",
                "sha256:2a063f71c4b06225543dddadbe09d203dc0c95ba352d8b85f1221173480a71d5",
                "sha256:2cec323a853c24fd0472517113768c92ae0be8f8c384ef4441d3632da8baa646",
                "sha256:308fce789a2f093dca1ff91ac391f11a9f99c35369117ad5a5c6c4903e1b3e3a",
                "sha256:335942557162ad372cc367ffaf93217117401bf930483b4b3ebdb1223dbddfa7",
                "sha256:368084d8d5c4fc40ff7c3cc513c4f73e02c85f6009217922d0823a48ee7adf61",
                "sha256:44dfc9ddfb9b51a5626568ef4e55ada462b7328996294fe4d36de02fce42721f",
                "sha256:462a52be85b53cd9bffd94e2d788a09984274fe6cebb893d6287e1c296d50653",
                "sha256:4829df14d656b3fb87e50ae8b48253a8851c707da9f30d45aacab2aa2ba2d614",
                "sha256:489875bf1a0ffb3cb38a727b01e6673f0f2e395b2aad3c9387f94187cb214bbf",
                "sha256:503b2c27d87dfff5ab717a8200fbbcf4714516c9d85558048b1fc14d2de7d8dc",
                "sha256:5206144578831a6de278a38896864ded4ed96af66e1e63ec5dd7f4a1fce38a3a",
                "sha256:5280e68e7740c8c128d3ae5ab63335ce6d1fb6603d3b809637b11713487af9e6",
                "sha256:528d742dcde73fad9d63e8242c036ab4a84389a56e04efd854062b660f559544",
                "sha256:550b11d669600dbc342364fd4adbe987f14d0bbedaf06feb1b983383dcc4b961",
                "sha256:583c57fc30cc1fec360e66323aadd7fc3edeec01289bfafc35d3b9dcb29495e4",
                "sha256:63314832e302cc10d8dfbda0333a384bf4bcfce80d65fe99b0f3c0da8945a91a",
                "sha256:649b0ee97a6e6da174bffcb3c8c051a5935d7d4f2f52ea1583b5b3e7822fbf14",
                "sha256:6baa88334e7af3f4d7a5c66c3a63808e5efbc3698a1c57626541ddd22f8e4fbf",
                "sha256:6d1f3d27cce923713933a844872d213d244e09b53ec99b7a7fdf73d543529d6d",
                "sha256:6f1223f88b6d76b519cb033a4d3687ca157c272ec5d6015c322fc5b3074d8a5e",
                "sha256:6f433a4169ad22fcb550b11179bb2b4fd405de9b982601914ef448390b2954f3",
                "sha256:702e3520384c88b6e270c55c772d4bd6d7b150608dcc94dea87ceba1b6391248",
                "sha256:7f5ad4a7c6b0d90776fdefa294f662e8a86871e601309643de30bf94bb93a64e",
                "sha256:8120c60f8121ac3d6f072b97ef0e71770cc72b3c23084c72c4189428b1b1d3b6",
                "sha256:8cf80e5fe6ab582c82f0c3331df27a7e1565e2dcf06265afd5173d809cdbf9ba",
                "sha256:8ea18e01f785c6667ca15407cd6dabbe029d77474d53595a189bdc813347218e",
                "sha256:92cc68b48d50fa472c79c93965e19bd48f40f207cb557a8346daa020d6ba973b",
                "sha256:9f664e7351604f91dcdd557603c57fc0d551bc65cc0a732fdacbf73ad335049a",
                "sha256:a25fbd8a5a58061e433d6fae6d5298777c0814a8bcefa1e5ecfff20c594bd749",
                "sha256:a42a4bdcf7307b86cb863b2fb9bb55029b422d8f86276a50487982d99eed7c6e",
                "sha256:a586832f70c3f1481732919215f36d41c59ca080fa27a65cf23d9490e75b2ef5",
                "sha256:aa1db0967130b5cab63dfe4d6ff547c88b2a394c3410db64744d491df7f069bb",
                "sha256:aa9d2b85b2ed7dc7697597dcfaac66e63c1b3028652f751c81c65a9f220899ae",
                "sha256:ab3a71ff31cf2d45cb216dc37af522d335211f3a972d2fe14ea99073de6cb104",
                "sha256:acc0d5b8b3dd12e91dd184b87273f864b363dfabc90ef29a1092d269f18c7e28",
                "sha256:ad4a6398c85d3a20067e6c69890ca01f68659da94d74c800298581724e426c7e",
                "sha256:afa66939d834b0ce063f57d9895e8036ffc41c4bd90e4a99631e5f261d9b518e",
                "sha256:b250ca2594f5599ca82ba7e68785a669b352156260c5362ea1b4e04a0f3e2389",
                "sha256:b2950e4798e82dd9176935ef6a55cf6a448b5c71515a556da3f6b811a7844f1e",
                "sha256:b599f4e89b3def9a94091e6ee52e1d7ad7bc33e238ebb9c4c63f211d74822c3f",
                "sha256:c22541f0b672f4d741382a97c65609332a783501551445ab2df137ada01e019e",
                "sha256:c451f7922992751a936b96c5f5b9bb9312243d9b754c34b33d0cb72c84669f4e",
                "sha256:c59614b225d9f434ea8fc0d0bec51ef5fa8c83679afedc0433905994fb36d631",
                "sha256:c6f16e21276074a12d8421692515b3fd6d2ea9c94fd0734c39a12960a20e85f3",
                "sha256:c95980207b3998f2c3b3098f357994d3fd7661121f30669ca7cb945f09510a87",
                "sha256:cccd3af9c48ac500c95e1bcbc498020c87e1781ff0345dd371462d67b76643eb",
                "sha256:ce03f7b4129eb72f1687fa11300fbf677b02990618428934662406d2a76742a1",
                "sha256:d4c8e1ed0ef31ad29cae5ea16b9e41529eb50a7fba70600008e9f8de6376d553",
                "sha256:e3bbe3910c724b877846186c25fe3c802e105a2c1fc2b57d6688b9f8772026e4",
                "sha256:e6375923c5f19888c9226582a124b77b622f8fd0018b843c45eeb19d9701c403",
                "sha256:ea189db75f8eca08807d02ae27929e890c7d47599ce3d0a6a5d41f2419ecf338",
                "sha256:f04bc2fc50dc77be9d10f73fcc4e39346402ffe21726ff41028f36e179b587e6",
                "sha256:f16ca8f10e62f25fd81d5310e852df6649af17824146ca74647a018424ddeccf",
                "sha256:f4be354c5de82157886ca7f5925dbda369b77344b4b4adf2723079715f823989"
            ],
            "markers": "python_version >= '3.8'",
            "version": "==0.5.0"
        },
        "jmespath": {
            "hashes": [
                "sha256:02e2e4cc71b5bcab88332eebf907519190dd9e6e82107fa7f83b1003a6252980",
                "sha256:90261b206d6defd58fdd5e85f478bf633a2901798906be2ad389150c5c60edbe"
            ],
            "markers": "python_version >= '3.7'",
            "version": "==1.0.1"
        },
        "numpy": {
            "hashes": [
                "sha256:046356b19d7ad1890c751b99acad5e82dc4a02232013bd9a9a712fddf8eb60f5",
                "sha256:0b8cc2715a84b7c3b161f9ebbd942740aaed913584cae9cdc7f8ad5ad41943d0",
                "sha256:0d07841fd284718feffe7dd17a63a2e6c78679b2d386d3e82f44f0108c905550",
                "sha256:13cc11c00000848702322af4de0147ced365c81d66053a67c2e962a485b3717c",
                "sha256:13ce49a34c44b6de5241f0b38b07e44c1b2dcacd9e36c30f9c2fcb1bb5135db7",
                "sha256:24c2ad697bd8593887b019817ddd9974a7f429c14a5469d7fad413f28340a6d2",
                "sha256:251105b7c42abe40e3a689881e1793370cc9724ad50d64b30b358bbb3a97553b",
                "sha256:2ca4b53e1e0b279142113b8c5eb7d7a877e967c306edc34f3b58e9be12fda8df",
                "sha256:3269c9eb8745e8d975980b3a7411a98976824e1fdef11f0aacf76147f662b15f",
                "sha256:397bc5ce62d3fb73f304bec332171535c187e0643e176a6e9421a6e3eacef06d",
                "sha256:3fc5eabfc720db95d68e6646e88f8b399bfedd235994016351b1d9e062c4b270",
                "sha256:50a95ca3560a6058d6ea91d4629a83a897ee27c00630aed9d933dff191f170cd",
                "sha256:52ac2e48f5ad847cd43c4755520a2317f3380213493b9d8a4c5e37f3b87df504",
                "sha256:53e27293b3a2b661c03f79aa51c3987492bd4641ef933e366e0f9f6c9bf257ec",
                "sha256:57eb525e7c2a8fdee02d731f647146ff54ea8c973364f3b850069ffb42799647",
                "sha256:5889dd24f03ca5a5b1e8a90a33b5a0846d8977565e4ae003a63d22ecddf6782f",
                "sha256:59ca673ad11d4b84ceb385290ed0ebe60266e356641428c845b39cd9df6713ab",
                "sha256:6435c48250c12f001920f0751fe50c0348f5f240852cfddc5e2f97e007544cbe",
                "sha256:6e5a9cb2be39350ae6c8f79410744e80154df658d5bea06e06e0ac5bb75480d5",
                "sha256:7be6a07520b88214ea85d8ac8b7d6d8a1839b0b5cb87412ac9f49fa934eb15d5",
                "sha256:7c803b7934a7f59563db459292e6aa078bb38b7ab1446ca38dd138646a38203e",
                "sha256:7dd86dfaf7c900c0bbdcb8b16e2f6ddf1eb1fe39c6c8cca6e94844ed3152a8fd",
                "sha256:8661c94e3aad18e1ea17a11f60f843a4933ccaf1a25a7c6a9182af70610b2313",
                "sha256:8ae0fd135e0b157365ac7cc31fff27f07a5572bdfc38f9c2d43b2aff416cc8b0",
                "sha256:910b47a6d0635ec1bd53b88f86120a52bf56dcc27b51f18c7b4a2e2224c29f0f",
                "sha256:913cc1d311060b1d409e609947fa1b9753701dac96e6581b58afc36b7ee35af6",
                "sha256:920b0911bb2e4414c50e55bd658baeb78281a47feeb064ab40c2b66ecba85553",
                "sha256:950802d17a33c07cba7fd7c3dcfa7d64705509206be1606f196d179e539111ed",
                "sha256:981707f6b31b59c0c24bcda52e5605f9701cb46da4b86c2e8023656ad3e833cb",
                "sha256:98ce7fb5b8063cfdd86596b9c762bf2b5e35a2cdd7e967494ab78a1fa7f8b86e",
                "sha256:99f4a9ee60eed1385a86e82288971a51e71df052ed0b2900ed30bc840c0f2e39",
                "sha256:9a8e06c7a980869ea67bbf551283bbed2856915f0a792dc32dd0f9dd2fb56728",
                "sha256:ae8ce252404cdd4de56dcfce8b11eac3c594a9c16c231d081fb705cf23bd4d9e",
                "sha256:afd9c680df4de71cd58582b51e88a61feed4abcc7530bcd3d48483f20fc76f2a",
                "sha256:b49742cdb85f1f81e4dc1b39dcf328244f4d8d1ded95dea725b316bd2cf18c95",
                "sha256:b5613cfeb1adfe791e8e681128f5f49f22f3fcaa942255a6124d58ca59d9528f",
                "sha256:bab7c09454460a487e631ffc0c42057e3d8f2a9ddccd1e60c7bb8ed774992480",
                "sha256:c8a0e34993b510fc19b9a2ce7f31cb8e94ecf6e924a40c0c9dd4f62d0aac47d9",
                "sha256:caf5d284ddea7462c32b8d4a6b8af030b6c9fd5332afb70e7414d7fdded4bfd0",
                "sha256:cea427d1350f3fd0d2818ce7350095c1a2ee33e30961d2f0fef48576ddbbe90f",
                "sha256:d0cf7d55b1051387807405b3898efafa862997b4cba8aa5dbe657be794afeafd",
                "sha256:d10c39947a2d351d6d466b4ae83dad4c37cd6c3cdd6d5d0fa797da56f710a6ae",
                "sha256:d2b9cd92c8f8e7b313b80e93cedc12c0112088541dcedd9197b5dee3738c1201",
                "sha256:d4c57b68c8ef5e1ebf47238e99bf27657511ec3f071c465f6b1bccbef12d4136",
                "sha256:d51fc141ddbe3f919e91a096ec739f49d686df8af254b2053ba21a910ae518bf",
                "sha256:e097507396c0be4e547ff15b13dc3866f45f3680f789c1a1301b07dadd3fbc78",
                "sha256:e30356d530528a42eeba51420ae8bf6c6c09559051887196599d96ee5f536468",
                "sha256:e8d5f8a8e3bc87334f025194c6193e408903d21ebaeb10952264943a985066ca",
                "sha256:e8dfa9e94fc127c40979c3eacbae1e61fda4fe71d84869cc129e2721973231ef",
                "sha256:f212d4f46b67ff604d11fff7cc62d36b3e8714edf68e44e9760e19be38c03eb0",
                "sha256:f7506387e191fe8cdb267f912469a3cccc538ab108471291636a96a54e599556",
                "sha256:fac6e277a41163d27dfab5f4ec1f7a83fac94e170665a4a50191b545721c6521",
                "sha256:fcd8f556cdc8cfe35e70efb92463082b7f43dd7e547eb071ffc36abc0ca4699b"
            ],
            "markers": "python_version >= '3.10'",
            "version": "==2.1.1"
        },
        "openai": {
            "hashes": [
                "sha256:23ed3aa71e89cf644c911f7ab80087d08c0bf46ce6b75d9a811fc7942cff85c2",
                "sha256:b64843711b7c92ded36795062ea1f8cad84ec6c2848646f2a786ac4617a6b9f5"
            ],
            "index": "pypi",
            "markers": "python_full_version >= '3.7.1'",
            "version": "==1.43.1"
        },
        "packaging": {
            "hashes": [
                "sha256:026ed72c8ed3fcce5bf8950572258698927fd1dbda10a5e981cdf0ac37f4f002",
                "sha256:5b8f2217dbdbd2f7f384c41c628544e6d52f2d0f53c6d0c3ea61aa5d1d7ff124"
            ],
            "markers": "python_version >= '3.8'",
            "version": "==24.1"
        },
        "pydantic": {
            "hashes": [
                "sha256:c7a8a9fdf7d100afa49647eae340e2d23efa382466a8d177efcd1381e9be5598",
                "sha256:f66a7073abd93214a20c5f7b32d56843137a7a2e70d02111f3be287035c45370"
            ],
            "markers": "python_version >= '3.8'",
            "version": "==2.9.0"
        },
        "pydantic-core": {
            "hashes": [
                "sha256:0102e49ac7d2df3379ef8d658d3bc59d3d769b0bdb17da189b75efa861fc07b4",
                "sha256:0123655fedacf035ab10c23450163c2f65a4174f2bb034b188240a6cf06bb123",
                "sha256:043ef8469f72609c4c3a5e06a07a1f713d53df4d53112c6d49207c0bd3c3bd9b",
                "sha256:0448b81c3dfcde439551bb04a9f41d7627f676b12701865c8a2574bcea034437",
                "sha256:05b366fb8fe3d8683b11ac35fa08947d7b92be78ec64e3277d03bd7f9b7cda79",
                "sha256:07049ec9306ec64e955b2e7c40c8d77dd78ea89adb97a2013d0b6e055c5ee4c5",
                "sha256:084414ffe9a85a52940b49631321d636dadf3576c30259607b75516d131fecd0",
                "sha256:086c5db95157dc84c63ff9d96ebb8856f47ce113c86b61065a066f8efbe80acf",
                "sha256:12625e69b1199e94b0ae1c9a95d000484ce9f0182f9965a26572f054b1537e44",
                "sha256:16b25a4a120a2bb7dab51b81e3d9f3cde4f9a4456566c403ed29ac81bf49744f",
                "sha256:19f1352fe4b248cae22a89268720fc74e83f008057a652894f08fa931e77dced",
                "sha256:1a2ab4f410f4b886de53b6bddf5dd6f337915a29dd9f22f20f3099659536b2f6",
                "sha256:1c7b81beaf7c7ebde978377dc53679c6cba0e946426fc7ade54251dfe24a7604",
                "sha256:1cf842265a3a820ebc6388b963ead065f5ce8f2068ac4e1c713ef77a67b71f7c",
                "sha256:1eb37f7d6a8001c0f86dc8ff2ee8d08291a536d76e49e78cda8587bb54d8b329",
                "sha256:23af245b8f2f4ee9e2c99cb3f93d0e22fb5c16df3f2f643f5a8da5caff12a653",
                "sha256:257d6a410a0d8aeb50b4283dea39bb79b14303e0fab0f2b9d617701331ed1515",
                "sha256:276ae78153a94b664e700ac362587c73b84399bd1145e135287513442e7dfbc7",
                "sha256:2b1a195efd347ede8bcf723e932300292eb13a9d2a3c1f84eb8f37cbbc905b7f",
                "sha256:329a721253c7e4cbd7aad4a377745fbcc0607f9d72a3cc2102dd40519be75ed2",
                "sha256:358331e21a897151e54d58e08d0219acf98ebb14c567267a87e971f3d2a3be59",
                "sha256:3649bd3ae6a8ebea7dc381afb7f3c6db237fc7cebd05c8ac36ca8a4187b03b30",
                "sha256:3713dc093d5048bfaedbba7a8dbc53e74c44a140d45ede020dc347dda18daf3f",
                "sha256:3ef71ec876fcc4d3bbf2ae81961959e8d62f8d74a83d116668409c224012e3af",
                "sha256:41ae8537ad371ec018e3c5da0eb3f3e40ee1011eb9be1da7f965357c4623c501",
                "sha256:4a801c5e1e13272e0909c520708122496647d1279d252c9e6e07dac216accc41",
                "sha256:4c83c64d05ffbbe12d4e8498ab72bdb05bcc1026340a4a597dc647a13c1605ec",
                "sha256:4cebb9794f67266d65e7e4cbe5dcf063e29fc7b81c79dc9475bd476d9534150e",
                "sha256:5668b3173bb0b2e65020b60d83f5910a7224027232c9f5dc05a71a1deac9f960",
                "sha256:56e6a12ec8d7679f41b3750ffa426d22b44ef97be226a9bab00a03365f217b2b",
                "sha256:582871902e1902b3c8e9b2c347f32a792a07094110c1bca6c2ea89b90150caac",
                "sha256:5c8aa40f6ca803f95b1c1c5aeaee6237b9e879e4dfb46ad713229a63651a95fb",
                "sha256:5d813fd871b3d5c3005157622ee102e8908ad6011ec915a18bd8fde673c4360e",
                "sha256:5dd0ec5f514ed40e49bf961d49cf1bc2c72e9b50f29a163b2cc9030c6742aa73",
                "sha256:5f3cf3721eaf8741cffaf092487f1ca80831202ce91672776b02b875580e174a",
                "sha256:6294907eaaccf71c076abdd1c7954e272efa39bb043161b4b8aa1cd76a16ce43",
                "sha256:64d094ea1aa97c6ded4748d40886076a931a8bf6f61b6e43e4a1041769c39dd2",
                "sha256:6650a7bbe17a2717167e3e23c186849bae5cef35d38949549f1c116031b2b3aa",
                "sha256:67b6655311b00581914aba481729971b88bb8bc7996206590700a3ac85e457b8",
                "sha256:6b06c5d4e8701ac2ba99a2ef835e4e1b187d41095a9c619c5b185c9068ed2a49",
                "sha256:6ce883906810b4c3bd90e0ada1f9e808d9ecf1c5f0b60c6b8831d6100bcc7dd6",
                "sha256:6db09153d8438425e98cdc9a289c5fade04a5d2128faff8f227c459da21b9703",
                "sha256:6f80fba4af0cb1d2344869d56430e304a51396b70d46b91a55ed4959993c0589",
                "sha256:743e5811b0c377eb830150d675b0847a74a44d4ad5ab8845923d5b3a756d8100",
                "sha256:753294d42fb072aa1775bfe1a2ba1012427376718fa4c72de52005a3d2a22178",
                "sha256:7568f682c06f10f30ef643a1e8eec4afeecdafde5c4af1b574c6df079e96f96c",
                "sha256:7706e15cdbf42f8fab1e6425247dfa98f4a6f8c63746c995d6a2017f78e619ae",
                "sha256:785e7f517ebb9890813d31cb5d328fa5eda825bb205065cde760b3150e4de1f7",
                "sha256:7a05c0240f6c711eb381ac392de987ee974fa9336071fb697768dfdb151345ce",
                "sha256:7ce7eaf9a98680b4312b7cebcdd9352531c43db00fca586115845df388f3c465",
                "sha256:7ce8e26b86a91e305858e018afc7a6e932f17428b1eaa60154bd1f7ee888b5f8",
                "sha256:7d0324a35ab436c9d768753cbc3c47a865a2cbc0757066cb864747baa61f6ece",
                "sha256:7e9b24cca4037a561422bf5dc52b38d390fb61f7bfff64053ce1b72f6938e6b2",
                "sha256:810ca06cca91de9107718dc83d9ac4d2e86efd6c02cba49a190abcaf33fb0472",
                "sha256:820f6ee5c06bc868335e3b6e42d7ef41f50dfb3ea32fbd523ab679d10d8741c0",
                "sha256:82764c0bd697159fe9947ad59b6db6d7329e88505c8f98990eb07e84cc0a5d81",
                "sha256:8ae65fdfb8a841556b52935dfd4c3f79132dc5253b12c0061b96415208f4d622",
                "sha256:8d5b0ff3218858859910295df6953d7bafac3a48d5cd18f4e3ed9999efd2245f",
                "sha256:95d6bf449a1ac81de562d65d180af5d8c19672793c81877a2eda8fde5d08f2fd",
                "sha256:964c7aa318da542cdcc60d4a648377ffe1a2ef0eb1e996026c7f74507b720a78",
                "sha256:96ef39add33ff58cd4c112cbac076726b96b98bb8f1e7f7595288dcfb2f10b57",
                "sha256:a6612c2a844043e4d10a8324c54cdff0042c558eef30bd705770793d70b224aa",
                "sha256:a8031074a397a5925d06b590121f8339d34a5a74cfe6970f8a1124eb8b83f4ac",
                "sha256:aab9e522efff3993a9e98ab14263d4e20211e62da088298089a03056980a3e69",
                "sha256:ae579143826c6f05a361d9546446c432a165ecf1c0b720bbfd81152645cb897d",
                "sha256:ae90b9e50fe1bd115b24785e962b51130340408156d34d67b5f8f3fa6540938e",
                "sha256:b18cf68255a476b927910c6873d9ed00da692bb293c5b10b282bd48a0afe3ae2",
                "sha256:b7efb12e5071ad8d5b547487bdad489fbd4a5a35a0fc36a1941517a6ad7f23e0",
                "sha256:c4d9f15ffe68bcd3898b0ad7233af01b15c57d91cd1667f8d868e0eacbfe3f87",
                "sha256:c53100c8ee5a1e102766abde2158077d8c374bee0639201f11d3032e3555dfbc",
                "sha256:c57e493a0faea1e4c38f860d6862ba6832723396c884fbf938ff5e9b224200e2",
                "sha256:c8319e0bd6a7b45ad76166cc3d5d6a36c97d0c82a196f478c3ee5346566eebfd",
                "sha256:caffda619099cfd4f63d48462f6aadbecee3ad9603b4b88b60cb821c1b258576",
                "sha256:cc0c316fba3ce72ac3ab7902a888b9dc4979162d320823679da270c2d9ad0cad",
                "sha256:cdd02a08205dc90238669f082747612cb3c82bd2c717adc60f9b9ecadb540f80",
                "sha256:d50ac34835c6a4a0d456b5db559b82047403c4317b3bc73b3455fefdbdc54b0a",
                "sha256:d6b9dd6aa03c812017411734e496c44fef29b43dba1e3dd1fa7361bbacfc1354",
                "sha256:da3131ef2b940b99106f29dfbc30d9505643f766704e14c5d5e504e6a480c35e",
                "sha256:da43cbe593e3c87d07108d0ebd73771dc414488f1f91ed2e204b0370b94b37ac",
                "sha256:dd59638025160056687d598b054b64a79183f8065eae0d3f5ca523cde9943940",
                "sha256:e1895e949f8849bc2757c0dbac28422a04be031204df46a56ab34bcf98507342",
                "sha256:e1a79ad49f346aa1a2921f31e8dbbab4d64484823e813a002679eaa46cba39e1",
                "sha256:e460475719721d59cd54a350c1f71c797c763212c836bf48585478c5514d2854",
                "sha256:e64ffaf8f6e17ca15eb48344d86a7a741454526f3a3fa56bc493ad9d7ec63936",
                "sha256:e6e3ccebdbd6e53474b0bb7ab8b88e83c0cfe91484b25e058e581348ee5a01a5",
                "sha256:e758d271ed0286d146cf7c04c539a5169a888dd0b57026be621547e756af55bc",
                "sha256:f087879f1ffde024dd2788a30d55acd67959dcf6c431e9d3682d1c491a0eb474",
                "sha256:f477d26183e94eaafc60b983ab25af2a809a1b48ce4debb57b343f671b7a90b6",
                "sha256:fc535cb898ef88333cf317777ecdfe0faac1c2a3187ef7eb061b6f7ecf7e6bae"
            ],
            "markers": "python_version >= '3.8'",
            "version": "==2.23.2"
        },
        "python-dateutil": {
            "hashes": [
                "sha256:37dd54208da7e1cd875388217d5e00ebd4179249f90fb72437e91a35459a0ad3",
                "sha256:a8b2bc7bffae282281c8140a97d3aa9c14da0b136dfe83f850eea9a5f7470427"
            ],
            "markers": "python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2'",
            "version": "==2.9.0.post0"
        },
        "pyyaml": {
            "hashes": [
                "sha256:01179a4a8559ab5de078078f37e5c1a30d76bb88519906844fd7bdea1b7729ff",
                "sha256:0833f8694549e586547b576dcfaba4a6b55b9e96098b36cdc7ebefe667dfed48",
                "sha256:0a9a2848a5b7feac301353437eb7d5957887edbf81d56e903999a75a3d743086",
                "sha256:0b69e4ce7a131fe56b7e4d770c67429700908fc0752af059838b1cfb41960e4e",
                "sha256:0ffe8360bab4910ef1b9e87fb812d8bc0a308b0d0eef8c8f44e0254ab3b07133",
                "sha256:11d8f3dd2b9c1207dcaf2ee0bbbfd5991f571186ec9cc78427ba5bd32afae4b5",
                "sha256:17e311b6c678207928d649faa7cb0d7b4c26a0ba73d41e99c4fff6b6c3276484",
                "sha256:1e2120ef853f59c7419231f3bf4e7021f1b936f6ebd222406c3b60212205d2ee",
                "sha256:1f71ea527786de97d1a0cc0eacd1defc0985dcf6b3f17bb77dcfc8c34bec4dc5",
                "sha256:23502f431948090f597378482b4812b0caae32c22213aecf3b55325e049a6c68",
                "sha256:24471b829b3bf607e04e88d79542a9d48bb037c2267d7927a874e6c205ca7e9a",
                "sha256:29717114e51c84ddfba879543fb232a6ed60086602313ca38cce623c1d62cfbf",
                "sha256:2e99c6826ffa974fe6e27cdb5ed0021786b03fc98e5ee3c5bfe1fd5015f42b99",
                "sha256:39693e1f8320ae4f43943590b49779ffb98acb81f788220ea932a6b6c51004d8",
                "sha256:3ad2a3decf9aaba3d29c8f537ac4b243e36bef957511b4766cb0057d32b0be85",
                "sha256:3b1fdb9dc17f5a7677423d508ab4f243a726dea51fa5e70992e59a7411c89d19",
                "sha256:41e4e3953a79407c794916fa277a82531dd93aad34e29c2a514c2c0c5fe971cc",
                "sha256:43fa96a3ca0d6b1812e01ced1044a003533c47f6ee8aca31724f78e93ccc089a",
                "sha256:50187695423ffe49e2deacb8cd10510bc361faac997de9efef88badc3bb9e2d1",
                "sha256:5ac9328ec4831237bec75defaf839f7d4564be1e6b25ac710bd1a96321cc8317",
                "sha256:5d225db5a45f21e78dd9358e58a98702a0302f2659a3c6cd320564b75b86f47c",
                "sha256:6395c297d42274772abc367baaa79683958044e5d3835486c16da75d2a694631",
                "sha256:688ba32a1cffef67fd2e9398a2efebaea461578b0923624778664cc1c914db5d",
                "sha256:68ccc6023a3400877818152ad9a1033e3db8625d899c72eacb5a668902e4d652",
                "sha256:70b189594dbe54f75ab3a1acec5f1e3faa7e8cf2f1e08d9b561cb41b845f69d5",
                "sha256:797b4f722ffa07cc8d62053e4cff1486fa6dc094105d13fea7b1de7d8bf71c9e",
                "sha256:7c36280e6fb8385e520936c3cb3b8042851904eba0e58d277dca80a5cfed590b",
                "sha256:7e7401d0de89a9a855c839bc697c079a4af81cf878373abd7dc625847d25cbd8",
                "sha256:80bab7bfc629882493af4aa31a4cfa43a4c57c83813253626916b8c7ada83476",
                "sha256:82d09873e40955485746739bcb8b4586983670466c23382c19cffecbf1fd8706",
                "sha256:8388ee1976c416731879ac16da0aff3f63b286ffdd57cdeb95f3f2e085687563",
                "sha256:8824b5a04a04a047e72eea5cec3bc266db09e35de6bdfe34c9436ac5ee27d237",
                "sha256:8b9c7197f7cb2738065c481a0461e50ad02f18c78cd75775628afb4d7137fb3b",
                "sha256:9056c1ecd25795207ad294bcf39f2db3d845767be0ea6e6a34d856f006006083",
                "sha256:936d68689298c36b53b29f23c6dbb74de12b4ac12ca6cfe0e047bedceea56180",
                "sha256:9b22676e8097e9e22e36d6b7bda33190d0d400f345f23d4065d48f4ca7ae0425",
                "sha256:a4d3091415f010369ae4ed1fc6b79def9416358877534caf6a0fdd2146c87a3e",
                "sha256:a8786accb172bd8afb8be14490a16625cbc387036876ab6ba70912730faf8e1f",
                "sha256:a9f8c2e67970f13b16084e04f134610fd1d374bf477b17ec1599185cf611d725",
                "sha256:bc2fa7c6b47d6bc618dd7fb02ef6fdedb1090ec036abab80d4681424b84c1183",
                "sha256:c70c95198c015b85feafc136515252a261a84561b7b1d51e3384e0655ddf25ab",
                "sha256:cc1c1159b3d456576af7a3e4d1ba7e6924cb39de8f67111c735f6fc832082774",
                "sha256:ce826d6ef20b1bc864f0a68340c8b3287705cae2f8b4b1d932177dcc76721725",
                "sha256:d584d9ec91ad65861cc08d42e834324ef890a082e591037abe114850ff7bbc3e",
                "sha256:d7fded462629cfa4b685c5416b949ebad6cec74af5e2d42905d41e257e0869f5",
                "sha256:d84a1718ee396f54f3a086ea0a66d8e552b2ab2017ef8b420e92edbc841c352d",
                "sha256:d8e03406cac8513435335dbab54c0d385e4a49e4945d2909a581c83647ca0290",
                "sha256:e10ce637b18caea04431ce14fabcf5c64a1c61ec9c56b071a4b7ca131ca52d44",
                "sha256:ec031d5d2feb36d1d1a24380e4db6d43695f3748343d99434e6f5f9156aaa2ed",
                "sha256:ef6107725bd54b262d6dedcc2af448a266975032bc85ef0172c5f059da6325b4",
                "sha256:efdca5630322a10774e8e98e1af481aad470dd62c3170801852d752aa7a783ba",
                "sha256:f753120cb8181e736c57ef7636e83f31b9c0d1722c516f7e86cf15b7aa57ff12",
                "sha256:ff3824dc5261f50c9b0dfb3be22b4567a6f938ccce4587b38952d85fd9e9afe4"
            ],
            "markers": "python_version >= '3.8'",
            "version": "==6.0.2"
        },
        "regex": {
            "hashes": [
                "sha256:01b689e887f612610c869421241e075c02f2e3d1ae93a037cb14f88ab6a8934c",
                "sha256:04ce29e2c5fedf296b1a1b0acc1724ba93a36fb14031f3abfb7abda2806c1535",
                "sha256:0ffe3f9d430cd37d8fa5632ff6fb36d5b24818c5c986893063b4e5bdb84cdf24",
                "sha256:18300a1d78cf1290fa583cd8b7cde26ecb73e9f5916690cf9d42de569c89b1ce",
                "sha256:185e029368d6f89f36e526764cf12bf8d6f0e3a2a7737da625a76f594bdfcbfc",
                "sha256:19c65b00d42804e3fbea9708f0937d157e53429a39b7c61253ff15670ff62cb5",
                "sha256:228b0d3f567fafa0633aee87f08b9276c7062da9616931382993c03808bb68ce",
                "sha256:23acc72f0f4e1a9e6e9843d6328177ae3074b4182167e34119ec7233dfeccf53",
                "sha256:25419b70ba00a16abc90ee5fce061228206173231f004437730b67ac77323f0d",
                "sha256:2dfbb8baf8ba2c2b9aa2807f44ed272f0913eeeba002478c4577b8d29cde215c",
                "sha256:2f1baff13cc2521bea83ab2528e7a80cbe0ebb2c6f0bfad15be7da3aed443908",
                "sha256:33e2614a7ce627f0cdf2ad104797d1f68342d967de3695678c0cb84f530709f8",
                "sha256:3426de3b91d1bc73249042742f45c2148803c111d1175b283270177fdf669024",
                "sha256:382281306e3adaaa7b8b9ebbb3ffb43358a7bbf585fa93821300a418bb975281",
                "sha256:3d974d24edb231446f708c455fd08f94c41c1ff4f04bcf06e5f36df5ef50b95a",
                "sha256:3f3b6ca8eae6d6c75a6cff525c8530c60e909a71a15e1b731723233331de4169",
                "sha256:3fac296f99283ac232d8125be932c5cd7644084a30748fda013028c815ba3364",
                "sha256:416c0e4f56308f34cdb18c3f59849479dde5b19febdcd6e6fa4d04b6c31c9faa",
                "sha256:438d9f0f4bc64e8dea78274caa5af971ceff0f8771e1a2333620969936ba10be",
                "sha256:43affe33137fcd679bdae93fb25924979517e011f9dea99163f80b82eadc7e53",
                "sha256:44fc61b99035fd9b3b9453f1713234e5a7c92a04f3577252b45feefe1b327759",
                "sha256:45104baae8b9f67569f0f1dca5e1f1ed77a54ae1cd8b0b07aba89272710db61e",
                "sha256:4fdd1384619f406ad9037fe6b6eaa3de2749e2e12084abc80169e8e075377d3b",
                "sha256:538d30cd96ed7d1416d3956f94d54e426a8daf7c14527f6e0d6d425fcb4cca52",
                "sha256:558a57cfc32adcf19d3f791f62b5ff564922942e389e3cfdb538a23d65a6b610",
                "sha256:5eefee9bfe23f6df09ffb6dfb23809f4d74a78acef004aa904dc7c88b9944b05",
                "sha256:64bd50cf16bcc54b274e20235bf8edbb64184a30e1e53873ff8d444e7ac656b2",
                "sha256:65fd3d2e228cae024c411c5ccdffae4c315271eee4a8b839291f84f796b34eca",
                "sha256:66b4c0731a5c81921e938dcf1a88e978264e26e6ac4ec96a4d21ae0354581ae0",
                "sha256:68a8f8c046c6466ac61a36b65bb2395c74451df2ffb8458492ef49900efed293",
                "sha256:6a1141a1dcc32904c47f6846b040275c6e5de0bf73f17d7a409035d55b76f289",
                "sha256:6b9fc7e9cc983e75e2518496ba1afc524227c163e43d706688a6bb9eca41617e",
                "sha256:6f51f9556785e5a203713f5efd9c085b4a45aecd2a42573e2b5041881b588d1f",
                "sha256:7214477bf9bd195894cf24005b1e7b496f46833337b5dedb7b2a6e33f66d962c",
                "sha256:731fcd76bbdbf225e2eb85b7c38da9633ad3073822f5ab32379381e8c3c12e94",
                "sha256:74007a5b25b7a678459f06559504f1eec2f0f17bca218c9d56f6a0a12bfffdad",
                "sha256:7a5486ca56c8869070a966321d5ab416ff0f83f30e0e2da1ab48815c8d165d46",
                "sha256:7c479f5ae937ec9985ecaf42e2e10631551d909f203e31308c12d703922742f9",
                "sha256:7df9ea48641da022c2a3c9c641650cd09f0cd15e8908bf931ad538f5ca7919c9",
                "sha256:7e37e809b9303ec3a179085415cb5f418ecf65ec98cdfe34f6a078b46ef823ee",
                "sha256:80c811cfcb5c331237d9bad3bea2c391114588cf4131707e84d9493064d267f9",
                "sha256:836d3cc225b3e8a943d0b02633fb2f28a66e281290302a79df0e1eaa984ff7c1",
                "sha256:84c312cdf839e8b579f504afcd7b65f35d60b6285d892b19adea16355e8343c9",
                "sha256:86b17ba823ea76256b1885652e3a141a99a5c4422f4a869189db328321b73799",
                "sha256:871e3ab2838fbcb4e0865a6e01233975df3a15e6fce93b6f99d75cacbd9862d1",
                "sha256:88ecc3afd7e776967fa16c80f974cb79399ee8dc6c96423321d6f7d4b881c92b",
                "sha256:8bc593dcce679206b60a538c302d03c29b18e3d862609317cb560e18b66d10cf",
                "sha256:8fd5afd101dcf86a270d254364e0e8dddedebe6bd1ab9d5f732f274fa00499a5",
                "sha256:945352286a541406f99b2655c973852da7911b3f4264e010218bbc1cc73168f2",
                "sha256:973335b1624859cb0e52f96062a28aa18f3a5fc77a96e4a3d6d76e29811a0e6e",
                "sha256:994448ee01864501912abf2bad9203bffc34158e80fe8bfb5b031f4f8e16da51",
                "sha256:9cfd009eed1a46b27c14039ad5bbc5e71b6367c5b2e6d5f5da0ea91600817506",
                "sha256:a2ec4419a3fe6cf8a4795752596dfe0adb4aea40d3683a132bae9c30b81e8d73",
                "sha256:a4997716674d36a82eab3e86f8fa77080a5d8d96a389a61ea1d0e3a94a582cf7",
                "sha256:a512eed9dfd4117110b1881ba9a59b31433caed0c4101b361f768e7bcbaf93c5",
                "sha256:a82465ebbc9b1c5c50738536fdfa7cab639a261a99b469c9d4c7dcbb2b3f1e57",
                "sha256:ae2757ace61bc4061b69af19e4689fa4416e1a04840f33b441034202b5cd02d4",
                "sha256:b16582783f44fbca6fcf46f61347340c787d7530d88b4d590a397a47583f31dd",
                "sha256:ba2537ef2163db9e6ccdbeb6f6424282ae4dea43177402152c67ef869cf3978b",
                "sha256:bf7a89eef64b5455835f5ed30254ec19bf41f7541cd94f266ab7cbd463f00c41",
                "sha256:c0abb5e4e8ce71a61d9446040c1e86d4e6d23f9097275c5bd49ed978755ff0fe",
                "sha256:c414cbda77dbf13c3bc88b073a1a9f375c7b0cb5e115e15d4b73ec3a2fbc6f59",
                "sha256:c51edc3541e11fbe83f0c4d9412ef6c79f664a3745fab261457e84465ec9d5a8",
                "sha256:c5e69fd3eb0b409432b537fe3c6f44ac089c458ab6b78dcec14478422879ec5f",
                "sha256:c918b7a1e26b4ab40409820ddccc5d49871a82329640f5005f73572d5eaa9b5e",
                "sha256:c9bb87fdf2ab2370f21e4d5636e5317775e5d51ff32ebff2cf389f71b9b13750",
                "sha256:ca5b2028c2f7af4e13fb9fc29b28d0ce767c38c7facdf64f6c2cd040413055f1",
                "sha256:d0a07763776188b4db4c9c7fb1b8c494049f84659bb387b71c73bbc07f189e96",
                "sha256:d33a0021893ede5969876052796165bab6006559ab845fd7b515a30abdd990dc",
                "sha256:d55588cba7553f0b6ec33130bc3e114b355570b45785cebdc9daed8c637dd440",
                "sha256:dac8e84fff5d27420f3c1e879ce9929108e873667ec87e0c8eeb413a5311adfe",
                "sha256:eaef80eac3b4cfbdd6de53c6e108b4c534c21ae055d1dbea2de6b3b8ff3def38",
                "sha256:eb462f0e346fcf41a901a126b50f8781e9a474d3927930f3490f38a6e73b6950",
                "sha256:eb563dd3aea54c797adf513eeec819c4213d7dbfc311874eb4fd28d10f2ff0f2",
                "sha256:f273674b445bcb6e4409bf8d1be67bc4b58e8b46fd0d560055d515b8830063cd",
                "sha256:f6442f0f0ff81775eaa5b05af8a0ffa1dda36e9cf6ec1e0d3d245e8564b684ce",
                "sha256:fb168b5924bef397b5ba13aabd8cf5df7d3d93f10218d7b925e360d436863f66",
                "sha256:fbf8c2f00904eaf63ff37718eb13acf8e178cb940520e47b2f05027f5bb34ce3",
                "sha256:fe4ebef608553aff8deb845c7f4f1d0740ff76fa672c011cc0bacb2a00fbde86"
            ],
            "markers": "python_version >= '3.8'",
            "version": "==2024.7.24"
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
        "safetensors": {
            "hashes": [
                "sha256:01c8f00da537af711979e1b42a69a8ec9e1d7112f208e0e9b8a35d2c381085ef",
                "sha256:023b6e5facda76989f4cba95a861b7e656b87e225f61811065d5c501f78cdb3f",
                "sha256:09566792588d77b68abe53754c9f1308fadd35c9f87be939e22c623eaacbed6b",
                "sha256:098923e2574ff237c517d6e840acada8e5b311cb1fa226019105ed82e9c3b62f",
                "sha256:09dedf7c2fda934ee68143202acff6e9e8eb0ddeeb4cfc24182bef999efa9f42",
                "sha256:133620f443450429322f238fda74d512c4008621227fccf2f8cf4a76206fea7c",
                "sha256:139fbee92570ecea774e6344fee908907db79646d00b12c535f66bc78bd5ea2c",
                "sha256:13ca0902d2648775089fa6a0c8fc9e6390c5f8ee576517d33f9261656f851e3f",
                "sha256:1500418454529d0ed5c1564bda376c4ddff43f30fce9517d9bee7bcce5a8ef50",
                "sha256:1524b54246e422ad6fb6aea1ac71edeeb77666efa67230e1faf6999df9b2e27f",
                "sha256:21742b391b859e67b26c0b2ac37f52c9c0944a879a25ad2f9f9f3cd61e7fda8f",
                "sha256:21f848d7aebd5954f92538552d6d75f7c1b4500f51664078b5b49720d180e47c",
                "sha256:23fc9b4ec7b602915cbb4ec1a7c1ad96d2743c322f20ab709e2c35d1b66dad27",
                "sha256:25e5f8e2e92a74f05b4ca55686234c32aac19927903792b30ee6d7bd5653d54e",
                "sha256:2783956926303dcfeb1de91a4d1204cd4089ab441e622e7caee0642281109db3",
                "sha256:309aaec9b66cbf07ad3a2e5cb8a03205663324fea024ba391594423d0f00d9fe",
                "sha256:313514b0b9b73ff4ddfb4edd71860696dbe3c1c9dc4d5cc13dbd74da283d2cbf",
                "sha256:31fa33ee326f750a2f2134a6174773c281d9a266ccd000bd4686d8021f1f3dac",
                "sha256:3685ce7ed036f916316b567152482b7e959dc754fcc4a8342333d222e05f407c",
                "sha256:39371fc551c1072976073ab258c3119395294cf49cdc1f8476794627de3130df",
                "sha256:3a6ba28118636a130ccbb968bc33d4684c48678695dba2590169d5ab03a45646",
                "sha256:4037676c86365a721a8c9510323a51861d703b399b78a6b4486a54a65a975fca",
                "sha256:473300314e026bd1043cef391bb16a8689453363381561b8a3e443870937cc1e",
                "sha256:4b99fbf72e3faf0b2f5f16e5e3458b93b7d0a83984fe8d5364c60aa169f2da89",
                "sha256:4fb3e0609ec12d2a77e882f07cced530b8262027f64b75d399f1504ffec0ba56",
                "sha256:500cac01d50b301ab7bb192353317035011c5ceeef0fca652f9f43c000bb7f8d",
                "sha256:52452fa5999dc50c4decaf0c53aa28371f7f1e0fe5c2dd9129059fbe1e1599c7",
                "sha256:53946c5813b8f9e26103c5efff4a931cc45d874f45229edd68557ffb35ffb9f8",
                "sha256:540ce6c4bf6b58cb0fd93fa5f143bc0ee341c93bb4f9287ccd92cf898cc1b0dd",
                "sha256:585f1703a518b437f5103aa9cf70e9bd437cb78eea9c51024329e4fb8a3e3679",
                "sha256:59b77e4b7a708988d84f26de3ebead61ef1659c73dcbc9946c18f3b1786d2688",
                "sha256:5a2d68a523a4cefd791156a4174189a4114cf0bf9c50ceb89f261600f3b2b81a",
                "sha256:5d3bc83e14d67adc2e9387e511097f254bd1b43c3020440e708858c684cbac68",
                "sha256:5f0032bedc869c56f8d26259fe39cd21c5199cd57f2228d817a0e23e8370af25",
                "sha256:60c828a27e852ded2c85fc0f87bf1ec20e464c5cd4d56ff0e0711855cc2e17f8",
                "sha256:63bfd425e25f5c733f572e2246e08a1c38bd6f2e027d3f7c87e2e43f228d1345",
                "sha256:65573dc35be9059770808e276b017256fa30058802c29e1038eb1c00028502ea",
                "sha256:670e95fe34e0d591d0529e5e59fd9d3d72bc77b1444fcaa14dccda4f36b5a38b",
                "sha256:67e1e7cb8678bb1b37ac48ec0df04faf689e2f4e9e81e566b5c63d9f23748523",
                "sha256:68814d599d25ed2fdd045ed54d370d1d03cf35e02dce56de44c651f828fb9b7b",
                "sha256:6885016f34bef80ea1085b7e99b3c1f92cb1be78a49839203060f67b40aee761",
                "sha256:6ac85d9a8c1af0e3132371d9f2d134695a06a96993c2e2f0bbe25debb9e3f67a",
                "sha256:6d3de65718b86c3eeaa8b73a9c3d123f9307a96bbd7be9698e21e76a56443af5",
                "sha256:7389129c03fadd1ccc37fd1ebbc773f2b031483b04700923c3511d2a939252cc",
                "sha256:73e7d408e9012cd17511b382b43547850969c7979efc2bc353f317abaf23c84c",
                "sha256:7469d70d3de970b1698d47c11ebbf296a308702cbaae7fcb993944751cf985f4",
                "sha256:75331c0c746f03158ded32465b7d0b0e24c5a22121743662a2393439c43a45cf",
                "sha256:76ded72f69209c9780fdb23ea89e56d35c54ae6abcdec67ccb22af8e696e449a",
                "sha256:775409ce0fcc58b10773fdb4221ed1eb007de10fe7adbdf8f5e8a56096b6f0bc",
                "sha256:77d9b228da8374c7262046a36c1f656ba32a93df6cc51cd4453af932011e77f1",
                "sha256:788ee7d04cc0e0e7f944c52ff05f52a4415b312f5efd2ee66389fb7685ee030c",
                "sha256:78dd8adfb48716233c45f676d6e48534d34b4bceb50162c13d1f0bdf6f78590a",
                "sha256:801183a0f76dc647f51a2d9141ad341f9665602a7899a693207a82fb102cc53e",
                "sha256:8158938cf3324172df024da511839d373c40fbfaa83e9abf467174b2910d7b4c",
                "sha256:81efb124b58af39fcd684254c645e35692fea81c51627259cdf6d67ff4458916",
                "sha256:834001bed193e4440c4a3950a31059523ee5090605c907c66808664c932b549c",
                "sha256:83c4f13a9e687335c3928f615cd63a37e3f8ef072a3f2a0599fa09f863fb06a2",
                "sha256:868f9df9e99ad1e7f38c52194063a982bc88fedc7d05096f4f8160403aaf4bd6",
                "sha256:87bc42bd04fd9ca31396d3ca0433db0be1411b6b53ac5a32b7845a85d01ffc2e",
                "sha256:8e8deb16c4321d61ae72533b8451ec4a9af8656d1c61ff81aa49f966406e4b68",
                "sha256:9483f42be3b6bc8ff77dd67302de8ae411c4db39f7224dec66b0eb95822e4163",
                "sha256:951d2fcf1817f4fb0ef0b48f6696688a4e852a95922a042b3f96aaa67eedc920",
                "sha256:9633b663393d5796f0b60249549371e392b75a0b955c07e9c6f8708a87fc841f",
                "sha256:96f1d038c827cdc552d97e71f522e1049fef0542be575421f7684756a748e457",
                "sha256:9cc9449bd0b0bc538bd5e268221f0c5590bc5c14c1934a6ae359d44410dc68c4",
                "sha256:9d1a94b9d793ed8fe35ab6d5cea28d540a46559bafc6aae98f30ee0867000cab",
                "sha256:9e347d77e2c77eb7624400ccd09bed69d35c0332f417ce8c048d404a096c593b",
                "sha256:9f556eea3aec1d3d955403159fe2123ddd68e880f83954ee9b4a3f2e15e716b6",
                "sha256:a01e232e6d3d5cf8b1667bc3b657a77bdab73f0743c26c1d3c5dd7ce86bd3a92",
                "sha256:a0dd565f83b30f2ca79b5d35748d0d99dd4b3454f80e03dfb41f0038e3bdf180",
                "sha256:a3a315a6d0054bc6889a17f5668a73f94f7fe55121ff59e0a199e3519c08565f",
                "sha256:a63eaccd22243c67e4f2b1c3e258b257effc4acd78f3b9d397edc8cf8f1298a7",
                "sha256:a659467495de201e2f282063808a41170448c78bada1e62707b07a27b05e6943",
                "sha256:a6c19feda32b931cae0acd42748a670bdf56bee6476a046af20181ad3fee4090",
                "sha256:adaa9c6dead67e2dd90d634f89131e43162012479d86e25618e821a03d1eb1dc",
                "sha256:b17b299ca9966ca983ecda1c0791a3f07f9ca6ab5ded8ef3d283fff45f6bcd5f",
                "sha256:b3139098e3e8b2ad7afbca96d30ad29157b50c90861084e69fcb80dec7430461",
                "sha256:b4db6a61d968de73722b858038c616a1bebd4a86abe2688e46ca0cc2d17558f2",
                "sha256:b5a8810ad6a6f933fff6c276eae92c1da217b39b4d8b1bc1c0b8af2d270dc532",
                "sha256:b75a616e02f21b6f1d5785b20cecbab5e2bd3f6358a90e8925b813d557666ec1",
                "sha256:b98d40a2ffa560653f6274e15b27b3544e8e3713a44627ce268f419f35c49478",
                "sha256:bad5e4b2476949bcd638a89f71b6916fa9a5cae5c1ae7eede337aca2100435c0",
                "sha256:bb07000b19d41e35eecef9a454f31a8b4718a185293f0d0b1c4b61d6e4487971",
                "sha256:bfeaa1a699c6b9ed514bd15e6a91e74738b71125a9292159e3d6b7f0a53d2cde",
                "sha256:c36302c1c69eebb383775a89645a32b9d266878fab619819ce660309d6176c9b",
                "sha256:c6d156bdb26732feada84f9388a9f135528c1ef5b05fae153da365ad4319c4c5",
                "sha256:c7db3006a4915151ce1913652e907cdede299b974641a83fbc092102ac41b644",
                "sha256:c859c7ed90b0047f58ee27751c8e56951452ed36a67afee1b0a87847d065eec6",
                "sha256:cbd39cae1ad3e3ef6f63a6f07296b080c951f24cec60188378e43d3713000c04",
                "sha256:cf727bb1281d66699bef5683b04d98c894a2803442c490a8d45cd365abfbdeb2",
                "sha256:d0f1dd769f064adc33831f5e97ad07babbd728427f98e3e1db6902e369122737",
                "sha256:d42ffd4c2259f31832cb17ff866c111684c87bd930892a1ba53fed28370c918c",
                "sha256:d5f23198821e227cfc52d50fa989813513db381255c6d100927b012f0cfec63d",
                "sha256:d641f5b8149ea98deb5ffcf604d764aad1de38a8285f86771ce1abf8e74c4891",
                "sha256:d73de19682deabb02524b3d5d1f8b3aaba94c72f1bbfc7911b9b9d5d391c0310",
                "sha256:d94581aab8c6b204def4d7320f07534d6ee34cd4855688004a4354e63b639a35",
                "sha256:dbd280b07e6054ea68b0cb4b16ad9703e7d63cd6890f577cb98acc5354780142",
                "sha256:dd8a1f6d2063a92cd04145c7fd9e31a1c7d85fbec20113a14b487563fdbc0597",
                "sha256:dde2bf390d25f67908278d6f5d59e46211ef98e44108727084d4637ee70ab4f1",
                "sha256:e3cec4a29eb7fe8da0b1c7988bc3828183080439dd559f720414450de076fcab",
                "sha256:e7a97058f96340850da0601a3309f3d29d6191b0702b2da201e54c6e3e44ccf0",
                "sha256:e98ef5524f8b6620c8cdef97220c0b6a5c1cef69852fcd2f174bb96c2bb316b1",
                "sha256:f0b6453c54c57c1781292c46593f8a37254b8b99004c68d6c3ce229688931a22",
                "sha256:f3664ac565d0e809b0b929dae7ccd74e4d3273cd0c6d1220c6430035befb678e",
                "sha256:f4b15f51b4f8f2a512341d9ce3475cacc19c5fdfc5db1f0e19449e75f95c7dc8",
                "sha256:f4beb84b6073b1247a773141a6331117e35d07134b3bb0383003f39971d414bb",
                "sha256:f6594d130d0ad933d885c6a7b75c5183cb0e8450f799b80a39eae2b8508955eb",
                "sha256:f68bf99ea970960a237f416ea394e266e0361895753df06e3e06e6ea7907d98b",
                "sha256:fd33da8e9407559f8779c82a0448e2133737f922d71f884da27184549416bfed",
                "sha256:fdadf66b5a22ceb645d5435a0be7a0292ce59648ca1d46b352f13cff3ea80410"
            ],
            "markers": "python_version >= '3.7'",
            "version": "==0.4.5"
        },
        "six": {
            "hashes": [
                "sha256:1e61c37477a1626458e36f7b1d82aa5c9b094fa4802892072e49de9c60c4c926",
                "sha256:8abb2f1d86890a2dfb989f9a77cfcfd3e47c2a354b01111771326f8aa26e0254"
            ],
            "markers": "python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2'",
            "version": "==1.16.0"
        },
        "sniffio": {
            "hashes": [
                "sha256:2f6da418d1f1e0fddd844478f41680e794e6051915791a034ff65e5f100525a2",
                "sha256:f4324edc670a0f49750a81b895f35c3adb843cca46f0530f79fc1babb23789dc"
            ],
            "markers": "python_version >= '3.7'",
            "version": "==1.3.1"
        },
        "tokenizers": {
            "hashes": [
                "sha256:01d62812454c188306755c94755465505836fd616f75067abcae529c35edeb57",
                "sha256:02e81bf089ebf0e7f4df34fa0207519f07e66d8491d963618252f2e0729e0b46",
                "sha256:04ce49e82d100594715ac1b2ce87d1a36e61891a91de774755f743babcd0dd52",
                "sha256:07f9295349bbbcedae8cefdbcfa7f686aa420be8aca5d4f7d1ae6016c128c0c5",
                "sha256:08a44864e42fa6d7d76d7be4bec62c9982f6f6248b4aa42f7302aa01e0abfd26",
                "sha256:0b5ca92bfa717759c052e345770792d02d1f43b06f9e790ca0a1db62838816f3",
                "sha256:0b9394bd204842a2a1fd37fe29935353742be4a3460b6ccbaefa93f58a8df43d",
                "sha256:0bcce02bf1ad9882345b34d5bd25ed4949a480cf0e656bbd468f4d8986f7a3f1",
                "sha256:0e64bfde9a723274e9a71630c3e9494ed7b4c0f76a1faacf7fe294cd26f7ae7c",
                "sha256:10a707cc6c4b6b183ec5dbfc5c34f3064e18cf62b4a938cb41699e33a99e03c1",
                "sha256:16baac68651701364b0289979ecec728546133e8e8fe38f66fe48ad07996b88b",
                "sha256:1de5bc8652252d9357a666e609cb1453d4f8e160eb1fb2830ee369dd658e8975",
                "sha256:1f0360cbea28ea99944ac089c00de7b2e3e1c58f479fb8613b6d8d511ce98267",
                "sha256:2e8a3dd055e515df7054378dc9d6fa8c8c34e1f32777fb9a01fea81496b3f9d3",
                "sha256:3174c76efd9d08f836bfccaca7cfec3f4d1c0a4cf3acbc7236ad577cc423c840",
                "sha256:35583cd46d16f07c054efd18b5d46af4a2f070a2dd0a47914e66f3ff5efb2b1e",
                "sha256:39c1ec76ea1027438fafe16ecb0fb84795e62e9d643444c1090179e63808c69d",
                "sha256:3b11853f17b54c2fe47742c56d8a33bf49ce31caf531e87ac0d7d13d327c9334",
                "sha256:427c4f0f3df9109314d4f75b8d1f65d9477033e67ffaec4bca53293d3aca286d",
                "sha256:43350270bfc16b06ad3f6f07eab21f089adb835544417afda0f83256a8bf8b75",
                "sha256:453e4422efdfc9c6b6bf2eae00d5e323f263fff62b29a8c9cd526c5003f3f642",
                "sha256:4692ab92f91b87769d950ca14dbb61f8a9ef36a62f94bad6c82cc84a51f76f6a",
                "sha256:4ad23d37d68cf00d54af184586d79b84075ada495e7c5c0f601f051b162112dc",
                "sha256:4f3fefdc0446b1a1e6d81cd4c07088ac015665d2e812f6dbba4a06267d1a2c95",
                "sha256:56ae39d4036b753994476a1b935584071093b55c7a72e3b8288e68c313ca26e7",
                "sha256:5c88d1481f1882c2e53e6bb06491e474e420d9ac7bdff172610c4f9ad3898059",
                "sha256:61b7fe8886f2e104d4caf9218b157b106207e0f2a4905c9c7ac98890688aabeb",
                "sha256:621d670e1b1c281a1c9698ed89451395d318802ff88d1fc1accff0867a06f153",
                "sha256:6258c2ef6f06259f70a682491c78561d492e885adeaf9f64f5389f78aa49a051",
                "sha256:6309271f57b397aa0aff0cbbe632ca9d70430839ca3178bf0f06f825924eca22",
                "sha256:638e43936cc8b2cbb9f9d8dde0fe5e7e30766a3318d2342999ae27f68fdc9bd6",
                "sha256:63c38f45d8f2a2ec0f3a20073cccb335b9f99f73b3c69483cd52ebc75369d8a1",
                "sha256:670b802d4d82bbbb832ddb0d41df7015b3e549714c0e77f9bed3e74d42400fbe",
                "sha256:6852c5b2a853b8b0ddc5993cd4f33bfffdca4fcc5d52f89dd4b8eada99379285",
                "sha256:6b2da5c32ed869bebd990c9420df49813709e953674c0722ff471a116d97b22d",
                "sha256:6c330c0eb815d212893c67a032e9dc1b38a803eccb32f3e8172c19cc69fbb439",
                "sha256:6f8a20266e695ec9d7a946a019c1d5ca4eddb6613d4f466888eee04f16eedb85",
                "sha256:706a37cc5332f85f26efbe2bdc9ef8a9b372b77e4645331a405073e4b3a8c1c6",
                "sha256:71e3ec71f0e78780851fef28c2a9babe20270404c921b756d7c532d280349214",
                "sha256:72791f9bb1ca78e3ae525d4782e85272c63faaef9940d92142aa3eb79f3407a3",
                "sha256:76951121890fea8330d3a0df9a954b3f2a37e3ec20e5b0530e9a0044ca2e11fe",
                "sha256:78e769eb3b2c79687d9cb0f89ef77223e8e279b75c0a968e637ca7043a84463f",
                "sha256:7c9d5b6c0e7a1e979bec10ff960fae925e947aab95619a6fdb4c1d8ff3708ce3",
                "sha256:7fb297edec6c6841ab2e4e8f357209519188e4a59b557ea4fafcf4691d1b4c98",
                "sha256:7ff898780a155ea053f5d934925f3902be2ed1f4d916461e1a93019cc7250837",
                "sha256:82c8b8063de6c0468f08e82c4e198763e7b97aabfe573fd4cf7b33930ca4df77",
                "sha256:85aa3ab4b03d5e99fdd31660872249df5e855334b6c333e0bc13032ff4469c4a",
                "sha256:89183e55fb86e61d848ff83753f64cded119f5d6e1f553d14ffee3700d0a4a49",
                "sha256:8a6298bde623725ca31c9035a04bf2ef63208d266acd2bed8c2cb7d2b7d53ce6",
                "sha256:8b01afb7193d47439f091cd8f070a1ced347ad0f9144952a30a41836902fe09e",
                "sha256:952078130b3d101e05ecfc7fc3640282d74ed26bcf691400f872563fca15ac97",
                "sha256:952b80dac1a6492170f8c2429bd11fcaa14377e097d12a1dbe0ef2fb2241e16c",
                "sha256:9620b78e0b2d52ef07b0d428323fb34e8ea1219c5eac98c2596311f20f1f9266",
                "sha256:9ed240c56b4403e22b9584ee37d87b8bfa14865134e3e1c3fb4b2c42fafd3256",
                "sha256:a179856d1caee06577220ebcfa332af046d576fb73454b8f4d4b0ba8324423ea",
                "sha256:a2b718f316b596f36e1dae097a7d5b91fc5b85e90bf08b01ff139bd8953b25af",
                "sha256:ac11016d0a04aa6487b1513a3a36e7bee7eec0e5d30057c9c0408067345c48d2",
                "sha256:ad57d59341710b94a7d9dbea13f5c1e7d76fd8d9bcd944a7a6ab0b0da6e0cc66",
                "sha256:b07c538ba956843833fee1190cf769c60dc62e1cf934ed50d77d5502194d63b1",
                "sha256:b279ab506ec4445166ac476fb4d3cc383accde1ea152998509a94d82547c8e2a",
                "sha256:b2edbc75744235eea94d595a8b70fe279dd42f3296f76d5a86dde1d46e35f574",
                "sha256:b342d2ce8fc8d00f376af068e3274e2e8649562e3bc6ae4a67784ded6b99428d",
                "sha256:b4399b59d1af5645bcee2072a463318114c39b8547437a7c2d6a186a1b5a0e2d",
                "sha256:b4c89aa46c269e4e70c4d4f9d6bc644fcc39bb409cb2a81227923404dd6f5227",
                "sha256:b70bfbe3a82d3e3fb2a5e9b22a39f8d1740c96c68b6ace0086b39074f08ab89a",
                "sha256:b82931fa619dbad979c0ee8e54dd5278acc418209cc897e42fac041f5366d626",
                "sha256:bac0b0eb952412b0b196ca7a40e7dce4ed6f6926489313414010f2e6b9ec2adf",
                "sha256:bb9dfe7dae85bc6119d705a76dc068c062b8b575abe3595e3c6276480e67e3f1",
                "sha256:bcd266ae85c3d39df2f7e7d0e07f6c41a55e9a3123bb11f854412952deacd828",
                "sha256:bea6f9947e9419c2fda21ae6c32871e3d398cba549b93f4a65a2d369662d9403",
                "sha256:c27b99889bd58b7e301468c0838c5ed75e60c66df0d4db80c08f43462f82e0d3",
                "sha256:c2a0d47a89b48d7daa241e004e71fb5a50533718897a4cd6235cb846d511a478",
                "sha256:c5c2ff13d157afe413bf7e25789879dd463e5a4abfb529a2d8f8473d8042e28f",
                "sha256:c85cf76561fbd01e0d9ea2d1cbe711a65400092bc52b5242b16cfd22e51f0c58",
                "sha256:ca407133536f19bdec44b3da117ef0d12e43f6d4b56ac4c765f37eca501c7bda",
                "sha256:cbf001afbbed111a79ca47d75941e9e5361297a87d186cbfc11ed45e30b5daba",
                "sha256:ce05fde79d2bc2e46ac08aacbc142bead21614d937aac950be88dc79f9db9022",
                "sha256:d16ff18907f4909dca9b076b9c2d899114dd6abceeb074eca0c93e2353f943aa",
                "sha256:d26194ef6c13302f446d39972aaa36a1dda6450bc8949f5eb4c27f51191375bd",
                "sha256:d8c5d59d7b59885eab559d5bc082b2985555a54cda04dda4c65528d90ad252ad",
                "sha256:d924204a3dbe50b75630bd16f821ebda6a5f729928df30f582fb5aade90c818a",
                "sha256:dadc509cc8a9fe460bd274c0e16ac4184d0958117cf026e0ea8b32b438171594",
                "sha256:dd26e3afe8a7b61422df3176e06664503d3f5973b94f45d5c45987e1cb711876",
                "sha256:ddf672ed719b4ed82b51499100f5417d7d9f6fb05a65e232249268f35de5ed14",
                "sha256:dfedf31824ca4915b511b03441784ff640378191918264268e6923da48104acc",
                "sha256:e28cab1582e0eec38b1f38c1c1fb2e56bce5dc180acb1724574fc5f47da2a4fe",
                "sha256:e742d76ad84acbdb1a8e4694f915fe59ff6edc381c97d6dfdd054954e3478ad4",
                "sha256:e83a31c9cf181a0a3ef0abad2b5f6b43399faf5da7e696196ddd110d332519ee",
                "sha256:e8d1ed93beda54bbd6131a2cb363a576eac746d5c26ba5b7556bc6f964425594",
                "sha256:e8ff5b90eabdcdaa19af697885f70fe0b714ce16709cf43d4952f1f85299e73a",
                "sha256:ec11802450a2487cdf0e634b750a04cbdc1c4d066b97d94ce7dd2cb51ebb325b",
                "sha256:ecb2651956eea2aa0a2d099434134b1b68f1c31f9a5084d6d53f08ed43d45ff2",
                "sha256:ed69af290c2b65169f0ba9034d1dc39a5db9459b32f1dd8b5f3f32a3fcf06eab",
                "sha256:eddd5783a4a6309ce23432353cdb36220e25cbb779bfa9122320666508b44b88",
                "sha256:ee59e6680ed0fdbe6b724cf38bd70400a0c1dd623b07ac729087270caeac88e3",
                "sha256:f03727225feaf340ceeb7e00604825addef622d551cbd46b7b775ac834c1e1c4",
                "sha256:f3bbb7a0c5fcb692950b041ae11067ac54826204318922da754f908d95619fbc",
                "sha256:f8a9c828277133af13f3859d1b6bf1c3cb6e9e1637df0e45312e6b7c2e622b1f",
                "sha256:f97660f6c43efd3e0bfd3f2e3e5615bf215680bad6ee3d469df6454b8c6e8256",
                "sha256:f9939ca7e58c2758c01b40324a59c034ce0cebad18e0d4563a9b1beab3018243"
            ],
            "markers": "python_version >= '3.7'",
            "version": "==0.19.1"
        },
        "tqdm": {
            "hashes": [
                "sha256:90279a3770753eafc9194a0364852159802111925aa30eb3f9d85b0e805ac7cd",
                "sha256:e1020aef2e5096702d8a025ac7d16b1577279c9d63f8375b63083e9a5f0fcbad"
            ],
            "markers": "python_version >= '3.7'",
            "version": "==4.66.5"
        },
        "transformers": {
            "hashes": [
                "sha256:55e1697e6f18b58273e7117bb469cdffc11be28995462d8d5e422fef38d2de36",
                "sha256:9d5ee0c8142a60501faf9e49a0b42f8e9cb8611823bce4f195a9325a6816337e"
            ],
            "index": "pypi",
            "markers": "python_full_version >= '3.8.0'",
            "version": "==4.40.1"
        },
        "typing-extensions": {
            "hashes": [
                "sha256:04e5ca0351e0f3f85c6853954072df659d0d13fac324d0072316b67d7794700d",
                "sha256:1a7ead55c7e559dd4dee8856e3a88b41225abfe1ce8df57b7c13915fe121ffb8"
            ],
            "markers": "python_version >= '3.8'",
            "version": "==4.12.2"
        },
        "tzdata": {
            "hashes": [
                "sha256:2674120f8d891909751c38abcdfd386ac0a5a1127954fbc332af6b5ceae07efd",
                "sha256:9068bc196136463f5245e51efda838afa15aaeca9903f49050dfa2679db4d252"
            ],
            "markers": "python_version >= '3.9'",
            "version": "==2024.1"
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
* Create a `Dockerfile` and base it from `python:3.11-slim-buster` the official Debian-hosted Python 3.8 image
* Set the following environment variables:
```
ENV PYENV_SHELL=/bin/bash

```

* Ensure we have an up to date baseline, install dependencies by running
```
apt-get update
apt-get upgrade -y
apt-get install -y --no-install-recommends build-essential
```

* Install pipenv
```
pip install --no-cache-dir --upgrade pip
pip install pipenv
```
* Create a `app` folder by running `mkdir -p /app`

* Set the working directory as `/app`
* Add `Pipfile`, `Pipfile.lock` to the `/app` folder
* Run `pipenv sync`

* Add the rest of your files to the `/app` folder
* Add Entry point to `/bin/bash`
* Add a command to get into the `pipenv shell`

* Example dockerfile can be found [here](https://github.com/dlops-io/mega-pipeline#sample-dockerfile)

### Docker Build & Run
* Build your docker image and give your image the name `generate_text`

* You should be able to run your docker image by using:
```
docker run --rm -ti -v "$(pwd)":/app --env-file .env generate_text 
```
* The `-v "(pwd)":/app` option is to mount your current working directory into the `/app` directory inside the container as a volume. This helps us during development of the app so when you change a source code file using VSCode from your host machine the files are automatically changed inside the container.

* The `--env-file .env` option is to pass the environment variables to the container from the `.env` file

### Python packages required
* `pipenv install` the following:
  - `boto3 = "1.35.10"`
  - `openai = "1.43.1"`
  - `transformers = "4.40.1"`

* If you exit your container at this point, in order to get the latest environment from the pipenv file. Make sure to re-build your docker image again

### CLI to interact with your code
* Use the given python file [`cli.py`](https://github.com/dlops-io/mega-pipeline/blob/main/generate_text/cli.py)
* The CLI should have the following command line argument options
```
python cli.py --help
usage: cli.py [-h] [-d] [-g] [-u]

Generate text from prompt

optional arguments:
  -h, --help      show this help message and exit
  -d, --download  Download text prompts from GCS bucket
  -g, --generate  Generate a text paragraph
  -u, --upload    Upload paragraph text to GCS bucket
```

### Testing your code locally
* Inside your docker shell make sure you run the following commands:
* `python cli.py -d` - Should download all the required data from GCS bucket
* `python cli.py -g` - Should generate text using GPT2 or OpenAI API and save it locally
* `python cli.py -u` - Should upload the generated text to the remote GCS bucket
* Verify that your uploaded data shows up in the [Mega Pipeline App](https://ai5-mega-pipeline.dlops.io/)

### OPTIONAL: Push Container to Docker Hub
* Sign up in Docker Hub and create an [Access Token](https://hub.docker.com/settings/security)
* Login to the Hub: `docker login -u <USER NAME> -p <ACCESS TOKEN>`
* Tag the Docker Image: `docker tag generate_text <USER NAME>/generate_text`
* Push to Docker Hub: `docker push <USER NAME>/generate_text`
