import pyautogui as pag
import time
from playsound import playsound
from threading import Event
from pynput import keyboard
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

wqeqw = input("Enter To Start")
x = pag.position()[0]
y = pag.position()[1]
playsound(filename)

exit = Event()

cancelCombination = keyboard.Key.esc
def on_press(key):
    global exit
    if(key == cancelCombination):
        exit.set()

listener =  keyboard.Listener(on_press=on_press) 
listener.start()

while True:
    try:
        color =pag.pixel(x,y)
        break
    except Exception as e:
        pass


while(not exit.is_set()):
    try:
        current_color = pag.pixel(x,y)
        if(current_color!=color):
            while True:
                playsound(filename)
                if(exit.is_set()):
                    break
    except Exception as e:
        pass
    exit.wait(1)
