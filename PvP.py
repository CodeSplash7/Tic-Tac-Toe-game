import pygame as pg
from os import path
from Settings import *
from Utilitys import *
from Sprites import *

imgDir = path.join("img")
table = Table(400,400)

PvPButtons = pg.sprite.Group() 
# Back button
backArrowIcon = path.join(imgDir, "back arrow icon.png")
backButton = Button((40, 40), (30, 10), backArrowIcon)
PvPButtons.add(backButton)
# Restart button 
restartArrowIcon = path.join(imgDir, "restart arrow icon.png")
restartButton = Button((50, 50), (35, 420), restartArrowIcon)
PvPButtons.add(restartButton)

# X/O
oIcon = path.join(imgDir, "O.png")
xIcon = path.join(imgDir, "X.png")
Ximg = pg.image.load(xIcon)
Oimg = pg.image.load(oIcon)
signs = [Ximg, Oimg]
P1sign = signs[player1SignIndex]
P2sign = signs[(player1SignIndex + 1) % len(signs)]

slotsPos = [
    (table.rect.centerx - table.rect.width //3, table.rect.centery - table.rect.height//3),
    (table.rect.centerx, table.rect.centery - table.rect.height //3),
    (table.rect.centerx + table.rect.width//3, table.rect.centery - table.rect.height//3),
    (table.rect.centerx - table.rect.width //3, table.rect.centery),
    (table.rect.centerx, table.rect.centery),
    (table.rect.centerx + table.rect.width //3, table.rect.centery),
    (table.rect.centerx - table.rect.width //3, table.rect.centery + table.rect.height//3),
    (table.rect.centerx, table.rect.centery + table.rect.height //3),
    (table.rect.centerx + table.rect.width //3, table.rect.centery + table.rect.height//3),
]
slotRects = [
    pg.Rect(table.rect.left, table.rect.top, table.cellL, table.cellL),
    pg.Rect(table.rect.left + table.cellL, table.rect.top, table.cellL, table.cellL),
    pg.Rect(table.rect.left + table.cellL*2, table.rect.top, table.cellL, table.cellL),
    pg.Rect(table.rect.left, table.rect.top + table.cellL, table.cellL, table.cellL),
    pg.Rect(table.rect.left + table.cellL, table.rect.top + table.cellL, table.cellL, table.cellL),
    pg.Rect(table.rect.left + table.cellL*2, table.rect.top + table.cellL, table.cellL, table.cellL),
    pg.Rect(table.rect.left, table.rect.top + table.cellL*2, table.cellL, table.cellL),
    pg.Rect(table.rect.left + table.cellL, table.rect.top + table.cellL*2, table.cellL, table.cellL),
    pg.Rect(table.rect.left + table.cellL*2, table.rect.top + table.cellL*2, table.cellL, table.cellL),
]
slotNames = [
    's0','s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8'
]

slots = []
for i in range(9):
    slot = Slot(slotsPos[i], slotRects[i], slotNames[i])
    slots.append(slot)

def win_screen(self, winner_name:str):
    if winner_name.lower() != "draw":
        text = "{} won".format(winner_name)
    else:
        text = winner_name
    self.inWinScreen = True
    restart_game(self)
    while self.inWinScreen:
        self.clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.inWinScreen = False
                self.playingPvP = False
                self.inMainScreen = False
            if event.type == pg.KEYDOWN:
                self.inWinScreen = False
        render_text(self, text, 70, winWidth//2, winHeight//4, "black", "white")
        render_text(self, "Press any key to restart", 40, winWidth//2, winHeight//2, "black", "white")
        pg.display.flip()
        

def get_slot(self):
    mx, my = pg.mouse.get_pos()
    for slot in slots:
        if self.clicking and (mx > slot.rect.left and mx < slot.rect.right) and (my > slot.rect.top and my < slot.rect.bottom):
            if self.P1Turn: 
                if not slot in self.slotsOcc:
                    sign = Sign(P1sign, slot.pos, (70, 70))
                    self.allSigns.add(sign)
                    self.slotsOcc.append(slot)
                    self.P1slotsOcc.append(slot.name)
                    self.P1Turn = not self.P1Turn
                    self.screenMsg = "Player 2's turn"
            else:
                if not slot in self.slotsOcc:
                    sign = Sign(P2sign, slot.pos, (70, 70))
                    self.allSigns.add(sign)
                    self.slotsOcc.append(slot)
                    self.P2slotsOcc.append(slot.name)
                    self.P1Turn = not self.P1Turn
                    self.screenMsg = "Player 1's turn"


def get_player1_slots_occupied(self):
    self.P1s = []
    P1s0 = True if ('s0' in self.P1slotsOcc) else False
    P1s1 = True if ('s1' in self.P1slotsOcc) else False
    P1s2 = True if ('s2' in self.P1slotsOcc) else False
    P1s3 = True if ('s3' in self.P1slotsOcc) else False
    P1s4 = True if ('s4' in self.P1slotsOcc) else False
    P1s5 = True if ('s5' in self.P1slotsOcc) else False
    P1s6 = True if ('s6' in self.P1slotsOcc) else False
    P1s7 = True if ('s7' in self.P1slotsOcc) else False
    P1s8 = True if ('s8' in self.P1slotsOcc) else False
    for i in slotNames:
        slot = True if (i in self.P1slotsOcc) else False
        self.P1s.append(slot)

def get_player2_slots_occupied(self):
    self.P2s = []
    P2s0 = True if ('s0' in self.P2slotsOcc) else False
    P2s1 = True if ('s1' in self.P2slotsOcc) else False
    P2s2 = True if ('s2' in self.P2slotsOcc) else False
    P2s3 = True if ('s3' in self.P2slotsOcc) else False
    P2s4 = True if ('s4' in self.P2slotsOcc) else False
    P2s5 = True if ('s5' in self.P2slotsOcc) else False
    P2s6 = True if ('s6' in self.P2slotsOcc) else False
    P2s7 = True if ('s7' in self.P2slotsOcc) else False
    P2s8 = True if ('s8' in self.P2slotsOcc) else False
    for i in slotNames:
        slot = True if (i in self.P2slotsOcc) else False
        self.P2s.append(slot)
    
def get_vertical_winner(self):
    # player 1
    if (self.P1s[0] and self.P1s[3] and self.P1s[6]):
        self.winner.lineStart = (slots[0].rect.midtop)
        self.winner.lineEnd = (slots[6].rect.midbottom)
        self.winner.name = "Player 1"
    if (self.P1s[1] and self.P1s[4] and self.P1s[7]):
        self.winner.lineStart = (slots[1].rect.midtop)
        self.winner.lineEnd = (slots[7].rect.midbottom)
        self.winner.name = "Player 1"
    if (self.P1s[2] and self.P1s[5] and self.P1s[8]):
        self.winner.lineStart = (slots[2].rect.midtop)
        self.winner.lineEnd = (slots[8].rect.midbottom)
        self.winner.name = "Player 1"
        
    # player 2
    if (self.P2s[0] and self.P2s[3] and self.P2s[6]):
        self.winner.lineStart = (slots[0].rect.midtop)
        self.winner.lineEnd = (slots[6].rect.midbottom)
        self.winner.name = "Player 2"
    if (self.P2s[1] and self.P2s[4] and self.P2s[7]):
        self.winner.lineStart = (slots[1].rect.midtop)
        self.winner.lineEnd = (slots[7].rect.midbottom)
        self.winner.name = "Player 2"
    if (self.P2s[2] and self.P2s[5] and self.P2s[8]):
        self.winner.lineStart = (slots[2].rect.midtop)
        self.winner.lineEnd = (slots[8].rect.midbottom)
        self.winner.name = "Player 2"
        
def get_orizontal_winner(self):
    # player 1
    if (self.P1s[0] and self.P1s[1] and self.P1s[2]):
        self.winner.lineStart = (slots[0].rect.midleft)
        self.winner.lineEnd = (slots[2].rect.midright)
        self.winner.name = "Player 1"
    if (self.P1s[3] and self.P1s[4] and self.P1s[5]):
        self.winner.lineStart = (slots[3].rect.midleft)
        self.winner.lineEnd = (slots[5].rect.midright)
        self.winner.name = "Player 1"
    if (self.P1s[6] and self.P1s[7] and self.P1s[8]):
        self.winner.lineStart = (slots[6].rect.midleft)
        self.winner.lineEnd = (slots[8].rect.midright)
        self.winner.name = "Player 1"
    
    # player 2
    if (self.P2s[0] and self.P2s[1] and self.P2s[2]):
        self.winner.lineStart = (slots[0].rect.midleft)
        self.winner.lineEnd = (slots[2].rect.midright)
        self.winner.name = "Player 2"
    if (self.P2s[3] and self.P2s[4] and self.P2s[5]):
        self.winner.lineStart = (slots[3].rect.midleft)
        self.winner.lineEnd = (slots[5].rect.midright)
        self.winner.name = "Player 2"
    if (self.P2s[6] and self.P2s[7] and self.P2s[8]):
        self.winner.lineStart = (slots[6].rect.midleft)
        self.winner.lineEnd = (slots[8].rect.midright)
        self.winner.name = "Player 2"
        
def get_oblic_winner(self):
    # player 1
    if (self.P1s[0] and self.P1s[4] and self.P1s[8]):
        self.winner.lineStart = (slots[0].rect.topleft)
        self.winner.lineEnd = (slots[8].rect.bottomright)
        self.winner.name = "Player 1"
    if (self.P1s[2] and self.P1s[4] and self.P1s[6]):
        self.winner.lineStart = (slots[2].rect.topright)
        self.winner.lineEnd = (slots[6].rect.bottomleft)
        self.winner.name = "Player 1"
    
    # player 2
    if (self.P2s[0] and self.P2s[4] and self.P2s[8]):
        self.winner.lineStart = (slots[0].rect.topleft)
        self.winner.lineEnd = (slots[8].rect.bottomright)
        self.winner.name = "Player 2"
    if (self.P2s[2] and self.P2s[4] and self.P2s[6]):
        self.winner.lineStart = (slots[2].rect.topright)
        self.winner.lineEnd = (slots[6].rect.bottomleft)
        self.winner.name = "Player 2"
        
def check_buttons(self):
    mx, my = pg.mouse.get_pos()
    for button in PvPButtons:
        if self.clicking:
            if mx > button.rect.left and mx < button.rect.right:
                if my > button.rect.top and my < button.rect.bottom:
                    if button.icon == backArrowIcon:
                        self.playingPvP = False
                    if button.icon == restartArrowIcon:
                        restart_game(self)

def restart_game(self):
    self.allSigns = pg.sprite.Group()
    self.screenMsg = "Player 1's turn"
    self.P1Turn = True
    self.slotsOcc = []
    self.P1slotsOcc = []
    self.P2slotsOcc = []
    self.winner = Winner((0,0), (0,0), "")
    self.clicking = False

def events(self):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            self.playingPvP = False
            self.inMainScreen = False
        if event.type == pg.MOUSEBUTTONDOWN:
            self.clicking = True
        else: self.clicking = False
        
def update(self):
    if len(self.allSigns) >= 9:
        self.winner.name = "Draw"
    self.now = pg.time.get_ticks()
    if self.now - self.whenPvPClick > 1000:
        get_slot(self)
    check_buttons(self)
    get_player1_slots_occupied(self)
    get_player2_slots_occupied(self)
    get_vertical_winner(self)
    get_orizontal_winner(self)
    get_oblic_winner(self)

def render(self):
    self.screen.fill(backgroundColor)
    self.screen.blit(table.surface, table.rect)
    PvPButtons.draw(self.screen)
    self.allSigns.draw(self.screen)
    pg.draw.line(self.screen, "Black", self.winner.lineStart, self.winner.lineEnd, 10)
    render_text(self, self.screenMsg, 40, winWidth//2, 0)
    if self.winner.name != "":
        win_screen(self, self.winner.name)
    pg.display.flip()


def playPvP(self):
    self.playingPvP = True
    restart_game(self)
    while self.playingPvP:
        self.clock.tick(FPS)
        events(self)     
        update(self)
        render(self)