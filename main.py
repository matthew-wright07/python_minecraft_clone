from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

block_texture_dirt = load_texture('dirt.png')
block_texture_grass = load_texture('grass.png')
sky_texture = load_texture('sky.png')
custom_crosshair_texture = load_texture('crosshair.png')

for z in range(20):
    for x in range(20):
        dirt_block = Entity(
            model='cube',
            texture=block_texture_dirt,
            scale=(1, 1, 1),
            position=(x, 0, z),
            collider='box'
        )
        grass_block = Entity(
            model='cube',
            texture=block_texture_grass,
            scale=(1, 1, 1),
            position=(x, 1, z)
        )
player = FirstPersonController()
player.gravity = .1
player.jump_height = 2
player.cursor.visible = True
player.cursor.color=color.white
player.cursor.texture = custom_crosshair_texture
player.cursor.scale = .05
player.cursor.rotation_z = 90

Sky(texture=sky_texture)

def input(key):
    if key == 'escape':
        application.quit()

app.run()