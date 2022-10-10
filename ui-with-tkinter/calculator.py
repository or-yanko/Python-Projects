from tkinter import *
import tkinter.font as font
from functools import partial
import json
import re

import math


buttonColor = (255, 255, 255)
historyPanelBackground = (255, 255, 255)

root = Tk()
root.geometry("550x270")
root.title("Calculator")
myFont = font.Font(family='Consolas', size=12)

formulas = [
    ['Pythagoras->c', '(({a}**2)+({b}**2))**0.5 ? a=5 & b=5'],
    ['Pythagoras->c**2', '({a}**2)+({b}**2) ? a=5 & b=5'],
    ['pq->(x1, x2)',
     '-({p}/2) + sqrt(({p}/2)**2 - ({q})), -({p}/2) - sqrt(({p}/2)**2 - ({q})) ? p=-1 & q=-12'],
    ['abc->(x1, x2)', 'quadratic_formula({a}, {b}, {c}) ? a=1 & b=5 & c=6'],
    ['Incline->y', '{m}*{x} + {q} ? m=4 & x=5 & q=6'],
]

history = []
historyFilePath = 'history.json'
print("Reading history from:", historyFilePath)
try:
    with open(historyFilePath, 'x') as fp:
        pass
    print("Created file at:", historyFilePath)
except:
    print('File already exists')


def rgb_to_hex(rgb):
    return "#%02x%02x%02x" % rgb


def addSymbol(event=None, symbol=None):
    if symbol == '<':
        entryVariable.set(entryVariable.get()[:-1])
    else:
        entryVariable.set(entryVariable.get()+symbol)


def varChange(*args):
    evaluationString = entryVariable.get().replace(' ', '').split('?')[0]
    print('Before insertion: ', evaluationString)
    if len(entryVariable.get().split('?')) == 2:
        parameters = entryVariable.get().replace(' ', '').split('?')[1]
        for param in parameters.split('&'):
            where, what = param.split('=')
            evaluationString = re.sub('{'+where+'}', what, evaluationString)
    try:
        print('After insertion: ', evaluationString)
        resultLabel.config(text=str(eval(evaluationString)))
    except:
        resultLabel.config(text='Invalid Input')


def saveCurrentInputToHistory(event=None):
    if entryVariable.get() in history:
        return
    history.append(entryVariable.get())
    with open(historyFilePath, 'w') as file:
        file.write(json.dumps(history))
    updateListBox()


def updateListBox(event=None):
    global history
    historyList.delete(0, END)
    try:
        with open(historyFilePath, 'r') as file:
            history = json.loads(file.read())
    except json.decoder.JSONDecodeError:
        print('File does not contain JSON')
    for index, item in enumerate(history):
        historyList.insert(index, item)


def setEntryFromHistory(event=None):
    historyItem = historyList.get(historyList.curselection()[0])
    entryVariable.set(historyItem)


def addFormula(formula=''):
    saveCurrentInputToHistory()
    entryVariable.set(formula)


def quadratic_formula(a, b, c):

    disc = b**2 - 4 * a * c

    x1 = (-b - math.sqrt(disc)) / (2 * a)
    x2 = (-b + math.sqrt(disc)) / (2 * a)

    return(x1, x2)


calcSide = Frame(root)
calcSide.pack(side=LEFT, fill=BOTH, expand=1)
entryVariable = StringVar(root, '4/2**2')
entryVariable.trace('w', varChange)

Entry(calcSide, textvariable=entryVariable, font=myFont,
      borderwidth=0).pack(fill=X, ipady=10, ipadx=10)
resultLabel = Label(calcSide, text='Result', font=myFont,
                    borderwidth=0, anchor="e")
resultLabel.pack(fill=X, ipady=10)

historySide = Frame(root, bg=rgb_to_hex(historyPanelBackground))
historySide.pack(side=LEFT, fill=BOTH, expand=1)

historyTopBar = Frame(historySide)
historyTopBar.pack(fill=X)
Label(historyTopBar, text='History').pack(side=LEFT)
Button(historyTopBar, text='Save Current Input', bg=rgb_to_hex(buttonColor),
       borderwidth=0, command=saveCurrentInputToHistory).pack(side=RIGHT)

historyList = Listbox(historySide, borderwidth=0)
historyList.pack(fill=BOTH, expand=True)
historyList.bind("<Double-Button-1>", setEntryFromHistory)

updateListBox()

symbols = [
    ['1', '2', '3', '+'],
    ['4', '5', '6', '-'],
    ['7', '8', '9', '/'],
    ['0', '.', '<', '*'],
]

for rowList in symbols:
    row = Frame(calcSide)
    row.pack(fill=BOTH, expand=True)
    for symbol in rowList:
        Button(
            row, text=symbol, command=partial(addSymbol, symbol=symbol),
            font=myFont, bg=rgb_to_hex(buttonColor), borderwidth=0) \
            .pack(side=LEFT, fill=BOTH, expand=1)
        buttonColor = (buttonColor[0] - 10,
                       buttonColor[1] - 10, buttonColor[1] - 2)


menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
for formula in formulas:
    filemenu.add_command(
        label=formula[0], command=partial(addFormula, formula[1]))

filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(menu=filemenu, label='Formulas')
root.config(menu=menubar)
varChange('foo')
root.mainloop()
