from os import path
import subprocess

mode = input('Enter mode: ')

file = open('mode.txt', 'w+')
file.write(mode)

content = file.read()

if content == 'pubg':
    print(content)
    subprocess.call([r'C:\Program Files\TxGameAssistant\ui\AndroidEmulator.exe'], shell=True)
else:
    print('no')
