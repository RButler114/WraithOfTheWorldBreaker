import sys, json, pygame
from app.states.character_select import CharacterSelect
from app.states.menu.menu import MenuState
from app.states.menu.game_settings import SettingsMenu

json_file_path = "save_data.json"
with open(json_file_path) as save_data:
	SAVED_DATA = json.load(save_data)

class TitleMenu(MenuState):
	def __init__(self, game):
		MenuState.__init__(self, game)
		
		# set menu options
		if SAVED_DATA:
			self.menu_options = ['New Game', 'Continue Game','Options', 'Credits', 'Quit']	
		else:
			self.menu_options = ['Start Game', 'Options', 'Credits', 'Quit']	
		self.set_background("menu_background.png")

		self.title_sound = pygame.mixer.Sound('audio/main.ogg')
		self.title_sound.set_volume(0.5)
		self.title_sound.play()

	def update(self, delta_time, actions):
		#update menu
		self.update_cursor(actions)   
		if (actions['start']): 
			if (self.menu_options[self.menu_index] == 'New Game') or (self.menu_options[self.menu_index] == 'Start Game'):
				self.title_sound.stop()
				new_state = CharacterSelect(self.game)
				new_state.enter_state()
			elif self.menu_options[self.menu_index] == 'Continue Game':
				pass
			elif self.menu_options[self.menu_index] == 'Options':
				new_state = SettingsMenu(self.game)
				new_state.enter_state()
			elif self.menu_options[self.menu_index] == 'Quit':
				pygame.quit()
				sys.exit()

		self.game.reset_keys()

	def render(self, display):
		display.fill((255,255,255))
		# set the current frame image
		display.blit(self.background_image, (0, 0))
		self.draw_options(display)
		display.blit(self.cursor_img, self.cursor_rect)

	def transition_menu(self):
		self.curr_menu = self.menu_options[self.menu_index]
