import discord
import os
import requests
import random

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

client = discord.Client()

colors = [0x0db2ff, 0x0c5913, 0xbf1600]

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    print('Message received')

    if message.author == client.user:
        return
    
    if message.content.startswith('?int'):
        inp = str(message.content).replace('?int ', '')
        min = inp.split(' ')[0]
        max = inp.split(' ')[1]
        try:
            amount = inp.split(' ')[2]
            amount_param_exists = True
        except:
            amount_param_exists = False

        rng = min + ' - ' + max
        
        embed = discord.Embed(
            title = str(message.author),
            colour = colors[abs((int(max) - int(min)) % len(colors))]
        )

        embed.set_footer(text = 'Straight from the horse- I mean Random.org\'s mout- I mean server!')
        embed.add_field(name = 'Range: ', value = rng)

        if amount_param_exists:
            embed.add_field(name = 'Numbers:', value = await int_req(min, max, amount))
        else:
            embed.add_field(name = 'Number:', value = await int_req(min, max))


        await message.channel.send(embed=embed)

    if message.content.startswith('?cols'):
        inp = str(message.content).replace('?int ', '')
        min = inp.split(' ')[0]
        max = inp.split(' ')[1]
        amount = inp.split(' ')[2]
        try:
            cols = inp.split(' ')[3]
            cols_param_exists = True
        except:
            cols_param_exists = False

        


async def int_req(min, max, amount = 1):
    return(requests.get('https://www.random.org/integers/?num={}&min={}&max={}&col=1&base=10&format=plain&rnd=new'.format(amount, min, max)).text)


async def col_req(min, max, cols, amount = 1):
    return(requests.get('https://www.random.org/integers/?num={}&min={}&max={}&col={}&base=10&format=plain&rnd=new'.format(amount, min, max, cols)).text)

client.run(TOKEN)