import logging
import os

import mongoengine

import discord
from discord.ext import commands

from Bot_DB.Azure.Load_Azure import load_azure
from Bot_Events.Misc_Events import MiscEvents

from Mango.database_models import Users


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
bot = commands.Bot(description="Ironic Bot by Perfect_Irony#5196", command_prefix="$", pm_help=False)

# Run the client using the built-in client.run. Clear restart is redundant, but keeping it just in case.
def run_client(*args, **kwargs):

    while True:


        mongo_connection = connect()
        print('\nLoading Azure:')
        load_azure()

        logging.basicConfig(level=logging.INFO)

        initial_extensions = ['Bot_Commands.Fun',
                              'Bot_Commands.Misc',
                              'Bot_Commands.Moderation']

        for extension in initial_extensions:
            try:
                bot.load_extension(extension)
            except Exception as e:
                print(f'Failed to load extension {extension}. error: ' + str(e.with_traceback()))

        bot.add_cog(MiscEvents(bot,mongo_connection))

        try:
            bot.run(bot_token)
        finally:
            bot.clear()
            print('restarting')


run_client()
