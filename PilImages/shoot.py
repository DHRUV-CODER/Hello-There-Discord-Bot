import discord
from discord.ext import commands
import datetime
import asyncio
import random
from PIL import Image
from io import BytesIO


class Wanted(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def shoot(self, ctx, user: discord.Member = None):
        if not user:
            user = ctx.author

        wanted = Image.open("./images/shoot.jpg")

        asset = user.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((501, 481))
        wanted.paste(pfp, (1349, 397))

        wanted.save("./finalimages/shooted.jpg")

        await ctx.send(file=discord.File("./finalimages/shooted.jpg"))


def setup(bot):
    bot.add_cog(Wanted(bot))
