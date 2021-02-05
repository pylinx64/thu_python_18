from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

while True:
	pos = mc.player.getTilePos()
	mc.setBlock(pos.x - 1, pos.y, pos.z, 46)
	mc.setBlock(pos.x - 1, pos.y + 1, pos.z, 152)
	mc.setBlock(pos.x - 1, pos.y + 1, pos.z, 0)
	time.sleep(1)

