import pygame, sys
from code.settings import *
from code.level import Level
from code.home_screen import HomeScreen
from code.gameover import GameOverScreen

class Game:
	def __init__(self):

		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('Zelda')
		self.clock = pygame.time.Clock()

		self.start = HomeScreen(self.screen)

		# sound 
		main_sound = pygame.mixer.Sound('audio/main.ogg')
		main_sound.set_volume(0.5)
		main_sound.play(loops = -1)
	
	def run(self):
		on_home_screen = True
		on_game_over_screen = False
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_m:
						self.level.toggle_menu()

			self.screen.fill(WATER_COLOR)

			if on_home_screen:
				result = self.start.run()
				if result == 'game_start':
					self.level = Level()
					on_home_screen = False
				elif result == 'exit':
					pygame.quit()
					sys.exit()
			
			elif on_game_over_screen:
				score = self.level.get_player_exp()
				game_over_screen = GameOverScreen(self.screen,score)
				result = game_over_screen.run()
				if result == 'restart':
					self.level = Level()
					on_game_over_screen = False
				elif result == 'exit':
					pygame.quit()
					sys.exit()
			else:
				result = self.level.run()
				if result == 'game_over':
					on_game_over_screen = True

			pygame.display.update()
			self.clock.tick(FPS)

if __name__ == '__main__':
	game = Game()
	game.run()