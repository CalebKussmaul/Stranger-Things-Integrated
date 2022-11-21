from whoop import secrets
import importlib

secrets_file = "secrets.py"


def update_secrets_from_response(response):
    secrets.access_token = response["access_token"]
    secrets.refresh_token = response["refresh_token"]
    secrets.expires_at = response["expires_at"]
    write_secrets()


def write_secrets():
    write(client_id=secrets.client_id,
          client_secret=secrets.client_secret,
          expires_at=secrets.expires_at,
          access_token=secrets.access_token,
          refresh_token=secrets.refresh_token)
    importlib.reload(secrets)


def quote(string):
    return f"\"{string}\""


def write(client_id, client_secret, expires_at, access_token, refresh_token):
    f = open(secrets_file, "w")
    f.write(f"client_id = { quote(client_id) if client_id else 'None' }\n")
    f.write(f"client_secret = { quote(client_secret) if client_secret else 'None' }\n")
    f.write(f"expires_at = { expires_at if expires_at else 'None' }\n")
    f.write(f"access_token = { quote(access_token) if access_token else 'None' }\n")
    f.write(f"refresh_token = { quote(refresh_token) if refresh_token else 'None' }\n")
