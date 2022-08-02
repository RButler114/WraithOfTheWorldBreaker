import os, pygame
from app.config.settings import CHARACTER_DATA
from app.states.state import State
from app.states.world.game_world import GameWorld

class CharacterSelect(State):
	def __init__(self, game):
		State.__init__(self, game)
		self.character_options = CHARACTER_DATA['characters']
		self.menu_index = 0
		self.background_image = pygame.image.load('graphics/backgrounds/character_select.png')
		self.selected_character = self.character_options[0]
		self.load_portrait()

		# set fonts
		self.font_size = 20
		self.title_font_size = 30
		self.line_scaling = 1.25

		self.cursor_rect = pygame.Rect(0, 0, 20, 20)
		# Set cursor states
		self.cursor_img = pygame.image.load('graphics/cursor/cursor.png')
		self.cursor_rect = self.cursor_img.get_rect()
		self.cursor_pos_y = 180
		self.cursor_rect.x, self.cursor_rect.y = 95, self.cursor_pos_y

		# sound 
		self.cursor_sound = pygame.mixer.Sound('audio/cursor.wav')
		self.select_sound = pygame.mixer.Sound('audio/selectTheme.wav')
		self.select_sound.set_volume(0.5)
		self.cursor_sound.set_volume(0.5)
		self.select_sound.play(loops=-1)


	def update(self, delta_time, actions):
		self.update_cursor(actions)   
		if (actions['start']): 
			self.selected_character = self.character_options[self.menu_index]
			self.load_portrait()
		elif (actions['yes']): 
			self.select_sound.stop()
			new_state = GameWorld(self.game, self.selected_character)
			new_state.enter_state()
			pass
		self.game.reset_keys()

	def render(self, display):
		display.fill((255,255,255))
		# set the current frame image
		display.blit(self.background_image, (0, 0))
		display.blit(self.cursor_img, self.cursor_rect)

		# Navigation Info
		self.game.draw_text(display, "[W] navigate Up [Enter] to Select", 'white', 140, 320 ,'default', 12)
		self.game.draw_text(display, "[S] Navigate Down [Y] to Start Game", 'white', 140, 340 ,'default', 12)

		# Character Options
		self.game.draw_text(display, "Select", 'white',190, 90 ,'default', self.title_font_size)
		self.game.draw_text(display, "Character", 'white',160, 90 + (self.title_font_size * self.line_scaling)  ,'default', self.title_font_size)
		for idx, character in enumerate(self.character_options):
			self.game.draw_text(
				display, 
				character['name'], 
				'white', 
				120, 
				self.cursor_pos_y + idx * (self.font_size * self.line_scaling), 
				'default', 
				self.font_size
			)

		# Selected Character
		self.draw_selection(display)

	def draw_selection(self, display):
		# Selection Stats
		self.game.draw_text(display, "Stats", 'white', 570, 100,'default', self.title_font_size)
		for idx, stat in enumerate(self.selected_character['stats'].items()):
			self.game.draw_text(
				display, 
				stat[0].capitalize()+": "+str(stat[1]), 
				'white',
				500, 
				150 + idx * (self.font_size * self.line_scaling) ,
				'default', 
				self.font_size
			)

		# Selection Details		
		self.game.draw_text(display, "Class: "+self.selected_character['class'] , 'white', 160, 480,'default', self.title_font_size)
		self.game.draw_text(display, "Weapons", 'white', 140, 520,'default', self.title_font_size)
		for idx, weapon in enumerate(self.selected_character['weapons']):
			self.game.draw_text(
				display, 
				weapon, 
				'white', 
				140, 
				(self.title_font_size * self.line_scaling) + 520 + idx * (self.font_size * self.line_scaling) ,
				'default', 
				self.font_size
			)
		self.game.draw_text(display, "Spells" if 'spells' in self.selected_character else "Skills", 'white', 440, 520,'default',  self.title_font_size)
		for idx, ability in enumerate(self.selected_character[("spells" if 'spells' in self.selected_character else "skills")]):
			self.game.draw_text(
				display, 
				ability, 
				'white', 
				440,  
				(self.title_font_size * self.line_scaling) + 520 + idx * (self.font_size * self.line_scaling) ,
				'default', 
				self.font_size
			)

		display.blit(self.character_portrait, (860, 120))
		self.game.draw_text(display, self.selected_character['race'] , 'white', 880, 610,'default', self.title_font_size)

	def update_cursor(self, actions):	
		if actions['down']:
			self.menu_index = (self.menu_index + 1) % len(self.character_options)
			self.cursor_sound.play()	
		elif actions['up']:
			self.menu_index = (self.menu_index - 1) % len(self.character_options)
			self.cursor_sound.play()	
		self.cursor_rect.y = self.cursor_pos_y + (self.menu_index * self.font_size * self.line_scaling)

	def load_portrait(self):
		self.character_portrait = pygame.image.load('graphics/player/'+self.selected_character['asset_path']+'/'+self.selected_character['portrait'])
		self.character_portrait = pygame.transform.scale(self.character_portrait, (312.5,312.5))

	def function():
		pass


