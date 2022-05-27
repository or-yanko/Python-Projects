import basic
from termcolor import colored
import datetime


while True:
    currentDT = datetime.datetime.now()
    #date = f'File {self.pos_start.fn}, line {self.pos_start.ln + 1}, pos {self.pos_start.col + 1}'
    text = input(
        colored(f'\nOR YANKO\'s programing language      {currentDT.day}/{currentDT.month}/{currentDT.year} at {currentDT.hour}:{currentDT.minute} :\nbasic => ', 'blue'))
    result, error = basic.run('<stdin>', text)

    if error:
        print(colored(error.as_string(), 'red'))
    else:
        print(colored(result, 'green'))
