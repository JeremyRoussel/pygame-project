import pygame
from sprites import *
# from gameinit import *

class MonChase():
    def __init__(self, width=512, height=480, fps=60):
        ### Initialize pygame, window, background, font, sprites
        pygame.init()
        pygame.display.set_caption('Monster Chase')
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.bkg = pygame.image.load('images/background.png').convert()
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.playtime = 0.0
        self.font = pygame.font.SysFont('mono', 20, bold=True)

    def run(self):
        # Game initialization

        # Sprite loading
        goblin_sp = pygame.image.load('images/goblin.png').convert_alpha()
        monster_sp = pygame.image.load('images/monster.png').convert_alpha()

    

        # Objects

        # Hero

        hero = Hero((self.width/2-16), (self.height/2-16))
  
        # Monster

        monster = Monster(150, 50)

        stop_game = False
        while not stop_game:
            for event in pygame.event.get():

                # Event handling

                if event.type == pygame.QUIT:
                    stop_game = True


            # Game logic
            monster.move(2,2)

            # Draw background - constant
            
            self.screen.blit(self.bkg, (0,0))

            #Draw Characters
            self.screen.blit(hero.sp, (hero.xpos, hero.ypos))
            self.screen.blit(monster.sp, (monster.xpos, monster.ypos))
            


            

            # Game display

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()

if __name__ == '__main__':
    MonChase().run()