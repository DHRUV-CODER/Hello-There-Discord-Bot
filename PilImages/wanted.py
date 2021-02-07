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
    async def wanted(self, ctx, user: discord.Member = None):
        if not user:
            user = ctx.author

        wanted = Image.open("./images/wanted.jpg")

        asset = user.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((298, 298))
        wanted.paste(pfp, (84, 190))

        wanted.save("./finalimages/profile.jpg")

        await ctx.send(file=discord.File("./finalimages/profile.jpg"))


def setup(bot):
    bot.add_cog(Wanted(bot))
