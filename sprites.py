import pygame as pygame

class sprites():
    def __init__(self, x_pos, y_pos):
        self.xpos = x_pos
        self.ypos = y_pos
        self.xspd = 0
        self.yspd = 0
    
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

    def update(self):
        x_mov = self.xspd
        y_mov = self.yspd
        self.move(x_mov, y_mov)

class Hero(sprites):
    def __init__(self, x_pos, y_pos):
        self.sp = pygame.image.load('images/hero.png').convert_alpha()
        super(Hero, self).__init__(x_pos, y_pos)

    def move(self, x_mov, y_mov):
        if x_mov > 0:
            if self.xpos + x_mov > 448:
                self.xpos = 448
            else:
                self.xpos += x_mov
        elif x_mov < 0:
            if self.xpos + x_mov < 32:
                self.xpos = 32
            else:
                self.xpos += x_mov
        if y_mov > 0:
            # Reset to top if off bottom
            if self.ypos + y_mov > 416:
                self.ypos = 416
            else:
                self.ypos += y_mov
        elif y_mov < 0:
            #Rest to bottom if off top
            if self.ypos + y_mov < 32:
                self.ypos = 32
            else:
                self.ypos += y_mov

class Monster(sprites):
    def __init__(self, x_pos, y_pos):
        self.sp = pygame.image.load('images/monster.png').convert_alpha()
        super(Monster, self).__init__(x_pos, y_pos)

class Goblin(sprites):
    def __init__(self, x_pos, y_pos):
        self.sp = pygame.image.load('images/goblin.png').convert_alpha()
        super(Goblin, self).__init__(x_pos, y_pos)