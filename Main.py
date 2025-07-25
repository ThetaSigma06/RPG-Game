import pygame
import sys
from settings import *
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen=pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("RPG Game")
        self.clock=pygame.time.Clock()
        self.level=Level()
        
        main_sound=pygame.mixer.Sound('Audio/main.mp3')
        main_sound.set_volume(0.5)
        main_sound.play(loops=-1)
        

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.KEYDOWN:
                     if event.key==pygame.K_m:
                          self.level.toggle_menu()
            self.screen.fill(WATER_COLOUR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)
            
    
    
    
if __name__ == '__main__':
	game = Game()
	game.run()
    

newvariable="sex"

