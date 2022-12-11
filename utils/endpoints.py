# Description: List of all endpoints used by the API
# ENDPOINTS = [
#     "/me/profile",
#     "/me/years",
#     "/me/agenda?start={start}&end={end}",
#     "/me/{year}/grades",
#     "/me/{year}/classes",
#     "/me/{year}/courses",
#     "/me/{year}/teachers",
#     "/me/news",
# ]

# store the endpoints in a dictionary, with the key being the endpoint name and the value being the endpoint itself
import os
import requests


ENDPOINTS = {
    "profile": "/me/profile",
    "years": "/me/years",
    "agenda": "/me/agenda?start={start}&end={end}",
    "grades": "/me/{year}/grades",
    "classes": "/me/{year}/classes",
    "courses": "/me/{year}/courses",
    "teachers": "/me/{year}/teachers",
    "news": "/me/news",
}


def get_endpoint(endpoint: str, **kwargs) -> str:
    """Get an endpoint from the list of endpoints

    Args:
        endpoint (str): Endpoint to get

    Returns:
        str: Endpoint
    """
    if endpoint in ENDPOINTS:
        return os.getenv("GES_API_URL") + ENDPOINTS[endpoint].format(**kwargs)
    else:
        return None


def get_request(endpoint: str, token: str, **kwargs) -> dict:
    """Make a GET request to the API

    Args:
        endpoint (str): Endpoint to request
        token (str): User's token
        **kwargs: Parameters to pass to the endpoint


    Returns:
        dict: Response
    """
    url = get_endpoint(endpoint, **kwargs)

    headers = {
        'Authorization': 'Bearer ' + token,
    }

    session = requests.Session()
    session.max_redirects = 1

    try:
        response = session.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.HTTPError as e:
        print(e)
        return None
