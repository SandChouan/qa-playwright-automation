import json
from pathlib import Path

#from utils.data_loader import load_json_data
from utils.data_loader import load_test_data

DEFAULTS = {
    "BASE_URL": "https://www.saucedemo.com/",
    "USERNAME": "standard_user",
    "PASSWORD": "secret_sauce",
}

CONFIG_FILE = Path(__file__).resolve().parent / "test_data.json"

try:
    _config = load_json_data(CONFIG_FILE)
except Exception:
    _config = {}

login_data = _config.get("login", {})
api_data = _config.get("api", {})

BASE_URL = api_data.get("base_url", DEFAULTS["BASE_URL"])
USERNAME = login_data.get("username", DEFAULTS["USERNAME"])
PASSWORD = login_data.get("password", DEFAULTS["PASSWORD"])
