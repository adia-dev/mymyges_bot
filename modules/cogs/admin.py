import asyncio
import datetime
import time
import discord
from discord.ext import commands
from discord import app_commands
from modules import login, data_manager, notification
from utils import redis_manager
from discord.ext.commands import Greedy, Context
from typing import Literal, Optional


class Admin(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        # print the bot's name and id and a timestamp
        timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        name = self.bot.user.name
        id = self.bot.user.id
        print(f'{timestamp} - Logged in as {name} (ID: {id})')
        # print the guilds the bot is connected to
        print(f'{timestamp} - Connected to the following guilds:')
        print('----------------------------------------------')
        for guild in self.bot.guilds:
            print(f'{guild.name} (ID: {guild.id})')
        print('----------------------------------------------')
        await self.bot.change_presence(activity=discord.Game(name="hacker MyGES"))

    @commands.command()
    async def sync(self, ctx):
        try:
            synced = await self.bot.tree.sync()
            print(f"Synced {len(synced)} commands")
            await ctx.send(f"Synced {synced} commands")
        except Exception as e:
            print(e)

    @commands.command()
    async def clear_commands(self, ctx):
        try:
            await self.bot.tree.clear_commands(guild=discord.Object(id=1041807074943844412))
            synced = await self.bot.tree.sync()
            print(f"Deleted {len(synced)} commands")
            await ctx.send(f"Deleted {synced} commands")
        except Exception as e:
            print(e)

    @commands.command()
    async def clear_chat(self, ctx: Context):
        await ctx.message.delete()
        await ctx.channel.purge(limit=1000)


async def setup(bot: commands.Bot):
    await bot.add_cog(Admin(bot))
