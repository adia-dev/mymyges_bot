import os

import discord
import requests
from discord.ext import commands

from utils.endpoints import get_endpoint


def get_profile(token: str) -> dict:
    """
    Gets the profile of the user.

    Args:
        token (str): The user's token.

    Returns:
        dict: The user's profile.
    """

    url = get_endpoint("profile")

    headers = {
        'Authorization': 'Bearer ' + token,
    }

    session = requests.Session()
    session.max_redirects = 1

    try:
        response = session.get(url, headers=headers)
        if response.status_code == 200:
            # only keep the fields that are needed
            # firstname, name, civility, email, picture
            json = response.json()["result"]
            photo = {key: json["_links"][key]
                     for key in ["photo"]}["photo"]["href"]
            filtered_json = {key: json[key] for key in [
                "firstname", "name", "civility", "email"]}
            filtered_json["picture"] = photo
            return filtered_json
    except requests.exceptions.HTTPError as e:
        print(e)
        return None
