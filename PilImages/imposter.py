import discord
from discord.ext import commands
import datetime
import asyncio
import random
from PIL import Image
from io import BytesIO


class Imposter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def imposter(self, ctx, user: discord.Member = None):
        if not user:
            user = ctx.author

        wanted = Image.open("./images/amongus.png")

        asset = user.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((134, 100))
        wanted.paste(pfp, (99, 68))

        wanted.save("./finalimages/imposter.png")

        await ctx.send(file=discord.File("./finalimages/imposter.png"))


def setup(bot):
    bot.add_cog(Imposter(bot))
