import os
import requests

LOGIN_URL = os.getenv('LOGIN_URL')


def get_token(username: str, password: str) -> str:
    """
    Logs in to a website using the provided username and password, and retrieves the token.

    Args:
        username (str): The username to use when logging in.
        password (str): The password to use when logging in.

    Returns:
        str: The token retrieved from the website.
    """
    payload = {
        'username': username,
        'password': password
    }

    response = requests.post(LOGIN_URL, json=payload)
    if response.status_code != 200:
        raise ValueError('Failed to login: Invalid credentials')

    return response.json()['token']
