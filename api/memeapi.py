import requests
import json
from termcolor import colored, cprint
from PIL import Image




def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def getMeme(allMemes, code):
    for m in allMemes:
        if m["id"] == code:
            return m
    return "wrong code..."

def openMeme(allCoins, code):
    meme = getMeme(allCoins, code)
    if meme == "wrong code...":
        print("wrong code...")
    else:
        Image.open(requests.get(meme["url"],stream=True).raw).show()
        print('meme has been opened')



link = "https://api.imgflip.com/get_memes"
dataFromApi = requests.get(link).json()["data"]["memes"]
inp = ""

#Image.open(requests.get(dataFromApi[1]["url"],stream=True).raw).show()



while(inp.lower()!='close' and inp.lower() != 'exit'):
    cprint('\n||==== **** meme api terminal ****\n||=>', 'green',end =" ")
    inp = input()
    if inp.lower() == 'pall':
        jprint(dataFromApi)
    elif inp.lower() == 'omeme':
        cprint('\n||==== enter meme code:\n||=>', 'green',end =" ")
        inp2 = input()
        openMeme(dataFromApi, inp2)
    elif inp.lower() == 'pcode':
        for m in dataFromApi:
            print(m["id"], '   :   ',m['name'])
