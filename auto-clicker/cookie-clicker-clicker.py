import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode
import pyautogui

TOGGLE_KEY = KeyCode(char="t")
clicking = False
mouse = Controller()
counter = 0



def left_click():
    print(pyautogui.position())
    x,y = pyautogui.position()
    pyautogui.click(x, y)





def clicker ():
    while True:
        if clicking:
            global counter
            mouse.click(Button.left,1)
            left_click()
            print('click'+str(counter))
            counter+=1
        else:
            print('no click')
        time.sleep(0.001)

def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking

clicking_thread = threading.Thread(target=clicker)
clicking_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()