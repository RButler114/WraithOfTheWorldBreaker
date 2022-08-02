import os, pygame
from math import sin
from app.config.support import import_folder
from app.states.state import State

class LoseScreen(State):
	def __init__(self, game):
		State.__init__(self, game)
		self.game = game
		# animation info
		self.frame_index = 0
		self.animation_speed = 0.175
		self.animations = {'gameover': []}
		self.animations['gameover'] = import_folder('graphics/backgrounds/game-over/')
		self.image = pygame.image.load('graphics/test/player.png').convert_alpha()

		# sounds
		self.title_sound = pygame.mixer.Sound('audio/gameover.wav')
		self.title_sound.set_volume(0.5)
		self.title_sound.play()

		self.timer = 500

	def update(self, delta_time, actions):
		if (actions['time_trigger']): 
			self.timer -= 1
			if self.timer == 0:
				pygame.time.set_timer(self.game.timer_event, 0)
				# reset state stack to start
				del self.game.state_stack[2:len(self.game.state_stack)]
				self.game.state_stack[0].__init__(self.game)
				self.exit_state()
		self.animate()
		
	def render(self, display):
		display.fill((0,0,0))
		display.blit(self.image, (self.game.GMID_W-(self.image.get_width()/2),self.game.GMID_H-(self.image.get_height()/2)))

	def animate(self):
		animation = self.animations['gameover']

		# loop over the frame index 
		self.frame_index += self.animation_speed
		if self.frame_index >= len(animation):
			self.frame_index = 0

		# set the image
		self.image = animation[int(self.frame_index)]
		self.rect = self.image.get_rect(center = (0,0))
		self.image.set_alpha(255)