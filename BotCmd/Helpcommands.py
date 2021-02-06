import discord
from discord.ext import commands


class helptry(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        


    
    @commands.command(aliases=['mod', 'Moderation'])
    async def moderation(self, ctx):
        embed = discord.Embed(title='All Moderation Command',
                              description='Commands:-',
                              colour=discord.Colour.gold())
        embed.set_footer(text='⭐Credits Go To: Dhruv⭐')
        embed.set_author(name='?moderation')
        embed.set_footer(text='⭐Credits Go To: Dhruv⭐')
        embed.add_field(name='ban <user.mention>',
                        value='`Bans the User`\n',
                        inline=True)
        embed.add_field(name='unban <name + #1234>',
                        value='`Revoke The ban of The user`',
                        inline=True)
        embed.add_field(name='kick <user.mention>',
                        value='`kicks The User`',
                        inline=True)
        embed.add_field(name='clean <value>',
                        value='`Clears the messgae in channel`',
                        inline=True)
        embed.add_field(name='av <user.mention> ',
                        value='`Brings the Users Avatar`',
                        inline=True)
        embed.add_field(name='warn <user.mention> ',
                        value='`warns The Person`',
                        inline=True)
        embed.add_field(name='ping ', value='`ping of the BOT`', inline=True)

        embed.set_thumbnail(
            url=
            'https://vignette.wikia.nocookie.net/drawception/images/8/85/ModeratorBadge.jpeg/revision/latest?cb=20190201180259'
        )

        await ctx.send(embed=embed)

    @commands.command(aliases=['Help_special'])
    async def special(self, ctx):
        embed = discord.Embed(
            title='*All Specials Command*',
            # description = 'Commands:-',
            colour=discord.Colour.lighter_gray())
        embed.set_footer(text='⭐Credits Go To: Dhruv⭐')
        # embed.set_author(name='?Help_specials')
        embed.set_footer(text='⭐Credits Go To: Dhruv⭐')
        embed.add_field(name='sendDM  <user.mention> <message>',
                        value="`Send's DM via bot Mentioning your name.`",
                        inline=False)
        embed.add_field(name='send_anonymous_dm  <user.mention>  <message>',
                        value="`Send's DM via bot NOT Mentioning your name.`",
                        inline=False)
        embed.set_thumbnail(
            url=
            'https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/9672dd15202123.5628e1d8e1e8c.jpg'
        )

        await ctx.send(embed=embed)

    @commands.command(aliases=['Fun'])
    async def fun(self, ctx):
        embed = discord.Embed(
            title="*Let's Have Some Fun*",
            # description = 'Commands:-',
            colour=discord.Colour.lighter_gray())
        embed.set_footer(text='⭐Credits Go To: Dhruv⭐')
        # embed.set_author(name='?Help_specials')
        embed.set_footer(text='⭐Credits Go To: Dhruv⭐')
        embed.add_field(name='8ball <question>',
                        value="`Classic 8ball Game with Predection`",
                        inline=False)
        embed.add_field(name='meme', value="`stuff meme`", inline=False)
        embed.add_field(name='reddit_meme or reddit_meme <subreddit>',
                        value="`Get's you the best Top 50 Subreddit.`",
                        inline=False)
        embed.set_thumbnail(
            url=
            'https://www.richardsonsholidayparks.co.uk/wp-content/uploads/2019/03/Entertainment.png'
        )

        await ctx.send(embed=embed)

    @commands.command(aliases=['Help'])
    async def help(self, ctx):
        embed = discord.Embed(
            title='*Here To your Help*',
            # description = 'Our capablities',
            colour=discord.Colour.orange())
        embed.set_footer(text='⭐Credits Go To: Dhruv⭐')
        # embed.set_author(name='?Help')
        embed.set_footer(text='⭐Credits Go To: Dhruv⭐')
        embed.set_footer(text='⭐Credits Go To: Dhruv⭐')
        embed.add_field(name='moderation',
                        value='`All The Moderation Command`',
                        inline=True)
        embed.add_field(name='special',
                        value="`All the Special features of OUR bot`",
                        inline=True)
        embed.add_field(name='fun', value='`Get some Fun`', inline=True)
        embed.add_field(name='image',
                        value='`Get some cute images and more`',
                        inline=True)
        embed.add_field(name='set_prefix',
                        value='`Customizes The Prefix For The Server`',
                        inline=False)
        embed.set_thumbnail(
            url=
            'https://www.graphicsprings.com/filestorage/stencils/d619ef29297bf4a1d98fa4bb57ab8d7f.png?width=500&height=500'
        )
        embed.add_field(name='bot_info',
                        value='```css\n Invite Bot , Source Code.. ```',
                        inline=False)

        await ctx.send(embed=embed)

    @commands.command(aliases=['social media'])
    async def sm(self, ctx):
        embed = discord.Embed(
            title='Social media',
            description=
            '**[Dhruv Nation ~~ YTB ](https://www.youtube.com/channel/UCb9kY0I01P23eOxbs3kNH0g)\n[Audio Nation ~~ YTB](https://www.youtube.com/channel/UC9KPOrSqEI1O4pPD0waDsaQ)\n[GitHub](https://github.com/DHRUV-CODER)**',
            colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @commands.command(aliases=['vbucks'])
    async def vb(self, ctx):
        embed = discord.Embed(
            title="free vbucks",
            url="https://www.youtube.com/watch?v=BLeOcCeqsfI",
            description="my man xaiver is giving some vbucks ",
            color=0xff0000)
        embed.set_author(
            name="Mr Xavier",
            icon_url=
            "https://images-ext-2.discordapp.net/external/RQ1hLYGEF-gxzvmw2H_UjWqrsRiXfw9yPbyJjkpF-fM/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/701146789348376607/eb2b6e18558ff135e8ef5867e8adf7e8.webp"
        )
        embed.set_thumbnail(
            url=
            "https://cnet4.cbsistatic.com/img/aTLKqWz80LEDLhuX74RcgdKiXMM=/1200x675/2020/02/14/676146ec-f899-4c73-a132-99f7bff87827/vbucks.png"
        )
        await ctx.send(embed=embed)

    # @client.event
    # async def on_command_error(ctx, error):
    #     if isinstance(error, commands.MissingPermissions):
    #         await ctx.send(f'`To use This you Require Administrator Privileges `\n \n **Assign A role Having Administrator Enabled**')

    @commands.command(aliases=['botinfo'])
    async def bot_info(self, ctx):
        embed = discord.Embed(
            title='__Info__',
            description=
            "**[Invite](https://discord.com/api/oauth2/authorize?client_id=790592850588336151&permissions=8&scope=bot)**\n\n**[Bot Support Server](https://discord.gg/j2NeBaCWYy)**\n\n **[Bot's Source Code](https://github.com/DHRUV-CODER/Discord-Bot)**\n\n **Btw I was Created On *21/12/2020***",
            colour=discord.Colour.gold())
        await ctx.send(embed=embed)

    @commands.command(aliases=['apihelp'])
    async def image(self, ctx):
        embed = discord.Embed(title="Help On Images",
                              description="API Request For Some Cool Stuff",
                              color=0xccb044)
        embed.set_thumbnail(
            url=
            "https://www.elemental.co.za/blog/wp-content/uploads/2020/04/api-2x.png"
        )
        embed.add_field(name="fox", value="`get some cute fox`", inline=True)
        embed.add_field(name="cat", value="`meow..`", inline=True)
        embed.add_field(name="panda", value="`get me bamboo`", inline=True)
        embed.add_field(name="dog", value="`woof...woof`", inline=True)
        embed.add_field(name="rp", value="`red pandas`", inline=True)
        embed.add_field(name="bird", value="`flying high`", inline=True)
        embed.add_field(name="pikachu",
                        value="`get my cool shots`",
                        inline=True)
        embed.add_field(name="trigger <link>",
                        value="`get you a image with triggered edit`",
                        inline=False)
        embed.add_field(name="pm <pokemon>",
                        value="`Get Details About The Pokemon`",
                        inline=False)
        embed.set_footer(text="\n\n ⭐Credits To Dhruv⭐\n\n")
        await ctx.send(embed=embed)
    

def setup(bot):
    bot.add_cog(helptry(bot))
