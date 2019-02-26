from discord.ext import commands
class Moderation(commands.Cog):
    def __init__(self, client):

        self.client = client

    async def on_message_delete(self, message):
        pass

def setup(bot):
    bot.add_cog(Moderation(bot))
