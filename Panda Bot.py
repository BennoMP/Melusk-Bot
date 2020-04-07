import time
import discord

TOKEN = # Put the token here.

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'bot!hi':
        msg = 'Hello there! :D'.format(message)
        await message.channel.send(msg)

    if message.content == 'bot!joke':
            msg = 'Hah. How about NO'.format(message)
            await message.channel.send(msg)

    if message.content == 'bot!help':
        msg = '```Panda Bot Command List:```'
        await message.channel.send(msg)
        msg = '```bot!hi   : Greets you```'
        await message.channel.send(msg)
        msg = '```bot!joke : Tells a joke```'
        await message.channel.send(msg)
        msg = '```bot!help : Shows this message```'
        await message.channel.send(msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Bot is online now')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="bot!help"))

client.run(TOKEN)

#def action1():
#    while True:
#        print('!d bump')
#        time.sleep(7200)

#input = input()
#if input == 'bot!start':
#    action1()
