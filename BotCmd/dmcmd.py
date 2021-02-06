import discord
from discord.ext import commands


class DmCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


#Send anonymous DM's
    @commands.command()
    async def send_anonymous_dm(self,ctx, member: discord.Member, *, content):
        channel = await member.create_dm(
        )  # creates a DM channel for mentioned user
        await channel.send(
            f'**Somebody Sent Anonymous Message Saying:** ||  {content}  ||'
        )  # send whatever in the content to the mentioned user.


    # Usage: !send_anonymous_dm @mention_user <your message here>


    # THIS FUNCTION WILL SEND A DM WITH THE AUTHORS NAME.
    @commands.command()
    async def sendDM(self,ctx, member: discord.Member, *, content):
        channel = await member.create_dm(
        )  # creates a DM channel for mentioned user
        await channel.send(
            f"**{ctx.message.author} said:** {content}"
        )  # send whatever in the content to the mentioned user along with the author's name.


    # Usage: !send_anonymous_dm @mention_user <your message here>


def setup(bot):
    bot.add_cog(DmCmd(bot))
