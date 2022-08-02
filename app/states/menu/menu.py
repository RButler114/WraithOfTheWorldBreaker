import os, sys, json, pygame
from app.states.state import State

class MenuState(State):
	def __init__(self, game ):
		State.__init__(self, game)
		self.menu_options = []	
		self.menu_index = 0
		self.cursor_rect = pygame.Rect(0, 0, 20, 20)

		self.y_offset = -50
		# Set cursor states
		self.cursor_img = pygame.image.load('graphics/cursor/cursor.png')
		self.cursor_rect = self.cursor_img.get_rect()
		self.cursor_pos_y = self.y_offset + self.game.GMID_H
		self.cursor_rect.x, self.cursor_rect.y = self.game.GMID_W - 75, self.cursor_pos_y

		self.cursor_sound = pygame.mixer.Sound('audio/cursor.wav')
		self.cursor_sound.set_volume(0.5)

	def update_cursor(self, actions):	
		if actions['down']:
			self.menu_index = (self.menu_index + 1) % len(self.menu_options)
			self.cursor_sound.play()	
		elif actions['up']:
			self.menu_index = (self.menu_index - 1) % len(self.menu_options)
			self.cursor_sound.play()
		# Update cursor location
		self.cursor_rect.y = self.cursor_pos_y + (self.menu_index * 38)

	def draw_options(self, display):
		for idx, option in enumerate(self.menu_options):
			self.game.draw_text(display, option, 'black', self.game.GMID_W, self.y_offset + self.game.GMID_H + idx * 40,'default', (40 if self.menu_index == idx else 30))

	def set_background(self, image):
		self.background_image = pygame.image.load('graphics/backgrounds/'+image)
