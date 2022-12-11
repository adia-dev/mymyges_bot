import os

import discord
import requests
from discord.ext import commands

from utils.endpoints import get_request


def get_profile(token: str) -> dict:
    """
    Gets the profile of the user.

    Args:
        token (str): The user's token.

    Returns:
        dict: The user's profile.
    """

    data = get_request("profile", token)

    if data is None:
        return None

    json = data["result"]
    photo = {key: json["_links"][key]
             for key in ["photo"]}["photo"]["href"]
    filtered_json = {key: json[key] for key in [
        "firstname", "name", "civility", "email"]}
    filtered_json["picture"] = photo
    return filtered_json


def get_grades(token: str, year: int = 2021) -> dict:
    """
    Gets the grades of the user.

    Args:
        token (str): The user's token.
        year (int, optional): The year to get the grades from. Defaults to 2021.

    Returns:
        dict: The grades of the user.
    """

    data = get_request("grades", token, year=year)

    if data is None:
        return None

    return data["result"]
