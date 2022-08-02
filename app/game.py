import pygame
import time

from app.config.settings import *
from app.states.menu.title_screen import TitleMenu

DEFAULT_ACTIONS = {
    "left": False,
    "right": False,
    "up": False,
    "down": False,
    "crouch": False,
    "attack": False,
    "cast": False,
    "switch_weapon": False,
    "switch_magic": False,
    "pause": False,
    "action2": False,
    "start": False,
    "yes": False,
    "time_trigger": False,
}


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Wraith Of The Worldbreaker')
        self.clock = pygame.time.Clock()

        # window variables
        self.GAME_W, self.GAME_H = WIDTH, HEIGHT  # 480, 270
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.GMID_W, self.GMID_H = WIDTH, HEIGHT, self.GAME_W / 2, self.GAME_H / 2
        self.game_canvas = pygame.Surface((self.GAME_W, self.GAME_H))
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        # event variables
        self.running, self.playing, self.paused = True, True, False
        self.actions = DEFAULT_ACTIONS
        self.dt, self.prev_time = 0, 0

        # main state stack
        self.state_stack = []

        # font variables
        self.default_fontsize = 20
        self.default_font = pygame.font.Font('font/PressStart2P-vaV7.ttf', 20)

        # run init methods
        self.init_states()

        self.timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.timer_event, 10000)

    def game_loop(self):
        while self.playing:
            self.get_dt()
            self.get_events()
            self.update()
            self.render()
            self.clock.tick(FPS)

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == self.timer_event:
                self.actions['time_trigger'] = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
                    self.running = False
                if event.key == pygame.K_a:
                    self.actions['left'] = True
                if event.key == pygame.K_d:
                    self.actions['right'] = True
                if event.key == pygame.K_w:
                    self.actions['up'] = True
                if event.key == pygame.K_s:
                    self.actions['down'] = True
                if event.key == pygame.K_p:
                    self.actions['pause'] = True
                if event.key == pygame.K_o:
                    self.actions['action2'] = True
                if event.key == pygame.K_y:
                    self.actions['yes'] = True
                if event.key == pygame.K_q:
                    self.actions['cast'] = True
                if event.key == pygame.K_x:
                    self.actions['switch_weapon'] = True
                if event.key == pygame.K_c:
                    self.actions['switch_magic'] = True
                if event.key == pygame.K_RETURN:
                    self.actions['start'] = True
                if event.key == pygame.K_SPACE:
                    self.actions['attack'] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.actions['left'] = False
                if event.key == pygame.K_d:
                    self.actions['right'] = False
                if event.key == pygame.K_w:
                    self.actions['up'] = False
                if event.key == pygame.K_s:
                    self.actions['down'] = False
                if event.key == pygame.K_p:
                    self.actions['pause'] = False
                if event.key == pygame.K_o:
                    self.actions['action2'] = False
                if event.key == pygame.K_y:
                    self.actions['yes'] = False
                if event.key == pygame.K_q:
                    self.actions['cast'] = False
                if event.key == pygame.K_x:
                    self.actions['switch_weapon'] = False
                if event.key == pygame.K_c:
                    self.actions['switch_magic'] = False
                if event.key == pygame.K_RETURN:
                    self.actions['start'] = False
                if event.key == pygame.K_SPACE:
                    self.actions['attack'] = False

    def update(self):
        self.state_stack[-1].update(self.dt, self.actions)

    def render(self):
        # Render current state to the canvas
        self.state_stack[-1].render(self.game_canvas)
        # Render canvas to screen
        self.screen.blit(pygame.transform.scale(self.game_canvas, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)), (0, 0))
        pygame.display.flip()

    def get_dt(self):
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now

    def draw_text(self, surface, text='', color='black', x=0, y=0, font='default', size='default'):
        if (font == 'default') and (size == 'default'):
            font = self.default_font
        elif (font == 'default') and (not size == 'default'):
            font = pygame.font.Font(pygame.font.get_default_font(), size)
        elif size == 'default':
            font = pygame.font.Font('font/' + font, self.default_fontsize)
        # font = pygame.font.Font(os.path.join(self.font_dir, "PressStart2P-vaV7.ttf"), 20)
        else:
            font = pygame.font.Font(font, size)

        text_surface = font.render(text, True, color)
        # text_surface.set_colorkey((0,0,0))
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        text_rect.left = x
        surface.blit(text_surface, text_rect)

    def init_states(self):
        # change here
        self.title_screen = TitleMenu(self)
        self.state_stack.append(self.title_screen)

    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False
