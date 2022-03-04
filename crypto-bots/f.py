import os.path
from os import path

def main():

   print ("File exists:"+str(path.exists('coins.txt')))
   print ("File exists:" , path.exists('coins-logs/bitcoin-logs.txt'))
   print ("directory exists:" + str(path.exists('myDirectory')))

if __name__== "__main__":
   main()
