import discord
from discord.ext import commands
from discord import app_commands
from utils import redis_manager, endpoints
from modules import user


class User(commands.Cog):

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

    @app_commands.command(name="grades", description="Get your grades")
    @app_commands.describe(year="The year to get the grades from", course="The course to get the grades from")
    @app_commands.choices(year=[
        app_commands.Choice(name="2022", value=2022),
        app_commands.Choice(name="2021", value=2021),
    ])
    @app_commands.choices(course=[
        app_commands.Choice(
            name="Unity", value="S2 - infographie et 3d avec unity"),
        app_commands.Choice(name="Algorithme Avancé",
                            value="S2 - algorithmique avancée"),
        app_commands.Choice(name="Développement mobile Android",
                            value="S2 - développement mobile android"),
        app_commands.Choice(name="Introduction au cloud",
                            value="S1 - introduction au cloud"),
        app_commands.Choice(name="Mission en entreprise",
                            value="S1 - mission en entreprise"),
        app_commands.Choice(name="Introduction à la gestion de projet",
                            value="S2 - introduction à la gestion de projets"),
        app_commands.Choice(name="Versioning avec git et GitHub",
                            value="S1 - versioning avec git et github"),
        app_commands.Choice(name="Langage C avancé",
                            value="S1 - langage c avancé"),
        app_commands.Choice(name="Programmation orientée objet et langage Java",
                            value="S2 - programmation orientée objet et langage java"),
        app_commands.Choice(name="Mathématiques et infographie",
                            value="S1 - mathématiques et infographie"),
        app_commands.Choice(
            name="Assembleur", value="S1 - architecture et programmation assembleur"),
        app_commands.Choice(name="Projet Annuel", value="S2 - projet annuel"),
        app_commands.Choice(name="Théorie des systèmes d'exploitation",
                            value="S1 - théorie des systèmes d'exploitation"),
        app_commands.Choice(name="Sécurité et vulnérabilités informatiques",
                            value="S1 - sécurité et vulnérabilités informatiques"),
        app_commands.Choice(name="Développement Web et API",
                            value="S2 - développement web et api"),
        app_commands.Choice(name="Programmation WebGL",
                            value="S1 - programmation webgl"),
        app_commands.Choice(
            name="Anglais", value="Anglais 2: informatique, expression orale et écrite"),
        app_commands.Choice(name="Administration et maintenance Windows Server",
                            value="S1 - administration et maintenance windows server"),
        app_commands.Choice(name="Virtualisation des réseaux",
                            value="S2 - virtualisation des réseaux"),
        app_commands.Choice(name="Linux administration",
                            value="S2 - linux administration"),
        app_commands.Choice(name="Modélisation UML 2",
                            value="S2 - modélisation uml 2"),
    ])
    async def grades(self, interaction: discord.Interaction, year: int = 2021, course: str = None) -> None:
        token = redis_manager.get_token(interaction.user.id)
        if token is None:
            await interaction.response.send_message("You need to login first, use /login to log in", ephemeral=True)
        else:
            grades = user.get_grades(token, year)
            if course is not None and course in [grade["course"] for grade in grades]:
                grades = [grade for grade in grades if grade["course"] == course]
            embed = discord.Embed(title="Grades", description="Your grades")
            for grade in grades:
                # embed the key and value of the grade
                embed.add_field(
                    name="Course", value=grade["course"], inline=True)
                embed.add_field(
                    name="Exam", value=f"`{grade['exam']}`", inline=True)
                embed.add_field(
                    name="Grades", value=grade["grades"], inline=True)
                embed.add_field(name="CC average",
                                value=grade["ccaverage"], inline=True)
                embed.add_field(
                    name="Average", value=grade["average"], inline=True)
                embed.add_field(name="ECTS", value=grade["ects"], inline=True)
                # empty field to separate the grades
                embed.add_field(name="\u200b", value="\u200b", inline=False)

            embed.set_footer(text="MyMyGES Bot")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            # await interaction.response.send_message("No grades found for this year", ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(User(bot))
