import datetime
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
        await self.bot.change_presence(activity=discord.Game(name="vec tes sentiments"))
        await self.bot.tree.sync(guild=discord.Object(id=1041807074943844412))

    @app_commands.command(name="introduce_me", description="Test command")
    async def my_command(self, interaction: discord.Interaction) -> None:
        """ /introduce_me """
        await interaction.response.send_message("Hello from command 1!", ephemeral=True)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

    @commands.command()
    @commands.guild_only()
    @commands.is_owner()
    async def sync(
            ctx: Context, guilds: Greedy[discord.Object], spec: Optional[Literal["~", "*", "^"]] = None) -> None:
        print(guilds)
        if not guilds:
            if spec == "~":
                synced = await ctx.bot.tree.sync(guild=ctx.guild)
            elif spec == "*":
                ctx.bot.tree.copy_global_to(guild=ctx.guild)
                synced = await ctx.bot.tree.sync(guild=ctx.guild)
            elif spec == "^":
                ctx.bot.tree.clear_commands(guild=ctx.guild)
                await ctx.bot.tree.sync(guild=ctx.guild)
                synced = []
            else:
                synced = await ctx.bot.tree.sync()

            await ctx.send(
                f"Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}"
            )
            return

        ret = 0
        await ctx.bot.tree.sync(guild=discord.Object(id=1041807074943844412))
        ret += 1
        # for guild in guilds:
        #     try:
        #     except discord.HTTPException:
        #         pass
        #     else:
        #         ret += 1

        await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")


async def setup(bot: commands.Bot):
    await bot.add_cog(Admin(bot))
