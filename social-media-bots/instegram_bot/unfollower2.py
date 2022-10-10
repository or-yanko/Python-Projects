"""

                                            dont work yet. the second one works
"""
from instabot import Bot
from time import sleep
from random import randint

bot = Bot()
bot.login(username="------",password="------")
print('--------------------------')
followers = bot.get_user_followers("username")
print("Total number of followers:")
print(len(followers))
print('--------------------------')


non_followers = set(bot.following) -set(bot.followers)
print(non_followers)