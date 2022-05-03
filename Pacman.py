#!/usr/bin/env python3
import init as init
import Game as ga
import pygame
import math
from random import randrange
import random
import copy
import os

def displayLaunchscreen():
    # Draw Pacman Title
    pacmanTitle = ["tile016.png", "tile000.png", "tile448.png", "tile012.png", "tile000.png", "tile013.png"]
    for i in range(len(pacmanTitle)):
        letter = pygame.image.load(init.TextPath + pacmanTitle[i])
        letter = pygame.transform.scale(letter, (int(init.square * 4), int(init.square * 4)))
        init.screen.blit(letter, ((2 + 4 * i) * init.square, 2 * init.square, init.square, init.square))

    # Draw Character / Nickname
    characterTitle = [
        #Character
        "tile002.png", "tile007.png", "tile000.png", "tile018.png", "tile000.png", "tile002.png", "tile020.png", "tile004.png", "tile018.png",
        # /
        "tile015.png", "tile042.png", "tile015.png",
        # Nickname
        "tile013.png", "tile008.png", "tile002.png", "tile010.png", "tile013.png", "tile000.png", "tile012.png", "tile004.png"
    ]
    for i in range(len(characterTitle)):
        letter = pygame.image.load(init.TextPath + characterTitle[i])
        letter = pygame.transform.scale(letter, (int(init.square), int(init.square)))
        init.screen.blit(letter, ((4 + i) * init.square, 10 * init.square, init.square, init.square))

    #Draw Characters and their Nickname
    characters = [
        # Red Ghost
        [
            "tile449.png", "tile015.png", "tile107.png", "tile015.png", "tile083.png", "tile071.png", "tile064.png", "tile067.png", "tile078.png", "tile087.png",
            "tile015.png", "tile015.png", "tile015.png", "tile015.png",
            "tile108.png", "tile065.png", "tile075.png", "tile072.png", "tile077.png", "tile074.png", "tile089.png", "tile108.png"
        ],
        # Pink Ghost
        [
            "tile450.png", "tile015.png", "tile363.png", "tile015.png", "tile339.png", "tile336.png", "tile324.png", "tile324.png", "tile323.png", "tile345.png",
            "tile015.png", "tile015.png", "tile015.png", "tile015.png",
            "tile364.png", "tile336.png", "tile328.png", "tile333.png", "tile330.png", "tile345.png", "tile364.png"
        ],
        # Blue Ghost
        [
            "tile452.png", "tile015.png", "tile363.png", "tile015.png", "tile193.png", "tile192.png", "tile211.png", "tile199.png", "tile197.png", "tile213.png", "tile203.png",
            "tile015.png", "tile015.png", "tile015.png",
            "tile236.png", "tile200.png", "tile205.png", "tile202.png", "tile217.png", "tile236.png"
        ],
        # Orange Ghost
        [
            "tile451.png", "tile015.png", "tile363.png", "tile015.png", "tile272.png", "tile270.png", "tile266.png", "tile260.png", "tile281.png",
            "tile015.png", "tile015.png", "tile015.png", "tile015.png", "tile015.png",
            "tile300.png", "tile258.png", "tile267.png", "tile281.png", "tile259.png", "tile260.png", "tile300.png"
        ]
    ]
    for i in range(len(characters)):
        for j in range(len(characters[i])):
            if j == 0:
                    letter = pygame.image.load(init.TextPath + characters[i][j])
                    letter = pygame.transform.scale(letter, (int(init.square * init.spriteRatio), int(init.square * init.spriteRatio)))
                    init.screen.blit(letter, ((2 + j) * init.square - init.square//2, (12 + 2 * i) * init.square - init.square//3, init.square, init.square))
            else:
                letter = pygame.image.load(init.TextPath + characters[i][j])
                letter = pygame.transform.scale(letter, (int(init.square), int(init.square)))
                init.screen.blit(letter, ((2 + j) * init.square, (12 + 2 * i) * init.square, init.square, init.square))
    # Draw Pacman and Ghosts
    event = ["tile449.png", "tile015.png", "tile452.png", "tile015.png",  "tile015.png", "tile448.png", "tile453.png", "tile015.png", "tile015.png", "tile015.png",  "tile453.png"]
    for i in range(len(event)):
        character = pygame.image.load(init.TextPath + event[i])
        character = pygame.transform.scale(character, (int(init.square * 2), int(init.square * 2)))
        init.screen.blit(character, ((4 + i * 2) * init.square, 24 * init.square, init.square, init.square))
    # Draw PlatForm from Pacman and Ghosts
    wall = ["tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png", "tile454.png"]
    for i in range(len(wall)):
        platform = pygame.image.load(init.TextPath + wall[i])
        platform = pygame.transform.scale(platform, (int(init.square * 2), int(init.square * 2)))
        init.screen.blit(platform, ((i * 2) * init.square, 26 * init.square, init.square, init.square))
    # Credit myself
    credit = ["tile020.png", "tile000.png", "tile025.png", "tile014.png", "tile015.png", "tile000.png", "tile018.png", "tile008.png", "tile010.png", "tile004.png", "tile013.png", "tile001.png", "tile008.png", "tile015.png", "tile418.png", "tile416.png", "tile418.png", "tile418.png"]
    for i in range(len(credit)):
        letter = pygame.image.load(init.TextPath + credit[i])
        letter = pygame.transform.scale(letter, (int(init.square), int(init.square)))
        init.screen.blit(letter, ((6 + i) * init.square, 30 * init.square, init.square, init.square))
    # Press Space to Play
    instructions = ["tile016.png", "tile018.png", "tile004.png", "tile019.png", "tile019.png", "tile015.png", "tile019.png", "tile016.png", "tile000.png", "tile002.png", "tile004.png", "tile015.png", "tile020.png", "tile014.png", "tile015.png", "tile016.png", "tile011.png", "tile000.png", "tile025.png"]
    for i in range(len(instructions)):
        letter = pygame.image.load(init.TextPath + instructions[i])
        letter = pygame.transform.scale(letter, (int(init.square), int(init.square)))
        init.screen.blit(letter, ((4.5 + i) * init.square, 35 * init.square - 10, init.square, init.square))

    pygame.display.update()

running = True
onLaunchscreen = True
displayLaunchscreen()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            ga.game.recordHighScore()
        elif event.type == pygame.KEYDOWN:
            ga.game.paused = False
            ga.game.started = True
            if event.key == pygame.K_z:
                if not onLaunchscreen:
                    ga.game.pacman.newDir = 0
            elif event.key == pygame.K_d:
                if not onLaunchscreen:
                    ga.game.pacman.newDir = 1
            elif event.key == pygame.K_s:
                if not onLaunchscreen:
                    ga.game.pacman.newDir = 2
            elif event.key == pygame.K_q:
                if not onLaunchscreen:
                    ga.game.pacman.newDir = 3
            elif event.key == pygame.K_SPACE:
                if onLaunchscreen:
                    onLaunchscreen = False
                    ga.game.paused = True
                    ga.game.started = False
                    ga.game.render()
                    pygame.mixer.music.load(init.MusicPath + "pacman_beginning.wav")
                    pygame.mixer.music.play()
                    musicPlaying = 1
            elif event.key == pygame.K_ESCAPE:
                running = False
                ga.game.recordHighScore()

    if not onLaunchscreen:
        ga.game.update()
