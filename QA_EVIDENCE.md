## autopilot-core2 QA Evidence

**Date:** 2026-01-31T17:42:33+00:00
**Host:** Linux runnervmkj6or 6.11.0-1018-azure #18~24.04.1-Ubuntu SMP Sat Jun 28 04:46:03 UTC 2025 x86_64 x86_64 x86_64 GNU/Linux
**Python:** Python 3.12.3

### 1) Fresh clone + requirements install
Cloning into 'autopilot-core2'...
pip 24.0 from /tmp/ap2/autopilot-core2/.venv_req/lib/python3.12/site-packages/pip (python 3.12)
Collecting fastapi>=0.110.0 (from -r requirements.txt (line 1))
  Downloading fastapi-0.128.0-py3-none-any.whl.metadata (30 kB)
Collecting uvicorn>=0.24.0 (from -r requirements.txt (line 2))
  Downloading uvicorn-0.40.0-py3-none-any.whl.metadata (6.7 kB)
Collecting pydantic>=2.0.0 (from -r requirements.txt (line 3))
  Downloading pydantic-2.12.5-py3-none-any.whl.metadata (90 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 90.6/90.6 kB 8.1 MB/s eta 0:00:00
Collecting sqlalchemy>=2.0.0 (from -r requirements.txt (line 4))
  Downloading sqlalchemy-2.0.46-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (9.5 kB)
Collecting aiohttp>=3.13.3 (from -r requirements.txt (line 5))
  Downloading aiohttp-3.13.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (8.1 kB)
Collecting praw>=7.7.0 (from -r requirements.txt (line 6))
  Downloading praw-7.8.1-py3-none-any.whl.metadata (9.4 kB)
Collecting PyGithub>=2.1.0 (from -r requirements.txt (line 7))
  Downloading pygithub-2.8.1-py3-none-any.whl.metadata (3.9 kB)
Collecting jinja2>=3.1.0 (from -r requirements.txt (line 8))
  Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting python-multipart>=0.0.6 (from -r requirements.txt (line 9))
  Downloading python_multipart-0.0.22-py3-none-any.whl.metadata (1.8 kB)
Collecting starlette<0.51.0,>=0.40.0 (from fastapi>=0.110.0->-r requirements.txt (line 1))
  Downloading starlette-0.50.0-py3-none-any.whl.metadata (6.3 kB)
Collecting typing-extensions>=4.8.0 (from fastapi>=0.110.0->-r requirements.txt (line 1))
  Downloading typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
Collecting annotated-doc>=0.0.2 (from fastapi>=0.110.0->-r requirements.txt (line 1))
  Downloading annotated_doc-0.0.4-py3-none-any.whl.metadata (6.6 kB)
Collecting click>=7.0 (from uvicorn>=0.24.0->-r requirements.txt (line 2))
  Downloading click-8.3.1-py3-none-any.whl.metadata (2.6 kB)
Collecting h11>=0.8 (from uvicorn>=0.24.0->-r requirements.txt (line 2))
  Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
Collecting annotated-types>=0.6.0 (from pydantic>=2.0.0->-r requirements.txt (line 3))
  Downloading annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
Collecting pydantic-core==2.41.5 (from pydantic>=2.0.0->-r requirements.txt (line 3))
  Downloading pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.3 kB)
Collecting typing-inspection>=0.4.2 (from pydantic>=2.0.0->-r requirements.txt (line 3))
  Downloading typing_inspection-0.4.2-py3-none-any.whl.metadata (2.6 kB)
Collecting greenlet>=1 (from sqlalchemy>=2.0.0->-r requirements.txt (line 4))
  Downloading greenlet-3.3.1-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (3.7 kB)
Collecting aiohappyeyeballs>=2.5.0 (from aiohttp>=3.13.3->-r requirements.txt (line 5))
  Downloading aiohappyeyeballs-2.6.1-py3-none-any.whl.metadata (5.9 kB)
Collecting aiosignal>=1.4.0 (from aiohttp>=3.13.3->-r requirements.txt (line 5))
  Downloading aiosignal-1.4.0-py3-none-any.whl.metadata (3.7 kB)
Collecting attrs>=17.3.0 (from aiohttp>=3.13.3->-r requirements.txt (line 5))
  Downloading attrs-25.4.0-py3-none-any.whl.metadata (10 kB)
Collecting frozenlist>=1.1.1 (from aiohttp>=3.13.3->-r requirements.txt (line 5))
  Downloading frozenlist-1.8.0-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (20 kB)
Collecting multidict<7.0,>=4.5 (from aiohttp>=3.13.3->-r requirements.txt (line 5))
  Downloading multidict-6.7.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (5.3 kB)
Collecting propcache>=0.2.0 (from aiohttp>=3.13.3->-r requirements.txt (line 5))
  Downloading propcache-0.4.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (13 kB)
Collecting yarl<2.0,>=1.17.0 (from aiohttp>=3.13.3->-r requirements.txt (line 5))
  Downloading yarl-1.22.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (75 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 75.1/75.1 kB 23.3 MB/s eta 0:00:00
Collecting prawcore<3,>=2.4 (from praw>=7.7.0->-r requirements.txt (line 6))
  Downloading prawcore-2.4.0-py3-none-any.whl.metadata (5.0 kB)
Collecting update_checker>=0.18 (from praw>=7.7.0->-r requirements.txt (line 6))
  Downloading update_checker-0.18.0-py3-none-any.whl.metadata (2.3 kB)
Collecting websocket-client>=0.54.0 (from praw>=7.7.0->-r requirements.txt (line 6))
  Downloading websocket_client-1.9.0-py3-none-any.whl.metadata (8.3 kB)
Collecting pynacl>=1.4.0 (from PyGithub>=2.1.0->-r requirements.txt (line 7))
  Downloading pynacl-1.6.2-cp38-abi3-manylinux_2_34_x86_64.whl.metadata (10.0 kB)
Collecting requests>=2.14.0 (from PyGithub>=2.1.0->-r requirements.txt (line 7))
  Downloading requests-2.32.5-py3-none-any.whl.metadata (4.9 kB)
Collecting pyjwt>=2.4.0 (from pyjwt[crypto]>=2.4.0->PyGithub>=2.1.0->-r requirements.txt (line 7))
  Downloading pyjwt-2.11.0-py3-none-any.whl.metadata (4.0 kB)
Collecting urllib3>=1.26.0 (from PyGithub>=2.1.0->-r requirements.txt (line 7))
  Downloading urllib3-2.6.3-py3-none-any.whl.metadata (6.9 kB)
Collecting MarkupSafe>=2.0 (from jinja2>=3.1.0->-r requirements.txt (line 8))
  Downloading markupsafe-3.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.7 kB)
Collecting cryptography>=3.4.0 (from pyjwt[crypto]>=2.4.0->PyGithub>=2.1.0->-r requirements.txt (line 7))
  Downloading cryptography-46.0.4-cp311-abi3-manylinux_2_34_x86_64.whl.metadata (5.7 kB)
Collecting cffi>=2.0.0 (from pynacl>=1.4.0->PyGithub>=2.1.0->-r requirements.txt (line 7))
  Downloading cffi-2.0.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.6 kB)
Collecting charset_normalizer<4,>=2 (from requests>=2.14.0->PyGithub>=2.1.0->-r requirements.txt (line 7))
  Downloading charset_normalizer-3.4.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (37 kB)
Collecting idna<4,>=2.5 (from requests>=2.14.0->PyGithub>=2.1.0->-r requirements.txt (line 7))
  Downloading idna-3.11-py3-none-any.whl.metadata (8.4 kB)
Collecting certifi>=2017.4.17 (from requests>=2.14.0->PyGithub>=2.1.0->-r requirements.txt (line 7))
  Downloading certifi-2026.1.4-py3-none-any.whl.metadata (2.5 kB)
Collecting anyio<5,>=3.6.2 (from starlette<0.51.0,>=0.40.0->fastapi>=0.110.0->-r requirements.txt (line 1))
  Downloading anyio-4.12.1-py3-none-any.whl.metadata (4.3 kB)
Collecting pycparser (from cffi>=2.0.0->pynacl>=1.4.0->PyGithub>=2.1.0->-r requirements.txt (line 7))
  Downloading pycparser-3.0-py3-none-any.whl.metadata (8.2 kB)
Downloading fastapi-0.128.0-py3-none-any.whl (103 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 103.1/103.1 kB 32.2 MB/s eta 0:00:00
Downloading uvicorn-0.40.0-py3-none-any.whl (68 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 68.5/68.5 kB 20.8 MB/s eta 0:00:00
Downloading pydantic-2.12.5-py3-none-any.whl (463 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 463.6/463.6 kB 35.9 MB/s eta 0:00:00
Downloading pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 102.6 MB/s eta 0:00:00
Downloading sqlalchemy-2.0.46-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (3.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.3/3.3 MB 139.8 MB/s eta 0:00:00
Downloading aiohttp-3.13.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (1.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 150.0 MB/s eta 0:00:00
Downloading praw-7.8.1-py3-none-any.whl (189 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 189.3/189.3 kB 53.3 MB/s eta 0:00:00
Downloading pygithub-2.8.1-py3-none-any.whl (432 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 432.7/432.7 kB 92.8 MB/s eta 0:00:00
Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 134.9/134.9 kB 40.4 MB/s eta 0:00:00
Downloading python_multipart-0.0.22-py3-none-any.whl (24 kB)
Downloading aiohappyeyeballs-2.6.1-py3-none-any.whl (15 kB)
Downloading aiosignal-1.4.0-py3-none-any.whl (7.5 kB)
Downloading annotated_doc-0.0.4-py3-none-any.whl (5.3 kB)
Downloading annotated_types-0.7.0-py3-none-any.whl (13 kB)
Downloading attrs-25.4.0-py3-none-any.whl (67 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 67.6/67.6 kB 22.0 MB/s eta 0:00:00
Downloading click-8.3.1-py3-none-any.whl (108 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 108.3/108.3 kB 31.9 MB/s eta 0:00:00
Downloading frozenlist-1.8.0-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (242 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 242.4/242.4 kB 62.9 MB/s eta 0:00:00
Downloading greenlet-3.3.1-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (609 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 609.9/609.9 kB 69.8 MB/s eta 0:00:00
Downloading h11-0.16.0-py3-none-any.whl (37 kB)
Downloading markupsafe-3.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (22 kB)
Downloading multidict-6.7.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (256 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 256.3/256.3 kB 46.6 MB/s eta 0:00:00
Downloading prawcore-2.4.0-py3-none-any.whl (17 kB)
Downloading propcache-0.4.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (221 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 221.6/221.6 kB 59.3 MB/s eta 0:00:00
Downloading pyjwt-2.11.0-py3-none-any.whl (28 kB)
Downloading pynacl-1.6.2-cp38-abi3-manylinux_2_34_x86_64.whl (1.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.4/1.4 MB 136.9 MB/s eta 0:00:00
Downloading requests-2.32.5-py3-none-any.whl (64 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 64.7/64.7 kB 20.2 MB/s eta 0:00:00
Downloading starlette-0.50.0-py3-none-any.whl (74 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 74.0/74.0 kB 22.9 MB/s eta 0:00:00
Downloading typing_extensions-4.15.0-py3-none-any.whl (44 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 44.6/44.6 kB 15.0 MB/s eta 0:00:00
Downloading typing_inspection-0.4.2-py3-none-any.whl (14 kB)
Downloading update_checker-0.18.0-py3-none-any.whl (7.0 kB)
Downloading urllib3-2.6.3-py3-none-any.whl (131 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 131.6/131.6 kB 39.3 MB/s eta 0:00:00
Downloading websocket_client-1.9.0-py3-none-any.whl (82 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 82.6/82.6 kB 26.5 MB/s eta 0:00:00
Downloading yarl-1.22.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (377 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 377.3/377.3 kB 83.8 MB/s eta 0:00:00
Downloading anyio-4.12.1-py3-none-any.whl (113 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 113.6/113.6 kB 38.3 MB/s eta 0:00:00
Downloading certifi-2026.1.4-py3-none-any.whl (152 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 152.9/152.9 kB 40.0 MB/s eta 0:00:00
Downloading cffi-2.0.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (219 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 219.6/219.6 kB 58.3 MB/s eta 0:00:00
Downloading charset_normalizer-3.4.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (153 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 153.5/153.5 kB 42.3 MB/s eta 0:00:00
Downloading cryptography-46.0.4-cp311-abi3-manylinux_2_34_x86_64.whl (4.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.5/4.5 MB 162.2 MB/s eta 0:00:00
Downloading idna-3.11-py3-none-any.whl (71 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 71.0/71.0 kB 22.4 MB/s eta 0:00:00
Downloading pycparser-3.0-py3-none-any.whl (48 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 48.2/48.2 kB 11.2 MB/s eta 0:00:00
Installing collected packages: websocket-client, urllib3, typing-extensions, python-multipart, pyjwt, pycparser, propcache, multidict, MarkupSafe, idna, h11, greenlet, frozenlist, click, charset_normalizer, certifi, attrs, annotated-types, annotated-doc, aiohappyeyeballs, yarl, uvicorn, typing-inspection, sqlalchemy, requests, pydantic-core, jinja2, cffi, anyio, aiosignal, update_checker, starlette, pynacl, pydantic, prawcore, cryptography, aiohttp, praw, fastapi, PyGithub
Successfully installed MarkupSafe-3.0.3 PyGithub-2.8.1 aiohappyeyeballs-2.6.1 aiohttp-3.13.3 aiosignal-1.4.0 annotated-doc-0.0.4 annotated-types-0.7.0 anyio-4.12.1 attrs-25.4.0 certifi-2026.1.4 cffi-2.0.0 charset_normalizer-3.4.4 click-8.3.1 cryptography-46.0.4 fastapi-0.128.0 frozenlist-1.8.0 greenlet-3.3.1 h11-0.16.0 idna-3.11 jinja2-3.1.6 multidict-6.7.1 praw-7.8.1 prawcore-2.4.0 propcache-0.4.1 pycparser-3.0 pydantic-2.12.5 pydantic-core-2.41.5 pyjwt-2.11.0 pynacl-1.6.2 python-multipart-0.0.22 requests-2.32.5 sqlalchemy-2.0.46 starlette-0.50.0 typing-extensions-4.15.0 typing-inspection-0.4.2 update_checker-0.18.0 urllib3-2.6.3 uvicorn-0.40.0 websocket-client-1.9.0 yarl-1.22.0
import ok: /tmp/ap2/autopilot-core2/pi_core/__init__.py
exe: /tmp/ap2/autopilot-core2/.venv_req/bin/python

### 2) Editable install
Obtaining file:///tmp/ap2/autopilot-core2
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Checking if build backend supports build_editable: started
  Checking if build backend supports build_editable: finished with status 'done'
  Getting requirements to build editable: started
  Getting requirements to build editable: finished with status 'done'
  Preparing editable metadata (pyproject.toml): started
  Preparing editable metadata (pyproject.toml): finished with status 'done'
Collecting fastapi>=0.110.0 (from pi-core==0.1.0)
  Using cached fastapi-0.128.0-py3-none-any.whl.metadata (30 kB)
Collecting uvicorn>=0.24.0 (from pi-core==0.1.0)
  Using cached uvicorn-0.40.0-py3-none-any.whl.metadata (6.7 kB)
Collecting pydantic>=2.0.0 (from pi-core==0.1.0)
  Using cached pydantic-2.12.5-py3-none-any.whl.metadata (90 kB)
Collecting sqlalchemy>=2.0.0 (from pi-core==0.1.0)
  Using cached sqlalchemy-2.0.46-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (9.5 kB)
Collecting aiohttp>=3.13.3 (from pi-core==0.1.0)
  Using cached aiohttp-3.13.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (8.1 kB)
Collecting praw>=7.7.0 (from pi-core==0.1.0)
  Using cached praw-7.8.1-py3-none-any.whl.metadata (9.4 kB)
Collecting PyGithub>=2.1.0 (from pi-core==0.1.0)
  Using cached pygithub-2.8.1-py3-none-any.whl.metadata (3.9 kB)
Collecting jinja2>=3.1.0 (from pi-core==0.1.0)
  Using cached jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting python-multipart>=0.0.6 (from pi-core==0.1.0)
  Using cached python_multipart-0.0.22-py3-none-any.whl.metadata (1.8 kB)
Collecting aiohappyeyeballs>=2.5.0 (from aiohttp>=3.13.3->pi-core==0.1.0)
  Using cached aiohappyeyeballs-2.6.1-py3-none-any.whl.metadata (5.9 kB)
Collecting aiosignal>=1.4.0 (from aiohttp>=3.13.3->pi-core==0.1.0)
  Using cached aiosignal-1.4.0-py3-none-any.whl.metadata (3.7 kB)
Collecting attrs>=17.3.0 (from aiohttp>=3.13.3->pi-core==0.1.0)
  Using cached attrs-25.4.0-py3-none-any.whl.metadata (10 kB)
Collecting frozenlist>=1.1.1 (from aiohttp>=3.13.3->pi-core==0.1.0)
  Using cached frozenlist-1.8.0-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (20 kB)
Collecting multidict<7.0,>=4.5 (from aiohttp>=3.13.3->pi-core==0.1.0)
  Using cached multidict-6.7.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (5.3 kB)
Collecting propcache>=0.2.0 (from aiohttp>=3.13.3->pi-core==0.1.0)
  Using cached propcache-0.4.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (13 kB)
Collecting yarl<2.0,>=1.17.0 (from aiohttp>=3.13.3->pi-core==0.1.0)
  Using cached yarl-1.22.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (75 kB)
Collecting starlette<0.51.0,>=0.40.0 (from fastapi>=0.110.0->pi-core==0.1.0)
  Using cached starlette-0.50.0-py3-none-any.whl.metadata (6.3 kB)
Collecting typing-extensions>=4.8.0 (from fastapi>=0.110.0->pi-core==0.1.0)
  Using cached typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
Collecting annotated-doc>=0.0.2 (from fastapi>=0.110.0->pi-core==0.1.0)
  Using cached annotated_doc-0.0.4-py3-none-any.whl.metadata (6.6 kB)
Collecting MarkupSafe>=2.0 (from jinja2>=3.1.0->pi-core==0.1.0)
  Using cached markupsafe-3.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.7 kB)
Collecting prawcore<3,>=2.4 (from praw>=7.7.0->pi-core==0.1.0)
  Using cached prawcore-2.4.0-py3-none-any.whl.metadata (5.0 kB)
Collecting update_checker>=0.18 (from praw>=7.7.0->pi-core==0.1.0)
  Using cached update_checker-0.18.0-py3-none-any.whl.metadata (2.3 kB)
Collecting websocket-client>=0.54.0 (from praw>=7.7.0->pi-core==0.1.0)
  Using cached websocket_client-1.9.0-py3-none-any.whl.metadata (8.3 kB)
Collecting annotated-types>=0.6.0 (from pydantic>=2.0.0->pi-core==0.1.0)
  Using cached annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
Collecting pydantic-core==2.41.5 (from pydantic>=2.0.0->pi-core==0.1.0)
  Using cached pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.3 kB)
Collecting typing-inspection>=0.4.2 (from pydantic>=2.0.0->pi-core==0.1.0)
  Using cached typing_inspection-0.4.2-py3-none-any.whl.metadata (2.6 kB)
Collecting pynacl>=1.4.0 (from PyGithub>=2.1.0->pi-core==0.1.0)
  Using cached pynacl-1.6.2-cp38-abi3-manylinux_2_34_x86_64.whl.metadata (10.0 kB)
Collecting requests>=2.14.0 (from PyGithub>=2.1.0->pi-core==0.1.0)
  Using cached requests-2.32.5-py3-none-any.whl.metadata (4.9 kB)
Collecting pyjwt>=2.4.0 (from pyjwt[crypto]>=2.4.0->PyGithub>=2.1.0->pi-core==0.1.0)
  Using cached pyjwt-2.11.0-py3-none-any.whl.metadata (4.0 kB)
Collecting urllib3>=1.26.0 (from PyGithub>=2.1.0->pi-core==0.1.0)
  Using cached urllib3-2.6.3-py3-none-any.whl.metadata (6.9 kB)
Collecting greenlet>=1 (from sqlalchemy>=2.0.0->pi-core==0.1.0)
  Using cached greenlet-3.3.1-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (3.7 kB)
Collecting click>=7.0 (from uvicorn>=0.24.0->pi-core==0.1.0)
  Using cached click-8.3.1-py3-none-any.whl.metadata (2.6 kB)
Collecting h11>=0.8 (from uvicorn>=0.24.0->pi-core==0.1.0)
  Using cached h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
Collecting cryptography>=3.4.0 (from pyjwt[crypto]>=2.4.0->PyGithub>=2.1.0->pi-core==0.1.0)
  Using cached cryptography-46.0.4-cp311-abi3-manylinux_2_34_x86_64.whl.metadata (5.7 kB)
Collecting cffi>=2.0.0 (from pynacl>=1.4.0->PyGithub>=2.1.0->pi-core==0.1.0)
  Using cached cffi-2.0.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.6 kB)
Collecting charset_normalizer<4,>=2 (from requests>=2.14.0->PyGithub>=2.1.0->pi-core==0.1.0)
  Using cached charset_normalizer-3.4.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (37 kB)
Collecting idna<4,>=2.5 (from requests>=2.14.0->PyGithub>=2.1.0->pi-core==0.1.0)
  Using cached idna-3.11-py3-none-any.whl.metadata (8.4 kB)
Collecting certifi>=2017.4.17 (from requests>=2.14.0->PyGithub>=2.1.0->pi-core==0.1.0)
  Using cached certifi-2026.1.4-py3-none-any.whl.metadata (2.5 kB)
Collecting anyio<5,>=3.6.2 (from starlette<0.51.0,>=0.40.0->fastapi>=0.110.0->pi-core==0.1.0)
  Using cached anyio-4.12.1-py3-none-any.whl.metadata (4.3 kB)
Collecting pycparser (from cffi>=2.0.0->pynacl>=1.4.0->PyGithub>=2.1.0->pi-core==0.1.0)
  Using cached pycparser-3.0-py3-none-any.whl.metadata (8.2 kB)
Using cached aiohttp-3.13.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (1.8 MB)
Using cached fastapi-0.128.0-py3-none-any.whl (103 kB)
Using cached jinja2-3.1.6-py3-none-any.whl (134 kB)
Using cached praw-7.8.1-py3-none-any.whl (189 kB)
Using cached pydantic-2.12.5-py3-none-any.whl (463 kB)
Using cached pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
Using cached pygithub-2.8.1-py3-none-any.whl (432 kB)
Using cached python_multipart-0.0.22-py3-none-any.whl (24 kB)
Using cached sqlalchemy-2.0.46-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (3.3 MB)
Using cached uvicorn-0.40.0-py3-none-any.whl (68 kB)
Using cached aiohappyeyeballs-2.6.1-py3-none-any.whl (15 kB)
Using cached aiosignal-1.4.0-py3-none-any.whl (7.5 kB)
Using cached annotated_doc-0.0.4-py3-none-any.whl (5.3 kB)
Using cached annotated_types-0.7.0-py3-none-any.whl (13 kB)
Using cached attrs-25.4.0-py3-none-any.whl (67 kB)
Using cached click-8.3.1-py3-none-any.whl (108 kB)
Using cached frozenlist-1.8.0-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (242 kB)
Using cached greenlet-3.3.1-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (609 kB)
Using cached h11-0.16.0-py3-none-any.whl (37 kB)
Using cached markupsafe-3.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (22 kB)
Using cached multidict-6.7.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (256 kB)
Using cached prawcore-2.4.0-py3-none-any.whl (17 kB)
Using cached propcache-0.4.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (221 kB)
Using cached pyjwt-2.11.0-py3-none-any.whl (28 kB)
Using cached pynacl-1.6.2-cp38-abi3-manylinux_2_34_x86_64.whl (1.4 MB)
Using cached requests-2.32.5-py3-none-any.whl (64 kB)
Using cached starlette-0.50.0-py3-none-any.whl (74 kB)
Using cached typing_extensions-4.15.0-py3-none-any.whl (44 kB)
Using cached typing_inspection-0.4.2-py3-none-any.whl (14 kB)
Using cached update_checker-0.18.0-py3-none-any.whl (7.0 kB)
Using cached urllib3-2.6.3-py3-none-any.whl (131 kB)
Using cached websocket_client-1.9.0-py3-none-any.whl (82 kB)
Using cached yarl-1.22.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (377 kB)
Using cached anyio-4.12.1-py3-none-any.whl (113 kB)
Using cached certifi-2026.1.4-py3-none-any.whl (152 kB)
Using cached cffi-2.0.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (219 kB)
Using cached charset_normalizer-3.4.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (153 kB)
Using cached cryptography-46.0.4-cp311-abi3-manylinux_2_34_x86_64.whl (4.5 MB)
Using cached idna-3.11-py3-none-any.whl (71 kB)
Using cached pycparser-3.0-py3-none-any.whl (48 kB)
Building wheels for collected packages: pi-core
  Building editable for pi-core (pyproject.toml): started
  Building editable for pi-core (pyproject.toml): finished with status 'done'
  Created wheel for pi-core: filename=pi_core-0.1.0-0.editable-py3-none-any.whl size=5562 sha256=2c78e2006b914ee9e75438aff7b466fb5d96168ca4ed8b72d6a23b990c00febd
  Stored in directory: /tmp/pip-ephem-wheel-cache-jejaoxpl/wheels/e7/83/87/b9f6b2126721b764cb5936465c54074d10a19a004d620bf849
Successfully built pi-core
Installing collected packages: websocket-client, urllib3, typing-extensions, python-multipart, pyjwt, pycparser, propcache, multidict, MarkupSafe, idna, h11, greenlet, frozenlist, click, charset_normalizer, certifi, attrs, annotated-types, annotated-doc, aiohappyeyeballs, yarl, uvicorn, typing-inspection, sqlalchemy, requests, pydantic-core, jinja2, cffi, anyio, aiosignal, update_checker, starlette, pynacl, pydantic, prawcore, cryptography, aiohttp, praw, fastapi, PyGithub, pi-core
Successfully installed MarkupSafe-3.0.3 PyGithub-2.8.1 aiohappyeyeballs-2.6.1 aiohttp-3.13.3 aiosignal-1.4.0 annotated-doc-0.0.4 annotated-types-0.7.0 anyio-4.12.1 attrs-25.4.0 certifi-2026.1.4 cffi-2.0.0 charset_normalizer-3.4.4 click-8.3.1 cryptography-46.0.4 fastapi-0.128.0 frozenlist-1.8.0 greenlet-3.3.1 h11-0.16.0 idna-3.11 jinja2-3.1.6 multidict-6.7.1 pi-core-0.1.0 praw-7.8.1 prawcore-2.4.0 propcache-0.4.1 pycparser-3.0 pydantic-2.12.5 pydantic-core-2.41.5 pyjwt-2.11.0 pynacl-1.6.2 python-multipart-0.0.22 requests-2.32.5 sqlalchemy-2.0.46 starlette-0.50.0 typing-extensions-4.15.0 typing-inspection-0.4.2 update_checker-0.18.0 urllib3-2.6.3 uvicorn-0.40.0 websocket-client-1.9.0 yarl-1.22.0
editable import ok: /tmp/ap2/autopilot-core2/pi_core/__init__.py
exe: /tmp/ap2/autopilot-core2/.venv_edit/bin/python

### 3) Golden path
Collecting fastapi>=0.110.0 (from -r requirements.txt (line 1))
  Using cached fastapi-0.128.0-py3-none-any.whl.metadata (30 kB)
Collecting uvicorn>=0.24.0 (from -r requirements.txt (line 2))
  Using cached uvicorn-0.40.0-py3-none-any.whl.metadata (6.7 kB)
Collecting pydantic>=2.0.0 (from -r requirements.txt (line 3))
  Using cached pydantic-2.12.5-py3-none-any.whl.metadata (90 kB)
Collecting sqlalchemy>=2.0.0 (from -r requirements.txt (line 4))
  Using cached sqlalchemy-2.0.46-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (9.5 kB)
Collecting aiohttp>=3.13.3 (from -r requirements.txt (line 5))
  Using cached aiohttp-3.13.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (8.1 kB)
Collecting praw>=7.7.0 (from -r requirements.txt (line 6))
  Using cached praw-7.8.1-py3-none-any.whl.metadata (9.4 kB)
Collecting PyGithub>=2.1.0 (from -r requirements.txt (line 7))
  Using cached pygithub-2.8.1-py3-none-any.whl.metadata (3.9 kB)
Collecting jinja2>=3.1.0 (from -r requirements.txt (line 8))
  Using cached jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting python-multipart>=0.0.6 (from -r requirements.txt (line 9))
  Using cached python_multipart-0.0.22-py3-none-any.whl.metadata (1.8 kB)
Collecting starlette<0.51.0,>=0.40.0 (from fastapi>=0.110.0->-r requirements.txt (line 1))
  Using cached starlette-0.50.0-py3-none-any.whl.metadata (6.3 kB)
Collecting typing-extensions>=4.8.0 (from fastapi>=0.110.0->-r requirements.txt (line 1))
  Using cached typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
Collecting annotated-doc>=0.0.2 (from fastapi>=0.110.0->-r requirements.txt (line 1))
  Using cached annotated_doc-0.0.4-py3-none-any.whl.metadata (6.6 kB)
Collecting click>=7.0 (from uvicorn>=0.24.0->-r requirements.txt (line 2))
  Using cached click-8.3.1-py3-none-any.whl.metadata (2.6 kB)
Collecting h11>=0.8 (from uvicorn>=0.24.0->-r requirements.txt (line 2))
  Using cached h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
Collecting annotated-types>=0.6.0 (from pydantic>=2.0.0->-r requirements.txt (line 3))
  Using cached annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
Collecting pydantic-core==2.41.5 (from pydantic>=2.0.0->-r requirements.txt (line 3))
  Using cached pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.3 kB)
Collecting typing-inspection>=0.4.2 (from pydantic>=2.0.0->-r requirements.txt (line 3))
  Using cached typing_inspection-0.4.2-py3-none-any.whl.metadata (2.6 kB)
Collecting greenlet>=1 (from sqlalchemy>=2.0.0->-r requirements.txt (line 4))
  Using cached greenlet-3.3.1-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (3.7 kB)
Collecting aiohappyeyeballs>=2.5.0 (from aiohttp>=3.13.3->-r requirements.txt (line 5))
  Using cached aiohappyeyeballs-2.6.1-py3-none-any.whl.metadata (5.9 kB)
Collecting aiosignal>=1.4.0 (from aiohttp>=3.13.3->-r requirements.txt (line 5))
  Using cached aiosignal-1.4.0-py3-none-any.whl.metadata (3.7 kB)
Collecting attrs>=17.3.0 (from aiohttp>=3.13.3->-r requirements.txt (line 5))
  Using cached attrs-25.4.0-py3-none-any.whl.metadata (10 kB)
Collecting frozenlist>=1.1.1 (from aiohttp>=3.13.3->-r requirements.txt (line 5))
  Using cached frozenlist-1.8.0-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (20 kB)
Collecting multidict<7.0,>=4.5 (from aiohttp>=3.13.3->-r requirements.txt (line 5))
  Using cached multidict-6.7.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (5.3 kB)
Collecting propcache>=0.2.0 (from aiohttp>=3.13.3->-r requirements.txt (line 5))
  Using cached propcache-0.4.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (13 kB)
Collecting yarl<2.0,>=1.17.0 (from aiohttp>=3.13.3->-r requirements.txt (line 5))
  Using cached yarl-1.22.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (75 kB)
Collecting prawcore<3,>=2.4 (from praw>=7.7.0->-r requirements.txt (line 6))
  Using cached prawcore-2.4.0-py3-none-any.whl.metadata (5.0 kB)
Collecting update_checker>=0.18 (from praw>=7.7.0->-r requirements.txt (line 6))
  Using cached update_checker-0.18.0-py3-none-any.whl.metadata (2.3 kB)
Collecting websocket-client>=0.54.0 (from praw>=7.7.0->-r requirements.txt (line 6))
  Using cached websocket_client-1.9.0-py3-none-any.whl.metadata (8.3 kB)
Collecting pynacl>=1.4.0 (from PyGithub>=2.1.0->-r requirements.txt (line 7))
  Using cached pynacl-1.6.2-cp38-abi3-manylinux_2_34_x86_64.whl.metadata (10.0 kB)
Collecting requests>=2.14.0 (from PyGithub>=2.1.0->-r requirements.txt (line 7))
  Using cached requests-2.32.5-py3-none-any.whl.metadata (4.9 kB)
Collecting pyjwt>=2.4.0 (from pyjwt[crypto]>=2.4.0->PyGithub>=2.1.0->-r requirements.txt (line 7))
  Using cached pyjwt-2.11.0-py3-none-any.whl.metadata (4.0 kB)
Collecting urllib3>=1.26.0 (from PyGithub>=2.1.0->-r requirements.txt (line 7))
  Using cached urllib3-2.6.3-py3-none-any.whl.metadata (6.9 kB)
Collecting MarkupSafe>=2.0 (from jinja2>=3.1.0->-r requirements.txt (line 8))
  Using cached markupsafe-3.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.7 kB)
Collecting cryptography>=3.4.0 (from pyjwt[crypto]>=2.4.0->PyGithub>=2.1.0->-r requirements.txt (line 7))
  Using cached cryptography-46.0.4-cp311-abi3-manylinux_2_34_x86_64.whl.metadata (5.7 kB)
Collecting cffi>=2.0.0 (from pynacl>=1.4.0->PyGithub>=2.1.0->-r requirements.txt (line 7))
  Using cached cffi-2.0.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.6 kB)
Collecting charset_normalizer<4,>=2 (from requests>=2.14.0->PyGithub>=2.1.0->-r requirements.txt (line 7))
  Using cached charset_normalizer-3.4.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (37 kB)
Collecting idna<4,>=2.5 (from requests>=2.14.0->PyGithub>=2.1.0->-r requirements.txt (line 7))
  Using cached idna-3.11-py3-none-any.whl.metadata (8.4 kB)
Collecting certifi>=2017.4.17 (from requests>=2.14.0->PyGithub>=2.1.0->-r requirements.txt (line 7))
  Using cached certifi-2026.1.4-py3-none-any.whl.metadata (2.5 kB)
Collecting anyio<5,>=3.6.2 (from starlette<0.51.0,>=0.40.0->fastapi>=0.110.0->-r requirements.txt (line 1))
  Using cached anyio-4.12.1-py3-none-any.whl.metadata (4.3 kB)
Collecting pycparser (from cffi>=2.0.0->pynacl>=1.4.0->PyGithub>=2.1.0->-r requirements.txt (line 7))
  Using cached pycparser-3.0-py3-none-any.whl.metadata (8.2 kB)
Using cached fastapi-0.128.0-py3-none-any.whl (103 kB)
Using cached uvicorn-0.40.0-py3-none-any.whl (68 kB)
Using cached pydantic-2.12.5-py3-none-any.whl (463 kB)
Using cached pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)
Using cached sqlalchemy-2.0.46-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (3.3 MB)
Using cached aiohttp-3.13.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (1.8 MB)
Using cached praw-7.8.1-py3-none-any.whl (189 kB)
Using cached pygithub-2.8.1-py3-none-any.whl (432 kB)
Using cached jinja2-3.1.6-py3-none-any.whl (134 kB)
Using cached python_multipart-0.0.22-py3-none-any.whl (24 kB)
Using cached aiohappyeyeballs-2.6.1-py3-none-any.whl (15 kB)
Using cached aiosignal-1.4.0-py3-none-any.whl (7.5 kB)
Using cached annotated_doc-0.0.4-py3-none-any.whl (5.3 kB)
Using cached annotated_types-0.7.0-py3-none-any.whl (13 kB)
Using cached attrs-25.4.0-py3-none-any.whl (67 kB)
Using cached click-8.3.1-py3-none-any.whl (108 kB)
Using cached frozenlist-1.8.0-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (242 kB)
Using cached greenlet-3.3.1-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (609 kB)
Using cached h11-0.16.0-py3-none-any.whl (37 kB)
Using cached markupsafe-3.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (22 kB)
Using cached multidict-6.7.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (256 kB)
Using cached prawcore-2.4.0-py3-none-any.whl (17 kB)
Using cached propcache-0.4.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (221 kB)
Using cached pyjwt-2.11.0-py3-none-any.whl (28 kB)
Using cached pynacl-1.6.2-cp38-abi3-manylinux_2_34_x86_64.whl (1.4 MB)
Using cached requests-2.32.5-py3-none-any.whl (64 kB)
Using cached starlette-0.50.0-py3-none-any.whl (74 kB)
Using cached typing_extensions-4.15.0-py3-none-any.whl (44 kB)
Using cached typing_inspection-0.4.2-py3-none-any.whl (14 kB)
Using cached update_checker-0.18.0-py3-none-any.whl (7.0 kB)
Using cached urllib3-2.6.3-py3-none-any.whl (131 kB)
Using cached websocket_client-1.9.0-py3-none-any.whl (82 kB)
Using cached yarl-1.22.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (377 kB)
Using cached anyio-4.12.1-py3-none-any.whl (113 kB)
Using cached certifi-2026.1.4-py3-none-any.whl (152 kB)
Using cached cffi-2.0.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (219 kB)
Using cached charset_normalizer-3.4.4-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (153 kB)
Using cached cryptography-46.0.4-cp311-abi3-manylinux_2_34_x86_64.whl (4.5 MB)
Using cached idna-3.11-py3-none-any.whl (71 kB)
Using cached pycparser-3.0-py3-none-any.whl (48 kB)
Installing collected packages: websocket-client, urllib3, typing-extensions, python-multipart, pyjwt, pycparser, propcache, multidict, MarkupSafe, idna, h11, greenlet, frozenlist, click, charset_normalizer, certifi, attrs, annotated-types, annotated-doc, aiohappyeyeballs, yarl, uvicorn, typing-inspection, sqlalchemy, requests, pydantic-core, jinja2, cffi, anyio, aiosignal, update_checker, starlette, pynacl, pydantic, prawcore, cryptography, aiohttp, praw, fastapi, PyGithub
Successfully installed MarkupSafe-3.0.3 PyGithub-2.8.1 aiohappyeyeballs-2.6.1 aiohttp-3.13.3 aiosignal-1.4.0 annotated-doc-0.0.4 annotated-types-0.7.0 anyio-4.12.1 attrs-25.4.0 certifi-2026.1.4 cffi-2.0.0 charset_normalizer-3.4.4 click-8.3.1 cryptography-46.0.4 fastapi-0.128.0 frozenlist-1.8.0 greenlet-3.3.1 h11-0.16.0 idna-3.11 jinja2-3.1.6 multidict-6.7.1 praw-7.8.1 prawcore-2.4.0 propcache-0.4.1 pycparser-3.0 pydantic-2.12.5 pydantic-core-2.41.5 pyjwt-2.11.0 pynacl-1.6.2 python-multipart-0.0.22 requests-2.32.5 sqlalchemy-2.0.46 starlette-0.50.0 typing-extensions-4.15.0 typing-inspection-0.4.2 update_checker-0.18.0 urllib3-2.6.3 uvicorn-0.40.0 websocket-client-1.9.0 yarl-1.22.0
🚀 Starting pi-core Demo Pipeline

1️⃣ Creating mock problem...
   ✅ Problem created: How to automate daily git commits
   📊 Confidence: 0.85, Frequency: 42

2️⃣ Defining product...
   ✅ Product defined: automate daily git commits - Template
   📦 Type: template
   💡 Value: Ready-to-use template that eliminates 'How to automate daily git commits' from your workflow.

3️⃣ Generating content and assets...
   ✅ Assets generated in: artifacts/f56ead22-4109-4a14-9145-87e97b112668
   📁 Files created: 5
      - INTEGRATION.md
      - USAGE.md
      - README.md
      - template/config.ini

4️⃣ Packaging for marketplace...
   ✅ Listing created: automate daily git commits - Template - Ready Template
   💰 Pricing: $24.99 (impulse) / $39.99 (anchor)
   📦 Bundle: f56ead22-4109-4a14-9145-87e97b112668.zip

✨ Demo Pipeline Complete!

Summary:
  - Problem discovered: How to automate daily git commits
  - Product created: automate daily git commits - Template (template)
  - Assets generated: 5 files
  - Marketplace listing: Ready with pricing and bundle

📊 View results:
  - Database: data/demo.db
  - Artifacts: artifacts
  - Product files: artifacts/f56ead22-4109-4a14-9145-87e97b112668

🌐 Start the dashboard to view in UI:
  python main.py

### 4) Artifacts (timestamps)
2026-01-31 17:42  ./IMPLEMENTATION_SUMMARY.md
2026-01-31 17:42  ./README.md
2026-01-31 17:43  ./artifacts/f56ead22-4109-4a14-9145-87e97b112668.zip
2026-01-31 17:43  ./artifacts/f56ead22-4109-4a14-9145-87e97b112668/INTEGRATION.md
2026-01-31 17:43  ./artifacts/f56ead22-4109-4a14-9145-87e97b112668/README.md
2026-01-31 17:43  ./artifacts/f56ead22-4109-4a14-9145-87e97b112668/USAGE.md
2026-01-31 17:43  ./data/demo.db

### 5) Zip contents
--- ./artifacts/f56ead22-4109-4a14-9145-87e97b112668.zip
Archive:  ./artifacts/f56ead22-4109-4a14-9145-87e97b112668.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
      286  2026-01-31 17:43   INTEGRATION.md
      262  2026-01-31 17:43   USAGE.md
      790  2026-01-31 17:43   README.md
      156  2026-01-31 17:43   template/config.ini
---------                     -------
     1494                     4 files

### 6) Checksums (run 1)
4b419373303c98b6a7cbd1e5cc278014cab1aa4e9d3c621f771dcfd640087a96  ./IMPLEMENTATION_SUMMARY.md
dc7c729fbaca4fbacf9100995255bf0486e257d3f5fc5f9ec834f8685a4337c5  ./README.md
1c854cd2de02145ddf99c5e1dcba6377621360ad2a39c40c1a1caff951919fa4  ./artifacts/f56ead22-4109-4a14-9145-87e97b112668/INTEGRATION.md
adf98e619f1659ddbbfd4cc58693444101c44068bcadd75c6228796fb97d1693  ./artifacts/f56ead22-4109-4a14-9145-87e97b112668/README.md
fd6ec95b8c228c062e4235d30847c218cd69900b72a0fe0488985e41066694fa  ./artifacts/f56ead22-4109-4a14-9145-87e97b112668/USAGE.md
f92978959918cb357161279f17b5b76f76965b7266df48a067b4edcc42f38984  ./data/demo.db

### 7) Demo run 2 + checksums (run 2)
🚀 Starting pi-core Demo Pipeline

1️⃣ Creating mock problem...
   ✅ Problem created: How to automate daily git commits
   📊 Confidence: 0.85, Frequency: 42

2️⃣ Defining product...
   ✅ Product defined: automate daily git commits - Template
   📦 Type: template
   💡 Value: Ready-to-use template that eliminates 'How to automate daily git commits' from your workflow.

3️⃣ Generating content and assets...
   ✅ Assets generated in: artifacts/03114c72-e8b2-4695-b171-c2a27748e1b0
   📁 Files created: 5
      - INTEGRATION.md
      - USAGE.md
      - README.md
      - template/config.ini

4️⃣ Packaging for marketplace...
   ✅ Listing created: automate daily git commits - Template - Ready Template
   💰 Pricing: $24.99 (impulse) / $39.99 (anchor)
   📦 Bundle: 03114c72-e8b2-4695-b171-c2a27748e1b0.zip

✨ Demo Pipeline Complete!

Summary:
  - Problem discovered: How to automate daily git commits
  - Product created: automate daily git commits - Template (template)
  - Assets generated: 5 files
  - Marketplace listing: Ready with pricing and bundle

📊 View results:
  - Database: data/demo.db
  - Artifacts: artifacts
  - Product files: artifacts/03114c72-e8b2-4695-b171-c2a27748e1b0

🌐 Start the dashboard to view in UI:
  python main.py
4b419373303c98b6a7cbd1e5cc278014cab1aa4e9d3c621f771dcfd640087a96  ./IMPLEMENTATION_SUMMARY.md
dc7c729fbaca4fbacf9100995255bf0486e257d3f5fc5f9ec834f8685a4337c5  ./README.md
1c854cd2de02145ddf99c5e1dcba6377621360ad2a39c40c1a1caff951919fa4  ./artifacts/03114c72-e8b2-4695-b171-c2a27748e1b0/INTEGRATION.md
adf98e619f1659ddbbfd4cc58693444101c44068bcadd75c6228796fb97d1693  ./artifacts/03114c72-e8b2-4695-b171-c2a27748e1b0/README.md
fd6ec95b8c228c062e4235d30847c218cd69900b72a0fe0488985e41066694fa  ./artifacts/03114c72-e8b2-4695-b171-c2a27748e1b0/USAGE.md
1c854cd2de02145ddf99c5e1dcba6377621360ad2a39c40c1a1caff951919fa4  ./artifacts/f56ead22-4109-4a14-9145-87e97b112668/INTEGRATION.md
adf98e619f1659ddbbfd4cc58693444101c44068bcadd75c6228796fb97d1693  ./artifacts/f56ead22-4109-4a14-9145-87e97b112668/README.md
fd6ec95b8c228c062e4235d30847c218cd69900b72a0fe0488985e41066694fa  ./artifacts/f56ead22-4109-4a14-9145-87e97b112668/USAGE.md
a8a6f0983f99ec6a8c6b974e924ccfa22c5d85e20b58570bad3f9768208e1b5a  ./data/demo.db

### 8) Secrets handling (no .env, env vars unset)
🚀 Starting pi-core Demo Pipeline

1️⃣ Creating mock problem...
   ✅ Problem created: How to automate daily git commits
   📊 Confidence: 0.85, Frequency: 42

2️⃣ Defining product...
   ✅ Product defined: automate daily git commits - Template
   📦 Type: template
   💡 Value: Ready-to-use template that eliminates 'How to automate daily git commits' from your workflow.

3️⃣ Generating content and assets...
   ✅ Assets generated in: artifacts/e8b06218-0d2f-4564-94ed-9bb68aa1c163
   📁 Files created: 5
      - INTEGRATION.md
      - USAGE.md
      - README.md
      - template/config.ini

4️⃣ Packaging for marketplace...
   ✅ Listing created: automate daily git commits - Template - Ready Template
   💰 Pricing: $24.99 (impulse) / $39.99 (anchor)
   📦 Bundle: e8b06218-0d2f-4564-94ed-9bb68aa1c163.zip

✨ Demo Pipeline Complete!

Summary:
  - Problem discovered: How to automate daily git commits
  - Product created: automate daily git commits - Template (template)
  - Assets generated: 5 files
  - Marketplace listing: Ready with pricing and bundle

📊 View results:
  - Database: data/demo.db
  - Artifacts: artifacts
  - Product files: artifacts/e8b06218-0d2f-4564-94ed-9bb68aa1c163

🌐 Start the dashboard to view in UI:
  python main.py
exit_code=0

### 9) No venv tracked
?? .venv_edit/
?? .venv_req/
no tracked venv dirs
no venv paths in history

