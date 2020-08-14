import discord
import os
import requests
import random

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

client = discord.Client()

colors = [0x0db2ff, 0x0c5913, 0xbf1600]

class intparams():
    def __init__(self, min, max, count = 1, cols = 1, base = 10):
        self.count = count
        self.cols = cols
        self.min = min
        self.max = max
        self.base = base


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

        # paramsdict = await return_paramsdict(inp)

        # print('paramsdict: {}'.format(paramsdict))
        # for param in paramsdict:
        #     print('for print: {}'.format(param))

        # count = paramsdict['c']

        # print(count)


        print(return_fullparamsclass(inp))


# note that input must have no command prefix
async def return_paramsdict(inp):
    params = inp.split(' ', 2)
    min = params.pop(0)
    max = params.pop(0)

    print(params)

    _params = str(params).replace('[\'', '')
    _params = _params.replace('\']', '')

    paramslist = _params.split('-')
    paramslist.pop(0)

    _dict = {}

    _dict['min'] = str(min)
    _dict['max'] = str(max)

    for param in paramslist:
        parameter = param.split(' ', 1)

        param0stripped = parameter[0].strip()
        param1stripped = parameter[1].strip()
        
        _dict[param0stripped] = param1stripped

    return _dict


# possible params - col, count

# note that input must have no command prefix
async def return_fullparamsclass(inp):
    params = await return_paramsdict(inp)
    
    _info = intparams()

    _info.min = params['min']
    _info.max = params['max']
    _info.count = params['count']
    _info.cols = params['cols']
    _info.base = params['base']

    return _info



async def int_req(amount, min, max, cols, base):
    return(requests.get('https://www.random.org/integers/?num={}&min={}&max={}&col={}&base={}&format=plain&rnd=new'.format(amount, min, max, cols, base)).text)


client.run(TOKEN)