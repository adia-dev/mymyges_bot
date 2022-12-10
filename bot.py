import os
import discord
import asyncio
from discord.ext import commands
from discord import app_commands

from modules.bot_manager import BotManager
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix='/',
                   description='A bot that fetches MyGES data and sends notifications to users via Discord !', intents=discord.Intents.all())
manager = BotManager(bot)


async def load_extensions():
    for filename in os.listdir("./modules/cogs"):
        if filename.endswith(".py"):
            try:
                # cut off the .py from the file name
                name = filename[:-3]
                await bot.load_extension(f"modules.cogs.{name}")
                print(f"~ Successfully loaded {name} cog ~")
            except Exception as e:
                print(e)
                print(f"{filename[:-3]} cannot be loaded:")


async def main():
    await load_extensions()
    await manager.start()

asyncio.run(main())
