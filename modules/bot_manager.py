import os
import discord
import asyncio
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
        self._last_member = None

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

        # Run the Discord bot using the DISCORD_TOKEN environment variable
        self.bot.run(os.environ["DISCORD_TOKEN"])
        # asyncio.run(self.load_extensions())

    @commands.command()
    async def load(self, ctx, extension):
        self.bot.load_extension(f'modules.cogs.{extension}')

    @commands.command()
    async def unload(self, ctx, extension):
        self.bot.unload_extension(f'modules.cogs.{extension}')


def setup(bot):
    print('BotManager cog loaded')
    bot.add_cog(BotManager(bot))
