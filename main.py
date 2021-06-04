import pyautogui
import requests
import time
import os
from os import system

botted = 0

os.system(f'title Roblox Visit Bot ^| Botted: {botted} ^')

def bot():
    while True:
        global botted
        time.sleep(3)
        button_pos = pyautogui.locateOnScreen('play.PNG')
        pyautogui.moveTo(button_pos)
        pyautogui.click()
        time.sleep(25)
        button_pos = pyautogui.locateOnScreen('exit.PNG')
        pyautogui.moveTo(button_pos)
        pyautogui.click()
        botted += 1
        os.system(f'title Roblox Visit Bot ^| Botted: {botted} ^')
bot()
