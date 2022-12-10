import os
import requests
import base64
import asyncio


class TokenError(Exception):
    """
    This exception is raised when an error occurs while getting an access token.
    """
    pass


def get_token(username: str, password: str):
    # Encode the username and password as a base64 string
    credentials = base64.b64encode(
        f"{username}:{password}".encode("utf-8")).decode("utf-8")

    # Set the URL for the login endpoint
    login_url = os.getenv("GES_AUTH_URL")

    # Set the headers for the request, including the encoded credentials in the Authorization header
    headers = {
        "Authorization": f"Basic {credentials}",
    }

    session = requests.Session()
    session.max_redirects = 1

    try:
        session.get(login_url, headers=headers)
        return None
    # except status_code == 401:
    except requests.exceptions.HTTPError as e:
        print(e)
        return None
    except Exception as e:
        # Split the error message on the : character
        parts = str(e).split("#")
        # Access the second element of the resulting list to get the URL
        token = parts[1].strip()
        # Split the string on the & character
        parts = token.split("&")

        # Create a list of tuples, where each tuple contains a key and a value
        pairs = [(part.split("=")[0], part.split("=")[1]) for part in parts]

        # Use the dict() constructor to create a dictionary from the list of tuples
        dictionary = dict(pairs)

        return dictionary["access_token"]
