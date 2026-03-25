import json
from pathlib import Path


def load_test_data():
    with open("config/test_data.json") as f:
        return json.load(f)


def load_json_data(path):
    """Load JSON data from a filesystem path.

    Args:
        path (str | Path): Path to a JSON file.

    Returns:
        dict: Parsed JSON data.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If JSON is invalid.
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"JSON data file not found: {p}")

    with p.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, dict):
        raise ValueError(f"Expected JSON object in {p}, got {type(data).__name__}")

    return data
