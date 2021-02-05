import random

import time

list_game = ['Minecraft', 'NFS', 'Far Cry', 'Dead Space 3', 'GTA 5']

t = 0.2

print("$$$ Hello KeysWorld $$$")
time.sleep(t)

money = input("-> Введите кол-во денег: ")

while True:
	if (money == 'q') or (int(money) < 0):
		print("Crasshhhhh.//sd324235teroptb4356b094")
		time.sleep(t)
		break
	else:
		game = random.choice(list_game)
		print("Ура ты выйграл ", game)
		time.sleep(t)
		money = int(money) - 200

print("Game over")
		
