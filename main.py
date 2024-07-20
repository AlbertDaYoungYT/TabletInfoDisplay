import subprocess
import threading
import requests
import hashlib
import time
import uuid
import sys
import os


id = hashlib.md5(f"{uuid.uuid1()}-{time.time()}")
process = subprocess.Popen(["python3", "app.py", f"{id}"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)


try:
    # Check for patches and content updates

    while True:
        


except KeyboardInterrupt as k:
    print("Keyboard Interrupt")
    process.kill()
    exit(1)