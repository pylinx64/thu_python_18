from mcpi.minecraft import Minecraft

mc = Minecraft.create()

#mc.player.setTilePos(100, 100, 100)

position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z
block = 1

mc.setBlock(x+1, y, z-1, block)
