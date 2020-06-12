import pygame as pygame
# import pgzrun

class sprites():
    def __init__(self, x_pos, y_pos):
        self.xpos = x_pos
        self.ypos = y_pos
    
    def move(self, x_mov, y_mov):
        if x_mov > 0:
            if self.xpos + x_mov > 512:
                self.xpos = self.xpos + x_mov - 512
            else:
                self.xpos += x_mov
        elif x_mov < 0:
            if self.xpos + x_mov < 0:
                self.xpos = self.xpos + x_mov + 512
            else:
                self.xpos += x_mov
        if y_mov > 0:
            # Reset to top if off bottom
            if self.ypos + y_mov > 480:
                self.ypos = self.ypos + y_mov - 480
            else:
                self.ypos += y_mov
        elif y_mov < 0:
            #Rest to bottom if off top
            if self.ypos + y_mov < 0:
                self.ypos = self.ypos + y_mov + 480
            else:
                self.ypos += y_mov
        

def main():
    width = 512
    height = 480
    
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()
    
    # Sprite loading
    bkg = pygame.image.load('images/background.png').convert()
    hero_sp = pygame.image.load('images/hero.png').convert_alpha()
    goblin_sp = pygame.image.load('images/goblin.png').convert_alpha()
    monster_sp = pygame.image.load('images/monster.png').convert_alpha()

    # Game initialization

    monster_x_pos = 50

    # Objects

    # Hero

    hero = sprites((width/2-16), (height/2-16))
    

    # Goblin

    # Monster

    monster = sprites(150, 50)

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        monster.move(2,2)

            # if monster_x_pos < 500:
            #     monster_x_pos += 2
            # else:
            #     monster_x_pos = 0


        # Draw background - constant
        
        screen.blit(bkg, (0,0))

        #Draw Characters
        screen.blit(hero_sp, (hero.xpos, hero.ypos))
        screen.blit(monster_sp, (monster.xpos, monster.ypos))
        


        

        # Game display

        pygame.display.update()
        clock.tick(60)

    pygame.quit()


# pgzrun.go()

if __name__ == '__main__':
    main()