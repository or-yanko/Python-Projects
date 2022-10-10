# Imports
from tkinter import *
import re

root = Tk()
root.title('Markdown Editor')
root.geometry('1000x600')

root.option_add('*Font', 'Courier 15')


def changes(event=None):
    display['state'] = NORMAL
    display.delete(1.0, END)
    text = editor.get('1.0', END)
    textRaw = text

    text = ''.join(text.split('#'))
    text = ''.join(text.split('*'))
    display.insert(1.0, text)

    for pattern, name, fontData, colorData, offset in replacements:
        locations = search_re(pattern, textRaw, offset)
        print(f'{name} at {locations}')
        for start, end in locations:
            display.tag_add(name, start, end)
        display.tag_config(name, font=fontData, foreground=colorData)
    display['state'] = DISABLED


def search_re(pattern, text, offset):
    matches = []
    text = text.splitlines()
    for i, line in enumerate(text):
        for match in re.finditer(pattern, line):
            matches.append(
                (f"{i + 1}.{match.start()}", f"{i + 1}.{match.end() - offset}")
            )
    return matches


def rgbToHex(rgb):
    return "#%02x%02x%02x" % rgb


editorBackground = rgbToHex((40, 40, 40))
editorTextColor = rgbToHex((230, 230, 230))
displayBackground = rgbToHex((60, 60, 60))
displayTextColor = rgbToHex((200, 200, 200))

caretColor = rgbToHex((255, 255, 255))
width = 10

editorfontName = 'Courier'
displayFontName = 'Calibri'

normalSize = 15
h1Size = 40
h2Size = 30
h3Size = 20

h1Color = rgbToHex((240, 240, 240))
h2Color = rgbToHex((200, 200, 200))
h3Color = rgbToHex((160, 160, 160))

replacements = [
    [
        '^#[a-zA-Z\s\d\?\!\.]+$',
        'Header 1',
        f'{displayFontName} {h1Size}',
        h1Color,
        0
    ], [
        '^##[a-zA-Z\s\d\?\!\.]+$',
        'Header 2',
        f'{displayFontName} {h2Size}',
        h2Color,
        0
    ], [
        '^###[a-zA-Z\s\d\?\!\.]+$',
        'Header 3',
        f'{displayFontName} {h3Size}',
        h3Color,
        0
    ], [
        '\*.+?\*',
        'Bold',
        f'{displayFontName} {normalSize} bold',
        displayTextColor,
        2
    ],
]

editor = Text(
    root,
    height=5,
    width=width,
    bg=editorBackground,
    fg=editorTextColor,
    border=30,
    relief=FLAT,
    insertbackground=caretColor
)
editor.pack(expand=1, fill=BOTH, side=LEFT)

editor.bind('<KeyRelease>', changes)
editor.focus_set()

editor.insert(INSERT, """#Heading 1

##Heading 2

###Heading 3
  
This is a *bold* move!


- Markdown Editor -

""")

display = Text(
    root,
    height=5,
    width=width,
    bg=displayBackground,
    fg=displayTextColor,
    border=30,
    relief=FLAT,
    font=f"{displayFontName} {normalSize}",
)
display.pack(expand=1, fill=BOTH, side=LEFT)
display['state'] = DISABLED
changes()
root.mainloop()
