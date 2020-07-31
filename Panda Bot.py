# Melusk BOT VERSION 0.4 ©2020 BENNO PRINS (Discord: Benno#9512)

# Setup and startup of the bot
import discord
import random
import os
from discord.ext.commands import bot
from os import system, name 
from time import sleep
import time

def clear(): 
    # for Windows
    if name == 'nt': 
        _ = system('cls') 
  
    # for MacOS and Linux (Works on Android too :D)
    else: 
        _ = system('clear') 

TOKEN = {token here}
PREFIX = 'mb!'

client = discord.Client(command_prefix=PREFIX)

print('Starting bot...')

@client.event
async def on_ready():
    clear()
    print('Logged in as')
    print('bot name: ' + client.user.name)
    print(client.user.id)
    print('------------------')
    print('bot is online now')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="mb!help"))
    print('Status has been set to "Listening to mb!help"')
    print('-----------------------------------------------')
    print('Secret commands:')
    print('mb!test - sends I\'m working')
    print('mb!chatrevive - Mentions everyone')

# End of setup and startup, terminal is displaying information about the bot

# Prevents bot from responding to itself
@client.event
async def on_message(message):
    if message.author == client.user:
        return

# Bot commands and execution

#    if message.content == "banhammer":
#        msg = 'I can\'t ban you but my creator can, {0.author.mention}'.format(message)
#        await message.channel.send(msg)

    if 'mb!amistupid' in message.content:
        msg = 'Yes, you\'re stupid, because you aren\'t using 8ball for this, {0.author.mention}'.format(message)
        await message.channel.send(msg)
        
    if 'mb!test' in message.content:
        await message.channel.send("Yes I'm working")
        
    if 'mb!hi' in message.content:
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)

    if 'mb!chatrevive' in message.content:
        msg = '@everyone wake up!'.format(message)
        await message.channel.send(msg)

    if 'mb!invite' in message.content:
        msg = 'Here\'s the invite link: https://discordapp.com/oauth2/authorize?client_id=695967478584573984&scope=bot'.format(message)
        await message.channel.send(msg)
    
    if 'mb!help' in message.content:
        msg = '```Melusk bot Command List:```'
        await message.channel.send(msg)
        msg = '```mb!amistupid   : Tells you if you\'re stupid```'
        await message.channel.send(msg)
        msg = '```mb!hi          : Greets you```'
        await message.channel.send(msg)
        msg = '```mb!ping        : Pong!```'
        await message.channel.send(msg)
        msg = '```mb!8ball       : Answers your 8ball question```'
        await message.channel.send(msg)
        msg = '```mb!help        : Shows this message```'
        await message.channel.send(msg)
        msg = '```mb!invite      : Sends a bot invite```'
        await message.channel.send(msg)

    if 'mb!ping' in message.content:
        msg = 'Pong!'
        await message.channel.send(msg)

    # Took me a while to get this to work. Basically gets a random answer to a yes/no question
    if 'mb!8ball' in message.content:
        possible_responses = [
        'It is decidedly so',
        'Without a doubt',
        'Yes - definitely',
        'You may rely on it',
        'As I see it, yes',
        'Most likely',
        'Signs point to yes',
        'Reply hazy, try again',
        'Ask again later',
        'Better not tell you now',
        'Cannot predict now',
        'Concentrate and ask again',
        'Not gonna happen fam',
        'My reply is no',
        'My sources say no',
        'Outlook not so good',
        'Outlook good',
        'Yes',
        'Very doubtful',
        ]
        await message.channel.send(random.choice(possible_responses) + ", " + message.author.mention)

client.run(TOKEN)
