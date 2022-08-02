import pygame
from app.states.menu.menu import MenuState

class SettingsMenu(MenuState):
	def __init__(self, game):
		MenuState.__init__(self, game)
		self.menu_options = ['Volume', 'Brightness','Back']	
		self.menu_index = 0

		if game.paused == True:
			self.set_background("menu_background.png")
		else:
			self.set_background("menu_background.png")

	def update(self, delta_time, actions):
		self.update_cursor(actions)   
		if (actions['start']): 
			if self.menu_options[self.menu_index] == 'Volume':
	 			self.edit_vol()
			elif self.menu_options[self.menu_index] == 'Brightness':
			 	self.edit_vol()
			else:
				self.exit_state()
		self.game.reset_keys()

	def render(self, display):
		display.fill((255,255,255))
		# set the current frame image
		display.blit(self.background_image, (0, 0))
		self.draw_options(display)
		display.blit(self.cursor_img, self.cursor_rect)

	def edit_vol(self):
		pass

	def edit_brightness(self):
		pass
