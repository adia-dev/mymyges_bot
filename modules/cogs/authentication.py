import os
import discord
from discord.ext import commands
from discord import app_commands
from modules import login, data_manager
from utils import redis_manager
from discord.ext.commands import Greedy, Context
from typing import Literal, Optional
from modules.login import get_token
from modules.data_manager import save_data


class Authentication(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="login", description="Login to MyGES")
    @app_commands.describe(username="username", password="password")
    async def login(self, interaction: discord.Interaction, username: str, password: str) -> None:
        """
        This command logs in to the bot using the given username and password.

        :param interaction: The interaction context, containing information about the user who invoked the command
        :type interaction: discord.Interaction
        :param username: The username to log in with
        :type username: str
        :param password: The password to log in with
        :type password: str
        :return: None
        """
        # print a message to the console that the bot is thinking
        # await interaction.response.defer(ephemeral=True)

        # Call the get_token function from the login module to get the access token

        token = get_token(username, password)

        if token is None:
            await interaction.response.send_message("Invalid credentials", ephemeral=True)
        else:
            print(f"User id: {interaction.user.id}")
            data_manager.save_data(
                f"data/users/{interaction.user.id}", "token.txt", token)
            redis_manager.set_token(interaction.user.id, token)
            await interaction.response.send_message("Successfully logged in", ephemeral=True)

    @app_commands.command(name="token", description="Get your access token")
    async def token(self, interaction: discord.Interaction) -> None:
        """
        This command gets the access token for the user who invoked it.

        :param interaction: The interaction context, containing information about the user who invoked the command
        :type interaction: discord.Interaction
        :return: None
        """
        # print a message to the console that the bot is thinking
        # await interaction.response.defer(ephemeral=True)

        # Get the token from the data file
        token = redis_manager.get_token(interaction.user.id)

        if token is None:
            await interaction.response.send_message("You are not logged in, use /login to log in", ephemeral=True)
        else:
            await interaction.response.send_message(f"Your access token: {token}", ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(Authentication(bot))
