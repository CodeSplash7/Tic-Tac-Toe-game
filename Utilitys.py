from turtle import back
import pygame as pg
from os import path

def render_text(self, text, size, x, y, color = "black", background_color = ""):
    font = pg.font.Font(self.fontName, size)
    surface = font.render(text, True, color, background_color if background_color != "" else None)
    rect = surface.get_rect(midtop = (x, y))
    self.screen.blit(surface, rect)
    
def load_data(self):
    imgDir = path.join("img")
    self.PvPIcon = path.join(imgDir, "Pvp icon.png")
    self.PvCIcon = path.join(imgDir, "PvC icon.png")
    
def check_buttons(self, screen = "main"):
    mx, my = pg.mouse.get_pos()
    if screen == "main":
        for button in self.mainButtons:
            if self.clicking:
                if mx > button.rect.left and mx < button.rect.right:
                    if my > button.rect.top and my < button.rect.bottom:
                        if button.icon == self.PvPIcon:
                            self.whenPvPClick = pg.time.get_ticks()
                            self.playPvP()
                            
    if screen == "PvP":
        for button in self.PvPButtons:
            if self.clicking:
                if mx > button.rect.left and mx < button.rect.right:
                    if my > button.rect.top and my < button.rect.bottom:
                        if button.icon == self.backArrowIcon:
                            self.playingPvP = False
                        if button.icon == self.restartArrowIcon:
                            self.restart_game(self)

