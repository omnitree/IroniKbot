import asyncio
import os

import mongoengine
from discord.ext.commands import Bot

from Bot_Commands.Fun import Fun
from Bot_Commands.Misc import Misc
from Bot_Events.Misc_Events import MiscEvents

bot_token = os.environ.get('BOT_TOKEN')

startup_extensions = ['Fun', 'Misc', 'Moderation', 'Misc_Events']

# Connect to the mongodb using mongoengine

def connect():
    db_username = os.environ.get('DB_USERNAME')
    db_password = os.environ.get('DB_PASSWORD')
    db_host = os.environ.get('DB_HOST')
    db_name = os.environ.get('DB_NAME')

    mongoengine.connect(db_name,
                        username=db_username,
                        password=db_password,
                        host=db_host)

    return mongoengine.connection

# Run the client using the built-in client.run
def run_client(*args, **kwargs):

    while True:
        client = Bot(description="Ironic Bot by Perfect_Irony#5196", command_prefix="$", pm_help=False)

        mongo_connection = connect()

        client.add_cog(Fun(client, mongo_connection))
        client.add_cog(Misc(client, mongo_connection))
        client.add_cog(MiscEvents(client, mongo_connection))

        client.run(bot_token)

        asyncio.sleep(250)


run_client()
