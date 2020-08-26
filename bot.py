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
    def __init__(self, min, max, count, cols, base):
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
    
    if message.content.startswith('?int') or message.content.startswith('?num'):
        inp = str(message.content).replace('?int ', '')
        inp = inp.replace('?num ', '')
        min = inp.split(' ')[0]
        max = inp.split(' ')[1]

        rng = '`' + min + ' - ' + max + '`'
        fullparams = await return_fullparamsclass(inp)

        toadd = '```' + await int_req(fullparams) + '```'
        embed = discord.Embed(
            title = str(message.author),
            colour = colors[abs((int(max) - int(min)) % len(colors))]
        )

        embed.set_footer(text = 'Straight from the horse- I mean Random.org\'s mout- I mean server!')
        embed.add_field(name = 'Range: ', value = rng)

        # if fullparams.cols == '1':
        embed.add_field(name = 'Number(s): ', value = toadd, inline = False)

        await message.channel.send(embed=embed)


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

    _dict = {'min' : str(min), 'max' : str(max), 'count' : '1', 'cols' : '1', 'base' : '10'}

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
    _info = intparams(params['min'], params['max'], params['count'], params['cols'], params['base'])

    return _info



async def int_req(intparams):
    return(requests.get('https://www.random.org/integers/?min={}&max={}&num={}&col={}&base={}&format=plain&rnd=new'.format(intparams.min, intparams.max, intparams.count, intparams.cols, intparams.base)).text)


client.run(TOKEN)