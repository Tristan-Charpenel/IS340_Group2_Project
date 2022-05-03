import init as init
import Game as ga
import pygame
import math
from random import randrange
import random
import copy
import os

def canMove(row, col):
    if col == -1 or col == len(init.gameBoard[0]):
        return True
    if init.gameBoard[int(row)][int(col)] != 3:
        return True
    return False


class Pacman:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.mouthOpen = False
        self.pacSpeed = 1/4
        self.mouthChangeDelay = 5
        self.mouthChangeCount = 0
        self.dir = 0 # 0: North, 1: East, 2: South, 3: West
        self.newDir = 0

    def update(self):
        if self.newDir == 0:
            if canMove(math.floor(self.row - self.pacSpeed), self.col) and self.col % 1.0 == 0:
                self.row -= self.pacSpeed
                self.dir = self.newDir
                return
        elif self.newDir == 1:
            if canMove(self.row, math.ceil(self.col + self.pacSpeed)) and self.row % 1.0 == 0:
                self.col += self.pacSpeed
                self.dir = self.newDir
                return
        elif self.newDir == 2:
            if canMove(math.ceil(self.row + self.pacSpeed), self.col) and self.col % 1.0 == 0:
                self.row += self.pacSpeed
                self.dir = self.newDir
                return
        elif self.newDir == 3:
            if canMove(self.row, math.floor(self.col - self.pacSpeed)) and self.row % 1.0 == 0:
                self.col -= self.pacSpeed
                self.dir = self.newDir
                return

        if self.dir == 0:
            if canMove(math.floor(self.row - self.pacSpeed), self.col) and self.col % 1.0 == 0:
                self.row -= self.pacSpeed
        elif self.dir == 1:
            if canMove(self.row, math.ceil(self.col + self.pacSpeed)) and self.row % 1.0 == 0:
                self.col += self.pacSpeed
        elif self.dir == 2:
            if canMove(math.ceil(self.row + self.pacSpeed), self.col) and self.col % 1.0 == 0:
                self.row += self.pacSpeed
        elif self.dir == 3:
            if canMove(self.row, math.floor(self.col - self.pacSpeed)) and self.row % 1.0 == 0:
                self.col -= self.pacSpeed

    # Draws pacman based on his current state
    def draw(self):
        # if not ga.game.started:
        #     pacmanImage = pygame.image.load(init.ElementPath + "tile112.png")
        #     pacmanImage = pygame.transform.scale(pacmanImage, (int(init.square * init.spriteRatio), int(init.square * init.spriteRatio)))
        #     init.screen.blit(pacmanImage, (self.col * init.square + init.spriteOffset, self.row * init.square + init.spriteOffset, init.square, init.square))
        #     return

        if self.mouthChangeCount == self.mouthChangeDelay:
            self.mouthChangeCount = 0
            self.mouthOpen = not self.mouthOpen
        self.mouthChangeCount += 1
        # pacmanImage = pygame.image.load("Sprites/tile049.png")
        if self.dir == 0:
            if self.mouthOpen:
                pacmanImage = pygame.image.load(init.ElementPath + "tile049.png")
            else:
                pacmanImage = pygame.image.load(init.ElementPath + "tile051.png")
        elif self.dir == 1:
            if self.mouthOpen:
                pacmanImage = pygame.image.load(init.ElementPath + "tile052.png")
            else:
                pacmanImage = pygame.image.load(init.ElementPath + "tile054.png")
        elif self.dir == 2:
            if self.mouthOpen:
                pacmanImage = pygame.image.load(init.ElementPath + "tile053.png")
            else:
                pacmanImage = pygame.image.load(init.ElementPath + "tile055.png")
        elif self.dir == 3:
            if self.mouthOpen:
                pacmanImage = pygame.image.load(init.ElementPath + "tile048.png")
            else:
                pacmanImage = pygame.image.load(init.ElementPath + "tile050.png")

        pacmanImage = pygame.transform.scale(pacmanImage, (int(init.square * init.spriteRatio), int(init.square * init.spriteRatio)))
        init.screen.blit(pacmanImage, (self.col * init.square + init.spriteOffset, self.row * init.square + init.spriteOffset, init.square, init.square))
