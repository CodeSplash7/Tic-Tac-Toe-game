import pygame as pg
from os import path
from Settings import *
from Utilitys import *
from Sprites import *
import MainMenuScreen as mm
import PvP as pvp

class Game():
    def __init__(self):
        pg.init()
        pg.mixer.init()
        pg.display.set_caption(winTitle)
        pg.display.set_icon(pg.image.load(path.join("img", "game icon.png")))
        self.running = True
        self.screen = pg.display.set_mode(winSize)
        self.clock = pg.time.Clock()
        self.fontName = pg.font.match_font(fontName)
        load_data(self)
        
    def mainMenu(self):
        mm.mainMenu(self)

    def playPvP(self):
        pvp.playPvP(self)

ttt = Game()
ttt.mainMenu()

pg.quit()