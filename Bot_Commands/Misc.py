import platform
from datetime import datetime

import discord  # discord api
from discord.ext import commands  # commands extension

from Bot_DB.Mango.database_models import Users


class Misc:

    def __init__(self, client, db_connection):
        self.client = client

    @commands.command(pass_context=True)
    async def versioninfo(self, ctx):
        """Gives some info on the Bot."""

        tmp = discord.Embed(title='Bot Version Info', type='rich',
                            description='Python Ver: ' + platform.python_version() + ' | '
                                        + 'Discord.py Ver: ' + discord.__version__ + '\n\n' + 'Ironic Bot Ver: 1.3 Stable\n\n' +
                                        'Created with weeb love by Perfect Irony')

        await ctx.send(embed=tmp)

    @commands.command()
    async def joined(self, ctx, member : discord.Member):
        """Says when a member joined."""
        await ctx.send('{0.name} joined on {0.joined_at}'.format(member))


    @commands.command()
    async def exp(self,ctx, member : discord.Member):
        """Check someone's exp"""
        user_entry = Users.objects(user_id=member.id).get()
        description = "**{0.name}** has `{1}` exp".format(member, user_entry.exp)

        tmp = discord.Embed(description=description)
        tmp.add_field(name="Level", value=str(user_entry.level), inline=True)
        tmp.set_thumbnail(url=member.avatar_url)

        await ctx.send(embed=tmp)

    @commands.command()
    async def userinfo(self, ctx, member: discord.User):
        tmp = discord.Embed(
            title="User info",
            type='rich')

        tmp.set_thumbnail(url=member.avatar_url)

        tmp.add_field(name='Username:', value=member.name + '#' + member.discriminator)
        tmp.add_field(name='ID:', value=member.id)
        tmp.add_field(name='Time on Discord:', value=str(datetime.now() - member.created_at).split(',')[0])

        if member.bot:
            tmp.add_field(name='Bot:', value='This user is a bot.')

        tmp.set_footer(text='For full size avatar try $avatar')
        await ctx.send(embed=tmp)

    @commands.command()
    async def avatar(self, ctx, member: discord.User):
        tmp = discord.Embed()

        tmp.set_image(url=member.avatar_url)
        tmp.set_footer(text=member.name + '#' + member.discriminator)

        await ctx.send(embed=tmp)
