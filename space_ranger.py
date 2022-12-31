import sys

import pygame

def run_game():
	"""Initialie game and draw screen"""
	pygame.init()
	screen = pygame.display.set_mode((1200,800))
	pygame.display.set_caption("Space Ranger")

	"""Game Start"""
	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		"""Display recently drawn screen"""
		pygame.display.flip()

run_game()
		