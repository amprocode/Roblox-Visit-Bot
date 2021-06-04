import pyautogui
import requests
import time
import os
from os import system

botted = 0

os.system(f'title Roblox Visit Bot By (...)#4953 ^| Botted: {botted} ^')

def bot():
    while True:
        global botted
        time.sleep(3) #this is here to allow roblox to close down fully before starting again (mainly for laggy PC's)
        button_pos = pyautogui.locateOnScreen('play.PNG')
        pyautogui.moveTo(button_pos)
        pyautogui.click()
        time.sleep(25) #change to average time to load up a roblox game (seconds)
        button_pos = pyautogui.locateOnScreen('exit.PNG')
        pyautogui.moveTo(button_pos)
        pyautogui.click()
        botted += 1
        os.system(f'title Roblox Visit Bot (...)#4953 ^| Botted: {botted} ^')
bot()
