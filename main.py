#!/usr/bin/python
import discord
import urllib.parse
from discord.ext import commands
from g_search import get_search
from sl_data import setup_db
from sl_data import update_history
from sl_data import show_history

#Assign values to unique variables
TOKEN = 'TOKEN'

client = commands.Bot(command_prefix = '')

#Handling Events
@client.event
async def on_ready():
    setup_db()
    print('Bot is  ready.')

@client.event
async def on_message(message):

    #To send Hey if user input hi or Hi or HI
    if message.content == 'hi' or message.content == 'Hi' or message.content == 'HI' :
        await message.channel.send('Hey')
        in_cmd = message.content


    #To filter out data and pass the search term to function google_search() and print links from raw data received
    elif message.content[:7] == '!google':
        results = get_search(message)
        await message.channel.send(f'Top 5 search result for {message.content[7:]} are:')
        for result in results:
            links = result.get('formattedUrl')
            links = urllib.parse.unquote(links)
            await message.channel.send(f'{links}\n')
        update_history(message,message.content[7:].lstrip())


    #Defining 'recent' functionality
    elif message.content[:7] == '!recent':
        search_term = message.content[7:].lstrip()
        if search_term == '':
            await message.channel.send('Please mention what you are looking for like \n!recent google')
        if search_term != '':
            result = show_history(message, search_term)
            for dict in result:
                for item in dict:
                    await message.channel.send(item)

client.run(TOKEN)
