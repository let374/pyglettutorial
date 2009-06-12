import pyglet, random
import physicalobject, resources, util

def player_lives(num_icons, batch=None):
    """Generate sprites for player life icons"""
    player_lives = []
    start_x = 800 - 30 * num_icons
    for i in range(num_icons):
        new_sprite = pyglet.sprite.Sprite(img=resources.player_image, 
                                          x=start_x+i*30, y=585, 
                                          batch=batch)
        new_sprite.scale = 0.5
        player_lives.append(new_sprite)
    return player_lives

def asteroids(num_asteroids, player_position, batch):
    """Generate asteroid objects with random positions and velocities, not close to the player"""
    asteroids = []
    for i in range(num_asteroids):
        asteroid_x, asteroid_y = player_position
        while util.distance((asteroid_x, asteroid_y), player_position) < 100:
            asteroid_x = random.randint(0, 800)
            asteroid_y = random.randint(0, 600)
        new_asteroid = physicalobject.PhysicalObject(img=resources.asteroid_image, 
                                                     x=asteroid_x, y=asteroid_y,
                                                     batch=batch)
        new_asteroid.rotation = random.randint(0, 360)
        new_asteroid.vx, new_asteroid.vy = random.random()*40, random.random()*40
        asteroids.append(new_asteroid)
    return asteroids