import pygame
import math
import random
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
        caught = 0
        music = 0
        cycles = 0
        x_rand_mon = random.randint(-4,4)
        y_rand_mon = random.randint(-4,4)

        # Sound
        win_sound = pygame.mixer.Sound('sounds/win.wav')

        # keys
        KEY_UP = 273
        KEY_DOWN = 274
        KEY_LEFT = 276
        KEY_RIGHT = 275

        # Objects

        # Hero

        hero = Hero((self.width/2-16), (self.height/2-16))
  
        # Monster

        monster = Monster(150, 50)

        stop_game = False
        while not stop_game:
            cycles += 1
            
            for event in pygame.event.get():

                # Event handling

                if event.type == pygame.KEYDOWN:
                    if event.key == KEY_DOWN:
                        hero.yspd += 2
                    elif event.key == KEY_UP:
                        hero.yspd += -2
                    elif event.key == KEY_LEFT:
                        hero.xspd += -2
                    elif event.key == KEY_RIGHT:
                        hero.xspd += 2
                    elif event.key == pygame.K_RETURN:
                        # RESTART CODE
                        hero = Hero((self.width/2-16), (self.height/2-16))
                        monster = Monster(150, 50)
                        caught = 0
                        music = 0
                    elif event.key == pygame.K_ESCAPE:
                        stop_game = True
                if event.type == pygame.KEYUP:
                    if event.key == KEY_DOWN:
                        hero.yspd += -2
                    elif event.key == KEY_UP:
                        hero.yspd += 2
                    elif event.key == KEY_LEFT:
                        hero.xspd += 2
                    elif event.key == KEY_RIGHT:
                        hero.xspd += -2
                    

                if event.type == pygame.QUIT:
                    stop_game = True

            # Game logic

            if cycles == 60:
                x_rand_mon = random.randint(-2,2)
                y_rand_mon = random.randint(-2,2)
                cycles = 0
            monster.move(x_rand_mon,y_rand_mon)
            hero.update()

            if monster.active == 1:
                if monster.xpos + 32 < hero.xpos:
                    caught = 0
                elif hero.xpos + 32 < monster.xpos:
                    caught = 0
                elif monster.ypos + 32 < hero.ypos:
                    caught = 0
                elif hero.ypos + 32 < monster.ypos:
                    caught = 0
                else:
                    caught = 1
            

            # Draw background - constant
            
            self.screen.blit(self.bkg, (0,0))

            #Draw Characters
            self.screen.blit(hero.sp, (hero.xpos, hero.ypos))

            if monster.active == 1:
                self.screen.blit(monster.sp, (monster.xpos, monster.ypos))
            
            if caught == 1:
                if music == 0:
                    win_sound.play()
                    music += 1
                self.draw_text("You win! Press enter to play again, ESC to quit!")
                monster.active = 0
 
            # Game display

            pygame.display.update()
            self.clock.tick(60)
  
        pygame.quit()

    def draw_text(self, text):
        """Center text in window
        """
        fw, fh = self.font.size(text) # fw: font width,  fh: font height
        surface = self.font.render(text, True, (255, 255, 255))
        # // makes integer division in python3
        self.screen.blit(surface, ((self.width - fw) // 2, (self.height - fh) // 2))

if __name__ == '__main__':
    MonChase().run()