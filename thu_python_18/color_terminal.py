import colorama
import tqdm
import time
from colorama import Fore

colorama.init()

print(Fore.RED+'доллар по 8!'+Fore.RESET)
print('доллар по 8!')

for elem in tqdm.tqdm(range(100), ascii=True, desc='Загрузка вируса 2020'):
	time.sleep(0.2)
