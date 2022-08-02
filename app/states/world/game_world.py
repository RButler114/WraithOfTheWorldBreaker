import pygame
from app.states.state import State
from app.levels.level import Level
from app.states.lose_screen import LoseScreen


class GameWorld(State):
	def __init__(self, game, character):
		State.__init__(self, game)
		self.game_paused = False
		self.game_over = False

		self.levels = []

		# Add further logic here to dertmine if save data exists
		# If save data exists, use the data to initiate the correct level 
		# Otherwise initiate a new game
		self.level = Level(game.game_canvas, character)
		self.levels.append(self.level)

		# set game world's current level
		self.current_level = self.levels[0]


	def update(self, delta_time, actions):
		self.current_level.check_state()
		if self.current_level.game_over:
			self.current_level.stopMusic()
			new_state = LoseScreen(self.game)
			new_state.enter_state()
		elif actions['pause']:
			self.current_level.toggle_menu()
		else:
			# make sure the  correct level is loaded in
			if self.current_level.level_complete:
				# logic to progress to next level
				new_state = WinScreen(self.game)
				new_state.enter_state()
				pass
			else:
				self.current_level.player.input(actions)
				pass
		#self.game.reset_keys()

	def render(self, display):
		self.current_level.render(display) 
