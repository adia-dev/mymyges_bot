# import os

# import discord
# from dotenv import load_dotenv

# from modules import login, data_manager, notification
# from utils import redis_manager

# load_dotenv()

# client = discord.Client()
# client = commands.Bot(command_prefix='/')


# @client.event
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')


# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('!login'):
#         username = message.content.split()[1]
#         password = message.content.split()[2]
#         token = login.get_token(username, password)
#         redis_manager.set_token(message.author.id, token)
#         await message.channel.send(f'{message.author.mention} has logged in successfully!')

# client.run(os.getenv('DISCORD_TOKEN'))
