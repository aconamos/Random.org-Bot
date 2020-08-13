import discord
import os
import requests
import random

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

client = discord.Client()

colors = [0x0db2ff, 0x0c5913, 0xbf1600]


default_params = {'c':'1', 'cols':'1'}


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

        paramsdict = await return_paramsdict(inp)

        print('paramslist: {}'.format(paramsdict))
        for param in paramsdict:
            print('for print: {}'.format(param))

        count = paramsdict['c']

        print(count)

        

# note that raw input must have no command prefix
async def return_paramsdict(rawinput):
    params = rawinput.split(' ', 2)
    params.pop(0)
    params.pop(0)

    _params = str(params).replace('[\'', '')
    _params = _params.replace('\']', '')

    paramslist = _params.split('-')
    paramslist.pop(0)

    _dict = {}

    for param in paramslist:
        parameter = param.split(' ', 1)

        param0stripped = parameter[0].strip()
        param1stripped = parameter[1].strip()
        
        _dict[param0stripped] = param1stripped

    return _dict


async def int_req(min, max, amount = 1):
    return(requests.get('https://www.random.org/integers/?num={}&min={}&max={}&col=1&base=10&format=plain&rnd=new'.format(amount, min, max)).text)


async def col_req(min, max, cols, amount = 1):
    return(requests.get('https://www.random.org/integers/?num={}&min={}&max={}&col={}&base=10&format=plain&rnd=new'.format(amount, min, max, cols)).text)

client.run(TOKEN)