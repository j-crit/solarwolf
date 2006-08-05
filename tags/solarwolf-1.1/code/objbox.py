#box class

import random
import pygame
from pygame.locals import *
import game, gfx, snd


boximages = []
yboximages = []
rboximages = []

def load_game_resources():
    global boximages
    for i in range(15):
        img = gfx.load_raw('box%02d.gif'%i)
        boximages.append(img.convert())
        pal = img.get_palette()
        newpal = [(g,g,b) for (r,g,b) in pal]
        img.set_palette(newpal)
        yboximages.append(img.convert())
        newpal = [(g,b,b) for (r,g,b) in pal]
        img.set_palette(newpal)
        rboximages.append(img.convert())  
    snd.preload('boxhit', 'yboxhit')
   

class Box:
    def __init__(self, pos, touches):
        self.rotate = random.randint(0, 89)
        self.rotspeed = random.randint(2, 4)
        if random.randint(0, 1):
            self.rotspeed = -self.rotspeed
        self.rect = boximages[0].get_rect().move(pos)
        self.touches = touches
        self.touching = 0
        self.dead = 0
        self.imglists = None, boximages, yboximages, rboximages

    def erase(self, background):
        r = background(self.rect)
        if self.dead:
            gfx.dirty(r)

    def draw(self, gfx):
        frame = (self.rotate/6)%15
        img = self.imglists[self.touches][frame]       
        r = gfx.surface.blit(img, self.rect)
        gfx.dirty(r)

    def tick(self, speedadjust):
        self.rotate = self.rotate + self.rotspeed

    def playercollide(self, rect):
        if self.touching:
            self.touching = self.rect.colliderect(rect)
            return 0
        elif self.rect.colliderect(rect):
            self.touches -= 1
            if self.touches:
                self.touching = 1
                snd.play('yboxhit', 1.0, self.rect.centerx)
                return 0
            snd.play('boxhit', 1.0, self.rect.centerx)
            return 1
        return 0            