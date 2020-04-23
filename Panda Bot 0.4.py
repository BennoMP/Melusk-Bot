import discord
from discord.ext.commands import bot
import os
import random 

TOKEN = #Token here
PREFIX = 'pbot!'

client = discord.Client(command_prefix=PREFIX)

@client.event
async def on_ready():
    print('Logged in as')
    print('bot name: ' + client.user.name)
    print(client.user.id)
    print('------------------')
    print('bot is online now')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="pbot!help"))
    print('Status has been set to "Listening to pbot!help"')
    print('----------------------------------------------')
    print('Secret commands:')
    print('pbot!test - sends I\'m working')
    print('pbot!chatrevive - Mentions everyone')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

#    if message.content == "banhammer":
#        msg = 'I can\'t ban you but my creator can, {0.author.mention}'.format(message)
#        await message.channel.send(msg)

    if message.content == "pbot!amistupid":
        msg = 'Yes, you\'re stupid {0.author.mention}'.format(message)
        await message.channel.send(msg)
        
    if message.content == "pbot!test":
        await message.channel.send("Yes I'm working")
        
    if message.content == "pbot!hi":
#        await message.channel.send("Hello <@{user.id}>")
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)

    if message.content == "pbot!chatrevive":
        msg = '@everyone wake up!'.format(message)
        await message.channel.send(msg)

    if message.content == "pbot!invite":
        msg = 'Here\'s the invite link: https://discordapp.com/oauth2/authorize?client_id=695967478584573984&scope=bot&permissions=8'.format(message)
        await message.channel.send(msg)
    
    if message.content == "pbot!help":
        msg = '```Panda bot Command List:```'
        await message.channel.send(msg)
        msg = '```pbot!amistupid   : Tells you if you\'re stupid```'
        await message.channel.send(msg)
        msg = '```pbot!hi          : Greets you```'
        await message.channel.send(msg)
#        msg = '```pbot!8ball {Question} : Answers your 8 ball question```'
#        await message.channel.send(msg)
        msg = '```pbot!ping        : Pong!```'
        await message.channel.send(msg)
        msg = '```pbot!help        : Shows this message```'
        await message.channel.send(msg)
        msg = '```pbot!invite      : Sends a bot invite. Please note that the bot is offline most of the time```'
        await message.channel.send(msg)

    if message.content == "pbot!ping":
        msg = 'Pong!'
        await message.channel.send(msg)

#@client.command(name='8ball', aliases=['eight_ball', 'eightball', '8-ball'], pass_context=True)
#async def eight_ball(context):
    possible_responses = [
    'It is decidedly so.',
        'Without a doubt.',
        'Yes - definitely.',
        'You may rely on it.',
        'As I see it, yes.',
        'Most likely.',
        'Signs point to yes.',
        'Reply hazy, try again.',
        'Ask again later.',
        'Better not tell you now.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        'Not gonna happen fam.',
        'My reply is no.',
        'My sources say no.',
        'Outlook not so good.',
        'Outlook good.',
        'Yes.',
        'Very doubtful.',
    ]
#    await message.channel.send(random.choice(possible_responses) + ", " + context.message.author.mention)
        
client.run(TOKEN)
