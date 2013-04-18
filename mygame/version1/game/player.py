import math, pyglet
from pyglet.window import key
import physicalobject, resources, bullet

class Player(physicalobject.PhysicalObject):

	def __init__(self, *args, **kwargs):
		super(Player, self).__init__(img=resources.player_image, *args, **kwargs)

		self.thrust = 300.0
		self.rotate_speed = 200.0
		self.bullet_speed = 700.0

		self.key_handler = key.KeyStateHandler()
		self.engine_sprite = pyglet.sprite.Sprite(img=resources.engine_image, *args, **kwargs)
		self.engine_sprite.visible = False

		self.reacts_to_bullets = False

	"""
	def on_key_press(self, symbol, modifiers):
		if symbol == key.UP:
			self.keys['up'] = True
		elif symbol == key.LEFT:
			self.keys['left'] = True
		elif symbol == key.RIGHT:
			self.keys['right'] = True

	def on_key_release(self, symbol, modifiers):
		if symbol == key.UP:
			self.keys['up'] = False
		elif symbol == key.LEFT:
			self.keys['left'] = False
		elif symbol == key.RIGHT:
			self.keys['right'] = False
	"""

	def on_key_press(self, symbol, modifiers):
		if symbol == key.SPACE:
			self.fire()


	def update(self, dt):
		super(Player, self).update(dt)

		if self.key_handler[key.LEFT]:
			self.rotation -= self.rotate_speed * dt
		if self.key_handler[key.RIGHT]:
			self.rotation += self.rotate_speed * dt

		if self.key_handler[key.UP]:
			angle_radians = -math.radians(self.rotation)
			force_x = math.cos(angle_radians) * self.thrust * dt
			force_y = math.sin(angle_radians) * self.thrust * dt
			self.velocity_x += force_x
			self.velocity_y += force_y

			self.engine_sprite.rotation = self.rotation
			self.engine_sprite.x = self.x
			self.engine_sprite.y = self.y
			self.engine_sprite.visible = True
		else:
			self.engine_sprite.visible = False

	def delete(self):
		self.engine_sprite.delete()
		super(Player, self).delete()

	def fire(self):
		angle_radians = -math.radians(self.rotation)

		ship_radius = self.image.width/2
		bullet_x = self.x + math.cos(angle_radians) * ship_radius
		bullet_y = self.y + math.sin(angle_radians) * ship_radius
		new_bullet = bullet.Bullet(bullet_x, bullet_y, batch=self.batch)

		bullet_vx = self.velocity_x + math.cos(angle_radians) * self.bullet_speed
		bullet_vy = self.velocity_y + math.sin(angle_radians) * self.bullet_speed
		new_bullet.velocity_x, new_bullet.velocity_y = bullet_vx, bullet_vy

		self.new_objects.append(new_bullet)