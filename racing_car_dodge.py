import pygame, sys, time, random
from pygame.locals import *


class DodgeCars:
    def __init__(self,Display):
        self.Display = Display
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.black = (0, 0, 0)
        self.width = 800
        self.height = 600
        self.GOImg = pygame.image.load("images/gameover.png")
        self.Pscore = []

    def Blit_image(self,Image,x,y):
        self.Display.blit(Image,(x,y))

    def lights(self, centerx, centery, radius, color):
        pygame.draw.circle(self.Display, color,(centerx,centery),radius)


