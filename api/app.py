from pathlib import Path

from fastapi import FastAPI
import json
import os

CWD = Path.cwd()
app = FastAPI()
BUILD_FILE = "build.json"

root_endpoint = "https://localhost:8000"


@app.get("/fetch_script")
def read_root():
    with open(os.path.join(CWD, BUILD_FILE), "r") as build_file:
        structure = json.load(build_file)
    return structure

