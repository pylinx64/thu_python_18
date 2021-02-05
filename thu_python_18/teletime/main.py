from telethon import TelegramClient, sync
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from datetime import datetime
import time
from config import *
from time_pic import *

# подключение к телеграмму
client = TelegramClient('ananas', api_id, api_hash)
client.start()


while True:
	# меняет картинки
    change_img()
    # удаляет картинку из телеграмм
    client(DeletePhotosRequest(client.get_profile_photos('me')))
    # хранится картинка
    file = client.upload_file(f"time.png")
    # заружает картинку из телеграмм
    client(UploadProfilePhotoRequest(file))
	# каждіе 1 мин меняет
    time.sleep(60)
