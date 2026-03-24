import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_posts():
    return requests.get(f"{BASE_URL}/posts")

def get_post(post_id):
    return requests.get(f"{BASE_URL}/posts/{post_id}")