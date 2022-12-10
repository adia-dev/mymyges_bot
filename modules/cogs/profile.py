import discord
from discord.ext import commands
from discord import app_commands
from utils import redis_manager, endpoints
from modules import user
from modules.user import get_profile


class Profile(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="profile", description="Get your profile")
    async def profile(self, interaction: discord.Interaction) -> None:
        token = redis_manager.get_token(interaction.user.id)
        if token is None:
            await interaction.response.send_message("You need to login first, use /login to log in", ephemeral=True)
        else:
            profile = user.get_profile(token)
            # embed = discord.Embed(title="Profile", description="Your profile")
            embed = discord.Embed(title="Profile", description="Your profile")
            embed.set_author(name=profile["firstname"] + " " + profile["name"])
            embed.set_thumbnail(url=profile["picture"])
            embed.add_field(name="Civility",
                            value=profile["civility"], inline=True)
            embed.add_field(name="Email", value=profile["email"], inline=True)
            embed.set_footer(text="MyMyGES Bot")
            await interaction.response.send_message(embed=embed, ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(Profile(bot))
