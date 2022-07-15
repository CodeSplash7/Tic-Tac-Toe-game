import pygame as pg
from os import path
from Settings import *

class Button(pg.sprite.Sprite):
    def __init__(self, size, pos, icon):
        self.icon = icon
        super().__init__()
        self.image = pg.image.load(icon)
        self.image = pg.transform.scale(self.image, size)
        self.image.set_colorkey('white')
        self.rect = self.image.get_rect(midtop = pos)

class Sign(pg.sprite.Sprite):
    def __init__(self, sign, pos, size):
        super().__init__()
        self.image = sign
        self.image = pg.transform.scale(self.image, size)
        self.image.set_colorkey('white')
        self.rect = self.image.get_rect(center = pos)
        
class Slot():
    def __init__(self, pos, rect, name):
        self.pos = pos
        self.rect = rect
        self.name = name
    
class Table():
    def __init__(self, sizeW, sizeH):
        self.imgDir = path.join("img")
        self.icon = path.join(self.imgDir, "table.png")
        self.surface = pg.image.load(self.icon)
        self.surface = pg.transform.scale(self.surface, (sizeW, sizeH))
        self.rect = self.surface.get_rect(center = (winWidth//2, winHeight//2 + 20))
        self.cellL = self.rect.width//3
        
class Winner():
    def __init__(self, lineStart, lineEnd, winnerName):
        self.lineStart = lineStart
        self.lineEnd = lineEnd
        self.name = winnerName