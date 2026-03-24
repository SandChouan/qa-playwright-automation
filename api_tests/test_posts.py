from utils.api_client import get_posts, get_post

def test_get_posts():
    response = get_posts()

    assert response.status_code == 200
    data = response.json()

    assert len(data) > 0


def test_get_single_post():
    response = get_post(1)

    assert response.status_code == 200
    assert response.json()["id"] == 1