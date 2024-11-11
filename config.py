import os
from dotenv import load_dotenv

base_dir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(base_dir, ".env"))

APIKEY = os.environ.get("KEY") or "Not Available"

if APIKEY == "Not Available":
    raise Exception("APIKEY not found, add KEY to .env file in main directory")