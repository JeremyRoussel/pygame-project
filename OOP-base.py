import pygame
import math
import random
from sprites import *
# from gameinit import *

class MonChase():
    def __init__(self, width=512, height=480, fps=60):
        ### Initialize pygame, window, background, font, sprites
        pygame.init()
        pygame.display.set_caption('Monster Chase Level 1')
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
        defeat = 0
        music = 0
        cycles = 0
        x_rand_mon = random.randint(-4,4)
        y_rand_mon = random.randint(-4,4)
        distance = 0
        level = 1
        start = 1
        loser = 0

        # Sound
        win_sound = pygame.mixer.Sound('sounds/win.wav')
        lose_sound = pygame.mixer.Sound('sounds/lose.wav')

        # keys
        KEY_UP = 273
        KEY_DOWN = 274
        KEY_LEFT = 276
        KEY_RIGHT = 275

        # Objects

        # Hero
        hero = Hero(420, 400)
  
        # Monster
        monster = Monster(random.randint(40,200), random.randint(40,200))

        # Create Goblins equal to current level
        goblin_list = []
        goblin_move_list = []
        for n in range(0,level):
            goblin_list.append(Goblin(random.randint(0,300), random.randint(0,300)))
            goblin_move_list.append([random.randint(-2,2), random.randint(-2,2)])

        stop_game = False
        while not stop_game:
            cycles += 1

            if start == 1:
                goblin_list = []
                goblin_move_list = []
                for n in range(0,level):
                    goblin_list.append(Goblin(random.randint(0,300), random.randint(0,300)))
                    goblin_move_list.append([random.randint(-2,2), random.randint(-2,2)])
                start = 0
            
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
                        # RESTART CODE, only if winner!
                        if loser == 0:
                            hero = Hero(420, 400)
                            monster = Monster(random.randint(40,200), random.randint(40,200))
                            caught = 0
                            music = 0
                            distance = 0
                            start = 1
                            level += 1
                            pygame.display.set_caption(f'Monster Chase Level {level}')
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
                
                goblin_move_list = []
                for n in range(0,level):
                    goblin_move_list.append([random.randint(-2,2), random.randint(-2,2)])

                cycles = 0
            
            monster.move(x_rand_mon,y_rand_mon)
            for i, gobbo in enumerate(goblin_list):
                gobbo.move(goblin_move_list[i][0], goblin_move_list[i][1])
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

            if monster.active == 1:
                for gobbo in goblin_list:
                    defeat = self.lost(gobbo, hero)
                    if defeat == 1:
                        loser = 1
            

            # Draw background - constant
            
            self.screen.blit(self.bkg, (0,0))

            #Draw Characters
            self.screen.blit(hero.sp, (hero.xpos, hero.ypos))

            if monster.active == 1:
                self.screen.blit(monster.sp, (monster.xpos, monster.ypos))
                for gobbo in goblin_list:
                    self.screen.blit(gobbo.sp, (gobbo.xpos, gobbo.ypos))
            
            if caught == 1:
                if music == 0:
                    win_sound.play()
                    music += 1
                self.draw_text("You win! Press enter to play again, ESC to quit!")
                monster.active = 0

            if loser == 1:
                if music == 0:
                    lose_sound.play()
                    music += 1
                else:
                    pass
                self.draw_text('You lose! Press ESC to quit!')
                monster.active = 0
            else:
                pass

 
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

    def lost(self, goblin, hero):
        if goblin.xpos + 32 < hero.xpos:
            defeat = 0
        elif hero.xpos + 32 < goblin.xpos:
            defeat = 0
        elif goblin.ypos + 32 < hero.ypos:
            defeat = 0
        elif hero.ypos + 32 < goblin.ypos:
            defeat = 0
        else:
            defeat = 1
        return defeat


if __name__ == '__main__':
    MonChase().run()