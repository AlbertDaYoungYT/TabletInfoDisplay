import subprocess
import threading
import requests
import hashlib
import json
import time
import uuid
import sys
import os

patch_uri = "https://raw.githubusercontent.com/AlbertDaYoungYT/TabletInfoDisplay/main/patches.json"

id = hashlib.md5(f"{uuid.uuid1()}-{time.time()}")
process = subprocess.Popen(["python3", "app.py", f"{id}"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)


try:
    # Check for patches and content updates

    while True:
        time.sleep(10)
        patches = json.loads(requests.get(patch_uri).text)


        open("patches.json", "w").write(json.dumps(patches))


except KeyboardInterrupt as k:
    print("Keyboard Interrupt")
    process.kill()
    exit(1)