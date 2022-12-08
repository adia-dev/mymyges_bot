import os
import discord
import asyncio
from discord.ext import commands

from modules.bot_manager import BotManager
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix='/',
                   description='A bot that fetches MyGES data and sends notifications to users via Discord !', intents=discord.Intents.all())


async def load_extensions():
    for filename in os.listdir("./modules/cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            return await bot.load_extension(f"modules.cogs.{filename[:-3]}")


asyncio.run(load_extensions())

manager = BotManager(bot)
manager.run()
