#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Fake Arkanoid
# Pablo Pizarro
# 2015

# Importación de librerias
import sys, os

_actualpath = str(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(_actualpath + "\\lib\\")

import pygame
from pygame.locals import *
import random
import math
from sympy.physics.units import speed

if not pygame.font: print "Error :: No se ha podido cargar la libreria de fuentes de pygame"
if not pygame.mixer: print "Error :: No se ha podido cargar la libreria de sonidos de pygame"

# CONSTANTES
LEVEL1 = [[(5, 1, 1), (5, 1, 1), (5, 1, 1), (5, 1, 1), (5, 1, 1), (5, 1, 1), (5, 1, 1), (5, 1, 1), (5, 1, 1)],
          [(5, 1, 1), (5, 1, 1), (5, 1, 1), (5, 1, 1), (5, 1, 1), (5, 1, 1), (5, 1, 1), (5, 1, 1), (5, 1, 1)],
          [(6, 1, 1), (6, 1, 1), (6, 1, 1), (6, 1, 1), (6, 1, 1), (6, 1, 1), (6, 1, 1), (6, 1, 1), (6, 1, 1)],
          [(7, 1, 1), (7, 1, 1), (7, 1, 1), (7, 1, 1), (7, 1, 1), (7, 1, 1), (7, 1, 1), (7, 1, 1), (7, 1, 1)],
          [(8, 1, 1), (8, 1, 1), (8, 1, 1), (8, 1, 1), (8, 1, 1), (8, 1, 1), (8, 1, 1), (8, 1, 1), (8, 1, 1)],
          [(9, 1, 1), (9, 1, 1), (9, 1, 1), (9, 1, 1), (9, 1, 1), (9, 1, 1), (9, 1, 1), (9, 1, 1), (9, 1, 1)],
          [(10, 1, 1), (10, 1, 1), (10, 1, 1), (10, 1, 1), (10, 1, 1), (10, 1, 1), (10, 1, 1), (10, 1, 1), (10, 1, 1)]
          ]

LEVEL2 = [[(5, 1, 1), (5, 1, 1), (5, 1, 1), (5, 1, 1), (5, 1, 1), (5, 1, 1), (5, 1, 1), (5, 1, 1), (5, 1, 1)],
          [(5, 1, 1), (5, 1, 1), (5, 1, 1), (2, 2, 3), (2, 2, 3), (2, 2, 3), (5, 1, 1), (5, 1, 1), (5, 1, 1)],
          [(6, 1, 1), (6, 1, 1), (2, 2, 3), (0, 0, 0), (0, 0, 0), (0, 0, 0), (2, 2, 3), (6, 1, 1), (6, 1, 1)],
          [(7, 1, 1), (2, 2, 3), (0, 0, 0), (0, 0, 0), (1, 2, 5), (0, 0, 0), (0, 0, 0), (2, 2, 3), (7, 1, 1)],
          [(8, 1, 1), (8, 1, 1), (2, 2, 1), (0, 0, 0), (0, 0, 0), (0, 0, 0), (2, 2, 3), (8, 1, 1), (8, 1, 1)],
          [(9, 1, 1), (9, 1, 1), (9, 1, 1), (2, 2, 3), (2, 2, 3), (2, 2, 3), (9, 1, 1), (9, 1, 1), (9, 1, 1)],
          [(10, 1, 1), (10, 1, 1), (10, 1, 1), (10, 1, 1), (10, 1, 1), (10, 1, 1), (10, 1, 1), (10, 1, 1), (10, 1, 1)]
          ]

LEVEL3 = [[(0, 0, 0), (0, 0, 0), (8, 2, 2), (8, 2, 2), (8, 2, 2), (8, 2, 2), (8, 2, 2), (0, 0, 0), (0, 0, 0)],
          [(0, 0, 0), (8, 2, 2), (8, 2, 2), (8, 2, 2), (8, 2, 2), (8, 2, 2), (8, 2, 2), (8, 2, 2), (0, 0, 0)],
          [(8, 2, 2), (8, 2, 2), (2, 2, 4), (2, 2, 4), (2, 2, 4), (2, 2, 4), (2, 2, 4), (8, 2, 2), (8, 2, 2)],
          [(8, 2, 2), (8, 2, 2), (2, 2, 4), (0, 0, 0), (0, 0, 0), (0, 0, 0), (2, 2, 4), (8, 2, 2), (8, 2, 2)],
          [(8, 2, 2), (8, 2, 2), (2, 2, 4), (0, 0, 0), (1, 2, 6), (0, 0, 0), (2, 2, 4), (8, 2, 2), (8, 2, 2)],
          [(8, 2, 2), (8, 2, 2), (2, 2, 4), (0, 0, 0), (0, 0, 0), (0, 0, 0), (2, 2, 4), (8, 2, 2), (8, 2, 2)],
          [(8, 2, 2), (8, 2, 2), (2, 2, 4), (2, 2, 4), (2, 2, 4), (2, 2, 4), (2, 2, 4), (8, 2, 2), (8, 2, 2)],
          [(0, 0, 0), (8, 2, 2), (8, 2, 2), (8, 2, 2), (8, 2, 2), (8, 2, 2), (8, 2, 2), (8, 2, 2), (0, 0, 0)],
          [(0, 0, 0), (0, 0, 0), (8, 2, 2), (8, 2, 2), (8, 2, 2), (8, 2, 2), (8, 2, 2), (0, 0, 0), (0, 0, 0)],
          ]

LEVELCAGE = [[(5, 1, 1), (5, 1, 1), (5, 1, 1), (5, 1, 1), (5, 1, 1), (5, 1, 1), (5, 1, 1), (5, 1, 1), (5, 1, 1)],
          [(6, 1, 1), (6, 1, 1), (6, 1, 1), (6, 1, 1), (6, 1, 1), (6, 1, 1), (6, 1, 1), (6, 1, 1), (6, 1, 1)],
          [(7, 1, 1), (7, 1, 1), (7, 1, 1), (7, 1, 1), (7, 1, 1), (7, 1, 1), (7, 1, 1), (7, 1, 1), (7, 1, 1)],
          [(8, 1, 1), (8, 1, 1), (8, 1, 1), (8, 1, 1), (8, 1, 1), (8, 1, 1), (8, 1, 1), (8, 1, 1), (8, 1, 1)],
          [(9, 1, 1), (9, 1, 1), (9, 1, 1), (9, 1, 1), (9, 1, 1), (9, 1, 1), (9, 1, 1), (9, 1, 1), (9, 1, 1)],
          [(10, 1, 1), (10, 1, 1), (10, 1, 1), (10, 1, 1), (10, 1, 1), (10, 1, 1), (10, 1, 1), (10, 1, 1), (10, 1, 1)],
          [(9, 1, 1), (9, 1, 1), (9, 1, 1), (9, 1, 1), (9, 1, 1), (9, 1, 1), (9, 1, 1), (9, 1, 1), (9, 1, 1)],
          [(8, 1, 1), (8, 1, 1), (8, 1, 1), (8, 1, 1), (8, 1, 1), (8, 1, 1), (8, 1, 1), (8, 1, 1), (8, 1, 1)],
          [(7, 1, 1), (7, 1, 1), (7, 1, 1), (7, 1, 1), (7, 1, 1), (7, 1, 1), (7, 1, 1), (7, 1, 1), (7, 1, 1)],
          [(6, 1, 1), (6, 1, 1), (6, 1, 1), (6, 1, 1), (6, 1, 1), (6, 1, 1), (6, 1, 1), (6, 1, 1), (6, 1, 1)],
          [(5, 1, 1), (5, 1, 1), (5, 1, 1), (5, 1, 1), (5, 1, 1), (5, 1, 1), (5, 1, 1), (5, 1, 1), (5, 1, 1)],
          ]

SW4G = 9

# Definición de funciones
def load_image(file, transparency=False, colorKey=None):
    try:
        image = pygame.image.load(file)
        image = image.convert()
        if colorKey is not None:
            if colorKey is -1:
                colorKey = image.get_at((0, 0))
            image.set_colorKey(colorKey, RLEACCEL)
        if transparency:
            image.set_alpha(127)
        return image, image.get_recl()
    except:
        print "Error :: No se ha podido cargar la imagen"

def load_sound(file):
    class Nonesound:
        def play(self): pass
    if not pygame.mixer: return Nonesound
    else:
        return pygame.mixer.Sound(file)

def sgn(x):
    if x == 0:
        return 0
    else:
        return abs(x) / x

def loadlevel(bricks, level):
    for i in range(len(level)):
        for j in range(len(level[0])):
            if level[i][j] != (0, 0, 0):
                brick = Brick("images/brick" + str(level[i][j][0]) + ".gif", level[i][j][1], level[i][j][2])
                brick.place(64 * j + 30, 32 * i + 40)
                bricks.append(brick)

def quit():
    os.system("taskkill /PID " + str(os.getpid()) + " /F")
    exit()

class Bar:
    def __init__(self, texture):
        self.pos = int((640 - 176) / 2) + 5
        self.defaultspeed = 3
        self.direction = 1
        self.speed = self.defaultspeed
        self.image = pygame.image.load(texture).convert()
        self.image = pygame.transform.scale2x(self.image)
        self.image = self.image.convert()
        self.rectl = self.image.get_rect()
        self.rectl.x = self.pos
        self.rectl.y = 440
        self.ball = None

    def move(self, i):
        if self.speed == 0:
            self.speed = self.defaultspeed
        if i > 0 and self.direction < 0:
            self.resetspeed()
            self.direction = 1
        elif i < 0 and self.direction > 0:
            self.resetspeed()
            self.direction = -1
        self.pos += i
        self.pos = min(self.pos, 460)
        self.pos = max(self.pos, 0)
        self.rectl.x = self.pos
        self.speed += 0.5
        if not self.ball.launched:
            self.ball.x = self.pos + 76
            self.ball.rectl.x = self.pos + 76

    def resetspeed(self):
        self.speed = 0

    def addball(self, ball):
        self.ball = ball

    def resetpad(self):
        self.pos = int((640 - 176) / 2) + 5
        self.defaultspeed = 3
        self.direction = 1
        self.rectl.x = self.pos
        self.rectl.y = 440

class Ball(pygame.sprite.Sprite):
    def __init__(self, texture, pad):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(texture).convert()
        self.image = pygame.transform.scale2x(self.image)
        self.rectl = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.launched = False
        self.speedy = -3
        self.speedx = 0
        self.pad = pad
        self.maxspeedx = 6
        self.maxspeedy = 6
        self.padgolpe = pygame.mixer.Sound("sounds/blip1.wav")
        self.wallgolpe = pygame.mixer.Sound("sounds/wall.wav")
        self.soundperder = pygame.mixer.Sound("sounds/gameover.wav")
        self.soundlevelup = pygame.mixer.Sound("sounds/levelup.wav")
        self.soundlevel1 = pygame.mixer.Sound("sounds/level1.wav")
        self.soundlevel2 = pygame.mixer.Sound("sounds/level2.wav")
        self.soundlevel3 = pygame.mixer.Sound("sounds/level3.wav")
        self.soundcage = pygame.mixer.Sound("sounds/cage.wav")
        self.brickgolpe = pygame.mixer.Sound("sounds/brickpunch.wav")
        self.screen = None
        self.perdio = False
        self.bricks = []
        self.bricksound = None
        self.vidas = 3
        self.score = 0
        self.level = 1
        self.lasthit = 0
        self.background = None

    def initializeball(self):
        self.x = int((640 - 40) / 2) + 13
        self.y = 416  # min y
        self.rectl.x = self.x
        self.rectl.y = self.y
        self.speedy = -3
        self.speedx = 0
        self.launched = False
        self.perdio = False

    def update(self, *args):
        if self.launched and not self.perdio:
            self.y += self.speedy
            self.y = max (self.y, 0)
            self.x += self.speedx

            self.rectl.y = self.y
            self.rectl.x = self.x

            if self.x >= 600 or self.x <= 15:
                self.speedx = -self.speedx
                self.wallgolpe.play()
                self.lasthit = -1

            if self.y == 0:
                self.speedy = -self.speedy
                self.wallgolpe.play()
                self.lasthit = -1

            if self.y >= 480:
                self.perdio = True
                self.soundperder.play()
                self.vidas -= 1
                self.lasthit = -1
                return

            if self.rectl.colliderect(self.pad.rectl) and self.speedy > 0:
                self.padgolpe.play()
                if self.speedy <= self.maxspeedy:
                    self.speedy = -(abs(self.speedy) + 0.3 * self.level)
                else:
                    self.speedy = -(self.speedy)
                dx = ((self.x - self.pad.pos) - 76 + random.randint(-10, 10)) * 0.005 * math.pi
                coef = math.sin(abs(dx))
                dir = -sgn(dx)
                if self.pad.direction > 0:
                    self.speedx += (self.pad.speed / 10.0) * self.level
                else:
                    self.speedx += -(self.pad.speed / 10.0) * self.level
                self.speedx = dir * (coef * self.speedy + self.speedx)
                self.rectl.inflate(5, 5)
                if abs(self.speedx) > self.maxspeedx:
                    self.speedx = sgn(self.speedx) * self.maxspeedx
                self.lasthit = -1

            for i, brick in enumerate(self.bricks):
                if self.rectl.colliderect(brick.rect) and self.lasthit != i:
                    brick.vidas -= 1
                    self.lasthit = i
                    self.speedx += 0.0025
                    self.speedy += 0.0025
                    if brick.vidas == 0:
                        if brick.getType() == 1: self.score += 10 * self.level
                        elif brick.getType() == 2: self.score += 30 * self.level
                        self.bricks.pop(i)
                        self.speedy = -self.speedy
                        self.bricksound.play()

                        if len(self.bricks) == 0:
                            self.score += 500 * self.level
                            self.level += 1
                            self.soundlevelup.play()
                            self.vidas += 1
                            self.maxspeedx += 0.7
                            self.maxspeedy += 0.7
                            self.loadlevel()
                    else:
                        self.brickgolpe.play()
                        self.speedy = -self.speedy
                    return

    def launch(self):
        self.launched = True
        self.speedx = 3 * random.randint(-1, 1) * random.random()

    def addscreen(self, screen):
        self.screen = screen

    def addbricksound(self, sound):
        self.bricksound = sound

    def loadlevel(self):
        self.initializeball()
        if self.level == 1:
            loadlevel(self.bricks, LEVEL1)
            self.soundlevel1.play(-1)
            self.background = pygame.image.load("images/background.png")
            self.background = pygame.transform.scale(self.background, (640, 480))
        elif self.level == 2:
            self.background = pygame.image.load("images/background2.png")
            self.background = pygame.transform.scale(self.background, (640, 480))
            self.soundlevel1.stop()
            loadlevel(self.bricks, LEVEL2)
            self.soundlevel2.play(-1)
        elif self.level == 3:
            self.background = pygame.image.load("images/background3.png")
            self.background = pygame.transform.scale(self.background, (640, 480))
            self.soundlevel2.stop()
            loadlevel(self.bricks, LEVEL3)
            self.soundlevel3.play(-1)
        elif self.level == SW4G:
            self.bricks = []
            self.soundlevel1.stop()
            self.soundlevel2.stop()
            self.soundlevel3.stop()
            self.background = pygame.image.load("images/wallpapercage.png")
            self.background = pygame.transform.scale(self.background, (640, 480))
            self.soundcage.play(-1)
            loadlevel(self.bricks, LEVELCAGE)
            pygame.display.set_caption("$W€G")
            self.vidas = 9999

class Brick:

    def __init__(self, texture, type, vidas):

        self.image = pygame.image.load(texture).convert()
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect()
        self.posx = 0
        self.posy = 0
        self.type = type
        self.vidas = vidas

    def place(self, x, y):
        self.posx = x
        self.posy = y
        self.rect.x = x
        self.rect.y = y

    def getType(self):
        return self.type

def main():

    # Inicializamos
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Fake Arkanoid")
    pygame.mouse.set_visible(True)
    icon = pygame.image.load("images/icon.png").convert_alpha()
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()

    bar = Bar("images/pad.gif")
    ball = Ball("images/ball.png", bar)
    ball.initializeball()
    bar.addball(ball)
    ball.addscreen(screen)

    bricks = []
    bricksound = pygame.mixer.Sound("sounds/brick.wav")
    ball.addbricksound(bricksound)

    scorefont = pygame.font.Font("fonts/font2.ttf", 15)

    ball.loadlevel()

    while True:
        screen.blit(ball.background, (0, 0))
        clock.tick(60)

        # Recupero los eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
                elif event.key == K_SPACE:
                    if not ball.launched:
                        ball.launch()
                        ball.padgolpe.play()
                elif event.key == K_F12:
                    ball.level = SW4G
                    ball.loadlevel()

        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            bar.move(-bar.speed)
        elif keys[K_RIGHT]:
            bar.move(bar.speed)
        else:
            bar.resetspeed()

        screen.blit(bar.image, (bar.pos, 440))
        screen.blit(ball.image, (ball.x, ball.y))

        for brick in ball.bricks:
            screen.blit(brick.image, (brick.posx, brick.posy))

        if ball.perdio:
            if ball.vidas == 0:
                text = pygame.font.Font("fonts/font2.ttf", 50)
                f1 = text.render("HAS PERDIDO", 1, (255, 255, 255))
                screen.blit(f1, (80, 210))
                bar.speed = 0
                bar.defaultspeed = 0
            else:
                ball.initializeball()
                bar.resetpad()

        if ball.level != SW4G:
            scoretext = scorefont.render("SCORE " + str(ball.score), 1, (255, 255, 255))
            screen.blit(scoretext, (10, 5))
            vidatext = scorefont.render("VIDAS " + str(ball.vidas), 1, (255, 255, 255))
            screen.blit(vidatext, (534, 5))
            leveltext = scorefont.render("NIVEL " + str(ball.level), 1, (255, 255, 255))
            screen.blit(leveltext, (400, 5))
        else:
            scoretext = scorefont.render("SCORE BILL GATES", 1, (255, 255, 255))
            screen.blit(scoretext, (10, 5))
            vidatext = scorefont.render("VIDAS YOLO", 1, (255, 255, 255))
            screen.blit(vidatext, (487, 5))
            leveltext = scorefont.render("NIVEL SWEG", 1, (255, 255, 255))
            screen.blit(leveltext, (320, 5))

        pygame.display.flip()
        ball.update()

if __name__ == "__main__":
    main()
