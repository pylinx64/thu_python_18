import time
from PIL import ImageDraw, Image, ImageFont
from datetime import datetime, timedelta

FONT_SIZE = 50
TEXT_Y_POSITION = 1
TEXT_X_POSITION = 1
KIEV_UTC = 4 #укажите ваш часовой пояс 

def convert_time_to_string(dt):
	'''Обновляет время по Киеву и возвращает строку'''
	dt += timedelta(hours=KIEV_UTC)
	return f"{dt.hour}:{dt.minute:02}"

def change_img():
	'''Создает фоточку часиков'''
	# старт время
	start_time = datetime.utcnow()
	# превращает дату в строку
	text = convert_time_to_string(start_time)
	# Цвет фона black,white тд
	row = Image.new('RGBA', (200, 200), "black")
	parsed = ImageDraw.Draw(row)
	#стиль шрифта
	font = ImageFont.truetype("HEADPLANE.ttf", FONT_SIZE)
	font2 = ImageFont.truetype("HEADPLANE.ttf", 15)
	# рисует текст часов на черном фоне с заданным шрифтом
	parsed.text((int(row.size[0]*0.23), int(row.size[1]*0.31)), f'{text}', 
				 align="center", font=font, fill=(3,33,212))
	# сохраняет файл
	row.save(f'time.png', "PNG")
	
if __name__ == '__main__':
    change_img()

