import pygame as pg
from Settings import *
from Utilitys import *
from Sprites import *

def mainMenu(self):
        self.inMainScreen = True
        self.mainButtons = pg.sprite.Group()
        # PvP button
        self.pvpButton = Button((140, 100), (winWidth//2, 300), self.PvPIcon)
        self.mainButtons.add(self.pvpButton)
        
        while self.inMainScreen:
            self.clock.tick(FPS)
            for event in pg.event.get():
                #events
                if event.type == pg.QUIT:
                    self.inMainScreen = False
                    self.playing = False
                    self.running = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.clicking = True
                else:
                    self.clicking = False
                    
                # Update
                check_buttons(self)
                if not self.inMainScreen:
                    break
                
                # render
                self.screen.fill(backgroundColor)
                render_text(self, "Tic-Tac-Toe", 100, winWidth //2, 50)
                self.mainButtons.draw(self.screen)
                pg.display.flip()