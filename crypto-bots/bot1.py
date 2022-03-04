'''
---------------------show coin live prices----------------------
'''
import multiprocessing
import pandas as pd
from bs4 import BeautifulSoup as BS
import requests
import time
from datetime import datetime
from termcolor import colored

path = 'coins-logs/'

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

def check_coin(crypto):
    last_price = '0'

    while True:
        try:
            price = get_crypto_price(crypto)
            onlyprice = price.split(' ')[0]
            if onlyprice != last_price:
                now = datetime.now()
                '''
                if float(last_price.replace(',',''))<float(onlyprice.replace(',','')):
                    print(crypto+' price:',colored(onlyprice, 'green'), 'ILS at', now.strftime("%d/%m/%Y %H:%M:%S")) 
                elif onlyprice < last_price:
                    print(crypto+' price:',colored(onlyprice, 'red'), 'ILS at', now.strftime("%d/%m/%Y %H:%M:%S")) 
                else:
                    print(crypto+' price:',onlyprice, 'ILS at', now.strftime("%d/%m/%Y %H:%M:%S")) 
                    '''
                last_price = onlyprice
                with open(str(path + crypto + "-logs.txt"), "a") as text_file:
                    text_file.write( onlyprice + " " + now.strftime("%d/%m/%Y %H:%M:%S") + "\n")
                    text_file.close()
            #else:
             #   print(colored(str(crypto + ' hasn\'t changed yet'), 'yellow'))
            time.sleep(10)
        except :
            print(colored(str(crypto+' is wrong coin name... '), 'red'))
            break

def main():

    




    '''
    crypto = ' '
    crypto = input('enter crypto coin to see his live price: ')
    if crypto.lower()  in ['exit','quit','bye','pipi']:
        print(colored('bye bye... :-(', 'red'))
    check_coin(crypto)
    '''

    '''
    processes = []
    crypto = ' '
    while True:
        print(processes)
        crypto = input('enter crypto coin to see his live price: ')
        if crypto.lower()  in ['exit','quit','bye','pipi']:
            print(colored('bye bye... :-(', 'red'))
            break
        processes.append(multiprocessing.Process(target=check_coin, args=(crypto)))
        processes[-1].start()
        for proc in processes:
            proc.join()
    '''




main()

