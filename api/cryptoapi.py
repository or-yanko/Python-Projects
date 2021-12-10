import requests
import json
from termcolor import colored, cprint


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def getCoin(allCoins, code):
    for c in allCoins:
        if c["symbol"] == code:
            return c
    return "wrong code..."

def printCoin(allCoins, code):
    coin = getCoin(allCoins, code)
    jprint(coin)




link = "https://api2.binance.com/api/v3/ticker/24hr"
dataFromApi = requests.get(link).json()
inp = ""

while(inp.lower()!='close' and inp.lower() != 'exit'):
    cprint('\n||==== **** meme api terminal ****\n||=>', 'green',end =" ")
    inp = input()
    if inp.lower() == 'pall':
        jprint(dataFromApi)
    elif inp.lower() == 'pcoin':
        cprint('\n||==== enter coin code:\n||=>', 'green',end =" ")
        inp2 = input()
        printCoin(dataFromApi, inp2)
    elif inp.lower() == 'pcode':
        counter = 0
        for c in dataFromApi:
            if counter < 8:
                print(c["symbol"], end=" ,")
                counter += 1
            else:
                print(c["symbol"])
                counter = 0
                

cprint('\nbye bye...\n', 'green')    
