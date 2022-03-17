# pip install pyfiglet
import pyfiglet
from pyfiglet import Figlet

msg1="""choose your font:
1
_                          _ _ 
| |__  _ __ __ ___   _____ | | |
| '_ \| '__/ _` \ \ / / _ \| | |
| |_) | | | (_| |\ V / (_) |_|_|
|_.__/|_|  \__,_| \_/ \___/(_|_)


2
  ___ ___         .__  .__        ._._.
 /   |   \   ____ |  | |  |   ____| | |
/    ~    \_/ __ \|  | |  |  /  _ \ | |
\    Y    /\  ___/|  |_|  |_(  <_> )|\|
 \___|_  /  \___  >____/____/\____/____
       \/       \/                 \/\/

"""
msg2="""print it or save to file?
1           print
2           save to file
"""

while True:
    inp1 =input(msg1)
    if(inp1.lower()=='q'):
        print("bye bye")
        break
    inp2 = input(msg2)
    inp3 = input('Enter text:')
    if inp2 == '1':
        if inp1 == '1':
            print(pyfiglet.figlet_format(inp3))
        elif inp1 =='2':
            custom_fig = Figlet(font='graffiti')
            print(custom_fig.renderText(inp3))

    if inp2 == '2':
        pass
    

    