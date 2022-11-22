import requests
from whoop import secrets, proxies

recovery_url = "https://api.prod.whoop.com/developer/v1/recovery"


def get_latest_recovery_score():
    response = requests.get(url=recovery_url, headers={"Authorization": f"Bearer {secrets.access_token}"}, params={"limit": 1}, proxies=proxies.oauth_proxies)
    return response.json()["records"][0]["score"]["recovery_score"]
