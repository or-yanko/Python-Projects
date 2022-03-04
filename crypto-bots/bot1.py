import pandas as pd
from bs4 import BeautifulSoup as BS
import requests
import time
from datetime import datetime
from termcolor import colored


def get_crypto_price(coin):
#Get the URL
    url = "https://www.google.com/search?q="+coin+"+price"
    
    #Make a request to the website
    HTML = requests.get(url) 
  
    #Parse the HTML
    soup = BS(HTML.text, 'html.parser') 
  
    #Find the current price 
    #text = soup.find("div", attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
    text = soup.find("div", attrs={'class':'BNeawe iBp4i AP7Wnd'}).find("div", attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
    #Return the text 
    return text

def main():
    now = datetime.now()

    last_price = '0'
    while True:
        crypto = 'bitcoin' 
        price = get_crypto_price(crypto)
        onlyprice = price.split(' ')[0]
        if onlyprice != last_price:
            if float(last_price.replace(',',''))<float(onlyprice.replace(',','')):
                print(crypto+' price: ',colored(onlyprice, 'green'), 'ILS at', now.strftime("%d/%m/%Y %H:%M:%S")) 
            elif onlyprice < last_price:
                print(crypto+' price: ',colored(onlyprice, 'red'), 'ILS at', now.strftime("%d/%m/%Y %H:%M:%S")) 
            else:
                print(crypto+' price: ',onlyprice, 'ILS at', now.strftime("%d/%m/%Y %H:%M:%S")) 
            last_price = onlyprice 
        time.sleep(10)



main()

