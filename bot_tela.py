from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import PySimpleGUI as sg

tela1 = [
    [sg.Text('SENHA')],
    [sg.Input(key='senha', password_char='*')],
    [sg.Button('ENTRAR')],
]

tela2 = [
    [sg.Text('segunda tela')],
]

windows1 = sg.Window('BOT WPP', layout=tela1)
windows2 = sg.Window('BOT WPP', layout=tela2)

while True:
    event, values = windows1.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'ENTRAR':
        senha = values['senha']
        if senha == '1234':
            windows1.close()
            event2, values2 = windows2.read()
