from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restplus import Api, Resource, fields
from dotenv import load_dotenv
from pathlib import Path

import os
import subprocess
import json

# Setting up environment

FLASK_DEBUG=1

project_folder = subprocess.check_output("pwd", shell=True)
print(project_folder.decode("utf-8"))
load_dotenv(os.path.join(project_folder.decode("utf-8"), '.env'))
PORT = os.getenv('PGPORT')
PASSWORD = os.getenv('PGPASSWORD')
print(PORT)