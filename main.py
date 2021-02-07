import discord
import keep_alive
import os
import json
import asyncio
from discord.ext import commands
import urllib
import traceback
import sys

intents = discord.Intents(messages=True,
                          guilds=True,
                          reactions=True,
                          members=True,
                          presences=True)
# getting my credentials
token = os.environ.get('DISCORD_BOT_SECREAT')


def get_prefix(client, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    try:
        x = prefixes.get(str(message.guild.id), "?")
        client.prefix = x
        return x
    except:
        pass


client = commands.Bot(command_prefix=get_prefix, intents=intents)


# Gets The Prefix
@client.event
async def on_guild_join(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    prefixes[str(guild.id)] = "?"
    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)


# Set your own preifx
@client.command(aliases=['setprefix', 'newprefix'])
@commands.has_permissions(administrator=True)
async def set_prefix(ctx, prefix):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    prefixes[str(ctx.guild.id)] = prefix
    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)
    # await ctx.send(f"Server prefix changed to: `{prefix}`")
    embed = discord.Embed(title=f"Prefix Changed {prefix}",
                          description="  ",
                          color=0x28fdfd)
    embed.add_field(name="Changed By:",
                    value=ctx.message.author.mention,
                    inline=True)
    embed.add_field(name="New Prefix:", value=f"**{prefix}**", inline=False)
    await ctx.send(embed=embed)
    client.prefix = prefix


@client.event
async def on_ready():
    print("On Ready Function Working")
    await client.change_presence(activity=discord.Activity(
        status=discord.Status.idle,
        type=discord.ActivityType.watching,
        name=f" ?help || {len(client.guilds)} servers!"))
    print('Guild Function Working')
    while 1:
        urllib.request.urlopen(
            "https://Latest-Discord-Bot.dhruvnation1.repl.co")
        await asyncio.sleep(500)


initial_extensions = [
    'PilImages.imposter', 'PilImages.pewds', "PilImages.shoot",
    "PilImages.wanted", "GameCmds.fortnite", "GameCmds.pokemon",
    "ApiWork.animals", "ApiWork.CoolCmds", "ApiWork.covid", "ApiWork.joke",
    "ApiWork.meme", "ApiWork.motivate", "GameCmds.8ball", "BotCmd.common_cmd",
    "BotCmd.moderation", "BotCmd.servercmd", "BotCmd.dmcmd", "BotCmd.dump",
    "BotCmd.Helpcommands", "BotCmd._my_Bot_error_handler", "RedditMeme.rmeme"
]

if __name__ == "__main__":
    for extensions in initial_extensions:
        try:
            client.load_extension(extensions)
        except Exception as e:
            print(f"Failed To Load Extension {extensions}", file=sys.stderr)
            traceback.print_exc()

keep_alive.keep_alive()

client.run(token)
from replit import db
