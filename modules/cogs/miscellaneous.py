import os
import discord
from discord.ext import commands
from discord import app_commands
from modules import login, data_manager, notification
from utils import redis_manager
from discord.ext.commands import Greedy, Context
from typing import Literal, Optional
from modules.login import get_token
from modules.data_manager import save_data


class Miscellaneous(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="whocares", description="Rappeler a une personne qu'on s'en fou ne fait pas de mal")
    @app_commands.describe(target="target")
    async def whocares(self, interaction: discord.Interaction, target: discord.Member) -> None:
        """
        This command logs in to the bot using the given username, to remind a person that we don't care about him.

        :param interaction: The interaction context, containing information about the user who invoked the command
        :type interaction: discord.Interaction
        :param target: The username to log in with
        :type target: str
        :return: None
        """

        if target is None:
            await interaction.response.send_message("Tu n'as pas mentionné de personne", ephemeral=True)
        elif os.getenv("OWNER_ID") == str(target.id):
            await interaction.response.send_message(f"{target.mention} c'est trop cool ahah ! merci de me faire part de ce savoir grand frère !")
        else:
            await interaction.response.send_message(f"{target.mention} on s'en fou !")


async def setup(bot: commands.Bot):
    await bot.add_cog(Miscellaneous(bot))
