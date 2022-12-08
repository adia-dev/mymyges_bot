import discord
from discord.ext import commands
from modules import login, data_manager, notification
from utils import redis_manager


class Playground(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """
        The on_ready event is called when the bot is ready to receive commands.
        """
        print(f'{self.bot.user} has connected to Discord!')
        await self.bot.change_presence(activity=discord.Game(name="MyGES"))
        # send a message to the #general channel
        await self.bot.get_channel(1050377835874877493).send('Bot is ready!')

    @commands.command()
    async def login(self, ctx, username: str, password: str):
        """
        A command that logs in to a website using the provided username and password,
        retrieves the token, and saves it in Redis.

        Args:
            ctx (discord.ext.commands.Context): The context of the command.
            username (str): The username to use when logging in.
            password (str): The password to use when logging in.
        """
        token = login.get_token(username, password)
        redis_manager.set_token(ctx.message.author.id, token)
        await ctx.send(f'{ctx.message.author.mention} has logged in successfully!')

    @commands.command()
    async def hello(self, ctx):
        """
            The hello command sends a "hello world" message to the Discord channel where the command was called.

            Parameters:
                ctx (discord.ext.commands.Context): The context in which the command was called.
            """

        # Use the send method of the ctx object to send a message to the Discord channel
        await ctx.send('Hello world!')

    @commands.command()
    async def insult(self, ctx, user: discord.Member):
        """
        The insult command sends an insult to the user mentioned in the command.

        Parameters:
            ctx (discord.ext.commands.Context): The context in which the command was called.
            user (discord.Member): The user to insult.
        """
        await ctx.send(f'{user.mention} imbecile')

    # add a listener for the on_message event when somebody other than @adia is sending a message
    @commands.Cog.listener()
    async def on_message(self, message):
        """
        The on_message event is called when a message is sent in a Discord channel.

        Parameters:
            message (discord.Message): The message that was sent.
        """
        if message.author != self.bot.user:
            # send a message to the #general channel
            await self.bot.get_channel(1049986177635201056).send(f'{message.author.mention} arrête de parler !')


async def setup(bot):
    print('Playground cog loaded')
    await bot.add_cog(Playground(bot))
