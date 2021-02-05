from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

pos = mc.player.getTilePos() # позиция игрока

x1 = pos.x - 2	# позиция танцпола
y1 = pos.y - 1
z1 = pos.z - 2

w = 15	# длина 
l = 20	# ширина
block = 41

x2 = x1 + w
y2 = y1
z2 = z1 + l

mc.setBlocks(x1, y1, z1, x2, y2, z2, block)	# ставит много блоков 

while True:
	if block == 41:
		block = 57
	elif block == 57:
		block = 81
	elif block == 81:
		block = 41
	mc.setBlocks(x1, y1, z1, x2, y2, z2, block)
	time.sleep(0.3)
