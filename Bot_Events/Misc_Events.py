import datetime
import math
from random import randint

import discord
import mongoengine

from Bot_DB.Mango.database_models import Users


class MiscEvents:

    def __init__(self, client, database):
        self.client = client
        self.database = database

    async def on_ready(self):
        print('Logged in as ' + str(self.client.user.name) + ' (ID:' + str(self.client.user.id) + ') | Connected to '
              + str(len(self.client.guilds)) + ' servers | Connected to ' + str(len(set(self.client.get_all_members())))
              + ' users')

        print('\nLoading Azure:')
        # await load_azure()


        print('\nLoading user DB...', end='')
        for member in self.client.get_all_members():
            try:
                Users(user_id=int(member.id), exp=0).save()
            except:
                pass
        print('done')


        print("\n\nBot is now ready.")
        return await self.client.change_presence(activity=discord.Game('with bits | $versioninfo'))

    async def on_member_join(self, member: discord.Member):
        try:
            User_tmp = Users(user_id=int(member.id), exp=0).save()
        except mongoengine.NotUniqueError:
            pass

    async def on_message(self, message: discord.Message):

        if message.author is not self.client.user:
            try:
                author_id = message.author.id

                # Get the user's info from the DB
                user_entry = Users.objects(user_id=author_id).get()
                current_exp = user_entry.exp

                # Get the time since their last message
                elapsedTime = datetime.datetime.utcnow() - user_entry.time_stamp

                if int(elapsedTime.total_seconds()) > 5:

                    print('Adding xp')

                    level = int(.9 * math.sqrt(current_exp))

                    if level == 0:
                        level = 1

                    multi = 1

                    if int(elapsedTime.total_seconds()) < 600:
                        multi = 2

                    if int(elapsedTime.total_seconds()) < 120:
                        multi = 3

                    Users.objects(user_id=author_id).modify(upsert=True, new=True, exp=((randint(10, 30)*multi) + current_exp),
                                                            time_stamp=datetime.datetime.utcnow(), level=level)
                else:
                    Users.objects(user_id=author_id).modify(upsert=True, new=True, time_stamp=datetime.datetime.utcnow())

            except mongoengine.errors.NotUniqueError:
                pass
            except Exception as error:

                print('\n Something happened while adding EXP to user: ' + str(error))
