from requests_oauthlib import OAuth2Session
from whoop import secrets
import secret_helper
from urllib import parse
import schedule

auth_url = "https://api.prod.whoop.com/oauth/oauth2/auth"
token_url = "https://api.prod.whoop.com/oauth/oauth2/token"
redirect_url = "http://localhost"
scopes = ["read:recovery",
          "read:cycles",
          "read:workout",
          "read:sleep",
          "read:profile",
          "read:body_measurement",
          "offline"]

oauth = OAuth2Session(secrets.client_id, redirect_uri=redirect_url, scope=scopes)


def authenticate(get_code):
    if get_code:
        # Get auth URL for this app
        authorization_url, state = oauth.authorization_url(auth_url)
        print(f"Log in and authorize: {authorization_url}")
        # User logs in, get tokens from pasted redirect with code
        redirected_url = input("Then paste redirect url: ")
        code = parse.parse_qs(parse.urlparse(redirected_url).query)["code"][0]
        response = oauth.fetch_token(token_url=token_url, include_client_id=True, code=code, client_secret=secrets.client_secret)
        secret_helper.update_secrets_from_response(response=response)
    else:
        refresh_token()


def refresh_token():
    response = oauth.refresh_token(token_url=token_url, include_client_id=True, refresh_token=secrets.refresh_token, client_secret=secrets.client_secret)
    print(f"refresh token response: {response}")
    secret_helper.update_secrets_from_response(response=response)
    return response


def setup_token_refresh_scheduler():
    schedule.every().day.at("07:45").do(refresh_token)
