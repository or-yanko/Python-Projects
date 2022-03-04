'''
---------------------- update a folder with all the ----------------------
--------------------- changes of any coin in the list --------------------
'''
import multiprocessing
import pandas as pd
from bs4 import BeautifulSoup as BS
import requests
import time
from datetime import datetime
from termcolor import colored
import os.path
from os import path as ospath

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

def check_coins():
    try:
        coins_file = open("coins.txt", "r")
        coinsList = coins_file.read()
        coins = coinsList.split('\n')
        coins_file.close()
        i = 0
        last_price = []
        for a in range(0, len(coins)):
            last_price.append('0')
                
        for crypto in coins:
            price = ''
            price = get_crypto_price(crypto)
            onlyprice = price.split(' ')[0].replace(',','')

            p = str(path + crypto + "-logs.txt")

            if ospath.exists(p) == True:
                    with open(p, "r") as lastfile:
                        s = lastfile.read().split('\n')[-2]
                        

                        last_price[i] = ' ' 
                        last_price[i] += s.split(' ')[0]

            if float(onlyprice) != float(last_price[i]):
                now = datetime.now()
                if float(last_price[i])<float(onlyprice):
                    print(crypto+' price:',colored(onlyprice, 'green'), 'ILS at', now.strftime("%d/%m/%Y %H:%M:%S")) 
                elif float(last_price[i])>float(onlyprice):
                    print(crypto+' price:',colored(onlyprice, 'red'), 'ILS at', now.strftime("%d/%m/%Y %H:%M:%S")) 
                else:
                    print(crypto+' price:',onlyprice, 'ILS at', now.strftime("%d/%m/%Y %H:%M:%S")) 
                with open(str(path + crypto + "-logs.txt"), "a") as text_file:
                    text_file.write( onlyprice + " " + now.strftime("%d/%m/%Y %H:%M:%S") + "\n")
                    text_file.close()
            else:
                print(colored(str(crypto + ' has\'nt changed yet...'),'yellow'))
            i+=1
    except RuntimeError:
        print(colored(str('somthing wrong with '+crypto), 'red'))
    return True

def main():
    round1 = 0

    while check_coins() == True:
        round1+=1
        print(colored(str('----- round '+str(round1)+' completed successfully ------\n\n'), 'green'))
        time.sleep(5)





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

