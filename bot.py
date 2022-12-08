import os
import discord
from discord.ext import commands

from modules.bot_manager import BotManager
from dotenv import load_dotenv

load_dotenv()

manager = BotManager()
manager.run()
