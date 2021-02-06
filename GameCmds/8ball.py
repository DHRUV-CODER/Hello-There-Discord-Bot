import discord
from discord.ext import commands
import random
from random import choice


class ball(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# 8ball game
    @commands.command(aliases=['8ball', '8 ball', 'predict'])
    async def _8ball(self,ctx, *, question):
        responses = [
            "It is certain.", "It is decidedly so.", "Without a doubt.",
            "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
            "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
            "Reply hazy, try again.", "Ask again later.",
            "Better not tell you now.", "Cannot predict now.",
            "Concentrate and ask again.", "Don't count on it.", "My reply is no.",
            "My sources say no.", "Outlook not so good.", "Very doubtful."
        ]
        embed = discord.Embed(title="")
        embed.set_author(
            name="Ball",
            icon_url=
            "https://img1.pnghut.com/13/18/1/4RJHCeMqkc/billiard-ball-indoor-games-and-sports-pool-eightball.jpg"
        )
        embed.add_field(name="Question", value=f"{question}", inline=True)
        embed.add_field(name="Answer",
                        value=f"{random.choice(responses)}",
                        inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(ball(bot))
