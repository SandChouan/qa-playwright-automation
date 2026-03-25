import pytest
import requests
from utils.data_loader import load_test_data


def test_get_posts():
    data = load_test_data()
    base_url = data["api"]["base_url"]

    response = requests.get(f"{base_url}/posts")

    # Status Code prüfen
    assert response.status_code == 200

    # Response Inhalt prüfen
    json_data = response.json()
    assert isinstance(json_data, list)
    assert len(json_data) > 0

    # Struktur prüfen
    first_post = json_data[0]
    assert "id" in first_post
    assert "title" in first_post