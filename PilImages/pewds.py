import discord
from discord.ext import commands
import datetime
import asyncio
import random
from PIL import Image
from io import BytesIO


class Pewd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pewdme(self, ctx, user: discord.Member = None):
        if not user:
            user = ctx.author

        wanted = Image.open("./images/pewd.png")

        asset = user.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((357, 353))
        wanted.paste(pfp, (277, 277))

        wanted.save("./finalimages/pewdlogo.png")

        await ctx.send(file=discord.File("./finalimages/pewdlogo.png"))


def setup(bot):
    bot.add_cog(Pewd(bot))
