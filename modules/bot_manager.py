import os

import discord
from discord.ext import commands


class BotManager():
    """
    The BotManager class is used to initialize and run a Discord bot.

    Attributes:
        client (discord.ext.commands.Bot): The Discord client instance.
    """

    def __init__(self, bot):
        """
        Initializes a new instance of the BotManager class.
        """
        self.bot = bot

    def run(self):
        """
        Runs the Discord bot by calling the `client.run` method.
        """
        # Check if the DISCORD_TOKEN environment variable is defined
        if "DISCORD_TOKEN" not in os.environ:
            raise ValueError(
                "The DISCORD_TOKEN environment variable is not defined")

        # Check if the DISCORD_TOKEN environment variable is None
        if os.environ["DISCORD_TOKEN"] is None:
            raise ValueError("The DISCORD_TOKEN environment variable is None")

        self.bot.run(os.getenv("DISCORD_TOKEN"))

    async def start(self):
        """
        Runs the Discord bot by calling the `client.run` method.
        """
        # Check if the DISCORD_TOKEN environment variable is defined
        if "DISCORD_TOKEN" not in os.environ:
            raise ValueError(
                "The DISCORD_TOKEN environment variable is not defined")

        # Check if the DISCORD_TOKEN environment variable is None
        if os.environ["DISCORD_TOKEN"] is None:
            raise ValueError("The DISCORD_TOKEN environment variable is None")

        await self.bot.start(os.getenv("DISCORD_TOKEN"))
