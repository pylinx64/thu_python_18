import pyxel
import random

class App:
    # конструктор
    def __init__(self):
        # запускает pyxel (x, y, название)
        pyxel.init(160, 160, caption='Hello cyberworld 2088 !#@$!@')
        # чтобы курсор не скрывать
        pyxel.mouse(True)
        # вместо while True
        pyxel.run(self.update, self.draw)
    
    # триггер обновление экрана
    def update(self):
        pass
        
    # рисование
    def draw(self):
        # обновляет экран
        pyxel.cls(0)
        # текст (x, y, текст, номер цвета)
        pyxel.text(50, 80, 'GTA 77 v magazine', random.randint(0,15))
    
App()
