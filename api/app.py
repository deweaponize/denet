from pathlib import Path

from pydantic import BaseModel
from fastapi import FastAPI
import json
import os
import subprocess

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from hashlib import md5

CWD = Path.cwd()
app = FastAPI()
BUILD_FILE = "build.json"
SECRET = "secret.json"

with open(os.path.join(CWD, SECRET)) as secret_file:
    FILE = json.load(secret_file)
    API = FILE["api"]
    PRIVATE = FILE["private"]

root_endpoint = "https://localhost:8000"


class ModelCommand(BaseModel):
    key: str
    command: str


class ModelReadRoot(BaseModel):
    key: str


def decrypt_data(encrypted_data, private_key):
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    decrypted_data = cipher.decrypt(encrypted_data)
    return decrypted_data


def run_command(run_command: str) -> str:
    process = subprocess.Popen(run_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode("utf-8")


@app.post("/fetch_script")
def read_root(item: ModelReadRoot):
    decrypt_key = decrypt_data(
        encrypted_data=item['key'],
        private_key=PRIVATE
    ).decode('utf-8')

    if md5(decrypt_key) == API:
        with open(os.path.join(CWD, BUILD_FILE), "r") as build_file:
            structure = json.load(build_file)
    else:
        out = {"response": "invalid API key"}

    return structure


@app.post("/command")
async def command(item: ModelCommand):
    decrypt_key = decrypt_data(
        encrypted_data=item['key'],
        private_key=PRIVATE
    ).decode('utf-8')
    decrypt_command = decrypt_data(
        encrypted_data=item['command'],
        private_key=PRIVATE
    ).decode('utf-8')

    if md5(decrypt_key) == API:
        out = run_command(
            run_command=decrypt_command
        )
    else:
        out = "invalid API key"

    return {"response": out}
