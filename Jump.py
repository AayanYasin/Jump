import os
import pygame as pg
from pygame.constants import *
import random as rd
import sys
from tkinter import *
from tkinter import messagebox, filedialog
import shutil
import time as t
import webbrowser as wb
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from pymongo import MongoClient, DESCENDING
from bson.objectid import ObjectId
from datetime import date, datetime
from numerize import numerize
import pyperclip
import pickle
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

pg.init()
root = Tk()
root.wm_withdraw()

musicFile = "assets\\background.mp3"
UserNameSavedFile = "assets\\UserCreds.dat"
IconFile = "assets\JUMP-ICON.png"
# ProfileImageFile = "assets\PROFILE-IMAGE.png"

screen_w = 700
screen_h = 400

window = pg.display.set_mode((screen_w, screen_h))
pg.display.set_caption("J.U.M.P")

try:
    pg.display.set_icon(pg.image.load(IconFile))
    IconFile_AvailableORnot = True
except Exception:
    IconFile_AvailableORnot = False

Play_Again = None
Current_Level = None

try:
    pg.mixer.music.load(musicFile)
    pg.mixer.music.play(-1)
    MusicFile_AvailableORnot = True
    pg.mixer.music.set_volume(0.2)
except Exception:
    MusicFile_AvailableORnot = False


if not os.path.isfile(UserNameSavedFile):
    pickle.dump("none", open(UserNameSavedFile, "wb"))

# defining this to get currently selected player
selected1, selected2, selected3, selected4, selected5, selected6 = (
    107, 87), (303, 87), (499, 87), (107, 245), (303, 245), (499, 245)
selected = selected1

# Colors/Skins
selected1_Color = (0, 0, 0)
selected2_Color = (0, 130, 0)
selected3_Color = (227, 0, 193)
selected5_Color = rd.choice(
    ((57, 217, 218), (57, 217, 103), (211, 135, 249), (96, 59, 44)))
selected6_Color = rd.choice(((255, 0, 0), (0, 255, 0), (0, 0, 255)))

# initializing Colors as global
player_skin = {selected1: selected1_Color,
               selected2: selected2_Color, selected3: selected3_Color}

version = "2.0.1.1"


def quit_game():
    global idusr
    global collection
    askexit = messagebox.askyesno(
        "Jump - exit", "Do you really want to exit the game ?")
    if askexit:
        names = collection.find({"_id": ObjectId(idusr)})
        for namess in names:
            status = namess["online"]
        collection.find_one_and_update(
            {"_id": ObjectId(idusr)}, {"$set": {"online": False}})
        sys.exit()


show_filemissing_error = 0
show_leaderBoard_winner = 0


def files_available_not():
    musicf = ""
    iconf = ""
    no_of_files = 0
    coma = ""
    s = ""
    if not MusicFile_AvailableORnot:
        musicf = "background.mp3"
        no_of_files += 1
    if not IconFile_AvailableORnot:
        iconf = "JUMP-ICON.png"
        no_of_files += 1
    if no_of_files == 2:
        coma = ", "
        s = "s"
    messagebox.showwarning(
        "Jump - Files missing", f"{no_of_files} file{s} missing ( {musicf}{coma}{iconf} )")


def text(text, color, x, y, family, size):
    font = pg.font.SysFont(family, size)
    rndFONT = font.render(text, True, color)
    window.blit(rndFONT, (x, y))


def add_image(url, x, y, width, height):
    image = pg.image.load(url)
    image = pg.transform.scale(image, (width, height))
    window.blit(image, (x, y))


def Game_over():
    go = True
    NorF_x = 383
    NorF = None

    SCORE = ((coinCollected+time)//2)
    idusr = pickle.load(open(UserNameSavedFile, "rb"))
    data_of_user = collection.find({"_id": ObjectId(idusr)})
    for data in data_of_user:
        currentC = data["coins"]
        Level1 = data["level1"].split()
        Level2 = data["level2"].split()
        Level3 = data["level3"].split()
        Level4 = data["level4"].split()
        Level5 = data["level5"].split()
        Level6 = data["level6"].split()

    def text_screen_Go(text, color, x, y, family, size):
        font2 = pg.font.SysFont(family, size)
        set_text2 = font2.render(text, True, color)
        window.blit(set_text2, (x, y))

    def level_unlock_gameover(Current_Levelw):
        pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_WAIT))
        match Current_Levelw:
            case 1:
                current_l = "level1"
            case 2:
                current_l = "level2"
            case 3:
                current_l = "level3"
            case 4:
                current_l = "level4"
            case 5:
                current_l = "level5"
            case 6:
                current_l = "level6"

        if Current_Level == 1:
            if int(Level1[1]) < int(SCORE):
                new_score_week = SCORE
            else:
                new_score_week = Level1[1]
            if int(Level1[2]) < int(SCORE):
                new_score_alltimes = SCORE
            else:
                new_score_alltimes = Level1[2]
        if Current_Level == 2:
            if int(Level2[1]) < int(SCORE):
                new_score_week = SCORE
            else:
                new_score_week = Level2[1]
            if int(Level2[2]) < int(SCORE):
                new_score_alltimes = SCORE
            else:
                new_score_alltimes = Level2[2]
        if Current_Level == 3:
            if int(Level3[1]) < int(SCORE):
                new_score_week = SCORE
            else:
                new_score_week = Level3[1]
            if int(Level3[2]) < int(SCORE):
                new_score_alltimes = SCORE
            else:
                new_score_alltimes = Level3[2]
        if Current_Level == 4:
            if int(Level4[1]) < int(SCORE):
                new_score_week = SCORE
            else:
                new_score_week = Level4[1]
            if int(Level4[2]) < int(SCORE):
                new_score_alltimes = SCORE
            else:
                new_score_alltimes = Level4[2]
        if Current_Level == 5:
            if int(Level5[1]) < int(SCORE):
                new_score_week = SCORE
            else:
                new_score_week = Level5[1]
            if int(Level5[2]) < int(SCORE):
                new_score_alltimes = SCORE
            else:
                new_score_alltimes = Level5[2]
        if Current_Level == 6:
            if int(Level6[1]) < int(SCORE):
                new_score_week = SCORE
            else:
                new_score_week = Level6[1]
            if int(Level6[2]) < int(SCORE):
                new_score_alltimes = SCORE
            else:
                new_score_alltimes = Level6[2]

        collection.find_one_and_update({"_id": ObjectId(idusr)}, {
                                       "$set": {current_l: f"True {new_score_week} {new_score_alltimes}"}})
        collection.find_one_and_update({"_id": ObjectId(idusr)}, {
                                       "$set": {"coins": str(int(currentC)+int(coinCollected))}})

    while go:
        for eventsGO in pg.event.get():
            pos = pg.mouse.get_pos()
            if eventsGO.type == pg.QUIT:
                quit_game()
            if pos[0] < 23 and pos[1] < 23 or pos[0] > 250 and pos[0] < 360 and pos[1] > 295 and pos[1] < 345 or pos[0] > 312 and pos[0] < 452 and pos[1] > 295 and pos[1] < 345:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))
            else:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_ARROW))
            if eventsGO.type == pg.MOUSEBUTTONUP:
                if pos[0] > 250 and pos[0] < 360 and pos[1] > 295 and pos[1] < 345:
                    pg.mouse.set_cursor(
                        pg.cursors.Cursor(pg.SYSTEM_CURSOR_WAIT))
                    collection.find_one_and_update({"_id": ObjectId(idusr)}, {
                                                   "$set": {"coins": str(int(currentC)+int(coinCollected))}})
                    Play_Again()
                if pos[0] < 23 and pos[1] < 23:
                    menu()
                if pos[0] > 312 and pos[0] < 452 and pos[1] > 295 and pos[1] < 345:
                    if Current_Level == 1:
                        level_unlock_gameover(2)
                        Level_2()
                    elif Current_Level == 2:
                        level_unlock_gameover(3)
                        Level_3()
                    elif Current_Level == 3:
                        level_unlock_gameover(4)
                        Level_4()
                    elif Current_Level == 4:
                        level_unlock_gameover(5)
                        Level_5()
                    elif Current_Level == 5:
                        level_unlock_gameover(6)
                        Level_6()
                    elif Current_Level == 6:
                        menu()

        if Current_Level != 6:
            NorF = "NEXT"
            NorF_x = 383
        else:
            NorF = "FINISH"
            NorF_x = 377

        black = (0, 0, 0)
        white = (255, 255, 255)
        window.fill((224, 224, 224))
        pg.draw.rect(window, black, (251, 105, 200, 50))
        pg.draw.rect(window, black, (251, 166, 200, 50))
        pg.draw.rect(window, black, (251, 226, 200, 50))
        pg.draw.rect(window, black, (251, 295, 109, 50))
        pg.draw.rect(window, black, (370, 295, 82, 50))
        pg.draw.rect(window, (172, 172, 172), (0, 0, 23, 23))

        text_screen_Go(u"\u2302", black, 5, 0, "segoeuisymbol", 15)
        text_screen_Go("Game Over", black, 240, 40, "areal", 57)
        text_screen_Go(f"Score : {SCORE}", white, 282, 112, "serif", 32)
        text_screen_Go(f"Time : {time}", white, 287, 173, "serif", 32)
        text_screen_Go(f"Coins : {coinCollected}",
                       white, 288, 233, "serif", 32)
        text_screen_Go("RESTART", white, 256, 307, "helvetica", 25)
        text_screen_Go(NorF, white, NorF_x, 307, "helvetica", 25)
        pg.display.flip()


def pause(crnt_lvl):
    while True:
        window.fill((224, 224, 224))
        for events in pg.event.get():
            pos = pg.mouse.get_pos()
            if events.type == pg.QUIT:
                quit_game()
            if events.type == pg.MOUSEBUTTONDOWN:
                if pos[0] > 266 and pos[1] > 145 and pos[0] < 422 and pos[1] < 180:
                    return
                if pos[0] > 267 and pos[1] > 236 and pos[0] < 422 and pos[1] < 270:
                    restart(crnt_lvl)
                if pos[0] > 267 and pos[1] > 330 and pos[0] < 422 and pos[1] < 363:
                    confirm_restart1 = messagebox.askokcancel(
                        "Jump - Back to menu", "Are you sure you want to quit ?\nYou will loose all your progress.")
                    if confirm_restart1:
                        menu()
                if pos[0] < 23 and pos[1] < 23:
                    return

        text("Paused", "black", (screen_w/2.5), 40, "comicsansms", 40)
        pg.draw.rect(window, (0, 0, 0), (screen_w/2.62, 145, 155, 35))
        text("Continue", (255, 255, 255), screen_w/2.44+5, 149, "corbel", 30)
        pg.draw.rect(window, (0, 0, 0), (screen_w/2.6, 236, 155, 35))
        text("Restart", (255, 255, 255), screen_w/2.34+3, 240, "corbel", 30)
        pg.draw.rect(window, (0, 0, 0), (screen_w/2.6, 329, 155, 35))
        text("M e n u", (255, 255, 255), screen_w/2.32, 333, "corbel", 30)
        pg.draw.rect(window, (172, 172, 172), (0, 0, 23, 23))
        text("<", (0, 0, 0), 5, -1, "helvetica", 20)
        pg.display.update()


def restart(crnt_level):
    confirm_restart = messagebox.askokcancel(
        "Jump - Restart Level", "Are you sure you want to restart level ?\nYou will loose all your progress.")
    if confirm_restart:
        if crnt_level == 1:
            Level_1()
        if crnt_level == 2:
            Level_2()
        if crnt_level == 3:
            Level_3()
        if crnt_level == 4:
            Level_4()
        if crnt_level == 5:
            Level_5()
        if crnt_level == 6:
            Level_6()
    else:
        return


def Level_1():
    global time
    global coinCollected
    global Play_Again
    global Current_Level
    selected4_Color = rd.choice(((254, 234, 0), (159, 32, 164),
                                 (57, 121, 42), (96, 59, 44)))
    selected5_Color = rd.choice(
        ((57, 217, 218), (57, 217, 103), (211, 135, 249), (96, 59, 44)))
    run = True
    gameover = False
    black = (0, 0, 0)
    grey = (166, 166, 166)
    greySky = (224, 224, 224)
    red = (255, 0, 0)
    golden = (253, 181, 2)
    coinCollected = 0
    coin_X = 710
    Move_coin_X = 0
    keypressed = False
    G_1 = 100
    G_2 = 200
    G_3 = 300
    G_4 = 400
    G_5 = 500
    G_6 = 600
    G_7 = 700
    G_MOVE = 0
    P_X = 380
    P_Y = 270
    P_height = 30
    O_X = 240
    O_Y = 280
    O_Xa = 710
    O_Xb = 710
    O_XaV = 0
    O_XbV = 0
    O_Ya = 271
    O_Yb = 285
    V_Y = 0
    VO_X = 0
    V_X = 0
    jump = -15
    time = 0
    sec_1 = 0
    fps = 30

    clock = pg.time.Clock()

    font1 = pg.font.SysFont("times", 25)
    font1_coins = pg.font.SysFont("times", 25)

    def text_screen(text, color, x, y):
        set_text = font1.render(text, True, color)
        window.blit(set_text, (x, y))

    def text_screen_coins(text, color, x, y):
        set_text_coin = font1_coins.render(text, True, color)
        window.blit(set_text_coin, (x, y))

    while run:
        PlayerM = pg.Rect(P_X, P_Y, 15, P_height)
        ObsticleM = pg.Rect(O_X, O_Y, 15, 20)
        ObsticleA = pg.Rect(O_Xa, O_Ya, 25, 10)
        ObsticleB = pg.Rect(O_Xb, O_Yb, 25, 10)
        GroundM = pg.Rect(0, 300, 700, 100)
        for events in pg.event.get():
            if events.type == pg.QUIT:
                quit_game()
                # For Computer -- Keyboard Arrow Keys
            if events.type == pg.KEYDOWN:
                if events.key == pg.K_UP or events.key == pg.K_w or events.key == pg.K_SPACE:
                    V_Y = jump
                # For Mobile -- Click Sensors
            posMain = pg.mouse.get_pos()
            if posMain[0] > 660 and posMain[1] > 380 and posMain[0] < 677 and posMain[1] < screen_h or posMain[0] > 678 and posMain[1] > 380 and posMain[0] < screen_w and posMain[1] < screen_h:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))
            else:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_ARROW))
            if events.type == pg.MOUSEBUTTONUP:
                if posMain[0] > 660 and posMain[1] > 380 and posMain[0] < 677 and posMain[1] < screen_h:
                    pause(1)
                if posMain[0] > 678 and posMain[1] > 380 and posMain[0] < screen_w and posMain[1] < screen_h:
                    restart(1)
            if events.type == pg.KEYDOWN:
                if events.key == K_RIGHT or events.key == K_d:
                    G_MOVE = 5
                    V_X = 1
                    VO_X = 1
                    O_XaV = 10
                    O_XbV = 10
                    Move_coin_X = 10
                    keypressed = True
                if events.key == K_DOWN or events.key == K_s:
                    P_height = 15
                    P_Y = 285
            if events.type == pg.KEYUP:
                if events.key == K_RIGHT or events.key == K_d:
                    keypressed = False
                    G_MOVE = 0
                    V_X = 0
                    P_X = 380
                    VO_X = 2
                if events.key == K_DOWN or events.key == K_s:
                    P_height = 30
                    P_Y = 270

        if PlayerM.colliderect(ObsticleM):
            gameover = True

        if PlayerM.colliderect(ObsticleA):
            gameover = True

        if PlayerM.colliderect(ObsticleB):
            gameover = True

        coin_X -= Move_coin_X
        O_Xa -= O_XaV
        if O_Xa < 0:
            O_Xb -= O_XbV
        if O_Xa < 0 and O_Xb < 0:
            O_Xa = 710
            O_Xb = 710
        if coin_X < -1:
            coin_X = 710
        if keypressed:
            if O_X > 240:
                VO_X = -1
            if O_X < 236:
                VO_X = 1
        O_X += VO_X
        G_1 -= G_MOVE
        G_2 -= G_MOVE
        G_3 -= G_MOVE
        G_4 -= G_MOVE
        G_5 -= G_MOVE
        G_6 -= G_MOVE
        G_7 -= G_MOVE
        if G_1 < 0:
            G_1 = 700
        if G_2 < 0:
            G_2 = 700
        if G_3 < 0:
            G_3 = 700
        if G_4 < 0:
            G_4 = 700
        if G_5 < 0:
            G_5 = 700
        if G_6 < 0:
            G_6 = 700
        if G_7 < 0:
            G_7 = 700
        O_X += VO_X
        P_X += V_X
        if P_X > 380:
            V_X = -1
        if P_X < 377:
            V_X = 1
        P_Y += V_Y
        if P_Y <= 200:
            V_Y = -jump
        if P_Y >= 270:
            V_Y = 0

        if not gameover:
            time += 1
        window.fill(greySky)
        text_screen(f"Time : {time} ms", black, 0, 0)
        text_screen_coins(f"Coins : {coinCollected}", black, screen_w-123, 0)
        pg.draw.rect(window, grey, GroundM)
        coin = pg.draw.circle(window, golden, (coin_X, 285), 8)
        pg.draw.rect(window, grey, (G_1, 298, 10, 10))
        pg.draw.rect(window, grey, (G_2, 298, 10, 10))
        pg.draw.rect(window, grey, (G_3, 298, 10, 10))
        pg.draw.rect(window, grey, (G_4, 298, 10, 10))
        pg.draw.rect(window, grey, (G_5, 298, 10, 10))
        pg.draw.rect(window, grey, (G_6, 298, 10, 10))
        pg.draw.rect(window, grey, (G_7, 298, 10, 10))
        pg.draw.rect(window, red, ObsticleA)
        pg.draw.rect(window, red, ObsticleB)
        pg.draw.rect(window, red, ObsticleM)
        pg.draw.rect(window, "white", (screen_w-20, screen_h-20, 20, 20))
        pg.draw.rect(window, "white", (screen_w-40, screen_h-20, 20, 20))
        text("\u23F8", "black", screen_w-37, screen_h-23, "segoeuisymbol", 16)
        text("↺", "black", screen_w-18, screen_h-23, "segoeuisymbol", 16)
        if selected is selected1 or selected is selected2 or selected is selected3:
            pg.draw.rect(window, player_skin[selected], PlayerM)
        if selected is selected4:
            pg.draw.rect(window, selected4_Color, PlayerM)
        if selected is selected5:
            if sec_1 > 30:
                selected5_Color = rd.choice(
                    ((57, 217, 218), (57, 217, 103), (211, 135, 249), (96, 59, 44)))
                sec_1 = 0
            pg.draw.rect(window, selected5_Color, PlayerM)
        if selected is selected6:
            pg.draw.rect(window, rd.choice(
                ((255, 0, 0), (0, 255, 0), (0, 0, 255))), PlayerM)

        if coin.colliderect(PlayerM):
            coinCollected += 1
            coin_X = 710

        if gameover:
            P_X = 350
            P_Y = 0
            V_X = 0
            V_Y = 0
            O_X = 0
            O_Xa = 0
            Play_Again = Level_1
            Current_Level = 1
            Game_over()
        pg.display.update()
        sec_1 += 1
        clock.tick(fps)


def Level_2():
    global time
    global coinCollected
    global Play_Again
    global Current_Level
    selected4_Color = rd.choice(((254, 234, 0), (159, 32, 164),
                                 (57, 121, 42), (96, 59, 44)))
    selected5_Color = rd.choice(
        ((57, 217, 218), (57, 217, 103), (211, 135, 249), (96, 59, 44)))
    run = True
    gameover = False
    black = (0, 0, 0)
    grey = (166, 166, 166)
    greySky = (224, 224, 224)
    red = (255, 0, 0)
    golden = (253, 181, 2)
    coinCollected = 0
    coin_X = rd.randint(10, 350)
    coin_X2 = rd.randint(350, 690)
    G_1 = 100
    G_2 = 200
    G_3 = 300
    G_4 = 400
    G_5 = 500
    G_6 = 600
    G_7 = 700
    P_X = 350
    P_Y = 270
    O_X = 685
    O_Y = 280
    O_X2 = 3
    O_Y2 = 280
    V_X = 0
    V_Y = 0
    move_f = 8
    move_b = -8
    move_o = -8
    move_o2 = 8
    jump = -15
    sec_1 = 0
    time = 0
    fps = 30

    clock = pg.time.Clock()

    font1 = pg.font.SysFont("times", 25)
    font1_coins = pg.font.SysFont("times", 25)

    def text_screen(text, color, x, y):
        set_text = font1.render(text, True, color)
        window.blit(set_text, (x, y))

    def text_screen_coins(text, color, x, y):
        set_text_coin = font1_coins.render(text, True, color)
        window.blit(set_text_coin, (x, y))

    while run:
        PlayerM = pg.Rect(P_X, P_Y, 15, 30)
        ObsticleM = pg.Rect(O_X, O_Y, 15, 20)
        ObsticleM2 = pg.Rect(O_X2, O_Y2, 15, 20)
        GroundM = pg.Rect(0, 300, 700, 100)
        for events in pg.event.get():
            if events.type == pg.QUIT:
                quit_game()
                # For Computer -- Keyboard Arrow Keys
            if events.type == pg.KEYDOWN:
                if events.key == pg.K_RIGHT or events.key == pg.K_d:
                    V_X = move_f
                if events.key == pg.K_LEFT or events.key == pg.K_a:
                    V_X = move_b
                if events.key == pg.K_UP or events.key == pg.K_w or events.key == pg.K_SPACE:
                    V_Y = jump
            if events.type == pg.KEYUP:
                if events.key == pg.K_RIGHT or events.key == pg.K_d:
                    V_X = 0
                if events.key == pg.K_LEFT or events.key == pg.K_a:
                    V_X = 0
                # For Mobile -- Click Sensors
            posMain = pg.mouse.get_pos()
            if posMain[0] > 660 and posMain[1] > 380 and posMain[0] < 677 and posMain[1] < screen_h or posMain[0] > 678 and posMain[1] > 380 and posMain[0] < screen_w and posMain[1] < screen_h:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))
            else:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_ARROW))
            if events.type == pg.MOUSEBUTTONDOWN:
                if posMain[0] > 660 and posMain[1] > 380 and posMain[0] < 677 and posMain[1] < screen_h:
                    pause(2)
                if posMain[0] > 678 and posMain[1] > 380 and posMain[0] < screen_w and posMain[1] < screen_h:
                    restart(2)

        if PlayerM.colliderect(ObsticleM):
            gameover = True

        if PlayerM.colliderect(ObsticleM2):
            gameover = True

        O_X += move_o
        O_X2 += move_o2
        P_X += V_X
        P_Y += V_Y
        if P_Y <= 200:
            V_Y = -jump
        if P_Y >= 270:
            V_Y = 0

        if O_X < 0:
            move_o = 8
        if O_X > 685:
            move_o = -8

        if O_X2 < 0:
            move_o2 = 8
        if O_X2 > 685:
            move_o2 = -8

        if P_X < 3 or P_X > 681:
            V_X = 0

        if not gameover:
            time += 1
        window.fill(greySky)
        text_screen(f"Time : {time} ms", black, 0, 0)
        text_screen_coins(f"Coins : {coinCollected}", black, screen_w-123, 0)
        pg.draw.rect(window, grey, GroundM)
        pg.draw.rect(window, grey, (G_1, 298, 10, 10))
        pg.draw.rect(window, grey, (G_2, 298, 10, 10))
        pg.draw.rect(window, grey, (G_3, 298, 10, 10))
        pg.draw.rect(window, grey, (G_4, 298, 10, 10))
        pg.draw.rect(window, grey, (G_5, 298, 10, 10))
        pg.draw.rect(window, grey, (G_6, 298, 10, 10))
        pg.draw.rect(window, grey, (G_7, 298, 10, 10))
        coin = pg.draw.circle(window, golden, (coin_X, 285), 8)
        coin2 = pg.draw.circle(window, golden, (coin_X2, 285), 8)
        pg.draw.rect(window, red, ObsticleM)
        pg.draw.rect(window, red, ObsticleM2)
        pg.draw.rect(window, "white", (screen_w-20, screen_h-20, 20, 20))
        pg.draw.rect(window, "white", (screen_w-40, screen_h-20, 20, 20))
        text("\u23F8", "black", screen_w-37, screen_h-23, "segoeuisymbol", 16)
        text("↺", "black", screen_w-18, screen_h-23, "segoeuisymbol", 16)
        if selected is selected1 or selected is selected2 or selected is selected3:
            pg.draw.rect(window, player_skin[selected], PlayerM)
        if selected is selected4:
            pg.draw.rect(window, selected4_Color, PlayerM)
        if selected is selected5:
            if sec_1 > 30:
                selected5_Color = rd.choice(
                    ((57, 217, 218), (57, 217, 103), (211, 135, 249), (96, 59, 44)))
                sec_1 = 0
            pg.draw.rect(window, selected5_Color, PlayerM)
        if selected is selected6:
            pg.draw.rect(window, rd.choice(
                ((255, 0, 0), (0, 255, 0), (0, 0, 255))), PlayerM)

        if coin.colliderect(PlayerM):
            coinCollected += 1
            coin_X = rd.randint(10, 350)

        if coin2.colliderect(PlayerM):
            coinCollected += 1
            coin_X2 = rd.randint(350, 690)

        if gameover:
            P_X = 350
            P_Y = 0
            V_X = 0
            V_Y = 0
            O_X = 0
            O_X2 = 0
            Play_Again = Level_2
            Current_Level = 2
            Game_over()
        sec_1 += 1
        pg.display.update()
        clock.tick(fps)


def Level_3():
    global time
    global coinCollected
    global Play_Again
    global Current_Level
    sec_1 = 0
    selected4_Color = rd.choice(((254, 234, 0), (159, 32, 164),
                                 (57, 121, 42), (96, 59, 44)))
    selected5_Color = rd.choice(
        ((57, 217, 218), (57, 217, 103), (211, 135, 249), (96, 59, 44)))
    run = True
    gameover = False
    black = (0, 0, 0)
    grey = (166, 166, 166)
    greySky = (224, 224, 224)
    golden = (253, 181, 2)
    coinCollected = 0
    coin_X = rd.choice((99, 603))
    G_1 = 100
    G_2 = 200
    G_3 = 300
    G_4 = 400
    G_5 = 500
    G_6 = 600
    G_7 = 700
    P_X = 350
    P_Y = 270
    O_Y1 = -50
    O_Y2 = -50
    O_Y3 = -50
    P_height = 30
    Turn = rd.randint(1, 3)
    V_Y = 0
    V_X = 0
    mover = 9
    movel = -9
    jump = -15
    time = 0
    fps = 30

    clock = pg.time.Clock()

    font1 = pg.font.SysFont("times", 25)
    font1_coins = pg.font.SysFont("times", 25)

    def text_screen(text, color, x, y):
        set_text = font1.render(text, True, color)
        window.blit(set_text, (x, y))

    def text_screen_coins(text, color, x, y):
        set_text_coin = font1_coins.render(text, True, color)
        window.blit(set_text_coin, (x, y))

    while run:
        PlayerM = pg.Rect(P_X, P_Y, 15, P_height)
        GroundM = pg.Rect(0, 300, 700, 100)
        for events in pg.event.get():
            if events.type == pg.QUIT:
                quit_game()
            pos = pg.mouse.get_pos()
            if pos[0] > 660 and pos[1] > 380 and pos[0] < 677 and pos[1] < screen_h or pos[0] > 678 and pos[1] > 380 and pos[0] < screen_w and pos[1] < screen_h:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))
            else:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_ARROW))
            if events.type == pg.MOUSEBUTTONDOWN:
                if pos[0] > 660 and pos[1] > 380 and pos[0] < 677 and pos[1] < screen_h:
                    pause(3)
                if pos[0] > 678 and pos[1] > 380 and pos[0] < screen_w and pos[1] < screen_h:
                    restart(3)
            if events.type == pg.KEYDOWN:
                if events.key == pg.K_UP or events.key == pg.K_w or events.key == pg.K_SPACE:
                    V_Y = jump
                if events.key == pg.K_RIGHT or events.key == pg.K_d:
                    V_X = mover
                if events.key == pg.K_LEFT or events.key == pg.K_a:
                    V_X = movel
            if events.type == pg.KEYUP:
                if events.key == pg.K_RIGHT or events.key == pg.K_d:
                    V_X = 0
                if events.key == pg.K_LEFT or events.key == pg.K_a:
                    V_X = 0

        if Turn == 1:
            O_Y1 += 5
        if Turn == 2:
            O_Y2 += 5
        if Turn == 3:
            O_Y3 += 5
        if O_Y1 > 700:
            O_Y1 = -50
            Turn = rd.randint(2, 3)
        if O_Y2 > 700:
            O_Y2 = -50
            Turn = rd.choice((1, 3))
        if O_Y3 > 700:
            O_Y3 = -50
            Turn = rd.randint(1, 2)
        P_X += V_X
        P_Y += V_Y
        if P_X < -20:
            P_X = 719
        if P_X > 720:
            P_X = -19
        if P_Y <= 200:
            V_Y = -jump
        if P_Y >= 270:
            V_Y = 0

        if not gameover:
            time += 1
        window.fill(greySky)
        coin1 = pg.draw.circle(window, golden, (coin_X, 285), 8)
        ObsticleM1 = pg.draw.circle(window, (255, 0, 0), (100, O_Y1), 50)
        ObsticleM2 = pg.draw.circle(window, (255, 0, 0), (350, O_Y2), 50)
        ObsticleM3 = pg.draw.circle(window, (255, 0, 0), (600, O_Y3), 50)
        text_screen(f"Time : {time} ms", black, 0, 0)
        text_screen_coins(f"Coins : {coinCollected}", black, screen_w-123, 0)
        pg.draw.rect(window, grey, GroundM)
        pg.draw.rect(window, grey, (G_1, 298, 10, 10))
        pg.draw.rect(window, grey, (G_2, 298, 10, 10))
        pg.draw.rect(window, grey, (G_3, 298, 10, 10))
        pg.draw.rect(window, grey, (G_4, 298, 10, 10))
        pg.draw.rect(window, grey, (G_5, 298, 10, 10))
        pg.draw.rect(window, grey, (G_6, 298, 10, 10))
        pg.draw.rect(window, grey, (G_7, 298, 10, 10))
        pg.draw.rect(window, "white", (screen_w-20, screen_h-20, 20, 20))
        pg.draw.rect(window, "white", (screen_w-40, screen_h-20, 20, 20))
        text("\u23F8", "black", screen_w-37, screen_h-23, "segoeuisymbol", 16)
        text("↺", "black", screen_w-18, screen_h-23, "segoeuisymbol", 16)
        ObsticleM4 = pg.draw.polygon(surface=window, color=(255, 0, 0),
                                     points=[(212, 300), (225, 280), (238, 300)])
        ObsticleM5 = pg.draw.polygon(surface=window, color=(255, 0, 0),
                                     points=[(482, 299), (495, 280), (508, 299)])
        if selected is selected1 or selected is selected2 or selected is selected3:
            pg.draw.rect(window, player_skin[selected], PlayerM)
        if selected is selected4:
            pg.draw.rect(window, selected4_Color, PlayerM)
        if selected is selected5:
            if sec_1 > 30:
                selected5_Color = rd.choice(
                    ((57, 217, 218), (57, 217, 103), (211, 135, 249), (96, 59, 44)))
                sec_1 = 0
            pg.draw.rect(window, selected5_Color, PlayerM)
        if selected is selected6:
            pg.draw.rect(window, rd.choice(
                ((255, 0, 0), (0, 255, 0), (0, 0, 255))), PlayerM)

        if coin1.colliderect(PlayerM):
            coinCollected += 1
            coin_X = rd.choice(
                (rd.randint(28, 175), rd.randint(548, 672), rd.randint(270, 458)))

        if ObsticleM1.colliderect(PlayerM) or ObsticleM2.colliderect(PlayerM) or ObsticleM3.colliderect(PlayerM) or ObsticleM4.colliderect(PlayerM) or ObsticleM5.colliderect(PlayerM):
            gameover = True

        if gameover:
            P_X = 350
            P_Y = 0
            V_X = 0
            V_Y = 0
            Play_Again = Level_3
            Current_Level = 3
            Game_over()

        sec_1 += 1
        pg.display.update()
        clock.tick(fps)


def Level_4():
    global time
    global coinCollected
    global Play_Again
    global Current_Level
    sec_1 = 0
    selected4_Color = rd.choice(((254, 234, 0), (159, 32, 164),
                                 (57, 121, 42), (96, 59, 44)))
    selected5_Color = rd.choice(
        ((57, 217, 218), (57, 217, 103), (211, 135, 249), (96, 59, 44)))
    time = 0
    gameover = False
    coinCollected = 0
    grey = (166, 166, 166)
    greySky = (224, 224, 224)
    Ox1 = -20
    Oy1 = 280
    Ox2 = 720
    Oy2 = 280
    Px = 350
    Hx = Px
    Py = 270
    Pw = 15
    Ph = 30
    V_X = 0
    V_Y = 0
    jump = -15
    LR = 0
    G_1 = 100
    G_2 = 200
    G_3 = 300
    G_4 = 400
    G_5 = 500
    G_6 = 600
    G_7 = 700
    Clas_x = -10
    Clas_y = -10
    Clas_x2 = -10
    Clas_y2 = -10
    Move = 0
    Move2 = 0
    ready1 = True
    ready2 = True
    barColor = (0, 153, 0)
    barM_width = 200
    fps = 45
    clock = pg.time.Clock()

    def text_screen(text, color, x, y, family, size):
        font1 = pg.font.SysFont(family, size)
        set_text = font1.render(text, True, color)
        window.blit(set_text, (x, y))

    def Health_Bar_Numbers(Numbers, plusORminus):
        sign = ""
        hncolor = "black"
        numberY = screen_h-44
        if plusORminus == 1:
            sign = "+"
            hncolor = "darkgreen"
        elif plusORminus == 0:
            sign = "-"
            hncolor = "red"
        else:
            sign = ""
        text_screen(sign+str(Numbers), hncolor, 230,
                    numberY, "comicsansms", 18)

    class Bullets:
        global BULLET_Object

        def __init__(self, X_axis, Y_axis):
            self.x = X_axis
            self.y = Y_axis

        def create_bullet(self):
            global BULLET_Object
            BULLET_Object = pg.draw.circle(
                window, (0, 0, 0), (self.x, self.y), 5)

    class Obsticles:
        global Obsticle_Main

        def __init__(self, X_axis, Yaxis):
            self.x = X_axis
            self.y = Yaxis

        def create_enemy(self):
            global ObsticlesMain
            ObsticlesMain = [Obsticle2]
            Obsticle_Main = pg.Rect(self.x, self.y, 15, 20)
            pg.draw.rect(window, "red", Obsticle_Main)
            ObsticlesMain.append(Obsticle_Main)

    while True:
        window.fill(greySky)
        pos = pg.mouse.get_pos()
        Player = pg.Rect(Px, Py, Pw, Ph)
        Hand = pg.Rect(Hx, Py+7, 30, 5)
        GroundM = pg.Rect(0, 300, 700, 100)
        Bullet = Bullets(Clas_x, Clas_y)
        Bullet2 = Bullets(Clas_x2, Clas_y2)
        Obsticle1 = Obsticles(Ox1, Oy1)
        Obsticle2 = Obsticles(Ox2, Oy2)
        barBG = pg.Rect(10, screen_h-45, 210, 30)
        barMbg = pg.Rect(15, screen_h-40, 200, 20)
        barM = pg.Rect(15, screen_h-40, barM_width, 20)
        for i in pg.event.get():
            if i.type == pg.QUIT:
                quit_game()
            if i.type == pg.KEYDOWN:
                if i.key == K_RIGHT or i.key == pg.K_d:
                    LR = 0
                    V_X = 10
                if i.key == K_SPACE:
                    if ready1:
                        if LR >= 0:
                            Clas_x, Clas_y = Px+37, Py+10
                            Move = 25
                            ready1 = False
                    if ready2:
                        if LR < 0:
                            Clas_x2, Clas_y2 = Px-37, Py+10
                            Move2 = -25
                            ready2 = False
                if i.key == pg.K_UP or i.key == pg.K_w:
                    V_Y = jump
            if i.type == pg.KEYUP:
                if i.key == K_RIGHT or i.key == pg.K_d:
                    LR = 0
                    V_X = 0
            if i.type == pg.KEYDOWN:
                if i.key == K_LEFT or i.key == pg.K_a:
                    LR = -15
                    V_X = -10
            if i.type == pg.KEYUP:
                if i.key == K_LEFT or i.key == pg.K_a:
                    LR = -15
                    V_X = 0
            posMain = pg.mouse.get_pos()
            if posMain[0] > 660 and posMain[1] > 380 and posMain[0] < 677 and posMain[1] < screen_h or posMain[0] > 678 and posMain[1] > 380 and posMain[0] < screen_w and posMain[1] < screen_h:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))
            else:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_ARROW))
            if i.type == pg.MOUSEBUTTONDOWN:
                if posMain[0] > 660 and posMain[1] > 380 and posMain[0] < 677 and posMain[1] < screen_h:
                    pause(4)
                if posMain[0] > 678 and posMain[1] > 380 and posMain[0] < screen_w and posMain[1] < screen_h:
                    restart(4)
                if ready1:
                    if LR >= 0:
                        Clas_x, Clas_y = Px+37, Py+10
                        Move = 25
                        ready1 = False
                if ready2:
                    if LR < 0:
                        Clas_x2, Clas_y2 = Px-37, Py+10
                        Move2 = -25
                        ready2 = False

        if not gameover:
            time += 1
        Px += V_X
        Py += V_Y
        Ox1 += 5
        Ox2 -= 5
        if Ox1 > 720:
            Ox1 = -20
        if Ox2 < -20:
            Ox2 = 720
        Hx = Px+LR
        Clas_x += Move
        Clas_x2 += Move2
        if Clas_x > 720:
            ready1 = True
        if Clas_x2 < -5:
            ready2 = True
        if Py <= 200:
            V_Y = -jump
        if Py >= 270:
            V_Y = 0
        if Px < 3 or Px > 679:
            V_X = 0

        # Health Bar color statements
        if barM_width <= 200:
            barColor = (0, 153, 0)
        if barM_width <= 150:
            barColor = (76, 153, 0)
        if barM_width <= 100:
            barColor = (153, 153, 0)
        if barM_width <= 50:
            barColor = (153, 76, 0)
        if barM_width <= 20:
            barColor = (204, 0, 0)
        if barM_width <= 0:
            barM_width = 0
            gameover = True
        if barM_width >= 200:
            barM_width = 200

        if gameover:
            coinCollected = (time+coinCollected)//10
            Play_Again = Level_4
            Current_Level = 4
            Game_over()

        try:
            # Obsticle 1 - Right Side
            if abs(Obsticle1.x-Bullet2.x) < 10 and abs(Obsticle1.y-Bullet2.y) < 6:
                Ox1 = -30
                coinCollected += 1
                ready1 = True
                barM_width += 10
                numb = 10
                pom = 1
            # Obsticle 1 - Left Side
            if abs(Obsticle1.x-Bullet.x) < 10 and abs(Obsticle1.y-Bullet.y) < 6:
                Ox1 = -30
                coinCollected += 1
                ready1 = True
                barM_width += 10
                numb = 10
                pom = 1
            # Obsticle 2 - Right Side
            if abs(Obsticle2.x-Bullet2.x) < 10 and abs(Obsticle2.y-Bullet2.y) < 6:
                Ox2 = 730
                coinCollected += 1
                ready2 = True
                barM_width += 10
                numb = 10
                pom = 1
            # Obsticle 2 - Left Side
            if abs(Obsticle2.x-Bullet.x) < 10 and abs(Obsticle2.y-Bullet.y) < 6:
                Ox2 = 730
                coinCollected += 1
                ready2 = True
                barM_width += 10
                numb = 10
                pom = 1
            # Collide with enemy - Game Over
            if abs(Px-Ox1) < 15 and abs(Py-Oy1) < 25:
                barM_width -= 30
                Ox1 = -20
                Oy1 = 280
                Ox2 = 720
                Oy2 = 280
                numb = 30
                pom = 0
            if abs(Px-Ox2) < 15 and abs(Py-Oy2) < 25:
                barM_width -= 30
                Ox1 = -30
                Oy1 = 280
                Ox2 = 720
                Oy2 = 280
                numb = 30
                pom = 0
        except Exception:
            pass

        Bullet.create_bullet()
        Bullet2.create_bullet()
        text_screen(f"Time : {time} ms", "black", 0, 0, "times", 25)
        text_screen(f"Kills : {coinCollected}", "black",
                    screen_w-123, 0, "times", 25)
        pg.draw.rect(window, grey, GroundM)
        pg.draw.rect(window, grey, (G_1, 298, 10, 10))
        pg.draw.rect(window, grey, (G_2, 298, 10, 10))
        pg.draw.rect(window, grey, (G_3, 298, 10, 10))
        pg.draw.rect(window, grey, (G_4, 298, 10, 10))
        pg.draw.rect(window, grey, (G_5, 298, 10, 10))
        pg.draw.rect(window, grey, (G_6, 298, 10, 10))
        pg.draw.rect(window, grey, (G_7, 298, 10, 10))
        pg.draw.rect(window, "black", barBG)
        pg.draw.rect(window, (224, 224, 224), barMbg)
        pg.draw.rect(window, barColor, barM)
        Obsticle1.create_enemy()
        Obsticle2.create_enemy()
        pg.draw.rect(window, "white", (screen_w-20, screen_h-20, 20, 20))
        pg.draw.rect(window, "white", (screen_w-40, screen_h-20, 20, 20))
        text("\u23F8", "black", screen_w-37, screen_h-23, "segoeuisymbol", 16)
        text("↺", "black", screen_w-18, screen_h-23, "segoeuisymbol", 16)
        try:
            Health_Bar_Numbers(Numbers=numb, plusORminus=pom)
        except Exception:
            pass
        if selected is selected1 or selected is selected2 or selected is selected3:
            pg.draw.rect(window, player_skin[selected], Hand)
            pg.draw.rect(window, player_skin[selected], Player)
        if selected is selected4:
            pg.draw.rect(window, selected4_Color, Hand)
            pg.draw.rect(window, selected4_Color, Player)
        if selected is selected5:
            if sec_1 > 30:
                selected5_Color = rd.choice(
                    ((57, 217, 218), (57, 217, 103), (211, 135, 249), (96, 59, 44)))
                sec_1 = 0
            pg.draw.rect(window, selected5_Color, Hand)
            pg.draw.rect(window, selected5_Color, Player)
        if selected is selected6:
            Skin_6 = rd.choice(((255, 0, 0), (0, 255, 0), (0, 0, 255)))
            pg.draw.rect(window, Skin_6, Hand)
            pg.draw.rect(
                window, Skin_6, Player)
        sec_1 += 1
        pg.display.update()
        clock.tick(fps)


def Level_5():
    global Current_Level
    global Play_Again
    global coinCollected
    global time
    sec_1 = 0
    selected4_Color = rd.choice(
        ((254, 234, 0), (159, 32, 164), (57, 121, 42), (96, 59, 44)))
    selected5_Color = rd.choice(
        ((57, 217, 218), (57, 217, 103), (211, 135, 249), (96, 59, 44)))
    G_1, G_2, G_3, G_4, G_5, G_6, G_7 = 100, 200, 300, 400, 500, 600, 700
    P_x, P_y = 250, 165
    wall1x_u, wall1y_u, wallh1_u = 500, rd.randint(-170, -130), 300
    wall2x_u, wall2y_u, wallh2_u = 580, rd.randint(-170, -130), 300
    wall3x_u, wall3y_u, wallh3_u = 660, rd.randint(-170, -130), 300
    wall4x_u, wall4y_u, wallh4_u = 740, rd.randint(-170, -130), 300
    wall5x_u, wall5y_u, wallh5_u = 820, rd.randint(-170, -130), 300
    wall6x_u, wall6y_u, wallh6_u = 900, rd.randint(-170, -130), 300
    wall7x_u, wall7y_u, wallh7_u = 980, rd.randint(-170, -130), 300
    wall8x_u, wall8y_u, wallh8_u = 1060, rd.randint(-170, -130), 300
    wall9x_u, wall9y_u, wallh9_u = 1140, rd.randint(-170, -130), 300
    space_between_walls_ul1 = ((wallh1_u+wall1y_u)+60)
    space_between_walls_ul2 = ((wallh2_u+wall2y_u)+60)
    space_between_walls_ul3 = ((wallh3_u+wall3y_u)+60)
    space_between_walls_ul4 = ((wallh4_u+wall4y_u)+60)
    space_between_walls_ul5 = ((wallh5_u+wall5y_u)+60)
    space_between_walls_ul6 = ((wallh6_u+wall6y_u)+60)
    space_between_walls_ul7 = ((wallh7_u+wall7y_u)+60)
    space_between_walls_ul8 = ((wallh8_u+wall8y_u)+60)
    space_between_walls_ul9 = ((wallh9_u+wall9y_u)+60)
    wall1x_l, wall1y_l, wallh1_l = 500, space_between_walls_ul1, 300
    wall2x_l, wall2y_l, wallh2_l = 580, space_between_walls_ul2, 300
    wall3x_l, wall3y_l, wallh3_l = 660, space_between_walls_ul3, 300
    wall4x_l, wall4y_l, wallh4_l = 740, space_between_walls_ul4, 300
    wall5x_l, wall5y_l, wallh5_l = 820, space_between_walls_ul5, 300
    wall6x_l, wall6y_l, wallh6_l = 900, space_between_walls_ul6, 300
    wall7x_l, wall7y_l, wallh7_l = 980, space_between_walls_ul7, 300
    wall8x_l, wall8y_l, wallh8_l = 1060, space_between_walls_ul8, 300
    wall9x_l, wall9y_l, wallh9_l = 1140, space_between_walls_ul9, 300
    CoinX1 = wall1x_u+15
    CoinY1 = wall1y_u+330
    CoinX2 = wall3x_u+15
    CoinY2 = wall3y_u+330
    CoinX3 = wall5x_u+15
    CoinY3 = wall5y_u+330
    CoinX4 = wall7x_u+15
    CoinY4 = wall7y_u+330
    CoinX5 = wall9x_u+15
    CoinY5 = wall9y_u+330
    V_y = 0
    clock = pg.time.Clock()
    fps = 30
    time = 0
    coinCollected = 0
    golden = (253, 181, 2)
    gameover = False

    def text_screen(text, color, x, y):
        font1 = pg.font.SysFont("times", 25)
        set_text = font1.render(text, True, color)
        window.blit(set_text, (x, y))

    while True:
        window.fill((224, 224, 224))
        PlayerM = pg.Rect(P_x, P_y, 20, 30)
        Wall1_u = pg.Rect(wall1x_u, wall1y_u, 30, wallh1_u)
        Wall2_u = pg.Rect(wall2x_u, wall2y_u, 30, wallh2_u)
        Wall3_u = pg.Rect(wall3x_u, wall3y_u, 30, wallh3_u)
        Wall4_u = pg.Rect(wall4x_u, wall4y_u, 30, wallh4_u)
        Wall5_u = pg.Rect(wall5x_u, wall5y_u, 30, wallh5_u)
        Wall6_u = pg.Rect(wall6x_u, wall6y_u, 30, wallh6_u)
        Wall7_u = pg.Rect(wall7x_u, wall7y_u, 30, wallh7_u)
        Wall8_u = pg.Rect(wall8x_u, wall8y_u, 30, wallh8_u)
        Wall9_u = pg.Rect(wall9x_u, wall9y_u, 30, wallh9_u)
        Wall1_l = pg.Rect(wall1x_l, wall1y_l, 30, wallh1_l)
        Wall2_l = pg.Rect(wall2x_l, wall2y_l, 30, wallh2_l)
        Wall3_l = pg.Rect(wall3x_l, wall3y_l, 30, wallh3_l)
        Wall4_l = pg.Rect(wall4x_l, wall4y_l, 30, wallh4_l)
        Wall5_l = pg.Rect(wall5x_l, wall5y_l, 30, wallh5_l)
        Wall6_l = pg.Rect(wall6x_l, wall6y_l, 30, wallh6_l)
        Wall7_l = pg.Rect(wall7x_l, wall7y_l, 30, wallh7_l)
        Wall8_l = pg.Rect(wall8x_l, wall8y_l, 30, wallh8_l)
        Wall9_l = pg.Rect(wall9x_l, wall9y_l, 30, wallh9_l)
        for eventsGO in pg.event.get():
            pos = pg.mouse.get_pos()
            if eventsGO.type == pg.QUIT:
                quit_game()
            if eventsGO.type == pg.KEYDOWN:
                if eventsGO.key == pg.K_UP or eventsGO.key == pg.K_w:
                    V_y = -5
                if eventsGO.key == pg.K_DOWN or eventsGO.key == pg.K_s:
                    V_y = 5
            if eventsGO.type == pg.KEYUP:
                if eventsGO.key == pg.K_UP or eventsGO.key == pg.K_w:
                    V_y = 0
                if eventsGO.key == pg.K_DOWN or eventsGO.key == pg.K_s:
                    V_y = 0
            if pos[0] > 660 and pos[1] > 380 and pos[0] < 677 and pos[1] < screen_h or pos[0] > 678 and pos[1] > 380 and pos[0] < screen_w and pos[1] < screen_h:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))
            else:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_ARROW))
            if eventsGO.type == pg.MOUSEBUTTONDOWN:
                if pos[0] > 660 and pos[1] > 380 and pos[0] < 677 and pos[1] < screen_h:
                    pause(5)
                if pos[0] > 678 and pos[1] > 380 and pos[0] < screen_w and pos[1] < screen_h:
                    restart(5)
        P_y += V_y
        CoinX1 -= 5
        CoinX2 -= 5
        CoinX3 -= 5
        CoinX4 -= 5
        CoinX5 -= 5
        wall1x_u -= 5
        wall1x_l -= 5
        wall2x_u -= 5
        wall2x_l -= 5
        wall3x_u -= 5
        wall3x_l -= 5
        wall4x_u -= 5
        wall4x_l -= 5
        wall5x_u -= 5
        wall5x_l -= 5
        wall6x_u -= 5
        wall6x_l -= 5
        wall7x_u -= 5
        wall7x_l -= 5
        wall8x_u -= 5
        wall8x_l -= 5
        wall9x_u -= 5
        wall9x_l -= 5
        if wall1x_u < -20:
            wall1x_u = 700
            wall1y_u = rd.randint(-170, -130)
        if wall1x_l < -20:
            wall1x_l = 700
            space_between_walls_ul1 = ((wallh1_u+wall1y_u)+60)
            wall1y_l = space_between_walls_ul1
            CoinX1 = wall1x_u+15
            CoinY1 = wall1y_u+330
        if wall2x_u < -20:
            wall2x_u = 700
            wall2y_u = rd.randint(-170, -130)
        if wall2x_l < -20:
            wall2x_l = 700
            space_between_walls_ul2 = ((wallh2_u+wall2y_u)+60)
            wall2y_l = space_between_walls_ul2
        if wall3x_u < -20:
            wall3x_u = 700
            wall3y_u = rd.randint(-170, -130)
        if wall3x_l < -20:
            wall3x_l = 700
            space_between_walls_ul3 = ((wallh3_u+wall3y_u)+60)
            wall3y_l = space_between_walls_ul3
            CoinX2 = wall3x_u+15
            CoinY2 = wall3y_u+330
        if wall4x_u < -20:
            wall4x_u = 700
            wall4y_u = rd.randint(-170, -130)
        if wall4x_l < -20:
            wall4x_l = 700
            space_between_walls_ul4 = ((wallh4_u+wall4y_u)+60)
            wall4y_l = space_between_walls_ul4
        if wall5x_u < -20:
            wall5x_u = 700
            wall5y_u = rd.randint(-170, -130)
        if wall5x_l < -20:
            wall5x_l = 700
            space_between_walls_ul5 = ((wallh5_u+wall5y_u)+60)
            wall5y_l = space_between_walls_ul5
            CoinX3 = wall5x_u+15
            CoinY3 = wall5y_u+330
        if wall6x_u < -20:
            wall6x_u = 700
            wall6y_u = rd.randint(-170, -130)
        if wall6x_l < -20:
            wall6x_l = 700
            space_between_walls_ul6 = ((wallh6_u+wall6y_u)+60)
            wall6y_l = space_between_walls_ul6
        if wall7x_u < -20:
            wall7x_u = 700
            wall7y_u = rd.randint(-170, -130)
        if wall7x_l < -20:
            wall7x_l = 700
            space_between_walls_ul7 = ((wallh7_u+wall7y_u)+60)
            wall7y_l = space_between_walls_ul7
            CoinX4 = wall7x_u+15
            CoinY4 = wall7y_u+330
        if wall8x_u < -20:
            wall8x_u = 700
            wall8y_u = rd.randint(-170, -130)
        if wall8x_l < -20:
            wall8x_l = 700
            space_between_walls_ul8 = ((wallh8_u+wall8y_u)+60)
            wall8y_l = space_between_walls_ul8
        if wall9x_u < -20:
            wall9x_u = 700
            wall9y_u = rd.randint(-170, -130)
        if wall9x_l < -20:
            wall9x_l = 700
            space_between_walls_ul9 = ((wallh9_u+wall9y_u)+60)
            wall9y_l = space_between_walls_ul9
            CoinX5 = wall9x_u+15
            CoinY5 = wall9y_u+330
        G_1 -= 5
        G_2 -= 5
        G_3 -= 5
        G_4 -= 5
        G_5 -= 5
        G_6 -= 5
        G_7 -= 5
        if G_1 < 0:
            G_1 = 700
        if G_2 < 0:
            G_2 = 700
        if G_3 < 0:
            G_3 = 700
        if G_4 < 0:
            G_4 = 700
        if G_5 < 0:
            G_5 = 700
        if G_6 < 0:
            G_6 = 700
        if G_7 < 0:
            G_7 = 700
        if not gameover:
            time += 1
        pg.draw.rect(window, (166, 166, 166), (G_1, 298, 10, 10))
        pg.draw.rect(window, (166, 166, 166), (G_2, 298, 10, 10))
        pg.draw.rect(window, (166, 166, 166), (G_3, 298, 10, 10))
        pg.draw.rect(window, (166, 166, 166), (G_4, 298, 10, 10))
        pg.draw.rect(window, (166, 166, 166), (G_5, 298, 10, 10))
        pg.draw.rect(window, (166, 166, 166), (G_6, 298, 10, 10))
        pg.draw.rect(window, (166, 166, 166), (G_7, 298, 10, 10))
        pg.draw.rect(window, "black", (Wall1_u))
        pg.draw.rect(window, "black", (Wall2_u))
        pg.draw.rect(window, "black", (Wall3_u))
        pg.draw.rect(window, "black", (Wall4_u))
        pg.draw.rect(window, "black", (Wall5_u))
        pg.draw.rect(window, "black", (Wall6_u))
        pg.draw.rect(window, "black", (Wall7_u))
        pg.draw.rect(window, "black", (Wall8_u))
        pg.draw.rect(window, "black", (Wall9_u))
        pg.draw.rect(window, "black", (Wall1_l))
        pg.draw.rect(window, "black", (Wall2_l))
        pg.draw.rect(window, "black", (Wall3_l))
        pg.draw.rect(window, "black", (Wall4_l))
        pg.draw.rect(window, "black", (Wall5_l))
        pg.draw.rect(window, "black", (Wall6_l))
        pg.draw.rect(window, "black", (Wall7_l))
        pg.draw.rect(window, "black", (Wall8_l))
        pg.draw.rect(window, "black", (Wall9_l))
        Coin1 = pg.draw.circle(window, golden, (CoinX1, CoinY1), 8)
        Coin2 = pg.draw.circle(window, golden, (CoinX2, CoinY2), 8)
        Coin3 = pg.draw.circle(window, golden, (CoinX3, CoinY3), 8)
        Coin4 = pg.draw.circle(window, golden, (CoinX4, CoinY4), 8)
        Coin5 = pg.draw.circle(window, golden, (CoinX5, CoinY5), 8)
        pg.draw.rect(window, (255, 255, 255), (0, 0, 710, 30))
        pg.draw.rect(window, (166, 166, 166), (0, 300, 700, 100))
        pg.draw.rect(window, "white", (screen_w-20, screen_h-20, 20, 20))
        pg.draw.rect(window, "white", (screen_w-40, screen_h-20, 20, 20))
        text("\u23F8", "black", screen_w-37, screen_h-23, "segoeuisymbol", 16)
        text("↺", "black", screen_w-18, screen_h-23, "segoeuisymbol", 16)
        text_screen(f"Time : {time} ms", "black", 0, 0)
        text_screen(f"Coins : {coinCollected}", "black",
                    screen_w-(84+len(str(coinCollected))*13), 0)
        if selected is selected1 or selected is selected2 or selected is selected3:
            pg.draw.rect(window, player_skin[selected], PlayerM)
        if selected is selected4:
            pg.draw.rect(window, selected4_Color, PlayerM)
        if selected is selected5:
            if sec_1 > 30:
                selected5_Color = rd.choice(
                    ((57, 217, 218), (57, 217, 103), (211, 135, 249), (96, 59, 44)))
                sec_1 = 0
            pg.draw.rect(window, selected5_Color, PlayerM)
        if selected is selected6:
            pg.draw.rect(window, rd.choice(
                ((255, 0, 0), (0, 255, 0), (0, 0, 255))), PlayerM)

        if gameover:
            Play_Again = Level_5
            Current_Level = 5
            Game_over()

        if PlayerM.colliderect(Coin1):
            coinCollected += 1
            CoinY1 = -15
        if PlayerM.colliderect(Coin2):
            coinCollected += 1
            CoinY2 = -15
        if PlayerM.colliderect(Coin3):
            coinCollected += 1
            CoinY3 = -15
        if PlayerM.colliderect(Coin4):
            coinCollected += 1
            CoinY4 = -15
        if PlayerM.colliderect(Coin5):
            coinCollected += 1
            CoinY5 = -15

        if PlayerM.colliderect(Wall1_u) or PlayerM.colliderect(Wall1_l) or PlayerM.colliderect(Wall2_u) or PlayerM.colliderect(Wall2_l) or PlayerM.colliderect(Wall3_u) or PlayerM.colliderect(Wall3_l) or PlayerM.colliderect(Wall4_u) or PlayerM.colliderect(Wall4_l) or PlayerM.colliderect(Wall5_u) or PlayerM.colliderect(Wall5_l) or PlayerM.colliderect(Wall6_u) or PlayerM.colliderect(Wall6_l) or PlayerM.colliderect(Wall7_u) or PlayerM.colliderect(Wall7_l) or PlayerM.colliderect(Wall8_u) or PlayerM.colliderect(Wall8_l) or PlayerM.colliderect(Wall9_u) or PlayerM.colliderect(Wall9_l):
            gameover = True

        sec_1 += 1
        pg.display.update()
        clock.tick(fps)


def Level_6():
    global time
    global coinCollected
    global Play_Again
    global Current_Level
    sec_1 = 0
    selected4_Color = rd.choice(((254, 234, 0), (159, 32, 164),
                                 (57, 121, 42), (96, 59, 44)))
    selected5_Color = rd.choice(
        ((57, 217, 218), (57, 217, 103), (211, 135, 249), (96, 59, 44)))
    time = 0
    gameover = False
    EnemiesKilled = 0
    grey = (166, 166, 166)
    greySky = (224, 224, 224)
    Ox1 = -20
    Oy1 = 280
    Ox2 = 720
    Oy2 = 280
    O_Y1 = -50
    O_Y2 = -50
    O_Y3 = -50
    O_Fx = -20
    O_Fx_By = 210
    O_Fx_By_velocity = 0
    O_Fx_B_Timer = 0
    O_Fvx = 5
    Turn = rd.randint(1, 3)
    Px = 350
    Hx = Px
    Py = 270
    Pw = 15
    Ph = 30
    V_X = 0
    V_Y = 0
    jump = -15
    LR = 0
    G_1 = 100
    G_2 = 200
    G_3 = 300
    G_4 = 400
    G_5 = 500
    G_6 = 600
    G_7 = 700
    Clas_x = -10
    Clas_y = -10
    Clas_x2 = -10
    Clas_y2 = -10
    Move = 0
    Move2 = 0
    ready1 = True
    ready2 = True
    barColor = (0, 153, 0)
    barM_width = 200
    fps = 35
    clock = pg.time.Clock()

    def text_screen(text, color, x, y, family, size):
        font1 = pg.font.SysFont(family, size)
        set_text = font1.render(text, True, color)
        window.blit(set_text, (x, y))

    def Health_Bar_Numbers(Numbers, plusORminus):
        sign = ""
        hncolor = "black"
        numberY = screen_h-44
        if plusORminus == 1:
            sign = "+"
            hncolor = "darkgreen"
        elif plusORminus == 0:
            sign = "-"
            hncolor = "red"
        else:
            sign = ""
        text_screen(sign+str(Numbers), hncolor, 230,
                    numberY, "comicsansms", 18)

    class Bullets:
        global BULLET_Object

        def __init__(self, X_axis, Y_axis):
            self.x = X_axis
            self.y = Y_axis

        def create_bullet(self):
            global BULLET_ObjectM
            # BULLET_Object = pg.draw.circle(window, (0, 0, 0), (self.x, self.y), 5)
            BULLET_ObjectM = pg.Rect(self.x, self.y, 10, 10)
            BULLET_Object = pg.draw.ellipse(
                window, (0, 0, 0), BULLET_ObjectM)

    class Obsticles:
        global Obsticle_Main

        def __init__(self, X_axis, Yaxis):
            self.x = X_axis
            self.y = Yaxis

        def create_enemy(self):
            global ObsticlesMain
            ObsticlesMain = [Obsticle2]
            Obsticle_Main = pg.Rect(self.x, self.y, 15, 20)
            pg.draw.rect(window, (220, 167, 0), Obsticle_Main)
            ObsticlesMain.append(Obsticle_Main)

    while True:
        window.fill(greySky)
        pos = pg.mouse.get_pos()
        PlayerM = pg.Rect(Px, Py, Pw, Ph)
        Hand = pg.Rect(Hx, Py+7, 30, 5)
        GroundM = pg.Rect(0, 300, 700, 100)
        Bullet = Bullets(Clas_x, Clas_y)
        Bullet2 = Bullets(Clas_x2, Clas_y2)
        Obsticle1 = Obsticles(Ox1, Oy1)
        Obsticle2 = Obsticles(Ox2, Oy2)
        ObsticleFly = pg.Rect(O_Fx, 200, 15, 30)
        barBG = pg.Rect(10, screen_h-45, 210, 30)
        barMbg = pg.Rect(15, screen_h-40, 200, 20)
        barM = pg.Rect(15, screen_h-40, barM_width, 20)
        ObsticleFly_Bullet = pg.Rect(O_Fx+2.5, O_Fx_By, 10, 10)
        for i in pg.event.get():
            if i.type == pg.QUIT:
                quit_game()
            if i.type == pg.KEYDOWN:
                if i.key == pg.K_RIGHT or i.key == pg.K_d:
                    LR = 0
                    V_X = 10
                if i.key == pg.K_SPACE:
                    if ready1:
                        if LR >= 0:
                            Clas_x, Clas_y = Px+37, Py+10
                            Move = 25
                            ready1 = False
                    if ready2:
                        if LR < 0:
                            Clas_x2, Clas_y2 = Px-37, Py+10
                            Move2 = -25
                            ready2 = False
                if i.key == pg.K_UP or i.key == pg.K_w:
                    V_Y = jump
            if i.type == pg.KEYUP:
                if i.key == pg.K_RIGHT or i.key == pg.K_d:
                    LR = 0
                    V_X = 0
            if i.type == pg.KEYDOWN:
                if i.key == pg.K_LEFT or i.key == pg.K_a:
                    LR = -15
                    V_X = -10
            if i.type == pg.KEYUP:
                if i.key == pg.K_LEFT or i.key == pg.K_a:
                    LR = -15
                    V_X = 0
            if pos[0] > 660 and pos[1] > 380 and pos[0] < 677 and pos[1] < screen_h or pos[0] > 678 and pos[1] > 380 and pos[0] < screen_w and pos[1] < screen_h:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))
            else:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_ARROW))
            if i.type == pg.MOUSEBUTTONDOWN:
                if pos[0] > 660 and pos[1] > 380 and pos[0] < 677 and pos[1] < screen_h:
                    pause(6)
                if pos[0] > 678 and pos[1] > 380 and pos[0] < screen_w and pos[1] < screen_h:
                    restart(6)
                if ready1:
                    if LR >= 0:
                        Clas_x, Clas_y = Px+37, Py+10
                        Move = 25
                        ready1 = False
                if ready2:
                    if LR < 0:
                        Clas_x2, Clas_y2 = Px-37, Py+10
                        Move2 = -25
                        ready2 = False

        if not gameover:
            time += 1
        Px += V_X
        Py += V_Y
        Ox1 += 5
        Ox2 -= 5
        if Ox1 > 720:
            Ox1 = -20
        if Ox2 < -20:
            Ox2 = 720
        Hx = Px+LR
        Clas_x += Move
        Clas_x2 += Move2
        if Clas_x > 720:
            ready1 = True
        if Clas_x2 < -5:
            ready2 = True
        if Py <= 200:
            V_Y = -jump
        if Py >= 270:
            V_Y = 0
        if Px < 3 or Px > 679:
            V_X = 0

        # Health Bar color statements
        if barM_width <= 200:
            barColor = (0, 153, 0)
        if barM_width <= 150:
            barColor = (76, 153, 0)
        if barM_width <= 100:
            barColor = (153, 153, 0)
        if barM_width <= 50:
            barColor = (153, 76, 0)
        if barM_width <= 20:
            barColor = (204, 0, 0)
        if barM_width <= 0:
            barM_width = 0
            gameover = True
        if barM_width >= 200:
            barM_width = 200

        # Large obstical fall movement
        if Turn == 1:
            O_Y1 += 5
        if Turn == 2:
            O_Y2 += 5
        if Turn == 3:
            O_Y3 += 5
        if O_Y1 > 700:
            O_Y1 = -50
            Turn = rd.randint(2, 3)
        if O_Y2 > 700:
            O_Y2 = -50
            Turn = rd.choice((1, 3))
        if O_Y3 > 700:
            O_Y3 = -50
            Turn = rd.randint(1, 2)

        # Fly enemy movement
        O_Fx += O_Fvx
        if O_Fx > 720 or O_Fx < -20:
            O_Fvx *= -1

        # Fly enemy Bullet movement
        if O_Fx_B_Timer > fps*2:
            O_Fx_By_velocity = 10
            O_Fx_B_Timer = 0

        O_Fx_By += O_Fx_By_velocity

        if O_Fx_By > screen_h:
            O_Fx_By_velocity = 0
            O_Fx_By = 210

        if gameover:
            coinCollected = (time+EnemiesKilled)//10
            Play_Again = Level_6
            Current_Level = 6
            Game_over()

        try:
            # Obsticle 1 - Right Side
            if abs(Obsticle1.x-Bullet2.x) < 10 and abs(Obsticle1.y-Bullet2.y) < 6:
                Ox1 = -30
                EnemiesKilled += 1
                ready1 = True
                barM_width += 10
                numb = 10
                pom = 1
            # Obsticle 1 - Left Side
            if abs(Obsticle1.x-Bullet.x) < 10 and abs(Obsticle1.y-Bullet.y) < 6:
                Ox1 = -30
                EnemiesKilled += 1
                ready1 = True
                barM_width += 10
                numb = 10
                pom = 1
            # Obsticle 2 - Right Side
            if abs(Obsticle2.x-Bullet2.x) < 10 and abs(Obsticle2.y-Bullet2.y) < 6:
                Ox2 = 730
                EnemiesKilled += 1
                ready2 = True
                barM_width += 10
                numb = 10
                pom = 1
            # Obsticle 2 - Left Side
            if abs(Obsticle2.x-Bullet.x) < 10 and abs(Obsticle2.y-Bullet.y) < 6:
                Ox2 = 730
                EnemiesKilled += 1
                ready2 = True
                barM_width += 10
                numb = 10
                pom = 1
            # Collide with enemy - Health redused
            if abs(Px-Ox1) < 15 and abs(Py-Oy1) < 25:
                barM_width -= 30
                Ox1 = -20
                Oy1 = 280
                Ox2 = 720
                Oy2 = 280
                numb = 30
                pom = 0
            if abs(Px-Ox2) < 15 and abs(Py-Oy2) < 25:
                barM_width -= 30
                Ox1 = -20
                Oy1 = 280
                Ox2 = 720
                Oy2 = 280
                numb = 30
                pom = 0
            if ObsticleM1.colliderect(PlayerM) or ObsticleM2.colliderect(PlayerM) or ObsticleM3.colliderect(PlayerM):
                barM_width -= 50
                O_Y1 = -50
                O_Y2 = -50
                O_Y3 = -50
                numb = 50
                pom = 0
            # Flying Bullet hit - Against Player
            if ObsticleFly.colliderect(PlayerM):
                barM_width -= 40
                O_Fx = -20
                numb = 40
                pom = 0
            if ObsticleFly_Bullet.colliderect(PlayerM) and not ObsticleFly.colliderect(PlayerM):
                barM_width -= 30
                O_Fx_By_velocity = 0
                O_Fx_By = 210
                numb = 30
                pom = 0
            if BULLET_ObjectM.colliderect(ObsticleFly):
                barM_width += 20
                O_Fx = -20
                EnemiesKilled += 1
                numb = 20
                pom = 1
        except Exception:
            pass

        Bullet.create_bullet()
        Bullet2.create_bullet()
        text_screen(f"Time : {time} ms", "black", 0, 0, "times", 25)
        text_screen(f"Kills : {EnemiesKilled}", "black",
                    screen_w-123, 0, "times", 25)
        pg.draw.ellipse(window, "black", ObsticleFly_Bullet)
        pg.draw.rect(window, (0, 0, 153), ObsticleFly)
        ObsticleM1 = pg.draw.circle(window, (255, 0, 0), (100, O_Y1), 50)
        ObsticleM2 = pg.draw.circle(window, (255, 0, 0), (350, O_Y2), 50)
        ObsticleM3 = pg.draw.circle(window, (255, 0, 0), (600, O_Y3), 50)
        pg.draw.rect(window, grey, GroundM)
        pg.draw.rect(window, grey, (G_1, 298, 10, 10))
        pg.draw.rect(window, grey, (G_2, 298, 10, 10))
        pg.draw.rect(window, grey, (G_3, 298, 10, 10))
        pg.draw.rect(window, grey, (G_4, 298, 10, 10))
        pg.draw.rect(window, grey, (G_5, 298, 10, 10))
        pg.draw.rect(window, grey, (G_6, 298, 10, 10))
        pg.draw.rect(window, grey, (G_7, 298, 10, 10))
        pg.draw.rect(window, "black", barBG)
        pg.draw.rect(window, (224, 224, 224), barMbg)
        pg.draw.rect(window, barColor, barM)
        Obsticle1.create_enemy()
        Obsticle2.create_enemy()
        pg.draw.rect(window, "black", Hand)
        pg.draw.rect(window, "black", PlayerM)
        pg.draw.rect(window, "white", (screen_w-20, screen_h-20, 20, 20))
        pg.draw.rect(window, "white", (screen_w-40, screen_h-20, 20, 20))
        text("\u23F8", "black", screen_w-37, screen_h-23, "segoeuisymbol", 16)
        text("↺", "black", screen_w-18, screen_h-23, "segoeuisymbol", 16)
        try:
            Health_Bar_Numbers(Numbers=numb, plusORminus=pom)
        except Exception:
            pass
        if selected is selected1 or selected is selected2 or selected is selected3:
            pg.draw.rect(window, player_skin[selected], Hand)
            pg.draw.rect(window, player_skin[selected], PlayerM)
        if selected is selected4:
            pg.draw.rect(window, selected4_Color, Hand)
            pg.draw.rect(window, selected4_Color, PlayerM)
        if selected is selected5:
            if sec_1 > 30:
                selected5_Color = rd.choice(
                    ((57, 217, 218), (57, 217, 103), (211, 135, 249), (96, 59, 44)))
                sec_1 = 0
            pg.draw.rect(window, selected5_Color, Hand)
            pg.draw.rect(window, selected5_Color, PlayerM)
        if selected is selected6:
            Skin_6 = rd.choice(((255, 0, 0), (0, 255, 0), (0, 0, 255)))
            pg.draw.rect(window, Skin_6, Hand)
            pg.draw.rect(
                window, Skin_6, PlayerM)
        sec_1 += 1
        O_Fx_B_Timer += 1
        pg.display.update()
        clock.tick(fps)


def Levels_Help():
    while True:
        window.fill((224, 224, 224))
        for eventsL in pg.event.get():
            if eventsL.type == pg.QUIT:
                quit_game()
            posL = pg.mouse.get_pos()
            if posL[0] < 23 and posL[1] < 23 or posL[0] > 167 and posL[0] < 297 and posL[1] > 150 and posL[1] < 185 or posL[0] > 167 and posL[0] < 297 and posL[1] > 225 and posL[1] < 259 or posL[0] > 167 and posL[0] < 297 and posL[1] > 300 and posL[1] < 334 or posL[0] > 400 and posL[0] < 530 and posL[1] > 150 and posL[1] < 185 or posL[0] > 400 and posL[0] < 530 and posL[1] > 225 and posL[1] < 259 or posL[0] > 400 and posL[0] < 530 and posL[1] > 300 and posL[1] < 334:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))
            else:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_ARROW))
            if eventsL.type == pg.MOUSEBUTTONUP:
                if posL[0] < 23 and posL[1] < 23:
                    Choose_Level()
                if posL[0] > 167 and posL[0] < 297 and posL[1] > 150 and posL[1] < 185:
                    messagebox.showinfo(
                        "Jump - Level 1 - Help", "1 : Hold down → ( Right Arrow or D ) key to run.\n2 : Use ↑ ( Up Arrow or Space ) key to jump.\n3 : Use ↓ ( Down Arrow ) key to crouch.\n4 : Dodge enemies from right while keep an eye on left one, he hits if you stop.")
                if posL[0] > 167 and posL[0] < 297 and posL[1] > 225 and posL[1] < 259:
                    messagebox.showinfo(
                        "Jump - Level 2 - Help", "1 : Hold down → or ← ( A or D ) to move.\n2 : Use ↑ ( Up Arrow or Space ) key to jump.\n3 : Dodge two enemies moving blindly left and right.")
                if posL[0] > 167 and posL[0] < 297 and posL[1] > 300 and posL[1] < 334:
                    messagebox.showinfo(
                        "Jump - Level 3 - Help", "1 : Hold down → or ← ( A or D ) to move.\n2 : Use ↑ ( Up Arrow or Space ) key to jump.\n3 : Dodge random circles droping from sky as well as sharp triangles on the ground.")
                if posL[0] > 400 and posL[0] < 530 and posL[1] > 150 and posL[1] < 185:
                    messagebox.showinfo(
                        "Jump - Level 4 - Help", "1 : Hold down → or ← ( A or D ) to move and aim.\n2 : Use ↑ ( Up Arrow or Space ) key to jump.\n3 : Press space to shoot.\n4 : Dont let them hit you because you only have limited health.")
                if posL[0] > 400 and posL[0] < 530 and posL[1] > 225 and posL[1] < 259:
                    messagebox.showinfo(
                        "Jump - Level 5 - Help", "1 : Use ↑ and ↓ ( W or S ) key to ascend or descend.\n2 : Dodge random pipes and fly between the gaps.")
                if posL[0] > 400 and posL[0] < 530 and posL[1] > 300 and posL[1] < 334:
                    messagebox.showinfo(
                        "Jump - Level 6 - Help", "1 : Hold down → or ← ( A or D ) to move and aim.\n2 : Use ↑ ( Up Arrow or Space ) key to jump.\n3 : Press space to shoot.\n4 : Dodge two enemies moving blindly and one flying shooter.\n5 : Dodge random circles droping from sky.")

        text("Help", (0, 0, 0), screen_w/2-50, 40, "helvetica", 50)
        pg.draw.rect(window, (172, 172, 172), (0, 0, 23, 23))
        pg.draw.rect(window, "black", (screen_w/3-65, 150, 130, 35))
        pg.draw.rect(window, "black", (screen_w/3-65, 225, 130, 35))
        pg.draw.rect(window, "black", (screen_w/3-65, 300, 130, 35))
        pg.draw.rect(window, "black", (screen_w/1.5-65, 150, 130, 35))
        pg.draw.rect(window, "black", (screen_w/1.5-65, 225, 130, 35))
        pg.draw.rect(window, "black", (screen_w/1.5-65, 300, 130, 35))
        text("<", (0, 0, 0), 5, -1, "helvetica", 20)
        text("Level 1", "white", screen_w/3-40, 152, "times", 25)
        text("Level 2", "white", screen_w/3-40, 227, "times", 25)
        text("Level 3", "white", screen_w/3-40, 302, "times", 25)
        text("Level 4", "white", screen_w/3+195, 152, "times", 25)
        text("Level 5", "white", screen_w/3+195, 227, "times", 25)
        text("Level 6", "white", screen_w/3+195, 302, "times", 25)
        pg.display.update()
        pg.time.Clock().tick(30)


def Choose_Level():
    global idusr

    def text_text_level(text, color, x, y, size):
        font_Level_text = pg.font.SysFont("helvetica", size)
        text_level2 = font_Level_text.render(text, True, color)
        window.blit(text_level2, (x, y))

    names = collection.find({"_id": ObjectId(idusr)})
    for namess in names:
        level1 = namess["level1"].split()
        level2 = namess["level2"].split()
        level3 = namess["level3"].split()
        level4 = namess["level4"].split()
        level5 = namess["level5"].split()
        level6 = namess["level6"].split()

    while True:
        ly = 157
        for eventsL in pg.event.get():
            if eventsL.type == pg.QUIT:
                quit_game()
            posL = pg.mouse.get_pos()
            if posL[0] < 23 and posL[1] < 23 or posL[0] > 24 and posL[0] < 75 and posL[1] < 24 and posL[1] > -1 or posL[0] > 95 and posL[0] < 145 and posL[1] > 135 and posL[1] < 185 or posL[0] > 184 and posL[0] < 235 and posL[1] > 135 and posL[1] < 185 or posL[0] > 275 and posL[0] < 325 and posL[1] > 135 and posL[1] < 185 or posL[0] > 365 and posL[0] < 415 and posL[1] > 135 and posL[1] < 185 or posL[0] > 455 and posL[0] < 504 and posL[1] > 135 and posL[1] < 185 or posL[0] > 545 and posL[0] < 595 and posL[1] > 135 and posL[1] < 185 or posL[0] > 125 and posL[0] < 143 and posL[1] > 115 and posL[1] < 128 or posL[0] > 215 and posL[0] < 233 and posL[1] > 115 and posL[1] < 128 or posL[0] > 305 and posL[0] < 323 and posL[1] > 115 and posL[1] < 128 or posL[0] > 395 and posL[0] < 413 and posL[1] > 115 and posL[1] < 128 or posL[0] > 485 and posL[0] < 503 and posL[1] > 115 and posL[1] < 128 or posL[0] > 575 and posL[0] < 593 and posL[1] > 115 and posL[1] < 128:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))
            else:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_ARROW))
            if eventsL.type == pg.MOUSEBUTTONUP:
                if posL[0] < 23 and posL[1] < 23:
                    pg.mouse.set_cursor(
                        pg.cursors.Cursor(pg.SYSTEM_CURSOR_WAIT))
                    menu()
                if posL[0] > 24 and posL[0] < 75 and posL[1] < 24 and posL[1] > -1:
                    Levels_Help()
                if posL[0] > 95 and posL[0] < 145 and posL[1] > 135 and posL[1] < 185:
                    Level_1()
                if posL[0] > 184 and posL[0] < 235 and posL[1] > 135 and posL[1] < 185 and levl_2:
                    Level_2()
                if posL[0] > 275 and posL[0] < 325 and posL[1] > 135 and posL[1] < 185 and levl_3:
                    Level_3()
                if posL[0] > 365 and posL[0] < 415 and posL[1] > 135 and posL[1] < 185 and levl_4:
                    Level_4()
                if posL[0] > 455 and posL[0] < 504 and posL[1] > 135 and posL[1] < 185 and levl_5:
                    Level_5()
                if posL[0] > 545 and posL[0] < 595 and posL[1] > 135 and posL[1] < 185 and levl_6:
                    Level_6()
                if posL[0] > 125 and posL[0] < 143 and posL[1] > 115 and posL[1] < 128:
                    messagebox.showinfo("Jump - Level 1 Highscore Info",
                                        f"Highscore Week : {str(numerize.numerize(int(level1[1])))}\nHighscore All times : {str(numerize.numerize(int(level1[2])))}")
                if posL[0] > 215 and posL[0] < 233 and posL[1] > 115 and posL[1] < 128:
                    messagebox.showinfo("Jump - Level 2 Highscore Info",
                                        f"Highscore Week : {str(numerize.numerize(int(level2[1])))}\nHighscore All times : {str(numerize.numerize(int(level2[2])))}")
                if posL[0] > 305 and posL[0] < 323 and posL[1] > 115 and posL[1] < 128:
                    messagebox.showinfo("Jump - Level 3 Highscore Info",
                                        f"Highscore Week : {str(numerize.numerize(int(level3[1])))}\nHighscore All times : {str(numerize.numerize(int(level3[2])))}")
                if posL[0] > 395 and posL[0] < 413 and posL[1] > 115 and posL[1] < 128:
                    messagebox.showinfo("Jump - Level 4 Highscore Info",
                                        f"Highscore Week : {str(numerize.numerize(int(level4[1])))}\nHighscore All times : {str(numerize.numerize(int(level4[2])))}")
                if posL[0] > 485 and posL[0] < 503 and posL[1] > 115 and posL[1] < 128:
                    messagebox.showinfo("Jump - Level 5 Highscore Info",
                                        f"Highscore Week : {str(numerize.numerize(int(level5[1])))}\nHighscore All times : {str(numerize.numerize(int(level5[2])))}")
                if posL[0] > 575 and posL[0] < 593 and posL[1] > 115 and posL[1] < 128:
                    messagebox.showinfo("Jump - Level 6 Highscore Info",
                                        f"Highscore Week : {str(numerize.numerize(int(level6[1])))}\nHighscore All times : {str(numerize.numerize(int(level6[2])))}")

        window.fill((224, 224, 224))
        text_text_level("Choose Level", (0, 0, 0), 220, 40, 50)
        pg.draw.rect(window, (0, 0, 0), (95, 136, 50, 50))
        pg.draw.rect(window, (0, 0, 0), (185, 136, 50, 50))
        pg.draw.rect(window, (0, 0, 0), (275, 136, 50, 50))
        pg.draw.rect(window, (0, 0, 0), (365, 136, 50, 50))
        pg.draw.rect(window, (0, 0, 0), (455, 136, 50, 50))
        pg.draw.rect(window, (0, 0, 0), (545, 136, 50, 50))
        pg.draw.rect(window, (172, 172, 172), (0, 0, 23, 23))
        pg.draw.rect(window, (172, 172, 172), (25, 0, 50, 23))

        if eval(level2[0]):
            levl_2 = True
            text_text_level("2", (255, 255, 255), 201, 138, 40)
        else:
            levl_2 = False
            lx = 198
            pg.draw.ellipse(window, "white", (lx+5, ly-16, 15, 40))
            pg.draw.ellipse(window, "black", (lx+7, ly-13, 11, 40))
            pg.draw.rect(window, "white", (lx, ly, 25, 25))
            pg.draw.ellipse(window, "black", (lx+9, ly+9, 7, 7))
            pg.draw.rect(window, "black", (lx+11, ly+14, 3, 5))
        if eval(level3[0]):
            levl_3 = True
            text_text_level("3", (255, 255, 255), 291, 138, 40)
        else:
            levl_3 = False
            lx = 288
            pg.draw.ellipse(window, "white", (lx+5, ly-16, 15, 40))
            pg.draw.ellipse(window, "black", (lx+7, ly-13, 11, 40))
            pg.draw.rect(window, "white", (lx, ly, 25, 25))
            pg.draw.ellipse(window, "black", (lx+9, ly+9, 7, 7))
            pg.draw.rect(window, "black", (lx+11, ly+14, 3, 5))
        if eval(level4[0]):
            levl_4 = True
            text_text_level("4", (255, 255, 255), 382, 138, 40)
        else:
            levl_4 = False
            lx = 378
            pg.draw.ellipse(window, "white", (lx+5, ly-16, 15, 40))
            pg.draw.ellipse(window, "black", (lx+7, ly-13, 11, 40))
            pg.draw.rect(window, "white", (lx, ly, 25, 25))
            pg.draw.ellipse(window, "black", (lx+9, ly+9, 7, 7))
            pg.draw.rect(window, "black", (lx+11, ly+14, 3, 5))
        if eval(level5[0]):
            levl_5 = True
            text_text_level("5", (255, 255, 255), 471, 138, 40)
        else:
            levl_5 = False
            lx = 468
            pg.draw.ellipse(window, "white", (lx+5, ly-16, 15, 40))
            pg.draw.ellipse(window, "black", (lx+7, ly-13, 11, 40))
            pg.draw.rect(window, "white", (lx, ly, 25, 25))
            pg.draw.ellipse(window, "black", (lx+9, ly+9, 7, 7))
            pg.draw.rect(window, "black", (lx+11, ly+14, 3, 5))
        if eval(level6[0]):
            levl_6 = True
            text_text_level("6", (255, 255, 255), 562, 138, 40)
        else:
            levl_6 = False
            lx = 558
            pg.draw.ellipse(window, "white", (lx+5, ly-16, 15, 40))
            pg.draw.ellipse(window, "black", (lx+7, ly-13, 11, 40))
            pg.draw.rect(window, "white", (lx, ly, 25, 25))
            pg.draw.ellipse(window, "black", (lx+9, ly+9, 7, 7))
            pg.draw.rect(window, "black", (lx+11, ly+14, 3, 5))

        text("ⓘ", "black", 128, 110, "segoeuisymbol", 18)
        text("ⓘ", "black", 218, 110, "segoeuisymbol", 18)
        text("ⓘ", "black", 308, 110, "segoeuisymbol", 18)
        text("ⓘ", "black", 398, 110, "segoeuisymbol", 18)
        text("ⓘ", "black", 488, 110, "segoeuisymbol", 18)
        text("ⓘ", "black", 578, 110, "segoeuisymbol", 18)

        text_text_level("<", (0, 0, 0), 5, -1, 20)
        text("HELP", (0, 0, 0), 30, 2, "times", 16)
        text_text_level("1", (255, 255, 255), 110, 138, 40)
        text_text_level("Run", (0, 0, 0), 105, 200, 20)
        text_text_level("Jump", (0, 0, 0), 191, 200, 20)
        text_text_level("Defend", (0, 0, 0), 275, 200, 20)
        text_text_level("Hit", (0, 0, 0), 382, 200, 20)
        text_text_level("Fly", (0, 0, 0), 469, 200, 20)
        text_text_level("Boss", (0, 0, 0), 553, 200, 20)
        text_text_level("More levels Comming Soon...",
                        (97, 81, 81), 215, 280, 25)
        pg.display.update()


def enter_code():
    global idusr
    global collection

    class Entry_Code:
        def __init__(self, x, y, w, h, color):
            self.x = x
            self.y = y
            self.height = h
            self.width = w
            self.color = color

        def place_widget(self):
            pg.draw.rect(window, self.color,
                         (self.x, self.y, self.width, self.height))

        def place_text(self, text):
            font = pg.font.SysFont("comicsansms", self.width+self.height)
            show = font.render(text, True, self.color)
            window.blit(show, (self.x, self.y))

        def place_text_back(self, text):
            font = pg.font.SysFont("helvetica", self.width+self.height)
            show = font.render(text, True, self.color)
            window.blit(show, (self.x, self.y))

        def draw_rect_for_back(self):
            pg.draw.rect(window, self.color,
                         (self.x, self.y, self.width, self.height))

        def Enter_code(self):
            pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_WAIT))
            prize = rd.randint(100, 800)
            names = collection.find({"_id": ObjectId(idusr)})
            for namess in names:
                removing = namess["codes"]
                Available_coins_Main = int(namess["coins"])
                removing = removing.split()
            if Code in removing:
                messagebox.showinfo(
                    "Code - JUMP", f"Yahoo ! You won {prize} coins.")
                removing.remove(Code)
                remaining_codes = " ".join(removing)
                if remaining_codes == "":
                    remaining_codes = "None"
                collection.find_one_and_update(
                    {"_id": ObjectId(idusr)}, {"$set": {"codes": remaining_codes}})
                collection.find_one_and_update(
                    {"_id": ObjectId(idusr)}, {"$set": {"coins": str(Available_coins_Main+prize)}})
            else:
                messagebox.showerror(
                    "Code - JUMP", "Sorry ! The code is invalid.")

    active_color = (224, 224, 224)
    entry_title = Entry_Code((screen_w//2)-75, 20, 20, 10, "black")
    entry1 = Entry_Code(200, 100+55, 300, 55, "black")
    entry_text1 = Entry_Code(215+50, 104+55, 16, 16, (30, 30, 30))
    entry_text2 = Entry_Code(245+50, 104+55, 16, 16, (30, 30, 30))
    entry_text3 = Entry_Code(275+50, 104+55, 16, 16, (30, 30, 30))
    entry_text4 = Entry_Code(305+50, 104+55, 16, 16, (30, 30, 30))
    entry_text5 = Entry_Code(335+50, 104+55, 16, 16, (30, 30, 30))
    entry_text6 = Entry_Code(365+50, 104+55, 16, 16, (30, 30, 30))
    button = Entry_Code(200, 200+25, 300, 50, "black")
    button_text = Entry_Code((screen_w//2)-45, 201.5+25, 16, 16, "white")
    entry_info = Entry_Code((screen_w//2)-200, 80, 20, 7, (50, 50, 50))
    buttonBack = Entry_Code(0, 0, 23, 23, (172, 172, 172))
    buttonBack_text = Entry_Code(5, -1, 10, 10, "black")
    check_code = Entry_Code(None, None, None, None, None)
    nums_only = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    active = False
    word = 1
    text1 = "-"
    text2 = "-"
    text3 = "-"
    text4 = "-"
    text5 = "-"
    text6 = "-"

    while True:
        window.fill((224, 224, 224))
        entry2 = Entry_Code(206, 107+55, 288, 40, active_color)
        for events in pg.event.get():
            pos = pg.mouse.get_pos()
            if events.type == QUIT:
                quit_game()
            if pos[0] > 206 and pos[0] < 495 and pos[1] > 162 and pos[1] < 201:
                pg.mouse.set_cursor(
                    pg.cursors.Cursor(pg.SYSTEM_CURSOR_IBEAM))
            elif pos[0] < 23 and pos[1] < 23 or pos[0] > 200 and pos[0] < 500 and pos[1] > 225 and pos[1] < 273:
                pg.mouse.set_cursor(
                    pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))
            else:
                pg.mouse.set_cursor(
                    pg.cursors.Cursor(pg.SYSTEM_CURSOR_ARROW))
            if events.type == pg.MOUSEBUTTONDOWN:
                if pos[0] < 23 and pos[1] < 23:
                    Options()
                if pos[0] > 206 and pos[0] < 495 and pos[1] > 162 and pos[1] < 201:
                    active = True
                    active_color = "white"
                else:
                    active = False
                    active_color = (224, 224, 224)
                if pos[0] > 200 and pos[0] < 500 and pos[1] > 225 and pos[1] < 273:
                    Code = text1+text2+text3+text4+text5+text6
                    if "-" not in Code:
                        check_code.Enter_code()
                    else:
                        messagebox.showwarning(
                            "Jump - Code", "Field cannot be empty.")
            if events.type == pg.KEYDOWN:
                if events.key == pg.K_RETURN:
                    Code = text1+text2+text3+text4+text5+text6
                    if "-" not in Code:
                        check_code.Enter_code()
                    else:
                        messagebox.showwarning(
                            "Jump - Code", "Field cannot be empty.")
                key_pressed = pg.key.name(events.key)
                if active:
                    if key_pressed in nums_only or key_pressed in alphabets:
                        if word == 1:
                            text1 = key_pressed
                        elif word == 2:
                            text2 = key_pressed
                        elif word == 3:
                            text3 = key_pressed
                        elif word == 4:
                            text4 = key_pressed
                        elif word == 5:
                            text5 = key_pressed
                        elif word == 6:
                            text6 = key_pressed
                        word += 1
                        if word > 6:
                            word = 7
                    if key_pressed == "backspace":
                        if word == 2:
                            text1 = "-"
                        elif word == 3:
                            text2 = "-"
                        elif word == 4:
                            text3 = "-"
                        elif word == 5:
                            text4 = "-"
                        elif word == 6:
                            text5 = "-"
                        elif word == 7:
                            text6 = "-"
                        word -= 1
                        if word < 1:
                            word = 1

        entry_title.place_text("Win Prize")
        entry1.place_widget()
        entry2.place_widget()
        entry_text1.place_text(text1)
        entry_text2.place_text(text2)
        entry_text3.place_text(text3)
        entry_text4.place_text(text4)
        entry_text5.place_text(text5)
        entry_text6.place_text(text6)
        button.place_widget()
        button_text.place_text("Check")
        entry_info.place_text("Enter 6-digit Code to win prize.")
        buttonBack.draw_rect_for_back()
        buttonBack_text.place_text_back("<")
        pg.display.update()


def Character_menu():
    global selected
    global selected1
    global selected2
    global selected3
    global selected4
    global selected5
    global selected6
    global once_per_start_m4
    global idusr
    black_m1 = (0, 0, 0)
    green_m2 = (0, 130, 0)
    pink_m3 = (227, 0, 193)
    once_per_start_m4 = rd.choice(
        ((254, 234, 0), (159, 32, 164), (57, 121, 42), (96, 59, 44)))
    once_every_sec_m5 = rd.choice(
        ((57, 217, 218), (57, 217, 103), (211, 135, 249), (96, 59, 44)))
    error_unsufficient_coins = "You do not have sufficient amount of coins for this character."
    owned = "Owned"
    eqipped = "Equipped"
    dict_i = {2: 500, 3: 1200, 4: 2700, 5: 5500, 6: 13000}
    price_2, price_3, price_4, price_5, price_6 = f"$ {dict_i[2]}", f"$ {dict_i[3]}", f"$ {dict_i[4]}", f"$ {dict_i[5]}", f"$ {dict_i[6]}"
    text_color = "black"
    text_to_display1, text_to_display2, text_to_display3, text_to_display4, text_to_display5, text_to_display6 = None, None, None, None, None, None
    sec_1 = 0
    clock = pg.time.Clock()
    fps = 35

    class Player_Models:
        def __init__(self, x_axis, y_axis):
            self.x = x_axis
            self.y = y_axis
            self.w = 22
            self.h = 50

        def draw_player(self, color):
            pg.draw.rect(window, color, (self.x, self.y, self.w, self.h))

    model1 = Player_Models(148, 110)
    model2 = Player_Models(345, 110)
    model3 = Player_Models(542, 110)
    model4 = Player_Models(148, 270)
    model5 = Player_Models(345, 270)
    model6 = Player_Models(542, 270)

    def text(text, x, y, color, family, size):
        font = pg.font.SysFont(family, size)
        rndFONT = font.render(text, True, color)
        window.blit(rndFONT, (x, y))

    def buyChar(fileNumber):
        pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_WAIT))
        coins_to_deduct_from_db = coins_owned-dict_i[fileNumber]
        collection.find_one_and_update(
            {"_id": ObjectId(idusr)}, {"$set": {"coins": str(coins_to_deduct_from_db)}})
        collection.find_one_and_update(
            {"_id": ObjectId(idusr)}, {"$set": {"coins": str(coins_to_deduct_from_db)}})
        if fileNumber == 2:
            collection.find_one_and_update(
                {"_id": ObjectId(idusr)}, {"$set": {"skin2": True}})
        if fileNumber == 3:
            collection.find_one_and_update(
                {"_id": ObjectId(idusr)}, {"$set": {"skin3": True}})
        if fileNumber == 4:
            collection.find_one_and_update(
                {"_id": ObjectId(idusr)}, {"$set": {"skin4": True}})
        if fileNumber == 5:
            collection.find_one_and_update(
                {"_id": ObjectId(idusr)}, {"$set": {"skin5": True}})
        if fileNumber == 6:
            collection.find_one_and_update(
                {"_id": ObjectId(idusr)}, {"$set": {"skin6": True}})

    while True:
        names = collection.find({"_id": ObjectId(idusr)})
        for namess in names:
            Available_coins = str(numerize.numerize(int(namess["coins"])))
            Available_coins_Main = int(namess["coins"])
            skin2 = namess["skin2"]
            skin3 = namess["skin3"]
            skin4 = namess["skin4"]
            skin5 = namess["skin5"]
            skin6 = namess["skin6"]
        coins_owned = Available_coins_Main
        random5_m6 = rd.choice(((255, 0, 0), (0, 255, 0), (0, 0, 255)))
        if sec_1 > 30:
            once_every_sec_m5 = rd.choice(
                ((57, 217, 218), (57, 217, 103), (211, 135, 249), (96, 59, 44)))
            sec_1 = 0
        window.fill((224, 224, 224))
        for events in pg.event.get():
            if events.type == pg.QUIT:
                quit_game()
            pos = pg.mouse.get_pos()
            if pos[0] < 23 and pos[1] < 23 or pos[0] > 25 and pos[1] > -1 and pos[0] < 48 and pos[1] < 24 or pos[0] > 107 and pos[0] < 211 and pos[1] > 87 and pos[1] < 215 or pos[0] > 303 and pos[0] < 407 and pos[1] > 87 and pos[1] < 215 or pos[0] > 499 and pos[0] < 602 and pos[1] > 87 and pos[1] < 215 or pos[0] > 107 and pos[0] < 211 and pos[1] > 250 and pos[1] < 373 or pos[0] > 303 and pos[0] < 407 and pos[1] > 250 and pos[1] < 373 or pos[0] > 499 and pos[0] < 602 and pos[1] > 250 and pos[1] < 373:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))
            else:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_ARROW))
            if events.type == MOUSEBUTTONDOWN:
                if pos[0] < 23 and pos[1] < 23:
                    Options()
                if pos[0] > 25 and pos[1] > -1 and pos[0] < 48 and pos[1] < 24:
                    messagebox.showinfo(
                        "Characters info - Jump", "1. Default solid black.\n2. Solid Dark Green.\n3. Solid Dark Pink.\n4. Changes color at the begning of each level.\n5. Change color after 5 seconds.\n6. Changes color dynamically.")
                if pos[0] > 107 and pos[0] < 211 and pos[1] > 87 and pos[1] < 215:
                    selected = selected1
                if pos[0] > 303 and pos[0] < 407 and pos[1] > 87 and pos[1] < 215:
                    if skin2:
                        selected = selected2
                    else:
                        if coins_owned >= dict_i[2]:
                            buyChar(2)
                        else:
                            messagebox.showerror(
                                "Peyment Unsuccessfull - Jump", error_unsufficient_coins)
                if pos[0] > 499 and pos[0] < 602 and pos[1] > 87 and pos[1] < 215:
                    if skin3:
                        selected = selected3
                    else:
                        if coins_owned >= dict_i[3]:
                            buyChar(3)
                        else:
                            messagebox.showerror(
                                "Peyment Unsuccessfull - Jump", error_unsufficient_coins)
                if pos[0] > 107 and pos[0] < 211 and pos[1] > 250 and pos[1] < 373:
                    if skin4:
                        selected = selected4
                    else:
                        if coins_owned >= dict_i[4]:
                            buyChar(4)
                        else:
                            messagebox.showerror(
                                "Peyment Unsuccessfull - Jump", error_unsufficient_coins)
                if pos[0] > 303 and pos[0] < 407 and pos[1] > 250 and pos[1] < 373:
                    if skin5:
                        selected = selected5
                    else:
                        if coins_owned >= dict_i[5]:
                            buyChar(5)
                        else:
                            messagebox.showerror(
                                "Peyment Unsuccessfull - Jump", error_unsufficient_coins)
                if pos[0] > 499 and pos[0] < 602 and pos[1] > 250 and pos[1] < 373:
                    if skin6:
                        selected = selected6
                    else:
                        if coins_owned >= dict_i[6]:
                            buyChar(6)
                        else:
                            messagebox.showerror(
                                "Peyment Unsuccessfull - Jump", error_unsufficient_coins)

        if selected is selected1:
            text_to_display1 = eqipped
            textx1, texty1 = 130, 180
        else:
            text_to_display1 = owned
            textx1, texty1 = 137, 180
        if selected is selected2:
            text_to_display2 = eqipped
            textx2, texty2 = 326, 180
        else:
            if skin2:
                text_to_display2 = owned
                textx2, texty2 = 334, 180
            else:
                text_to_display2 = price_2
                textx2, texty2 = 336, 180
        if selected is selected3:
            text_to_display3 = eqipped
            textx3, texty3 = 524, 180
        else:
            if skin3:
                text_to_display3 = owned
                textx3, texty3 = 531, 180
            else:
                text_to_display3 = price_3
                textx3, texty3 = 529, 180
        if selected is selected4:
            text_to_display4 = eqipped
            textx4, texty4 = 130, 340
        else:
            if skin4:
                text_to_display4 = owned
                textx4, texty4 = 137, 340
            else:
                text_to_display4 = price_4
                textx4, texty4 = 134, 340
        if selected is selected5:
            text_to_display5 = eqipped
            textx5, texty5 = 326, 340
        else:
            if skin5:
                text_to_display5 = owned
                textx5, texty5 = 334, 340
            else:
                text_to_display5 = price_5
                textx5, texty5 = 332, 340
        if selected is selected6:
            text_to_display6 = eqipped
            textx6, texty6 = 524, 340
        else:
            if skin6:
                text_to_display6 = owned
                textx6, texty6 = 531, 340
            else:
                text_to_display6 = price_6
                textx6, texty6 = 524, 340

        CharPlayer = random5_m6
        pg.draw.rect(window, (177, 177, 177),
                     (selected[0], selected[1], 105, 129))
        text(f"Coins : {str(Available_coins)}", screen_w -
             (83+len(str(Available_coins))*13), 2, (30, 30, 30), "comicsansms", 22)
        text("Characters", (screen_w//2)-80, 30, "black", "comicsansms", 30)
        pg.draw.rect(window, (172, 172, 172), (0, 0, 23, 23))
        text("<", 5, -1, "black", "helvetica", 20)
        pg.draw.rect(window, (172, 172, 172), (25, 0, 23, 23))
        text("ⓘ", 28, -3, "black", "segoeuisymbol", 20)
        model1.draw_player(black_m1)
        model2.draw_player(green_m2)
        model3.draw_player(pink_m3)
        model4.draw_player(once_per_start_m4)
        model5.draw_player(once_every_sec_m5)
        model6.draw_player(random5_m6)
        text(text_to_display1, textx1, texty1, text_color, "helvatica", 20)
        text(text_to_display2, textx2, texty2, text_color, "helvatica", 20)
        text(text_to_display3, textx3, texty3, text_color, "helvatica", 20)
        text(text_to_display4, textx4, texty4, text_color, "helvatica", 20)
        text(text_to_display5, textx5, texty5, text_color, "helvatica", 20)
        text(text_to_display6, textx6, texty6, text_color, "helvatica", 20)
        sec_1 += 1
        pg.display.update()
        clock.tick(fps)


def leaderboard_week():
    global show_leaderBoard_winner
    names = collection.find({"_id": ObjectId(idusr)})
    for namess in names:
        current_user_name = namess["name"]
        current_user_highscore = str(
            numerize.numerize(namess["highscore_week"]))
        Available_coins_Main = int(namess["coins"])
        leaderBoard_prize_availed_not = namess["leaderboard_prize"]
    clock = pg.time.Clock()
    req = Request("http://todays-date.net")
    html_page = urlopen(req)
    soup = BeautifulSoup(html_page, "html.parser")
    html_text = soup.get_text()
    html_text = html_text.split()
    day_today = html_text[4].replace(",", "").lower()
    days = {"monday": 0, "tuesday": 1, "wednesday": 2,
            "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}
    date = 7 - days[day_today]
    # day_today = calendar.day_name[date.weekday()]
    list_of_top_players = list(collection.find().sort(
        "highscore_All_times", DESCENDING))
    current_user_rank = next((index for (index, d) in enumerate(
        list_of_top_players) if d["name"] == MainName), None)+1

    try:
        name1 = list_of_top_players[0]["name"]
    except IndexError:
        name1 = "None"
    try:
        name2 = list_of_top_players[1]["name"]
    except IndexError:
        name2 = "None"
    try:
        name3 = list_of_top_players[2]["name"]
    except IndexError:
        name3 = "None"
    try:
        name4 = list_of_top_players[3]["name"]
    except IndexError:
        name4 = "None"
    try:
        name5 = list_of_top_players[4]["name"]
    except IndexError:
        name5 = "None"
    try:
        name6 = list_of_top_players[5]["name"]
    except IndexError:
        name6 = "None"
    try:
        name7 = list_of_top_players[6]["name"]
    except IndexError:
        name7 = "None"
    try:
        name8 = list_of_top_players[7]["name"]
    except IndexError:
        name8 = "None"
    try:
        name9 = list_of_top_players[8]["name"]
    except IndexError:
        name9 = "None"
    try:
        name10 = list_of_top_players[9]["name"]
    except IndexError:
        name10 = "None"
    try:
        Highscore_1 = str(numerize.numerize(
            int(list_of_top_players[0]["highscore_week"])))
    except IndexError:
        Highscore_1 = "-:-"
    try:
        Highscore_2 = str(numerize.numerize(
            int(list_of_top_players[1]["highscore_week"])))
    except IndexError:
        Highscore_2 = "-:-"
    try:
        Highscore_3 = str(numerize.numerize(
            int(list_of_top_players[2]["highscore_week"])))
    except IndexError:
        Highscore_3 = "-:-"
    try:
        Highscore_4 = str(numerize.numerize(
            int(list_of_top_players[3]["highscore_week"])))
    except IndexError:
        Highscore_4 = "-:-"
    try:
        Highscore_5 = str(numerize.numerize(
            int(list_of_top_players[4]["highscore_week"])))
    except IndexError:
        Highscore_5 = "-:-"
    try:
        Highscore_6 = str(numerize.numerize(
            int(list_of_top_players[5]["highscore_week"])))
    except IndexError:
        Highscore_6 = "-:-"
    try:
        Highscore_7 = str(numerize.numerize(
            int(list_of_top_players[6]["highscore_week"])))
    except IndexError:
        Highscore_7 = "-:-"
    try:
        Highscore_8 = str(numerize.numerize(
            int(list_of_top_players[7]["highscore_week"])))
    except IndexError:
        Highscore_8 = "-:-"
    try:
        Highscore_9 = str(numerize.numerize(
            int(list_of_top_players[8]["highscore_week"])))
    except IndexError:
        Highscore_9 = "-:-"
    try:
        Highscore_10 = str(numerize.numerize(
            int(list_of_top_players[9]["highscore_week"])))
    except IndexError:
        Highscore_10 = "-:-"

    while True:
        window.fill((224, 224, 224))
        for events in pg.event.get():
            pos = pg.mouse.get_pos()
            if events.type == QUIT:
                quit_game()
            if pos[0] < 23 and pos[1] < 23 or pos[0] > 25 and pos[1] > -1 and pos[0] < 48 and pos[1] < 24 or pos[0] > 351 and pos[1] > 5 and pos[0] < 427 and pos[1] < 27:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))
            else:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_ARROW))
            if events.type == MOUSEBUTTONDOWN:
                if pos[0] < 23 and pos[1] < 23:
                    Options()
                if pos[0] > 351 and pos[1] > 5 and pos[0] < 427 and pos[1] < 27:
                    pg.mouse.set_cursor(
                        pg.cursors.Cursor(pg.SYSTEM_CURSOR_WAIT))
                    leaderboard_all_Times()
                if pos[0] > 25 and pos[1] > -1 and pos[0] < 48 and pos[1] < 24:
                    messagebox.showinfo(
                        "Leaderboard info - Jump", "Ranking :-\nPlayers from all over the world are based on their highscore made in all levels. Top 10 players are shown.\n\nTimer :-\nAt the end of week Top 10 players would get prize coins according to their rank.\n\nPrize :-\n#1 => 5,000\n#2 => 3,500\n#3 => 1,800\n#4-6 => 750\n#7-10 => 500\n\nHighscores are reseted to 0 at the end of week.")

        if show_leaderBoard_winner == 15:
            if date == 7:
                if not leaderBoard_prize_availed_not:
                    if current_user_rank == 1:
                        messagebox.showinfo(
                            "Jump - Winner", "Congratulations for placing on #1. You win $ 5000.")
                        leaderboard_prize = 5000
                    if current_user_rank == 2:
                        messagebox.showinfo(
                            "Jump - Winner", "Congratulations for placing on #2. You win $ 3500.")
                        leaderboard_prize = 3500
                    if current_user_rank == 3:
                        messagebox.showinfo(
                            "Jump - Winner", "Congratulations for placing on #3. You win $ 1800.")
                        leaderboard_prize = 1800
                    if current_user_rank >= 4 and current_user_rank <= 6:
                        messagebox.showinfo(
                            "Jump - Winner", f"Congratulations for placing on #{current_user_rank}. You win $ 750.")
                        leaderboard_prize = 750
                    if current_user_rank >= 7 and current_user_rank <= 10:
                        messagebox.showinfo(
                            "Jump - Winner", f"Congratulations for placing on #{current_user_rank}. You win $ 500.")
                        leaderboard_prize = 500
                    collection.find_one_and_update(
                        {"_id": ObjectId(idusr)}, {"$set": {"coins": str(Available_coins_Main+leaderboard_prize)}})
                    collection.find_one_and_update(
                        {"_id": ObjectId(idusr)}, {"$set": {"leaderboard_prize": True}})
                    collection.find_one_and_update(
                        {"_id": ObjectId(idusr)}, {"$set": {"highscore_week": 0}})
            elif date != 0:
                collection.find_one_and_update(
                    {"_id": ObjectId(idusr)}, {"$set": {"leaderboard_prize": False}})

        text(f"Time left : {date} days", "black",
             screen_w-146, 4,  "comicsansms", 15)
        pg.draw.rect(window, (172, 172, 172), (0, 0, 23, 23))
        text("<", "black", 5, -1,  "helvetica", 20)
        pg.draw.rect(window, (172, 172, 172), (25, 0, 23, 23))
        text("ⓘ", "black", 28, -3,  "segoeuisymbol", 20)
        pg.draw.rect(window, (150, 150, 150), (265, 6, 81, 21))
        text("This Week | All Times", "black",
             screen_w/2.6, 5,  "comicsansms", 15)
        pg.draw.rect(window, "black", (25, 32, 650, 25))
        pg.draw.rect(window, "gray", (25, 80-16, 650, 25))
        pg.draw.rect(window, "gray", (25, 110-16, 650, 25))
        pg.draw.rect(window, "gray", (25, 140-16, 650, 25))
        pg.draw.rect(window, "gray", (25, 170-16, 650, 25))
        pg.draw.rect(window, "gray", (25, 200-16, 650, 25))
        pg.draw.rect(window, "gray", (25, 230-16, 650, 25))
        pg.draw.rect(window, "gray", (25, 260-16, 650, 25))
        pg.draw.rect(window, "gray", (25, 290-16, 650, 25))
        pg.draw.rect(window, "gray", (25, 320-16, 650, 25))
        pg.draw.rect(window, "gray", (25, 350-16, 650, 25))
        pg.draw.rect(window, (90, 90, 90), (25, screen_h-32, 650, 25))
        text("Rank", (224, 224, 224), 40, 33, "comicsansms", 15)
        text("Username", (224, 224, 224), 120, 33, "comicsansms", 15)
        text("Highscore", (224, 224, 224), 540, 33, "comicsansms", 15)
        text("1", "black", 50, 66, "comicsansms", 15)
        text("2", "black", 50, 96, "comicsansms", 15)
        text("3", "black", 50, 126, "comicsansms", 15)
        text("4", "black", 50, 156, "comicsansms", 15)
        text("5", "black", 50, 186, "comicsansms", 15)
        text("6", "black", 50, 216, "comicsansms", 15)
        text("7", "black", 50, 246, "comicsansms", 15)
        text("8", "black", 50, 276, "comicsansms", 15)
        text("9", "black", 50, 306, "comicsansms", 15)
        text("10", "black", 45, 336, "comicsansms", 15)
        text(str(current_user_rank), "white", 45,
             369, "comicsansms", 15)  # Current User
        text(name1, "black", 125, 66, "comicsansms", 15)
        text(name2, "black", 125, 96, "comicsansms", 15)
        text(name3, "black", 125, 126, "comicsansms", 15)
        text(name4, "black", 125, 156, "comicsansms", 15)
        text(name5, "black", 125, 186, "comicsansms", 15)
        text(name6, "black", 125, 216, "comicsansms", 15)
        text(name7, "black", 125, 246, "comicsansms", 15)
        text(name8, "black", 125, 276, "comicsansms", 15)
        text(name9, "black", 125, 306, "comicsansms", 15)
        text(name10, "black", 125, 336, "comicsansms", 15)
        text(current_user_name, "white", 125, 369,
             "comicsansms", 15)  # Current User
        text(Highscore_1, "black", 555, 66, "comicsansms", 15)
        text(Highscore_2, "black", 555, 96, "comicsansms", 15)
        text(Highscore_3, "black", 555, 126, "comicsansms", 15)
        text(Highscore_4, "black", 555, 156, "comicsansms", 15)
        text(Highscore_5, "black", 555, 186, "comicsansms", 15)
        text(Highscore_6, "black", 555, 216, "comicsansms", 15)
        text(Highscore_7, "black", 555, 246, "comicsansms", 15)
        text(Highscore_8, "black", 555, 276, "comicsansms", 15)
        text(Highscore_9, "black", 555, 306, "comicsansms", 15)
        text(Highscore_10, "black", 555, 336, "comicsansms", 15)
        text(current_user_highscore, "white", 555, 369,
             "comicsansms", 15)  # Current User
        show_leaderBoard_winner += 1
        pg.display.update()
        clock.tick(30)


def leaderboard_all_Times():
    names = collection.find({"_id": ObjectId(idusr)})
    for namess in names:
        current_user_name = namess["name"]
        current_user_highscore = str(
            numerize.numerize(namess["highscore_All_times"]))
        rank_leaderboard_alltime = namess["rank_all_time"]
    clock = pg.time.Clock()
    list_of_top_players = list(collection.find().sort(
        "highscore_All_times", DESCENDING))
    current_user_rank = next((index for (index, d) in enumerate(
        list_of_top_players) if d["name"] == MainName), None)+1

    try:
        name1 = list_of_top_players[0]["name"]
    except IndexError:
        name1 = "None"
    try:
        name2 = list_of_top_players[1]["name"]
    except IndexError:
        name2 = "None"
    try:
        name3 = list_of_top_players[2]["name"]
    except IndexError:
        name3 = "None"
    try:
        name4 = list_of_top_players[3]["name"]
    except IndexError:
        name4 = "None"
    try:
        name5 = list_of_top_players[4]["name"]
    except IndexError:
        name5 = "None"
    try:
        name6 = list_of_top_players[5]["name"]
    except IndexError:
        name6 = "None"
    try:
        name7 = list_of_top_players[6]["name"]
    except IndexError:
        name7 = "None"
    try:
        name8 = list_of_top_players[7]["name"]
    except IndexError:
        name8 = "None"
    try:
        name9 = list_of_top_players[8]["name"]
    except IndexError:
        name9 = "None"
    try:
        name10 = list_of_top_players[9]["name"]
    except IndexError:
        name10 = "None"
    try:
        Highscore_1 = str(numerize.numerize(
            int(list_of_top_players[0]["highscore_All_times"])))
    except IndexError:
        Highscore_1 = "-:-"
    try:
        Highscore_2 = str(numerize.numerize(
            int(list_of_top_players[1]["highscore_All_times"])))
    except IndexError:
        Highscore_2 = "-:-"
    try:
        Highscore_3 = str(numerize.numerize(
            int(list_of_top_players[2]["highscore_All_times"])))
    except IndexError:
        Highscore_3 = "-:-"
    try:
        Highscore_4 = str(numerize.numerize(
            int(list_of_top_players[3]["highscore_All_times"])))
    except IndexError:
        Highscore_4 = "-:-"
    try:
        Highscore_5 = str(numerize.numerize(
            int(list_of_top_players[4]["highscore_All_times"])))
    except IndexError:
        Highscore_5 = "-:-"
    try:
        Highscore_6 = str(numerize.numerize(
            int(list_of_top_players[5]["highscore_All_times"])))
    except IndexError:
        Highscore_6 = "-:-"
    try:
        Highscore_7 = str(numerize.numerize(
            int(list_of_top_players[6]["highscore_All_times"])))
    except IndexError:
        Highscore_7 = "-:-"
    try:
        Highscore_8 = str(numerize.numerize(
            int(list_of_top_players[7]["highscore_All_times"])))
    except IndexError:
        Highscore_8 = "-:-"
    try:
        Highscore_9 = str(numerize.numerize(
            int(list_of_top_players[8]["highscore_All_times"])))
    except IndexError:
        Highscore_9 = "-:-"
    try:
        Highscore_10 = str(numerize.numerize(
            int(list_of_top_players[9]["highscore_All_times"])))
    except IndexError:
        Highscore_10 = "-:-"

    rank_leaderboard_alltime = current_user_rank
    collection.find_one_and_update({"_id": ObjectId(idusr)}, {
                                   "$set": {"rank_all_time": rank_leaderboard_alltime}})

    while True:
        window.fill((224, 224, 224))
        for events in pg.event.get():
            pos = pg.mouse.get_pos()
            if events.type == QUIT:
                quit_game()
            if pos[0] < 23 and pos[1] < 23 or pos[0] > 25 and pos[1] > -1 and pos[0] < 48 and pos[1] < 24 or pos[0] > 263 and pos[1] > 5 and pos[0] < 344 and pos[1] < 27:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))
            else:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_ARROW))
            if events.type == MOUSEBUTTONDOWN:
                if pos[0] < 23 and pos[1] < 23:
                    Options()
                if pos[0] > 263 and pos[1] > 5 and pos[0] < 344 and pos[1] < 27:
                    pg.mouse.set_cursor(
                        pg.cursors.Cursor(pg.SYSTEM_CURSOR_WAIT))
                    leaderboard_week()
                if pos[0] > 25 and pos[1] > -1 and pos[0] < 48 and pos[1] < 24:
                    messagebox.showinfo(
                        "Leaderboard info - Jump", "Ranking :-\nPlayers from all over the world are based on their highscore made in all levels. Top 10 players are shown.\n\nRanks :-\nTop 10 players would get Rank on their profile according to their position on leaderboard.\n\nHighscores are not reset at the end of week.")

        pg.draw.rect(window, (172, 172, 172), (0, 0, 23, 23))
        text("<", "black", 5, -1,  "helvetica", 20)
        pg.draw.rect(window, (172, 172, 172), (25, 0, 23, 23))
        text("ⓘ", "black", 28, -3,  "segoeuisymbol", 20)
        pg.draw.rect(window, (150, 150, 150), (353.5, 6, 74, 21))
        text("This Week | All Times", "black",
             screen_w/2.6, 5,  "comicsansms", 15)
        pg.draw.rect(window, "black", (25, 32, 650, 25))
        pg.draw.rect(window, "gray", (25, 80-16, 650, 25))
        pg.draw.rect(window, "gray", (25, 110-16, 650, 25))
        pg.draw.rect(window, "gray", (25, 140-16, 650, 25))
        pg.draw.rect(window, "gray", (25, 170-16, 650, 25))
        pg.draw.rect(window, "gray", (25, 200-16, 650, 25))
        pg.draw.rect(window, "gray", (25, 230-16, 650, 25))
        pg.draw.rect(window, "gray", (25, 260-16, 650, 25))
        pg.draw.rect(window, "gray", (25, 290-16, 650, 25))
        pg.draw.rect(window, "gray", (25, 320-16, 650, 25))
        pg.draw.rect(window, "gray", (25, 350-16, 650, 25))
        pg.draw.rect(window, (90, 90, 90), (25, screen_h-32, 650, 25))
        text("Rank", (224, 224, 224), 40, 33, "comicsansms", 15)
        text("Username", (224, 224, 224), 120, 33, "comicsansms", 15)
        text("Highscore", (224, 224, 224), 540, 33, "comicsansms", 15)
        text("1", "black", 50, 66, "comicsansms", 15)
        text("2", "black", 50, 96, "comicsansms", 15)
        text("3", "black", 50, 126, "comicsansms", 15)
        text("4", "black", 50, 156, "comicsansms", 15)
        text("5", "black", 50, 186, "comicsansms", 15)
        text("6", "black", 50, 216, "comicsansms", 15)
        text("7", "black", 50, 246, "comicsansms", 15)
        text("8", "black", 50, 276, "comicsansms", 15)
        text("9", "black", 50, 306, "comicsansms", 15)
        text("10", "black", 45, 336, "comicsansms", 15)
        text(str(current_user_rank), "white", 45,
             369, "comicsansms", 15)  # Current User
        text(name1, "black", 125, 66, "comicsansms", 15)
        text(name2, "black", 125, 96, "comicsansms", 15)
        text(name3, "black", 125, 126, "comicsansms", 15)
        text(name4, "black", 125, 156, "comicsansms", 15)
        text(name5, "black", 125, 186, "comicsansms", 15)
        text(name6, "black", 125, 216, "comicsansms", 15)
        text(name7, "black", 125, 246, "comicsansms", 15)
        text(name8, "black", 125, 276, "comicsansms", 15)
        text(name9, "black", 125, 306, "comicsansms", 15)
        text(name10, "black", 125, 336, "comicsansms", 15)
        text(current_user_name, "white", 125, 369,
             "comicsansms", 15)  # Current User
        text(Highscore_1, "black", 555, 66, "comicsansms", 15)
        text(Highscore_2, "black", 555, 96, "comicsansms", 15)
        text(Highscore_3, "black", 555, 126, "comicsansms", 15)
        text(Highscore_4, "black", 555, 156, "comicsansms", 15)
        text(Highscore_5, "black", 555, 186, "comicsansms", 15)
        text(Highscore_6, "black", 555, 216, "comicsansms", 15)
        text(Highscore_7, "black", 555, 246, "comicsansms", 15)
        text(Highscore_8, "black", 555, 276, "comicsansms", 15)
        text(Highscore_9, "black", 555, 306, "comicsansms", 15)
        text(Highscore_10, "black", 555, 336, "comicsansms", 15)
        text(current_user_highscore, "white", 555, 369,
             "comicsansms", 15)  # Current User
        pg.display.update()
        clock.tick(30)


def Options():
    class Buttons:
        def bg_rect(self, x, y):
            pg.draw.rect(window, "black", (x, y, 200, 50))

        def text(self, text, x, y, size, color):
            font = pg.font.SysFont("helvetica", size)
            rndFONT = font.render(text, True, color)
            window.blit(rndFONT, (x, y))

    button = Buttons()
    bx1, by1 = 150, 120
    bx2, by2 = 350, 290
    tx1, ty1 = 180, 126
    tx2, ty2 = 364, 298
    Option_Click = False
    Vx1, Vx2, Vx3, Vx4 = 5, 5, 5, 5
    clock = pg.time.Clock()

    while True:
        window.fill((224, 224, 224))
        for events in pg.event.get():
            pos = pg.mouse.get_pos()
            if events.type == QUIT:
                quit_game()
            if (pos[0] < 23 and pos[1] < 23 or pos[0] > 250 and pos[0] < 450 and pos[1] > 120 and pos[1] < 170 or pos[0] > 250 and pos[0] < 450 and pos[1] > 205 and pos[1] < 255 or pos[0] > 250 and pos[0] < 450 and pos[1] > 290 and pos[1] < 340) and Option_Click:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))
            else:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_ARROW))
            if events.type == MOUSEBUTTONDOWN:
                if pos[0] < 23 and pos[1] < 23:
                    menu()
                if pos[0] > 250 and pos[0] < 450 and pos[1] > 120 and pos[1] < 170 and Option_Click:
                    More()
                if pos[0] > 250 and pos[0] < 450 and pos[1] > 205 and pos[1] < 255 and Option_Click:
                    pg.mouse.set_cursor(
                        pg.cursors.Cursor(pg.SYSTEM_CURSOR_WAIT))
                    leaderboard_week()
                if pos[0] > 250 and pos[0] < 450 and pos[1] > 290 and pos[1] < 340 and Option_Click:
                    Settings()

        bx1 += Vx1
        bx2 -= Vx2
        tx1 += Vx3
        tx2 -= Vx4
        if bx1 == 250:
            Vx1 = 0
            Option_Click = True
        if bx2 == 250:
            Vx2 = 0
            Option_Click = True
        if tx1 > 275:
            Vx3 = 0
            Option_Click = True
        if tx2 < 269:
            Vx4 = 0
            Option_Click = True

        button.bg_rect(bx1, by1)
        button.bg_rect(250, 205)
        button.bg_rect(bx2, by2)
        pg.draw.rect(window, (172, 172, 172), (0, 0, 23, 23))
        button.text("<", 5, -1, 20, "black")
        button.text("OPTIONS", (screen_w//2)-92, 30, 50, "black")
        button.text("M . O . R . E", tx1, ty1, 30, "white")
        button.text("L E A D E R B O A R D", 263, 218, 20, "white")
        button.text("S E T T I N G S", tx2, ty2, 30, "white")
        pg.display.update()
        clock.tick(30)


def More():
    class Buttons:
        def bg_rect(self, x, y):
            pg.draw.rect(window, "black", (x, y, 200, 50))

        def text(self, text, x, y, size, color):
            font = pg.font.SysFont("helvetica", size)
            rndFONT = font.render(text, True, color)
            window.blit(rndFONT, (x, y))

    button = Buttons()
    bx1, by1 = 150, 120
    bx2, by2 = 350, 290
    tx1, ty1 = 177, 126
    tx2, ty2 = 364, 300
    Option_Click = False
    Vx1, Vx2, Vx3, Vx4 = 5, 5, 5, 5
    clock = pg.time.Clock()

    while True:
        window.fill((224, 224, 224))
        for events in pg.event.get():
            pos = pg.mouse.get_pos()
            if events.type == QUIT:
                quit_game()
            if (pos[0] < 23 and pos[1] < 23 or pos[0] > 250 and pos[0] < 450 and pos[1] > 120 and pos[1] < 170 or pos[0] > 250 and pos[0] < 450 and pos[1] > 205 and pos[1] < 255 or pos[0] > 250 and pos[0] < 450 and pos[1] > 290 and pos[1] < 340) and Option_Click:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))
            else:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_ARROW))
            if events.type == MOUSEBUTTONDOWN:
                if pos[0] < 23 and pos[1] < 23:
                    Options()
                if pos[0] > 250 and pos[0] < 450 and pos[1] > 120 and pos[1] < 170 and Option_Click:
                    people()
                if pos[0] > 250 and pos[0] < 450 and pos[1] > 205 and pos[1] < 255 and Option_Click:
                    enter_code()
                if pos[0] > 250 and pos[0] < 450 and pos[1] > 290 and pos[1] < 340 and Option_Click:
                    Character_menu()

        bx1 += Vx1
        bx2 -= Vx2
        tx1 += Vx3
        tx2 -= Vx4
        if bx1 == 250:
            Vx1 = 0
            Option_Click = True
        if bx2 == 250:
            Vx2 = 0
            Option_Click = True
        if tx1 > 279:
            Vx3 = 0
            Option_Click = True
        if tx2 < 269:
            Vx4 = 0
            Option_Click = True

        button.bg_rect(bx1, by1)
        button.bg_rect(250, 205)
        button.bg_rect(bx2, by2)
        pg.draw.rect(window, (172, 172, 172), (0, 0, 23, 23))
        button.text("<", 5, -1, 20, "black")
        button.text("MORE", (screen_w//2)-62, 30, 50, "black")
        button.text("P E O P L E", tx1, ty1, 30, "white")
        button.text("C . O . D . E", 280, 211, 30, "white")
        button.text("C H A R A C T E R", tx2, ty2, 25, "white")
        pg.display.update()
        clock.tick(30)


def people():
    global collection

    class Entry_Code:
        def __init__(self, x, y, w, h, color):
            self.x = x
            self.y = y
            self.height = h
            self.width = w
            self.color = color

        def place_widget(self):
            pg.draw.rect(window, self.color,
                         (self.x, self.y, self.width, self.height))

        def place_text(self, text):
            font = pg.font.SysFont("comicsansms", self.width+self.height)
            show = font.render(text, True, self.color)
            window.blit(show, (self.x, self.y))

        def place_text_back(self, text):
            font = pg.font.SysFont("helvetica", self.width+self.height)
            show = font.render(text, True, self.color)
            window.blit(show, (self.x, self.y))

        def draw_rect_for_back(self):
            pg.draw.rect(window, self.color,
                         (self.x, self.y, self.width, self.height))

        def Enter_code(self, name):
            pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_WAIT))
            data = list(collection.find())
            current_name_list_fromDB = []
            for users in data:
                current_name_list_fromDB.append(users["name"])
            if name in current_name_list_fromDB:
                data_of_other_user = collection.find({"name": name})
                for data in data_of_other_user:
                    id_other = str(data["_id"])
                    profile("other", id_other)
            elif name not in current_name_list_fromDB:
                messagebox.askretrycancel(
                    "Jump - Log In", "Account with this username doesn't exist, please try again !")

    active_color = (224, 224, 224)
    entry_title = Entry_Code((screen_w//2)-50, 20, 32, 0, "black")
    entry1 = Entry_Code(200, 100+55, 300, 55, "black")
    entry_text1 = Entry_Code(215+35, 104+55, 16, 16, (30, 30, 30))
    entry_text2 = Entry_Code(245+35, 104+55, 16, 16, (30, 30, 30))
    entry_text3 = Entry_Code(275+35, 104+55, 16, 16, (30, 30, 30))
    entry_text4 = Entry_Code(305+35, 104+55, 16, 16, (30, 30, 30))
    entry_text5 = Entry_Code(335+35, 104+55, 16, 16, (30, 30, 30))
    entry_text6 = Entry_Code(365+35, 104+55, 16, 16, (30, 30, 30))
    entry_text7 = Entry_Code(395+35, 104+55, 16, 16, (30, 30, 30))
    button = Entry_Code(200, 200+25, 300, 50, "black")
    button_text = Entry_Code((screen_w//2)-45, 201.5+25, 16, 16, "white")
    entry_info = Entry_Code((screen_w//2)-150, 94, 17, 0, (5, 5, 5))
    buttonBack = Entry_Code(0, 0, 23, 23, (172, 172, 172))
    buttonBack_text = Entry_Code(5, -1, 10, 10, "black")
    check_code = Entry_Code(None, None, None, None, None)
    nums_only = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    active = False
    word = 1
    text1 = "-"
    text2 = "-"
    text3 = "-"
    text4 = "-"
    text5 = "-"
    text6 = "-"
    text7 = "-"

    while True:
        window.fill((224, 224, 224))
        entry2 = Entry_Code(206, 107+55, 288, 40, active_color)
        for events in pg.event.get():
            pos = pg.mouse.get_pos()
            if events.type == pg.QUIT:
                sys.exit()
            if pos[0] > 206 and pos[0] < 495 and pos[1] > 162 and pos[1] < 201:
                pg.mouse.set_cursor(
                    pg.cursors.Cursor(pg.SYSTEM_CURSOR_IBEAM))
            elif pos[0] < 23 and pos[1] < 23 or pos[0] > 200 and pos[0] < 500 and pos[1] > 225 and pos[1] < 273:
                pg.mouse.set_cursor(
                    pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))
            else:
                pg.mouse.set_cursor(
                    pg.cursors.Cursor(pg.SYSTEM_CURSOR_ARROW))
            if events.type == pg.MOUSEBUTTONDOWN:
                if pos[0] < 23 and pos[1] < 23:
                    More()
                if pos[0] > 206 and pos[0] < 495 and pos[1] > 162 and pos[1] < 201:
                    active = True
                    active_color = "white"
                else:
                    active = False
                    active_color = (224, 224, 224)
                if pos[0] > 200 and pos[0] < 500 and pos[1] > 225 and pos[1] < 273:
                    name = text1+text2+text3+text4+text5+text6+text7
                    check_code.Enter_code(name=name)
            if events.type == pg.KEYDOWN:
                if events.key == pg.K_RETURN:
                    name = text1+text2+text3+text4+text5+text6+text7
                    check_code.Enter_code(name=name)
                key_pressed = pg.key.name(events.key)
                if active:
                    if key_pressed in nums_only or key_pressed in alphabets:
                        if word == 1:
                            text1 = key_pressed
                        elif word == 2:
                            text2 = key_pressed
                        elif word == 3:
                            text3 = key_pressed
                        elif word == 4:
                            text4 = key_pressed
                        elif word == 5:
                            text5 = key_pressed
                        elif word == 6:
                            text6 = key_pressed
                        elif word == 7:
                            text7 = key_pressed
                        word += 1
                        if word > 7:
                            word = 8
                    if key_pressed == "backspace":
                        if word == 2:
                            text1 = "-"
                        elif word == 3:
                            text2 = "-"
                        elif word == 4:
                            text3 = "-"
                        elif word == 5:
                            text4 = "-"
                        elif word == 6:
                            text5 = "-"
                        elif word == 7:
                            text6 = "-"
                        elif word == 8:
                            text7 = "-"
                        word -= 1
                        if word < 1:
                            word = 1

        entry_title.place_text("People")
        entry1.place_widget()
        entry2.place_widget()
        entry_text1.place_text(text1)
        entry_text2.place_text(text2)
        entry_text3.place_text(text3)
        entry_text4.place_text(text4)
        entry_text5.place_text(text5)
        entry_text6.place_text(text6)
        entry_text7.place_text(text7)
        button.place_widget()
        button_text.place_text("Search")
        entry_info.place_text(
            f"Enter username to search for account !")
        buttonBack.draw_rect_for_back()
        buttonBack_text.place_text_back("<")
        pg.display.update()


btmClick = 420
btmClick2 = 420
ConnectvsLout = "Connect"
CvsL = 0


def Settings():
    global btmClick
    global btmClick2
    global ConnectvsLout
    global CvsL

    def text_text_setting(text, color, x, y, size, family):
        font_Level_text = pg.font.SysFont(family, size)
        text_level2 = font_Level_text.render(text, True, color)
        window.blit(text_level2, (x, y))

    def Game_Update():
        text_text_setting("CHECKING", (255, 255, 255), 433, 198, 25, "times")
        try:
            req = Request(
                "https://playwithaayan.000webhostapp.com/game_update.html")
            html_page = urlopen(req)
            soup = BeautifulSoup(html_page, "html.parser")
            html_text = soup.get_text()
            html_text = html_text.split()
            # Here if value is 0 then theres no update, while 1 indicates update. Every version has an incremented value from before.
            if html_text[0] == "1":
                updateORnot = messagebox.askyesno(
                    "Jump - Update", "Version 2.0 found. Do you want to update the game ?")
                if updateORnot:
                    wb.open_new_tab("https://aayan-yasin25.itch.io/jump")
            elif html_text[0] == "0":
                messagebox.showinfo(
                    "Jump - Update", "No update found, Keep playing :)")
        except Exception:
            messagebox.showerror(
                "Jump - Error", "An unknown error occurred, try again later.")

    while True:
        for eventsS in pg.event.get():
            posS = pg.mouse.get_pos()
            if eventsS.type == pg.QUIT:
                quit_game()
            if posS[0] < 23 and posS[1] < 23 or posS[0] > 420 and posS[0] < 480 and posS[1] > 128 and posS[1] < 153 or posS[0] > 491 and posS[0] < 552 and posS[1] > 128 and posS[1] < 153 or posS[0] > 411 and posS[0] < 559 and posS[1] > 195 and posS[1] < 228 or posS[0] > 411 and posS[0] < 559 and posS[1] > 266 and posS[1] < 301:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))
            else:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_ARROW))
            if eventsS.type == pg.MOUSEBUTTONDOWN:
                if posS[0] < 23 and posS[1] < 23:
                    Options()
                if posS[0] > 420 and posS[0] < 480 and posS[1] > 128 and posS[1] < 153:
                    pg.mixer.music.set_volume(0.5)
                    btmClick = 420
                if posS[0] > 491 and posS[0] < 552 and posS[1] > 128 and posS[1] < 153:
                    pg.mixer.music.set_volume(0)
                    btmClick = 492
                if posS[0] > 411 and posS[0] < 559 and posS[1] > 195 and posS[1] < 228:
                    pg.mouse.set_cursor(
                        pg.cursors.Cursor(pg.SYSTEM_CURSOR_WAIT))
                    Game_Update()
                if posS[0] > 411 and posS[0] < 559 and posS[1] > 266 and posS[1] < 301:
                    wb.open_new_tab("https://aayan-yasin25.itch.io")

        window.fill((224, 224, 224))
        text_text_setting("Settings", (0, 0, 0), 255, 40, 60, "areal")
        pg.draw.rect(window, (172, 172, 172), (0, 0, 23, 23))
        text_text_setting("<", (0, 0, 0), 5, -1, 20, "helvetica")
        text_text_setting("Music", (0, 0, 0), 135, 131, 30, "corbel")
        text_text_setting("Update", (0, 0, 0), 136, 201, 30, "corbel")
        text_text_setting("More Games", (0, 0, 0), 136, 272, 30, "corbel")
        pg.draw.rect(window, (0, 0, 0), (412, 125, 148, 35))
        pg.draw.rect(window, (225, 225, 225), (492, 130, 60, 25))
        pg.draw.rect(window, (225, 225, 225), (420, 130, 60, 25))
        pg.draw.rect(window, (255, 255, 255), (btmClick, 130, 60, 25))
        pg.draw.rect(window, (0, 0, 0), (412, 195, 148, 35))
        text_text_setting("ON", (0, 0, 0), 433, 128, 25, "helvetica")
        text_text_setting("OFF", (0, 0, 0), 501, 128, 25, "helvetica")
        pg.draw.rect(window, (0, 0, 0), (412, 266, 148, 35))
        text_text_setting("CHECK", (255, 255, 255), 443, 198, 25, "times")
        text_text_setting("EXPLORE", (255, 255, 255), 432, 269, 25, "times")
        text_text_setting("A  Game  By  Aayan  Yasin",
                          (97, 81, 81), 235, 348, 20, "corbel")
        pg.display.update()


def account_settings(email, uname):

    def check_login(name, paswd1, paswd2):
        # print(f"Email : {email}\nName : {paswd1}\nPassword : {paswd2}")
        pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_WAIT))
        changed_name = 0
        changed_pass = 0
        data_of_current_player = collection.find({"_id": ObjectId(idusr)})
        for namess in data_of_current_player:
            MainName = namess["name"]
            Mainpass = namess["password"]
        if paswd1 == Mainpass:
            if name != MainName:
                data = list(collection.find())
                current_name_list_fromDB = []
                for users in data:
                    current_name_list_fromDB.append(users["name"])
                if name in current_name_list_fromDB:
                    messagebox.askretrycancel(
                        "Jump - Account Settings", "Account with this username already exist, please try again !")
                if name not in current_name_list_fromDB:
                    collection.find_one_and_update({"_id": ObjectId(idusr)}, {
                                                   "$set": {"name": name}})
                    changed_name = 1
            if "-" not in paswd2:
                collection.find_one_and_update({"_id": ObjectId(idusr)}, {
                                               "$set": {"password": paswd2}})
                changed_pass = 1
        elif paswd1 != Mainpass:
            messagebox.showerror("Jump - Account Settings",
                                 "Incorrect password !")

        if changed_name == 1:
            sender_email = "aayanjump@gmail.com"
            receiver_email = email
            password = "A10485766a"

            message = MIMEMultipart("alternative")
            message["Subject"] = "Accounts Username Changed"
            message["From"] = sender_email
            message["To"] = receiver_email

            # Create the plain-text and HTML version of your message
            text = f"""\
            Hi {uname},
            Your accounts username was changed to {name}.

            If this wasn't you, then reset/secure your account in the game.

            Thanks,
            The Jump Support"""
            html = f"""\
            <html>
              <body>
                <p>Hi {"".join(uname)},<br>
                   Your accounts username was changed to {name}.<br><br>
                   If this wasn't you, then reset/secure your account in the game.<br><br>
                   Thanks<br>
                   The Jump Support
                </p>
              </body>
            </html>"""

            # Turn these into plain/html MIMEText objects
            part1 = MIMEText(str(text), "plain")
            part2 = MIMEText(html, "html")

            # Add HTML/plain-text parts to MIMEMultipart message
            # The email client will try to render the last part first
            message.attach(part1)
            message.attach(part2)

            # Create secure connection with server and send email
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(
                    sender_email, receiver_email, message.as_string()
                )

        if changed_pass == 1:
            sender_email = "aayanjump@gmail.com"
            receiver_email = email
            password = "A10485766a"

            message = MIMEMultipart("alternative")
            message["Subject"] = "Accounts Password Changed"
            message["From"] = sender_email
            message["To"] = receiver_email

            # Create the plain-text and HTML version of your message
            text = f"""\
            Hi {uname},
            Your accounts password was changed.

            If this wasn't you, then reset/secure your account in the game.

            Thanks,
            The Jump Support"""
            html = f"""\
            <html>
              <body>
                <p>Hi {"".join(uname)},<br>
                   Your accounts password was changed.<br><br>
                   If this wasn't you, then reset/secure your account in the game.<br><br>
                   Thanks<br>
                   The Jump Support
                </p>
              </body>
            </html>"""

            # Turn these into plain/html MIMEText objects
            part1 = MIMEText(str(text), "plain")
            part2 = MIMEText(html, "html")

            # Add HTML/plain-text parts to MIMEMultipart message
            # The email client will try to render the last part first
            message.attach(part1)
            message.attach(part2)

            # Create secure connection with server and send email
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(
                    sender_email, receiver_email, message.as_string()
                )

        pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_ARROW))
        messagebox.showinfo("Jump - Account Settings",
                            "Accounts credentials changed successfully.")
        menu()

    class Entry_Name:
        def __init__(self, x, y, w, h, color):
            self.x = x
            self.y = y
            self.height = h
            self.width = w
            self.color = color

        def place_widget(self):
            pg.draw.rect(window, self.color,
                         (self.x, self.y, self.width, self.height))

        def place_text(self, text):
            font = pg.font.SysFont("comicsansms", self.width+self.height)
            show = font.render(text, True, self.color)
            window.blit(show, (self.x, self.y))

        def text(text, x, y, color, family, size):
            font = pg.font.SysFont(family, size)
            rndFONT = font.render(text, True, color)
            window.blit(rndFONT, (x, y))

    active_colora = (224, 224, 224)
    active_colorb = (224, 224, 224)
    active_colorc = (224, 224, 224)
    entry_title = Entry_Name((screen_w//2)-118, 25, 20, 10, "black")
    entrya1 = Entry_Name(200, 100-12, 300, 55, "black")
    entryb1 = Entry_Name(200, 100+65-12, 300, 55, "black")
    entryc1 = Entry_Name(200, 100+65+65-12, 300, 55, "black")
    entry_textc1 = Entry_Name(215+35, 114-20, 16, 16, (30, 30, 30))
    entry_textc2 = Entry_Name(245+35, 114-20, 16, 16, (30, 30, 30))
    entry_textc3 = Entry_Name(275+35, 114-20, 16, 16, (30, 30, 30))
    entry_textc4 = Entry_Name(305+35, 114-20, 16, 16, (30, 30, 30))
    entry_textc5 = Entry_Name(335+35, 114-20, 16, 16, (30, 30, 30))
    entry_textc6 = Entry_Name(365+35, 114-20, 16, 16, (30, 30, 30))
    entry_textc7 = Entry_Name(395+35, 114-20, 16, 16, (30, 30, 30))
    entry_texta1 = Entry_Name(215+35, 104+55, 16, 16, (30, 30, 30))
    entry_texta2 = Entry_Name(245+35, 104+55, 16, 16, (30, 30, 30))
    entry_texta3 = Entry_Name(275+35, 104+55, 16, 16, (30, 30, 30))
    entry_texta4 = Entry_Name(305+35, 104+55, 16, 16, (30, 30, 30))
    entry_texta5 = Entry_Name(335+35, 104+55, 16, 16, (30, 30, 30))
    entry_texta6 = Entry_Name(365+35, 104+55, 16, 16, (30, 30, 30))
    entry_texta7 = Entry_Name(395+35, 104+55, 16, 16, (30, 30, 30))
    entry_textb1 = Entry_Name(215+35, 104+55+13+50+1, 16, 16, (30, 30, 30))
    entry_textb2 = Entry_Name(245+35, 104+55+13+50+1, 16, 16, (30, 30, 30))
    entry_textb3 = Entry_Name(275+35, 104+55+13+50+1, 16, 16, (30, 30, 30))
    entry_textb4 = Entry_Name(305+35, 104+55+13+50+1, 16, 16, (30, 30, 30))
    entry_textb5 = Entry_Name(335+35, 104+55+13+50+1, 16, 16, (30, 30, 30))
    entry_textb6 = Entry_Name(365+35, 104+55+13+50+1, 16, 16, (30, 30, 30))
    entry_textb7 = Entry_Name(395+35, 104+55+13+50+1, 16, 16, (30, 30, 30))
    button = Entry_Name(200, 200+25+65-8, 300, 50, "black")
    nums_only = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    email_placeholder = ""
    username_placeholder = ""
    password_placeholder = ""
    activea = False
    activeb = False
    activec = False
    worda = 1
    wordb = 1
    wordc = 8
    uname = list(uname)
    texta1 = "-"
    texta2 = "-"
    texta3 = "-"
    texta4 = "-"
    texta5 = "-"
    texta6 = "-"
    texta7 = "-"
    textb1 = "-"
    textb2 = "-"
    textb3 = "-"
    textb4 = "-"
    textb5 = "-"
    textb6 = "-"
    textb7 = "-"
    textb1_password_old_main = "-"
    textb2_password_old_main = "-"
    textb3_password_old_main = "-"
    textb4_password_old_main = "-"
    textb5_password_old_main = "-"
    textb6_password_old_main = "-"
    textb7_password_old_main = "-"
    textb1_oldPassword_sideShow = ""
    textb2_oldPassword_sideShow = ""
    textb3_oldPassword_sideShow = ""
    textb4_oldPassword_sideShow = ""
    textb5_oldPassword_sideShow = ""
    textb6_oldPassword_sideShow = ""
    textb7_oldPassword_sideShow = ""
    textb1_Password = "-"
    textb2_Password = "-"
    textb3_Password = "-"
    textb4_Password = "-"
    textb5_Password = "-"
    textb6_Password = "-"
    textb7_Password = "-"
    textb1_Password_sideShow = ""
    textb2_Password_sideShow = ""
    textb3_Password_sideShow = ""
    textb4_Password_sideShow = ""
    textb5_Password_sideShow = ""
    textb6_Password_sideShow = ""
    textb7_Password_sideShow = ""
    textb1_email = uname[0]
    textb2_email = uname[1]
    textb3_email = uname[2]
    textb4_email = uname[3]
    textb5_email = uname[4]
    textb6_email = uname[5]
    textb7_email = uname[6]

    while True:
        window.fill((224, 224, 224))
        entrya2 = Entry_Name(206, 107-12, 288, 40, active_colora)
        entryb2 = Entry_Name(206, 107+65-12, 288, 40, active_colorb)
        entryc2 = Entry_Name(206, 107+65+65-12, 288, 40, active_colorc)
        name = textb1_email + textb2_email + textb3_email + \
            textb4_email + textb5_email + textb6_email + textb7_email
        old_pass = textb1_password_old_main+textb2_password_old_main+textb3_password_old_main + \
            textb4_password_old_main+textb5_password_old_main + \
            textb6_password_old_main+textb7_password_old_main
        new_pass = textb1_Password+textb2_Password+textb3_Password + \
            textb4_Password+textb5_Password+textb6_Password+textb7_Password
        old__password__sideShow = textb1_oldPassword_sideShow+textb2_oldPassword_sideShow+textb3_oldPassword_sideShow + \
            textb4_oldPassword_sideShow+textb5_oldPassword_sideShow + \
            textb6_oldPassword_sideShow+textb7_oldPassword_sideShow
        new__password__sideShow = textb1_Password_sideShow+textb2_Password_sideShow+textb3_Password_sideShow + \
            textb4_Password_sideShow+textb5_Password_sideShow + \
            textb6_Password_sideShow+textb7_Password_sideShow
        for events in pg.event.get():
            pos = pg.mouse.get_pos()
            if events.type == pg.QUIT:
                sys.exit()
            if pos[0] > 206 and pos[0] < 492 and pos[1] > 94 and pos[1] < 134 or pos[0] > 206 and pos[0] < 492 and pos[1] > 158 and pos[1] < 199 or pos[0] > 206 and pos[0] < 492 and pos[1] > 225 and pos[1] < 264:
                pg.mouse.set_cursor(
                    pg.cursors.Cursor(pg.SYSTEM_CURSOR_IBEAM))
            elif pos[0] < 23 and pos[1] < 23 or pos[0] > 25 and pos[1] > -1 and pos[0] < 48 and pos[1] < 24 or pos[0] > 198 and pos[0] < 500 and pos[1] > 284 and pos[1] < 331 or pos[0] > 505 and pos[0] < 530 and pos[1] > 237 and pos[1] < 256 or pos[0] > 505 and pos[0] < 530 and pos[1] > 171 and pos[1] < 194 or pos[0] > 505 and pos[0] < 530 and pos[1] > 106 and pos[1] < 129 or pos[0] > 197 and pos[1] > 337 and pos[0] < 301 and pos[1] < 356:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))
            else:
                pg.mouse.set_cursor(
                    pg.cursors.Cursor(pg.SYSTEM_CURSOR_ARROW))
            if pos[0] > 505 and pos[0] < 530 and pos[1] > 106 and pos[1] < 129:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))
                email_placeholder = "Enter Username"
            else:
                email_placeholder = ""
            if pos[0] > 505 and pos[0] < 530 and pos[1] > 171 and pos[1] < 194:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))
                username_placeholder = "Enter Old Password"
            else:
                username_placeholder = old__password__sideShow
            if pos[0] > 505 and pos[0] < 530 and pos[1] > 237 and pos[1] < 256:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))
                password_placeholder = "Enter New Password"
            else:
                password_placeholder = new__password__sideShow
            if events.type == pg.MOUSEBUTTONDOWN:
                if pos[0] < 23 and pos[1] < 23:
                    profile("own", "none")
                if pos[0] > 25 and pos[1] > -1 and pos[0] < 48 and pos[1] < 24:
                    messagebox.showinfo("Jump - Account Settings", "Change Username :-\nInorder to change your username, you need to enter your old password plus new username.\n\nChange password :-\nInorder to change your password enter old password plus new password leaving.\n\nChange Email :-\nInorder to change your email address please contact Jump Support.\n\nNote : Username and password can be changed simultaneously, however you can leave new password feild empty.")
                if pos[0] > 197 and pos[1] > 337 and pos[0] < 301 and pos[1] < 356:
                    asktoleaveandresetpassword = messagebox.askokcancel(
                        "Jump - Log Out", "If you want to reset your password we first need to log you out from this account !")
                    if asktoleaveandresetpassword:
                        pg.mouse.set_cursor(
                            pg.cursors.Cursor(pg.SYSTEM_CURSOR_WAIT))
                        pickle.dump("none", open(UserNameSavedFile, "wb"))
                        # Make player offline after logging out of Account
                        names = collection.find({"_id": ObjectId(idusr)})
                        for namess in names:
                            status = namess["online"]
                        collection.find_one_and_update({"_id": ObjectId(idusr)}, {
                                                       "$set": {"online": False}})
                        forgot_pass()
                if pos[0] > 206 and pos[0] < 492 and pos[1] > 94 and pos[1] < 134:
                    activea = True
                    active_colora = "white"
                else:
                    activea = False
                    active_colora = (224, 224, 224)
                if pos[0] > 206 and pos[0] < 492 and pos[1] > 158 and pos[1] < 199:
                    activeb = True
                    active_colorb = "white"
                else:
                    activeb = False
                    active_colorb = (224, 224, 224)
                if pos[0] > 206 and pos[0] < 492 and pos[1] > 225 and pos[1] < 264:
                    activec = True
                    active_colorc = "white"
                else:
                    activec = False
                    active_colorc = (224, 224, 224)
                if pos[0] > 198 and pos[0] < 500 and pos[1] > 284 and pos[1] < 331:
                    if "-" not in name and "-" not in old_pass:
                        check_login(name, old_pass, new_pass)
                    else:
                        messagebox.showwarrning(
                            "Jump - Account Settings", f"Fields cannot contain spaces.")
            if events.type == pg.KEYDOWN:
                if events.key == pg.K_RETURN:
                    if "-" not in name and "-" not in old_pass:
                        check_login(name, old_pass, new_pass)
                    else:
                        messagebox.showwarrning(
                            "Jump - Account Settings", f"Fields cannot contain spaces.")
                key_pressed = pg.key.name(events.key)
                bullets = "\u2022"
                if activeb:
                    if key_pressed in nums_only or key_pressed in alphabets:
                        if worda == 1:
                            texta1 = bullets
                            textb1_password_old_main = key_pressed
                            textb1_oldPassword_sideShow = key_pressed
                        elif worda == 2:
                            texta2 = bullets
                            textb2_password_old_main = key_pressed
                            textb2_oldPassword_sideShow = key_pressed
                        elif worda == 3:
                            texta3 = bullets
                            textb3_password_old_main = key_pressed
                            textb3_oldPassword_sideShow = key_pressed
                        elif worda == 4:
                            texta4 = bullets
                            textb4_password_old_main = key_pressed
                            textb4_oldPassword_sideShow = key_pressed
                        elif worda == 5:
                            texta5 = bullets
                            textb5_password_old_main = key_pressed
                            textb5_oldPassword_sideShow = key_pressed
                        elif worda == 6:
                            texta6 = bullets
                            textb6_password_old_main = key_pressed
                            textb6_oldPassword_sideShow = key_pressed
                        elif worda == 7:
                            texta7 = bullets
                            textb7_password_old_main = key_pressed
                            textb7_oldPassword_sideShow = key_pressed
                        worda += 1
                        if worda > 7:
                            worda = 8
                    if key_pressed == "backspace":
                        if worda == 2:
                            texta1 = "-"
                            textb1_password_old_main = "-"
                            textb1_oldPassword_sideShow = ""
                        elif worda == 3:
                            texta2 = "-"
                            textb2_password_old_main = "-"
                            textb2_oldPassword_sideShow = ""
                        elif worda == 4:
                            texta3 = "-"
                            textb3_password_old_main = "-"
                            textb3_oldPassword_sideShow = ""
                        elif worda == 5:
                            texta4 = "-"
                            textb4_password_old_main = "-"
                            textb4_oldPassword_sideShow = ""
                        elif worda == 6:
                            texta5 = "-"
                            textb5_password_old_main = "-"
                            textb5_oldPassword_sideShow = ""
                        elif worda == 7:
                            texta6 = "-"
                            textb6_password_old_main = "-"
                            textb6_oldPassword_sideShow = ""
                        elif worda == 8:
                            texta7 = "-"
                            textb7_password_old_main = "-"
                            textb7_oldPassword_sideShow = ""
                        worda -= 1
                        if worda < 1:
                            worda = 1
                if activec:
                    if key_pressed in nums_only or key_pressed in alphabets:
                        if wordb == 1:
                            textb1 = bullets
                            textb1_Password = key_pressed
                            textb1_Password_sideShow = key_pressed
                        elif wordb == 2:
                            textb2 = bullets
                            textb2_Password = key_pressed
                            textb2_Password_sideShow = key_pressed
                        elif wordb == 3:
                            textb3 = bullets
                            textb3_Password = key_pressed
                            textb3_Password_sideShow = key_pressed
                        elif wordb == 4:
                            textb4 = bullets
                            textb4_Password = key_pressed
                            textb4_Password_sideShow = key_pressed
                        elif wordb == 5:
                            textb5 = bullets
                            textb5_Password = key_pressed
                            textb5_Password_sideShow = key_pressed
                        elif wordb == 6:
                            textb6 = bullets
                            textb6_Password = key_pressed
                            textb6_Password_sideShow = key_pressed
                        elif wordb == 7:
                            textb7 = bullets
                            textb7_Password = key_pressed
                            textb7_Password_sideShow = key_pressed
                        wordb += 1
                        if wordb > 7:
                            wordb = 8
                    if key_pressed == "backspace":
                        if wordb == 2:
                            textb1 = "-"
                            textb1_Password = "-"
                            textb1_Password_sideShow = ""
                        elif wordb == 3:
                            textb2 = "-"
                            textb2_Password = "-"
                            textb2_Password_sideShow = ""
                        elif wordb == 4:
                            textb3 = "-"
                            textb3_Password = "-"
                            textb3_Password_sideShow = ""
                        elif wordb == 5:
                            textb4 = "-"
                            textb4_Password = "-"
                            textb4_Password_sideShow = ""
                        elif wordb == 6:
                            textb5 = "-"
                            textb5_Password = "-"
                            textb5_Password_sideShow = ""
                        elif wordb == 7:
                            textb6 = "-"
                            textb6_Password = "-"
                            textb6_Password_sideShow = ""
                        elif wordb == 8:
                            textb7 = "-"
                            textb7_Password = "-"
                            textb7_Password_sideShow = ""
                        wordb -= 1
                        if wordb < 1:
                            wordb = 1
                if activea:
                    if key_pressed in nums_only or key_pressed in alphabets:
                        if wordc == 1:
                            textb1_email = key_pressed
                        elif wordc == 2:
                            textb2_email = key_pressed
                        elif wordc == 3:
                            textb3_email = key_pressed
                        elif wordc == 4:
                            textb4_email = key_pressed
                        elif wordc == 5:
                            textb5_email = key_pressed
                        elif wordc == 6:
                            textb6_email = key_pressed
                        elif wordc == 7:
                            textb7_email = key_pressed
                        wordc += 1
                        if wordc > 7:
                            wordc = 8
                    if key_pressed == "backspace":
                        if wordc == 2:
                            textb1_email = "-"
                        elif wordc == 3:
                            textb2_email = "-"
                        elif wordc == 4:
                            textb3_email = "-"
                        elif wordc == 5:
                            textb4_email = "-"
                        elif wordc == 6:
                            textb5_email = "-"
                        elif wordc == 7:
                            textb6_email = "-"
                        elif wordc == 8:
                            textb7_email = "-"
                        wordc -= 1
                        if wordc < 1:
                            wordc = 1

        entry_title.place_text("Account Settings")
        entrya1.place_widget()
        entryb1.place_widget()
        entryc1.place_widget()
        entrya2.place_widget()
        entryb2.place_widget()
        entryc2.place_widget()
        entry_texta1.place_text(texta1)
        entry_texta2.place_text(texta2)
        entry_texta3.place_text(texta3)
        entry_texta4.place_text(texta4)
        entry_texta5.place_text(texta5)
        entry_texta6.place_text(texta6)
        entry_texta7.place_text(texta7)
        entry_textb1.place_text(textb1)
        entry_textb2.place_text(textb2)
        entry_textb3.place_text(textb3)
        entry_textb4.place_text(textb4)
        entry_textb5.place_text(textb5)
        entry_textb6.place_text(textb6)
        entry_textb7.place_text(textb7)
        entry_textc1.place_text(textb1_email)
        entry_textc2.place_text(textb2_email)
        entry_textc3.place_text(textb3_email)
        entry_textc4.place_text(textb4_email)
        entry_textc5.place_text(textb5_email)
        entry_textc6.place_text(textb6_email)
        entry_textc7.place_text(textb7_email)
        button.place_widget()
        pg.draw.rect(window, (172, 172, 172), (0, 0, 23, 23))
        text("<", "black", 5, -1,  "helvetica", 20)
        pg.draw.rect(window, (172, 172, 172), (25, 0, 23, 23))
        text("ⓘ", "black", 28, -3,  "segoeuisymbol", 20)
        text("ⓘ", "black", 510, 103, "segoeuisymbol", 20)
        text("ⓘ", "black", 510, 168, "segoeuisymbol", 20)
        text("ⓘ", "black", 510, 232, "segoeuisymbol", 20)
        text(email_placeholder, "black", 530, 106, "comicsansms", 15)
        text(username_placeholder, "black", 530, 171, "comicsansms", 15)
        text(password_placeholder, "black", 530, 235, "comicsansms", 15)
        Entry_Name.text("Continue", (screen_w//2)-60,
                        284, "white", "comicsansms", 30)
        text("Forgot Password ?", "black", 200, 337, "segoeuisymbol", 12)
        text(f"Account connected to {email}", "black",
             5, screen_h-21, "segoeuisymbol", 13)
        pg.display.update()


def profile(own_or_other, id_of_user):
    if own_or_other == "own":
        global IconFile

        #### Depressiated probabbly would show up next update ####
        # def change_profile_pic():
        #     original = filedialog.askopenfilename(
        #         filetypes=[("All Files", ("*.jpg", "*.jpeg", "*.png"))])
        #     if not original:
        #         return
        #     target = os.getcwd()+"\\assets\PROFILE-IMAGE.png"
        #     shutil.copyfile(original, target)
        ###########################################################

        names = collection.find({"_id": ObjectId(idusr)})
        for namess in names:
            MainName = namess["name"]
            MainEmail = namess["email"]
            Available_coins = str(numerize.numerize(int(namess["coins"])))
            MainScore = numerize.numerize(namess["highscore_All_times"])
            rank_leaderboard_alltime = namess["rank_all_time"]
            if rank_leaderboard_alltime == 0:
                rank_leaderboard_alltime = "None"
            player_likes = str(numerize.numerize(namess["likes"]))
            char2_owned = namess["skin2"]
            char3_owned = namess["skin3"]
            char4_owned = namess["skin4"]
            char5_owned = namess["skin5"]
            char6_owned = namess["skin6"]

        Char4 = rd.choice(((254, 234, 0), (159, 32, 164),
                           (57, 121, 42), (96, 59, 44)))
        Char5 = rd.choice(((57, 217, 218), (57, 217, 103),
                           (211, 135, 249), (96, 59, 44)))
        Char6 = rd.choice(((255, 0, 0), (0, 255, 0), (0, 0, 255)))
        copy_text = "✂"
        sec_1 = 0
        sec_2 = 0
        sec_3 = 0
        fps = 30
        clock = pg.time.Clock()
        while True:
            for events2 in pg.event.get():
                pos = pg.mouse.get_pos()
                if events2.type == pg.QUIT:
                    quit_game()
                if pos[0] < 23 and pos[1] < 23 or pos[0] > 623 and pos[1] < 23 or pos[0] > 85 and pos[1] > 74 and pos[0] < 166 and pos[1] < 95 or pos[0] > 178 and pos[1] > 41 and pos[0] < 202 and pos[1] < 61:
                    pg.mouse.set_cursor(
                        pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))
                else:
                    pg.mouse.set_cursor(
                        pg.cursors.Cursor(pg.SYSTEM_CURSOR_ARROW))
                if events2.type == pg.MOUSEBUTTONDOWN:
                    if pos[0] < 23 and pos[1] < 23:
                        pg.mouse.set_cursor(
                            pg.cursors.Cursor(pg.SYSTEM_CURSOR_WAIT))
                        menu()
                    if pos[0] > 623 and pos[1] < 23:
                        pg.mouse.set_cursor(
                            pg.cursors.Cursor(pg.SYSTEM_CURSOR_WAIT))
                        pickle.dump("none", open(UserNameSavedFile, "wb"))
                        # Make player offline after logging out of Account
                        names = collection.find({"_id": ObjectId(idusr)})
                        for namess in names:
                            status = namess["online"]
                        collection.find_one_and_update({"_id": ObjectId(idusr)}, {
                                                       "$set": {"online": False}})
                        Log_In()
                    if pos[0] > 85 and pos[1] > 74 and pos[0] < 166 and pos[1] < 95:
                        account_settings(MainEmail, MainName)
                    # if pos[0] > 60 and pos[1] > 30 and pos[0] < 75 and pos[1] < 47:
                        # change_profile_pic()
                    if pos[0] > 178 and pos[1] > 41 and pos[0] < 202 and pos[1] < 61:
                        pyperclip.copy(MainName)
                        copy_text = "✔"

            if os.path.isfile(IconFile):
                IconFile = "assets\JUMP-ICON.png"

            if sec_1 > 30:
                Char5 = rd.choice(
                    ((57, 217, 218), (57, 217, 103), (211, 135, 249), (96, 59, 44)))
                sec_1 = 0

            if sec_2 > 2:
                Char6 = rd.choice(((255, 0, 0), (0, 255, 0), (0, 0, 255)))
                sec_2 = 0

            if copy_text == "✔":
                sec_3 += 1
                if sec_3 > 80:
                    copy_text = "✂"
                    sec_3 = 0

            window.fill((224, 224, 224))
            try:
                add_image(IconFile, 5, 30, 70, 70)
            except Exception:
                pass
            pg.draw.rect(window, (172, 172, 172), (0, 0, 23, 23))
            pg.draw.rect(window, (172, 172, 172), (25, 0, screen_w-100, 23))
            text("<", "black", 5, -1, "helvetica", 20)
            text(MainName, "black", 84, 32, "comicsansms", 25)
            text(copy_text, "black", 183, 39, "segoeuisymbol", 15)
            pg.draw.rect(window, (172, 172, 172), (87, 75, 80, 20))
            text("Account ", "black", 111, 76, "segoeuisymbol", 12)
            text("⚙", "black", 91, 73, "segoeuisymbol", 16)
            text(f"{player_likes} likes", "black",
                 175, 76, "segoeuisymbol", 12)
            text("Log Out", "black", screen_w-67, 0, "comicsansms", 15)
            # pg.draw.rect(window, (224, 224, 224), (60, 27, 20, 20))
            # text("✎", "black", 63, 25, "segoeuisymbol", 15)
            text(f"Title : Expert", "black", 10, 150, "comicsansms", 18)
            text(f"Rank : # {rank_leaderboard_alltime}",
                 "black", 10, 200, "comicsansms", 18)
            text(f"Coins : {Available_coins}",
                 "black", 10, 250, "comicsansms", 18)
            text(f"Highscore : {MainScore}",
                 "black", 10, 300, "comicsansms", 18)
            text(f"Joined : {str(date_player_joined_jump)}",
                 "black", 10, 350, "comicsansms", 18)
            text(f"Character's Owned :",
                 "black", 353, 125, "comicsansms", 15)
            pg.draw.rect(window, "gray", (350, 155, 310, 215))
            pg.draw.rect(window, (0, 0, 0), (380, 183, 30, 50))
            if char2_owned:
                pg.draw.rect(window, (0, 130, 0), (490, 183, 30, 50))
            if char3_owned:
                pg.draw.rect(window, (227, 0, 193), (595, 183, 30, 50))
            if char4_owned:
                pg.draw.rect(window, Char4, (380, 295, 30, 50))
            if char5_owned:
                pg.draw.rect(window, Char5, (490, 295, 30, 50))
            if char6_owned:
                pg.draw.rect(window, Char6, (595, 295, 30, 50))
            sec_1 += 1
            sec_2 += 1
            pg.display.update()
            clock.tick(fps)

    elif own_or_other == "other":

        def like_player_profile():
            all_players_now = players_who_already_liked_this_account + " " + MainName
            curr_likes = player_likes + 1
            collection.find_one_and_update({"_id": ObjectId(id_of_user)}, {
                                           "$set": {"liked_by": all_players_now}})
            collection.find_one_and_update({"_id": ObjectId(id_of_user)}, {
                                           "$set": {"likes": curr_likes}})

        names = collection.find({"_id": ObjectId(idusr)})
        for namess in names:
            MainName = namess["name"]
        Others = collection.find({"_id": ObjectId(id_of_user)})
        for otherss in Others:
            OtherName = otherss["name"]
            Other_coins = str(numerize.numerize(int(otherss["coins"])))
            OtherScore = str(numerize.numerize(otherss["highscore_All_times"]))
            rank_leaderboard_alltime = otherss["rank_all_time"]
            player_likes = otherss["likes"]
            player_likes_show = numerize.numerize(otherss["likes"])
            players_who_already_liked_this_account = otherss["liked_by"]
            online_offline = otherss["online"]
            char2_owned = otherss["skin2"]
            char3_owned = otherss["skin3"]
            char4_owned = otherss["skin4"]
            char5_owned = otherss["skin5"]
            char6_owned = otherss["skin6"]
            date_other_joined_jump = otherss["date_joined"]

        Char4 = rd.choice(((254, 234, 0), (159, 32, 164),
                           (57, 121, 42), (96, 59, 44)))
        Char5 = rd.choice(((57, 217, 218), (57, 217, 103),
                           (211, 135, 249), (96, 59, 44)))
        copy_text = "✂"
        sec_1 = 0
        sec_2 = 0
        sec_3 = 0
        fps = 30
        clock = pg.time.Clock()
        while True:
            Others = collection.find({"_id": ObjectId(id_of_user)})
            for otherss in Others:
                player_likes_show = str(numerize.numerize(otherss["likes"]))
                players_who_already_liked_this_account = otherss["liked_by"]
            for events2 in pg.event.get():
                pos = pg.mouse.get_pos()
                if events2.type == pg.QUIT:
                    quit_game()
                if pos[0] < 23 and pos[1] < 23 or pos[0] > 85 and pos[1] > 74 and pos[0] < 166 and pos[1] < 95 or pos[0] > 178 and pos[1] > 41 and pos[0] < 202 and pos[1] < 61:
                    pg.mouse.set_cursor(
                        pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))
                else:
                    pg.mouse.set_cursor(
                        pg.cursors.Cursor(pg.SYSTEM_CURSOR_ARROW))
                if events2.type == pg.MOUSEBUTTONDOWN:
                    if pos[0] < 23 and pos[1] < 23:
                        pg.mouse.set_cursor(
                            pg.cursors.Cursor(pg.SYSTEM_CURSOR_WAIT))
                        people()
                    if pos[0] > 85 and pos[1] > 74 and pos[0] < 166 and pos[1] < 95 and like_or_not_tf:
                        pg.mouse.set_cursor(
                            pg.cursors.Cursor(pg.SYSTEM_CURSOR_WAIT))
                        like_player_profile()
                    if pos[0] > 178 and pos[1] > 41 and pos[0] < 202 and pos[1] < 61:
                        pyperclip.copy(OtherName)
                        copy_text = "✔"

            IconFile = "assets\JUMP-ICON.png"

            if online_offline:
                online_offline_show = "Online"
                online_width = 6
            else:
                online_offline_show = "Offline"
                online_width = 1

            if sec_1 > 30:
                Char5 = rd.choice(
                    ((57, 217, 218), (57, 217, 103), (211, 135, 249), (96, 59, 44)))
                sec_1 = 0

            if copy_text == "✔":
                sec_3 += 1
                if sec_3 > 10:
                    copy_text = "✂"
                    sec_3 = 0

            if MainName in players_who_already_liked_this_account:
                like_or_not = "Already Liked"
                like_or_not_tf = False
            else:
                like_or_not = "Like Account"
                like_or_not_tf = True

            window.fill((224, 224, 224))
            try:
                add_image(IconFile, 5, 30, 70, 70)
            except Exception:
                pass
            pg.draw.rect(window, (172, 172, 172), (0, 0, 23, 23))
            pg.draw.rect(window, (172, 172, 172), (25, 0, screen_w-100, 23))
            text("<", "black", 5, -1, "helvetica", 20)
            text(OtherName, "black", 84, 32, "comicsansms", 25)
            text(copy_text, "black", 183, 39, "segoeuisymbol", 15)
            pg.draw.rect(window, (172, 172, 172), (87, 75, 80, 20))
            text(like_or_not, "black", 91, 76, "segoeuisymbol", 12)
            text(player_likes_show, "black", 175, 76, "segoeuisymbol", 12)
            text(online_offline_show, "black", screen_w -
                 67+online_width, 0, "comicsansms", 15)
            text(f"Title : Expert", "black", 10, 150, "comicsansms", 18)
            text(f"Rank : # {rank_leaderboard_alltime}",
                 "black", 10, 200, "comicsansms", 18)
            text(f"Coins : {Other_coins}",
                 "black", 10, 250, "comicsansms", 18)
            text(f"Highscore : {OtherScore}",
                 "black", 10, 300, "comicsansms", 18)
            text(f"Joined : {str(date_other_joined_jump)}",
                 "black", 10, 350, "comicsansms", 18)
            text(f"Character's Owned :",
                 "black", 353, 125, "comicsansms", 15)
            pg.draw.rect(window, "gray", (350, 155, 310, 215))
            pg.draw.rect(window, (0, 0, 0), (380, 183, 30, 50))
            if char2_owned:
                pg.draw.rect(window, (0, 130, 0), (490, 183, 30, 50))
            if char3_owned:
                pg.draw.rect(window, (227, 0, 193), (595, 183, 30, 50))
            if char4_owned:
                pg.draw.rect(window, Char4, (380, 295, 30, 50))
            if char5_owned:
                pg.draw.rect(window, Char5, (490, 295, 30, 50))
            if char6_owned:
                pg.draw.rect(window, rd.choice(
                    ((255, 0, 0), (0, 255, 0), (0, 0, 255))), (595, 295, 30, 50))
            sec_1 += 1
            sec_2 += 1
            pg.display.update()
            clock.tick(fps)


def menu():
    global show_filemissing_error
    global IconFile
    global date
    global idusr
    global MainName
    global Available_coins
    global date_player_joined_jump
    black = (0, 0, 0)
    white = (255, 255, 255)
    title_x = 270
    title_y = 60
    title_V = 1
    fps = 30
    clock = pg.time.Clock()
    show_message_if_available_from_developer = 0

    def Text(text, color, x, y, family, size):
        title = pg.font.SysFont(family, size)
        name = title.render(text, True, color)
        window.blit(name, (x, y))

    idusr = pickle.load(open(UserNameSavedFile, "rb"))
    data = list(collection.find())
    All_user_ids = []
    for users in data:
        All_user_ids.append(str(users["_id"]))
    if idusr not in All_user_ids:
        pickle.dump("none", open(UserNameSavedFile, "wb"))
        Log_In()
    names = collection.find({"_id": ObjectId(idusr)})
    for namess in names:
        MainName = namess["name"]
        MainScore = namess["highscore_All_times"]
        MainScore_week = namess["highscore_week"]
        Available_coins = str(numerize.numerize(int(namess["coins"])))
        account_banned_not = namess["banned"]
        status = namess["online"]
        show_message = namess["show_message"]
        date_player_joined_jump = namess["date_joined"]
        level1 = namess["level1"].split()
        level2 = namess["level2"].split()
        level3 = namess["level3"].split()
        level4 = namess["level4"].split()
        level5 = namess["level5"].split()
        level6 = namess["level6"].split()
        Sum_Score_week = int(level1[1]) + int(level2[1]) + int(level3[1]) + \
            int(level4[1]) + int(level5[1]) + int(level6[1])
        Sum_Score_Alltime = int(level1[2]) + int(level2[2]) + int(
            level3[2]) + int(level4[2]) + int(level5[2]) + int(level6[2])

    if MainScore_week < Sum_Score_week:
        collection.find_one_and_update({"_id": ObjectId(idusr)}, {
                                       "$set": {"highscore_week": Sum_Score_week}})  # Total Highsocre ( Week )
    if MainScore < Sum_Score_Alltime:
        collection.find_one_and_update({"_id": ObjectId(idusr)}, {"$set": {
                                       "highscore_All_times": Sum_Score_Alltime}})  # Total Highsocre ( All Times )

    if not status:
        collection.find_one_and_update(
            {"_id": ObjectId(idusr)}, {"$set": {"online": True}})  # True if user is playing

    while True:
        if os.path.isfile(IconFile):
            IconFile = "assets\JUMP-ICON.png"
        # else:
        #     IconFile = "assets\PROFILE-IMAGE.png"
        if account_banned_not:
            messagebox.showerror(
                "Jump - Account Banned", f"Dear {MainName} your account has been banned permanently. For further details contact at costumer support.")
            pickle.dump("none", open(UserNameSavedFile, "wb"))
            Log_In()
        for events2 in pg.event.get():
            pos = pg.mouse.get_pos()
            if events2.type == pg.QUIT:
                quit_game()
            if pos[0] > 0 and pos[0] < 59 and pos[1] > 0 and pos[1] < 59 or pos[0] > 251 and pos[0] < 451 and pos[1] > 149 and pos[1] < 200 or pos[0] > 251 and pos[0] < 451 and pos[1] > 220 and pos[1] < 270 or pos[0] > 251 and pos[0] < 451 and pos[1] > 289 and pos[1] < 340:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))
            else:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_ARROW))
            if events2.type == pg.MOUSEBUTTONDOWN:
                if pos[0] > 251 and pos[0] < 451 and pos[1] > 149 and pos[1] < 200:
                    Level_1()
                if pos[0] > 251 and pos[0] < 451 and pos[1] > 220 and pos[1] < 270:
                    pg.mouse.set_cursor(
                        pg.cursors.Cursor(pg.SYSTEM_CURSOR_WAIT))
                    Choose_Level()
                if pos[0] > 251 and pos[0] < 451 and pos[1] > 289 and pos[1] < 340:
                    Options()
                if pos[0] > 0 and pos[0] < 59 and pos[1] > 0 and pos[1] < 59:
                    pg.mouse.set_cursor(
                        pg.cursors.Cursor(pg.SYSTEM_CURSOR_WAIT))
                    profile("own", "none")

        if show_message_if_available_from_developer == 15:
            if show_message != "none":
                show_message = show_message.split()
                if show_message[0].lower() == "error":
                    messagebox.showerror(
                        "jump - Error notice from developer", show_message[1].replace("_", " "))
                if show_message[0].lower() == "warning":
                    messagebox.showwarning(
                        "jump - Warning notice from developer", show_message[1].replace("_", " "))
                if show_message[0].lower() == "info":
                    messagebox.showinfo(
                        "jump - Info notice from developer", show_message[1].replace("_", " "))
                collection.find_one_and_update({"_id": ObjectId(idusr)}, {
                                               "$set": {"show_message": "none"}})

        title_y += title_V
        if title_y > 62:
            title_V = -1
        if title_y < 58:
            title_V = 1

        if show_filemissing_error == 15:
            if not MusicFile_AvailableORnot or not IconFile_AvailableORnot:
                files_available_not()

        window.fill((224, 224, 224))
        add_image(IconFile, 5, 5, 50, 50)
        Text(f"{MainName}", (30, 30, 30), 60, 3, "comicsansms", 20)
        Text(f"Score : {str(numerize.numerize(MainScore))}",
             (30, 30, 30), 60, 33, "comicsansms", 15)
        Text(f"Coins : {Available_coins}",
             (30, 30, 30), screen_w-(83+len(Available_coins)*13), 2, "comicsansms", 22)
        Text("J U M P", black, title_x, title_y, "helvetica", 55)
        pg.draw.rect(window, black, (251, 150, 200, 50))
        Text("P L A Y", white, 312, 156, "helvetica", 30)
        pg.draw.rect(window, black, (251, 220, 200, 50))
        Text("L E V E L", white, 303, 226, "helvetica", 30)
        pg.draw.rect(window, black, (251, 290, 200, 50))
        Text("O P T I O N S", white, 276, 296, "helvetica", 30)
        Text(f"Version {version}", (70, 70, 70),
             7, screen_h-23, "helvetica", 15)
        Text("©2021 Aayan Yasin", "black", screen_w -
             115, screen_h-23, "helvetica", 15)
        show_filemissing_error += 1
        show_message_if_available_from_developer += 1
        pg.display.update()
        clock.tick(fps)


def sign_up():

    def check_login(email, name, paswd):
        # print(f"Email : {email}\nName : {name}\nPassword : {paswd}")
        pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_WAIT))
        data = list(collection.find())
        current_email_list_fromDB = []
        current_name_list_fromDB = []
        for users in data:
            current_email_list_fromDB.append(users["email"])
            current_name_list_fromDB.append(users["name"])
        if email in current_email_list_fromDB:
            messagebox.askretrycancel(
                "Jump - Log In", "Account with this email address already exist, please try again !")
        else:
            if name in current_name_list_fromDB:
                messagebox.askretrycancel(
                    "Jump - Log In", "Account with this username already exist, please try again !")
            else:
                collection.insert_one({
                    "name": name,
                    "password": paswd,
                    "codes": "iloveu jumpay aayany",
                    "coins": "0",
                    "email": email,
                    "highscore_All_times": 0,
                    "level1": "True 0 0",
                    "level2": "False 0 0",
                    "level3": "False 0 0",
                    "level4": "False 0 0",
                    "level5": "False 0 0",
                    "level6": "False 0 0",
                    "skin2": False,
                    "skin3": False,
                    "skin4": False,
                    "skin5": False,
                    "skin6": False,
                    "online": False,
                    "leaderboard_prize": False,
                    "banned": False,
                    "show_message": "none",
                    "rank_all_time": 0,
                    "highscore_week": 0,
                    "likes": 0,
                    "liked_by": "",
                    "date_joined": datetime.today().strftime('%d/%m/%Y')})
                Log_In()

    class Entry_Name:
        def __init__(self, x, y, w, h, color):
            self.x = x
            self.y = y
            self.height = h
            self.width = w
            self.color = color

        def place_widget(self):
            pg.draw.rect(window, self.color,
                         (self.x, self.y, self.width, self.height))

        def place_text(self, text):
            font = pg.font.SysFont("comicsansms", self.width+self.height)
            show = font.render(text, True, self.color)
            window.blit(show, (self.x, self.y))

        def text(text, x, y, color, family, size):
            font = pg.font.SysFont(family, size)
            rndFONT = font.render(text, True, color)
            window.blit(rndFONT, (x, y))

    active_colora = (224, 224, 224)
    active_colorb = (224, 224, 224)
    active_colorc = (224, 224, 224)
    entry_title = Entry_Name((screen_w//2)-60, 25, 20, 10, "black")
    entrya1 = Entry_Name(200, 100-12, 300, 55, "black")
    entryb1 = Entry_Name(200, 100+65-12, 300, 55, "black")
    entryc1 = Entry_Name(200, 100+65+65-12, 300, 55, "black")
    email_placeholder = ""
    username_placeholder = ""
    password_placeholder = ""
    entry_textc1 = Entry_Name(215, 114-12, 10, 10, (30, 30, 30))
    entry_textc2 = Entry_Name(225, 114-12, 10, 10, (30, 30, 30))
    entry_textc3 = Entry_Name(235, 114-12, 10, 10, (30, 30, 30))
    entry_textc4 = Entry_Name(245, 114-12, 10, 10, (30, 30, 30))
    entry_textc5 = Entry_Name(255, 114-12, 10, 10, (30, 30, 30))
    entry_textc6 = Entry_Name(265, 114-12, 10, 10, (30, 30, 30))
    entry_textc7 = Entry_Name(275, 114-12, 10, 10, (30, 30, 30))
    entry_textc8 = Entry_Name(285, 114-12, 10, 10, (30, 30, 30))
    entry_textc9 = Entry_Name(295, 114-12, 10, 10, (30, 30, 30))
    entry_textc10 = Entry_Name(305, 114-12, 10, 10, (30, 30, 30))
    entry_textc11 = Entry_Name(315, 114-12, 10, 10, (30, 30, 30))
    entry_textc12 = Entry_Name(325, 114-12, 10, 10, (30, 30, 30))
    entry_textc13 = Entry_Name(335, 114-12, 10, 10, (30, 30, 30))
    entry_textc14 = Entry_Name(345, 114-12, 10, 10, (30, 30, 30))
    entry_textc15 = Entry_Name(355, 114-12, 10, 10, (30, 30, 30))
    entry_textc16 = Entry_Name(365, 114-12, 10, 10, (30, 30, 30))
    entry_textc17 = Entry_Name(375, 114-12, 10, 10, (30, 30, 30))
    entry_textc18 = Entry_Name(385, 114-12, 10, 10, (30, 30, 30))
    entry_textc19 = Entry_Name(395, 114-12, 10, 10, (30, 30, 30))
    entry_textc20 = Entry_Name(405, 114-12, 10, 10, (30, 30, 30))
    entry_textc21 = Entry_Name(415, 114-12, 10, 10, (30, 30, 30))
    entry_textc22 = Entry_Name(425, 114-12, 10, 10, (30, 30, 30))
    entry_textc23 = Entry_Name(435, 114-12, 10, 10, (30, 30, 30))
    entry_textc24 = Entry_Name(445, 114-12, 10, 10, (30, 30, 30))
    entry_textc25 = Entry_Name(455, 114-12, 10, 10, (30, 30, 30))
    entry_textc26 = Entry_Name(465, 114-12, 10, 10, (30, 30, 30))
    entry_textc27 = Entry_Name(475, 114-12, 10, 10, (30, 30, 30))
    entry_texta1 = Entry_Name(215+35, 104+55, 16, 16, (30, 30, 30))
    entry_texta2 = Entry_Name(245+35, 104+55, 16, 16, (30, 30, 30))
    entry_texta3 = Entry_Name(275+35, 104+55, 16, 16, (30, 30, 30))
    entry_texta4 = Entry_Name(305+35, 104+55, 16, 16, (30, 30, 30))
    entry_texta5 = Entry_Name(335+35, 104+55, 16, 16, (30, 30, 30))
    entry_texta6 = Entry_Name(365+35, 104+55, 16, 16, (30, 30, 30))
    entry_texta7 = Entry_Name(395+35, 104+55, 16, 16, (30, 30, 30))
    entry_textb1 = Entry_Name(215+35, 104+55+13+50+1, 16, 16, (30, 30, 30))
    entry_textb2 = Entry_Name(245+35, 104+55+13+50+1, 16, 16, (30, 30, 30))
    entry_textb3 = Entry_Name(275+35, 104+55+13+50+1, 16, 16, (30, 30, 30))
    entry_textb4 = Entry_Name(305+35, 104+55+13+50+1, 16, 16, (30, 30, 30))
    entry_textb5 = Entry_Name(335+35, 104+55+13+50+1, 16, 16, (30, 30, 30))
    entry_textb6 = Entry_Name(365+35, 104+55+13+50+1, 16, 16, (30, 30, 30))
    entry_textb7 = Entry_Name(395+35, 104+55+13+50+1, 16, 16, (30, 30, 30))
    button = Entry_Name(200, 200+25+65-8, 300, 50, "black")
    email_only = ["@", "."]
    nums_only = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    password = ""
    activea = False
    activeb = False
    activec = False
    worda = 1
    wordb = 1
    wordc = 1
    texta1 = "-"
    texta2 = "-"
    texta3 = "-"
    texta4 = "-"
    texta5 = "-"
    texta6 = "-"
    texta7 = "-"
    textb1 = "-"
    textb2 = "-"
    textb3 = "-"
    textb4 = "-"
    textb5 = "-"
    textb6 = "-"
    textb7 = "-"
    textb1_Password = "-"
    textb2_Password = "-"
    textb3_Password = "-"
    textb4_Password = "-"
    textb5_Password = "-"
    textb6_Password = "-"
    textb7_Password = "-"
    textb1_Password_sideShow = ""
    textb2_Password_sideShow = ""
    textb3_Password_sideShow = ""
    textb4_Password_sideShow = ""
    textb5_Password_sideShow = ""
    textb6_Password_sideShow = ""
    textb7_Password_sideShow = ""
    textb1_email = "-"
    textb2_email = "-"
    textb3_email = "-"
    textb4_email = "-"
    textb5_email = "-"
    textb6_email = "-"
    textb7_email = "-"
    textb8_email = "-"
    textb9_email = "-"
    textb10_email = "-"
    textb11_email = "-"
    textb12_email = "-"
    textb13_email = "-"
    textb14_email = "-"
    textb15_email = "-"
    textb16_email = "-"
    textb17_email = "-"
    textb18_email = "-"
    textb19_email = "-"
    textb20_email = "-"
    textb21_email = "-"
    textb22_email = "-"
    textb23_email = "-"
    textb24_email = "-"
    textb25_email = "-"
    textb26_email = "-"
    textb27_email = "-"

    while True:
        window.fill((224, 224, 224))
        entrya2 = Entry_Name(206, 107-12, 288, 40, active_colora)
        entryb2 = Entry_Name(206, 107+65-12, 288, 40, active_colorb)
        entryc2 = Entry_Name(206, 107+65+65-12, 288, 40, active_colorc)
        email = textb1_email + textb2_email + textb3_email + textb4_email + textb5_email + textb6_email + textb7_email + textb8_email + textb9_email + textb10_email + textb11_email + textb12_email + textb13_email + \
            textb14_email + textb15_email + textb16_email + textb17_email + textb18_email + textb19_email + textb20_email + \
            textb21_email + textb22_email + textb23_email + \
            textb24_email + textb25_email + textb26_email + textb27_email
        email = email.replace("-", "")
        name = texta1+texta2+texta3+texta4+texta5+texta6+texta7
        password = textb1_Password+textb2_Password+textb3_Password + \
            textb4_Password+textb5_Password+textb6_Password+textb7_Password
        password__sideShow = textb1_Password_sideShow+textb2_Password_sideShow+textb3_Password_sideShow + \
            textb4_Password_sideShow+textb5_Password_sideShow + \
            textb6_Password_sideShow+textb7_Password_sideShow
        for events in pg.event.get():
            pos = pg.mouse.get_pos()
            if events.type == pg.QUIT:
                sys.exit()
            if pos[0] > 206 and pos[0] < 492 and pos[1] > 94 and pos[1] < 134 or pos[0] > 206 and pos[0] < 492 and pos[1] > 158 and pos[1] < 199 or pos[0] > 206 and pos[0] < 492 and pos[1] > 225 and pos[1] < 264:
                pg.mouse.set_cursor(
                    pg.cursors.Cursor(pg.SYSTEM_CURSOR_IBEAM))
            elif pos[0] > 198 and pos[0] < 500 and pos[1] > 284 and pos[1] < 331 or pos[0] > 505 and pos[0] < 530 and pos[1] > 237 and pos[1] < 256 or pos[0] > 505 and pos[0] < 530 and pos[1] > 171 and pos[1] < 194 or pos[0] > 505 and pos[0] < 530 and pos[1] > 106 and pos[1] < 129 or pos[0] > 197 and pos[0] < 343 and pos[1] > 339 and pos[1] < 356:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))
            else:
                pg.mouse.set_cursor(
                    pg.cursors.Cursor(pg.SYSTEM_CURSOR_ARROW))
            if pos[0] > 505 and pos[0] < 530 and pos[1] > 106 and pos[1] < 129:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))
                email_placeholder = "Enter Email Address"
            else:
                email_placeholder = ""
            if pos[0] > 505 and pos[0] < 530 and pos[1] > 171 and pos[1] < 194:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))
                username_placeholder = "Enter Username"
            else:
                username_placeholder = ""
            if pos[0] > 505 and pos[0] < 530 and pos[1] > 237 and pos[1] < 256:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))
                password_placeholder = "Enter Password"
            else:
                password_placeholder = password__sideShow
            if events.type == pg.MOUSEBUTTONDOWN:
                if pos[0] > 197 and pos[0] < 343 and pos[1] > 339 and pos[1] < 356:
                    Log_In()
                if pos[0] > 206 and pos[0] < 492 and pos[1] > 94 and pos[1] < 134:
                    activea = True
                    active_colora = "white"
                else:
                    activea = False
                    active_colora = (224, 224, 224)
                if pos[0] > 206 and pos[0] < 492 and pos[1] > 158 and pos[1] < 199:
                    activeb = True
                    active_colorb = "white"
                else:
                    activeb = False
                    active_colorb = (224, 224, 224)
                if pos[0] > 206 and pos[0] < 492 and pos[1] > 225 and pos[1] < 264:
                    activec = True
                    active_colorc = "white"
                else:
                    activec = False
                    active_colorc = (224, 224, 224)
                if pos[0] > 198 and pos[0] < 500 and pos[1] > 284 and pos[1] < 331:
                    if "@" in email and ".com" in email:
                        if "-" not in name and "-" not in password:
                            check_login(email, name, password)
                        else:
                            messagebox.showwarrning(
                                "Jump - Log In", f"Fields cannot contain spaces.")
                    else:
                        messagebox.showerror(
                            "Jump - Log In", f"Invalid Email Address !")
            if events.type == pg.KEYDOWN:
                if events.key == pg.K_RETURN:
                    if "@" in email and ".com" in email:
                        if "-" not in name and "-" not in password:
                            check_login(email, name, password)
                        else:
                            messagebox.showwarrning(
                                "Jump - Log In", f"Fields cannot contain spaces.")
                    else:
                        messagebox.showerror(
                            "Jump - Log In", f"Invalid Email Address !")
                key_pressed = pg.key.name(events.key)
                if events.key == pg.K_2 and pg.key.get_mods() & pg.KMOD_SHIFT:
                    key_pressed = "@"
                if activeb:
                    if key_pressed in nums_only or key_pressed in alphabets:
                        if worda == 1:
                            texta1 = key_pressed
                        elif worda == 2:
                            texta2 = key_pressed
                        elif worda == 3:
                            texta3 = key_pressed
                        elif worda == 4:
                            texta4 = key_pressed
                        elif worda == 5:
                            texta5 = key_pressed
                        elif worda == 6:
                            texta6 = key_pressed
                        elif worda == 7:
                            texta7 = key_pressed
                        worda += 1
                        if worda > 7:
                            worda = 8
                    if key_pressed == "backspace":
                        if worda == 2:
                            texta1 = "-"
                        elif worda == 3:
                            texta2 = "-"
                        elif worda == 4:
                            texta3 = "-"
                        elif worda == 5:
                            texta4 = "-"
                        elif worda == 6:
                            texta5 = "-"
                        elif worda == 7:
                            texta6 = "-"
                        elif worda == 8:
                            texta7 = "-"
                        worda -= 1
                        if worda < 1:
                            worda = 1
                if activec:
                    if key_pressed in nums_only or key_pressed in alphabets:
                        bullets = "\u2022"
                        if wordb == 1:
                            textb1 = bullets
                            textb1_Password = key_pressed
                            textb1_Password_sideShow = key_pressed
                        elif wordb == 2:
                            textb2 = bullets
                            textb2_Password = key_pressed
                            textb2_Password_sideShow = key_pressed
                        elif wordb == 3:
                            textb3 = bullets
                            textb3_Password = key_pressed
                            textb3_Password_sideShow = key_pressed
                        elif wordb == 4:
                            textb4 = bullets
                            textb4_Password = key_pressed
                            textb4_Password_sideShow = key_pressed
                        elif wordb == 5:
                            textb5 = bullets
                            textb5_Password = key_pressed
                            textb5_Password_sideShow = key_pressed
                        elif wordb == 6:
                            textb6 = bullets
                            textb6_Password = key_pressed
                            textb6_Password_sideShow = key_pressed
                        elif wordb == 7:
                            textb7 = bullets
                            textb7_Password = key_pressed
                            textb7_Password_sideShow = key_pressed
                        wordb += 1
                        if wordb > 7:
                            wordb = 8
                    if key_pressed == "backspace":
                        if wordb == 2:
                            textb1 = "-"
                            textb1_Password = "-"
                            textb1_Password_sideShow = ""
                        elif wordb == 3:
                            textb2 = "-"
                            textb2_Password = "-"
                            textb2_Password_sideShow = ""
                        elif wordb == 4:
                            textb3 = "-"
                            textb3_Password = "-"
                            textb3_Password_sideShow = ""
                        elif wordb == 5:
                            textb4 = "-"
                            textb4_Password = "-"
                            textb4_Password_sideShow = ""
                        elif wordb == 6:
                            textb5 = "-"
                            textb5_Password = "-"
                            textb5_Password_sideShow = ""
                        elif wordb == 7:
                            textb6 = "-"
                            textb6_Password = "-"
                            textb6_Password_sideShow = ""
                        elif wordb == 8:
                            textb7 = "-"
                            textb7_Password = "-"
                            textb7_Password_sideShow = ""
                        wordb -= 1
                        if wordb < 1:
                            wordb = 1
                if activea:
                    if key_pressed in nums_only or key_pressed in alphabets or key_pressed in email_only:
                        if wordc == 1:
                            textb1_email = key_pressed
                        elif wordc == 2:
                            textb2_email = key_pressed
                        elif wordc == 3:
                            textb3_email = key_pressed
                        elif wordc == 4:
                            textb4_email = key_pressed
                        elif wordc == 5:
                            textb5_email = key_pressed
                        elif wordc == 6:
                            textb6_email = key_pressed
                        elif wordc == 7:
                            textb7_email = key_pressed
                        elif wordc == 8:
                            textb8_email = key_pressed
                        elif wordc == 9:
                            textb9_email = key_pressed
                        elif wordc == 10:
                            textb10_email = key_pressed
                        elif wordc == 11:
                            textb11_email = key_pressed
                        elif wordc == 12:
                            textb12_email = key_pressed
                        elif wordc == 13:
                            textb13_email = key_pressed
                        elif wordc == 14:
                            textb14_email = key_pressed
                        elif wordc == 15:
                            textb15_email = key_pressed
                        elif wordc == 16:
                            textb16_email = key_pressed
                        elif wordc == 17:
                            textb17_email = key_pressed
                        elif wordc == 18:
                            textb18_email = key_pressed
                        elif wordc == 19:
                            textb19_email = key_pressed
                        elif wordc == 20:
                            textb20_email = key_pressed
                        elif wordc == 21:
                            textb21_email = key_pressed
                        elif wordc == 22:
                            textb22_email = key_pressed
                        elif wordc == 23:
                            textb23_email = key_pressed
                        elif wordc == 24:
                            textb24_email = key_pressed
                        elif wordc == 25:
                            textb25_email = key_pressed
                        elif wordc == 26:
                            textb26_email = key_pressed
                        elif wordc == 27:
                            textb27_email = key_pressed
                        wordc += 1
                        if wordc > 27:
                            wordc = 28
                    if key_pressed == "backspace":
                        if wordc == 2:
                            textb1_email = "-"
                        elif wordc == 3:
                            textb2_email = "-"
                        elif wordc == 4:
                            textb3_email = "-"
                        elif wordc == 5:
                            textb4_email = "-"
                        elif wordc == 6:
                            textb5_email = "-"
                        elif wordc == 7:
                            textb6_email = "-"
                        elif wordc == 8:
                            textb7_email = "-"
                        elif wordc == 9:
                            textb8_email = "-"
                        elif wordc == 10:
                            textb9_email = "-"
                        elif wordc == 11:
                            textb10_email = "-"
                        elif wordc == 12:
                            textb11_email = "-"
                        elif wordc == 13:
                            textb12_email = "-"
                        elif wordc == 14:
                            textb13_email = "-"
                        elif wordc == 15:
                            textb14_email = "-"
                        elif wordc == 16:
                            textb15_email = "-"
                        elif wordc == 17:
                            textb16_email = "-"
                        elif wordc == 18:
                            textb17_email = "-"
                        elif wordc == 19:
                            textb18_email = "-"
                        elif wordc == 20:
                            textb19_email = "-"
                        elif wordc == 21:
                            textb20_email = "-"
                        elif wordc == 22:
                            textb21_email = "-"
                        elif wordc == 23:
                            textb22_email = "-"
                        elif wordc == 24:
                            textb23_email = "-"
                        elif wordc == 25:
                            textb24_email = "-"
                        elif wordc == 26:
                            textb25_email = "-"
                        elif wordc == 27:
                            textb26_email = "-"
                        elif wordc == 28:
                            textb27_email = "-"
                        wordc -= 1
                        if wordc < 1:
                            wordc = 1

        entry_title.place_text("Sign Up")
        entrya1.place_widget()
        entryb1.place_widget()
        entryc1.place_widget()
        entrya2.place_widget()
        entryb2.place_widget()
        entryc2.place_widget()
        entry_texta1.place_text(texta1)
        entry_texta2.place_text(texta2)
        entry_texta3.place_text(texta3)
        entry_texta4.place_text(texta4)
        entry_texta5.place_text(texta5)
        entry_texta6.place_text(texta6)
        entry_texta7.place_text(texta7)
        entry_textb1.place_text(textb1)
        entry_textb2.place_text(textb2)
        entry_textb3.place_text(textb3)
        entry_textb4.place_text(textb4)
        entry_textb5.place_text(textb5)
        entry_textb6.place_text(textb6)
        entry_textb7.place_text(textb7)
        entry_textc1.place_text(textb1_email)
        entry_textc2.place_text(textb2_email)
        entry_textc3.place_text(textb3_email)
        entry_textc4.place_text(textb4_email)
        entry_textc5.place_text(textb5_email)
        entry_textc6.place_text(textb6_email)
        entry_textc7.place_text(textb7_email)
        entry_textc8.place_text(textb8_email)
        entry_textc9.place_text(textb9_email)
        entry_textc10.place_text(textb10_email)
        entry_textc11.place_text(textb11_email)
        entry_textc12.place_text(textb12_email)
        entry_textc13.place_text(textb13_email)
        entry_textc14.place_text(textb14_email)
        entry_textc15.place_text(textb15_email)
        entry_textc16.place_text(textb16_email)
        entry_textc17.place_text(textb17_email)
        entry_textc18.place_text(textb18_email)
        entry_textc19.place_text(textb19_email)
        entry_textc20.place_text(textb20_email)
        entry_textc21.place_text(textb21_email)
        entry_textc22.place_text(textb22_email)
        entry_textc23.place_text(textb23_email)
        entry_textc24.place_text(textb24_email)
        entry_textc25.place_text(textb25_email)
        entry_textc26.place_text(textb26_email)
        entry_textc27.place_text(textb27_email)
        button.place_widget()
        text("ⓘ", "black", 510, 103, "segoeuisymbol", 20)
        text("ⓘ", "black", 510, 168, "segoeuisymbol", 20)
        text("ⓘ", "black", 510, 232, "segoeuisymbol", 20)
        text(email_placeholder, "black", 530, 106, "comicsansms", 15)
        text(username_placeholder, "black", 530, 171, "comicsansms", 15)
        text(password_placeholder, "black", 530, 235, "comicsansms", 15)
        Entry_Name.text("Continue", (screen_w//2)-60,
                        284, "white", "comicsansms", 30)
        Entry_Name.text("Already have an Account ?",
                        200, 339, "black", "segoeuisymbol", 12)
        Entry_Name.text(f"Version {version}", 7,
                        screen_h-23, (70, 70, 70), "helvetica", 15)
        Entry_Name.text("©2021 Aayan Yasin", screen_w -
                        115, screen_h-23, "black", "helvetica", 15)
        pg.display.update()


def send_email_func(email, uname):
    global _6digit_Code
    _6digit_Code = rd.randrange(111111, 999999)
    receiver_email = email
    sender_email = "aayanjump@gmail.com"
    password = "A10485766a"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Reset Your Jump Password"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = f"""\
    Hi {uname},
    Inorder to reset your account's password enter the following 6 digit code in the game :

    {_6digit_Code}

    If you didn't send any request, then you can safely ignore this email.

    Thanks,
    The Jump Support"""
    html = """\
    <html>
    <body>
        <p>Hi """+uname+""",<br>
        Inorder to reset your account's password enter the following 6 digit code in the game :<br>
        <h3>"""+str(_6digit_Code)+"""</h3>
        If you didn't send any request, then you can safely ignore this email.<br><br>
        Thanks<br>
        The Jump Support
        </p>
    </body>
    </html>"""

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(str(text), "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )


def forgot_pass():

    def check_email(email):
        pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_WAIT))
        send_email = False
        if "@" not in email and ".com" not in email:
            if len(email) < 8:
                data = list(collection.find())
                current_name_list_fromDB = []
                for users in data:
                    current_name_list_fromDB.append(users["name"])
                if email not in current_name_list_fromDB:
                    messagebox.showwarning(
                        "Jump - Forgot Password", "There is no account connected to this username !")
                    send_email = False
                elif email in current_name_list_fromDB:
                    emails = collection.find({"name": email})
                    for emailss in emails:
                        emailMain = emailss["email"]
                        unameMain = emailss["name"]
                        came_from = "From Username"
                    send_email = True
            else:
                messagebox.showwarning(
                    "Jump - Forgot Password", "Username can only be 7 characters long !")
                send_email = False
        if "@" in email and ".com" in email:
            data = list(collection.find())
            current_email_list_fromDB = []
            for users in data:
                current_email_list_fromDB.append(users["email"])
            if email not in current_email_list_fromDB:
                messagebox.showwarning(
                    "Jump - Forgot Password", "There is no account connected to this email !")
                send_email = False
            elif email in current_email_list_fromDB:
                emails = collection.find({"email": email})
                for emailss in emails:
                    emailMain = emailss["email"]
                    unameMain = emailss["name"]
                    came_from = "From Email"
                send_email = True

        if send_email:
            send_email_func(emailMain, unameMain)
            enter_6digitCode(unameMain, emailMain)

    class Entry_Name:
        def __init__(self, x, y, w, h, color):
            self.x = x
            self.y = y
            self.height = h
            self.width = w
            self.color = color

        def place_widget(self):
            pg.draw.rect(window, self.color,
                         (self.x, self.y, self.width, self.height))

        def place_text(self, text):
            font = pg.font.SysFont("comicsansms", self.width+self.height)
            show = font.render(text, True, self.color)
            window.blit(show, (self.x, self.y))

        def text(text, x, y, color, family, size):
            font = pg.font.SysFont(family, size)
            rndFONT = font.render(text, True, color)
            window.blit(rndFONT, (x, y))

    active_colora = (224, 224, 224)
    entry_title = Entry_Name((screen_w//2)-110, 25, 20, 10, "black")
    entrya1 = Entry_Name(200, 100-12+80, 300, 55, "black")
    email_placeholder = ""
    entry_textc1 = Entry_Name(215, 114-12+80, 10, 10, (30, 30, 30))
    entry_textc2 = Entry_Name(225, 114-12+80, 10, 10, (30, 30, 30))
    entry_textc3 = Entry_Name(235, 114-12+80, 10, 10, (30, 30, 30))
    entry_textc4 = Entry_Name(245, 114-12+80, 10, 10, (30, 30, 30))
    entry_textc5 = Entry_Name(255, 114-12+80, 10, 10, (30, 30, 30))
    entry_textc6 = Entry_Name(265, 114-12+80, 10, 10, (30, 30, 30))
    entry_textc7 = Entry_Name(275, 114-12+80, 10, 10, (30, 30, 30))
    entry_textc8 = Entry_Name(285, 114-12+80, 10, 10, (30, 30, 30))
    entry_textc9 = Entry_Name(295, 114-12+80, 10, 10, (30, 30, 30))
    entry_textc10 = Entry_Name(305, 114-12+80, 10, 10, (30, 30, 30))
    entry_textc11 = Entry_Name(315, 114-12+80, 10, 10, (30, 30, 30))
    entry_textc12 = Entry_Name(325, 114-12+80, 10, 10, (30, 30, 30))
    entry_textc13 = Entry_Name(335, 114-12+80, 10, 10, (30, 30, 30))
    entry_textc14 = Entry_Name(345, 114-12+80, 10, 10, (30, 30, 30))
    entry_textc15 = Entry_Name(355, 114-12+80, 10, 10, (30, 30, 30))
    entry_textc16 = Entry_Name(365, 114-12+80, 10, 10, (30, 30, 30))
    entry_textc17 = Entry_Name(375, 114-12+80, 10, 10, (30, 30, 30))
    entry_textc18 = Entry_Name(385, 114-12+80, 10, 10, (30, 30, 30))
    entry_textc19 = Entry_Name(395, 114-12+80, 10, 10, (30, 30, 30))
    entry_textc20 = Entry_Name(405, 114-12+80, 10, 10, (30, 30, 30))
    entry_textc21 = Entry_Name(415, 114-12+80, 10, 10, (30, 30, 30))
    entry_textc22 = Entry_Name(425, 114-12+80, 10, 10, (30, 30, 30))
    entry_textc23 = Entry_Name(435, 114-12+80, 10, 10, (30, 30, 30))
    entry_textc24 = Entry_Name(445, 114-12+80, 10, 10, (30, 30, 30))
    entry_textc25 = Entry_Name(455, 114-12+80, 10, 10, (30, 30, 30))
    entry_textc26 = Entry_Name(465, 114-12+80, 10, 10, (30, 30, 30))
    entry_textc27 = Entry_Name(475, 114-12+80, 10, 10, (30, 30, 30))
    button = Entry_Name(200, 200+25+20, 300, 50, "black")
    email_only = ["@", "."]
    nums_only = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    wordc = 1
    textb1_email = "-"
    textb2_email = "-"
    textb3_email = "-"
    textb4_email = "-"
    textb5_email = "-"
    textb6_email = "-"
    textb7_email = "-"
    textb8_email = "-"
    textb9_email = "-"
    textb10_email = "-"
    textb11_email = "-"
    textb12_email = "-"
    textb13_email = "-"
    textb14_email = "-"
    textb15_email = "-"
    textb16_email = "-"
    textb17_email = "-"
    textb18_email = "-"
    textb19_email = "-"
    textb20_email = "-"
    textb21_email = "-"
    textb22_email = "-"
    textb23_email = "-"
    textb24_email = "-"
    textb25_email = "-"
    textb26_email = "-"
    textb27_email = "-"

    while True:
        window.fill((224, 224, 224))
        entrya2 = Entry_Name(206, 107-12+80, 288, 40, active_colora)
        email = textb1_email + textb2_email + textb3_email + textb4_email + textb5_email + textb6_email + textb7_email + textb8_email + textb9_email + textb10_email + textb11_email + textb12_email + textb13_email + \
            textb14_email + textb15_email + textb16_email + textb17_email + textb18_email + textb19_email + textb20_email + \
            textb21_email + textb22_email + textb23_email + \
            textb24_email + textb25_email + textb26_email + textb27_email
        email = email.replace("-", "")
        for events in pg.event.get():
            pos = pg.mouse.get_pos()
            if events.type == pg.QUIT:
                sys.exit()
            if pos[0] > 206 and pos[0] < 492 and pos[1] > 174 and pos[1] < 215:
                pg.mouse.set_cursor(
                    pg.cursors.Cursor(pg.SYSTEM_CURSOR_IBEAM))
            elif pos[0] < 24 and pos[1] < 24 or pos[0] > 198 and pos[0] < 500 and pos[1] > 245 and pos[1] < 294:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))
            else:
                pg.mouse.set_cursor(
                    pg.cursors.Cursor(pg.SYSTEM_CURSOR_ARROW))
            if "@" in email or ".com" in email:
                email_placeholder = "Email"
            elif "@" not in email and ".com" not in email:
                email_placeholder = "Username"
            else:
                email_placeholder = ""
            if events.type == pg.MOUSEBUTTONDOWN:
                if pos[0] < 24 and pos[1] < 24:
                    Log_In()
                if pos[0] > 206 and pos[0] < 492 and pos[1] > 174 and pos[1] < 215:
                    activea = True
                    active_colora = "white"
                else:
                    activea = False
                    active_colora = (224, 224, 224)
                if pos[0] > 198 and pos[0] < 500 and pos[1] > 245 and pos[1] < 294:
                    check_email(email)
            if events.type == pg.KEYDOWN:
                if events.key == pg.K_RETURN:
                    check_email(email)
                key_pressed = pg.key.name(events.key)
                if events.key == pg.K_2 and pg.key.get_mods() & pg.KMOD_SHIFT:
                    key_pressed = "@"
                if activea:
                    if key_pressed in nums_only or key_pressed in alphabets or key_pressed in email_only:
                        if wordc == 1:
                            textb1_email = key_pressed
                        elif wordc == 2:
                            textb2_email = key_pressed
                        elif wordc == 3:
                            textb3_email = key_pressed
                        elif wordc == 4:
                            textb4_email = key_pressed
                        elif wordc == 5:
                            textb5_email = key_pressed
                        elif wordc == 6:
                            textb6_email = key_pressed
                        elif wordc == 7:
                            textb7_email = key_pressed
                        elif wordc == 8:
                            textb8_email = key_pressed
                        elif wordc == 9:
                            textb9_email = key_pressed
                        elif wordc == 10:
                            textb10_email = key_pressed
                        elif wordc == 11:
                            textb11_email = key_pressed
                        elif wordc == 12:
                            textb12_email = key_pressed
                        elif wordc == 13:
                            textb13_email = key_pressed
                        elif wordc == 14:
                            textb14_email = key_pressed
                        elif wordc == 15:
                            textb15_email = key_pressed
                        elif wordc == 16:
                            textb16_email = key_pressed
                        elif wordc == 17:
                            textb17_email = key_pressed
                        elif wordc == 18:
                            textb18_email = key_pressed
                        elif wordc == 19:
                            textb19_email = key_pressed
                        elif wordc == 20:
                            textb20_email = key_pressed
                        elif wordc == 21:
                            textb21_email = key_pressed
                        elif wordc == 22:
                            textb22_email = key_pressed
                        elif wordc == 23:
                            textb23_email = key_pressed
                        elif wordc == 24:
                            textb24_email = key_pressed
                        elif wordc == 25:
                            textb25_email = key_pressed
                        elif wordc == 26:
                            textb26_email = key_pressed
                        elif wordc == 27:
                            textb27_email = key_pressed
                        wordc += 1
                        if wordc > 27:
                            wordc = 28
                    if key_pressed == "backspace":
                        if wordc == 2:
                            textb1_email = "-"
                        elif wordc == 3:
                            textb2_email = "-"
                        elif wordc == 4:
                            textb3_email = "-"
                        elif wordc == 5:
                            textb4_email = "-"
                        elif wordc == 6:
                            textb5_email = "-"
                        elif wordc == 7:
                            textb6_email = "-"
                        elif wordc == 8:
                            textb7_email = "-"
                        elif wordc == 9:
                            textb8_email = "-"
                        elif wordc == 10:
                            textb9_email = "-"
                        elif wordc == 11:
                            textb10_email = "-"
                        elif wordc == 12:
                            textb11_email = "-"
                        elif wordc == 13:
                            textb12_email = "-"
                        elif wordc == 14:
                            textb13_email = "-"
                        elif wordc == 15:
                            textb14_email = "-"
                        elif wordc == 16:
                            textb15_email = "-"
                        elif wordc == 17:
                            textb16_email = "-"
                        elif wordc == 18:
                            textb17_email = "-"
                        elif wordc == 19:
                            textb18_email = "-"
                        elif wordc == 20:
                            textb19_email = "-"
                        elif wordc == 21:
                            textb20_email = "-"
                        elif wordc == 22:
                            textb21_email = "-"
                        elif wordc == 23:
                            textb22_email = "-"
                        elif wordc == 24:
                            textb23_email = "-"
                        elif wordc == 25:
                            textb24_email = "-"
                        elif wordc == 26:
                            textb25_email = "-"
                        elif wordc == 27:
                            textb26_email = "-"
                        elif wordc == 28:
                            textb27_email = "-"
                        wordc -= 1
                        if wordc < 1:
                            wordc = 1

        entry_title.place_text("Forgot Password")
        entrya1.place_widget()
        entrya2.place_widget()
        entry_textc1.place_text(textb1_email)
        entry_textc2.place_text(textb2_email)
        entry_textc3.place_text(textb3_email)
        entry_textc4.place_text(textb4_email)
        entry_textc5.place_text(textb5_email)
        entry_textc6.place_text(textb6_email)
        entry_textc7.place_text(textb7_email)
        entry_textc8.place_text(textb8_email)
        entry_textc9.place_text(textb9_email)
        entry_textc10.place_text(textb10_email)
        entry_textc11.place_text(textb11_email)
        entry_textc12.place_text(textb12_email)
        entry_textc13.place_text(textb13_email)
        entry_textc14.place_text(textb14_email)
        entry_textc15.place_text(textb15_email)
        entry_textc16.place_text(textb16_email)
        entry_textc17.place_text(textb17_email)
        entry_textc18.place_text(textb18_email)
        entry_textc19.place_text(textb19_email)
        entry_textc20.place_text(textb20_email)
        entry_textc21.place_text(textb21_email)
        entry_textc22.place_text(textb22_email)
        entry_textc23.place_text(textb23_email)
        entry_textc24.place_text(textb24_email)
        entry_textc25.place_text(textb25_email)
        entry_textc26.place_text(textb26_email)
        entry_textc27.place_text(textb27_email)
        button.place_widget()
        pg.draw.rect(window, (172, 172, 172), (0, 0, 23, 23))
        text("<", "black", 5, -1, "helvetica", 20)
        text("ⓘ", "black", 510, 178, "segoeuisymbol", 20)
        text("Enter Email or Username so we send you a code",
             "black", (screen_w/2)-182, 108, "comicsansms", 18)
        text(email_placeholder, "black", 530, 181, "comicsansms", 15)
        Entry_Name.text("Continue", (screen_w//2)-60,
                        284-37, "white", "comicsansms", 30)
        Entry_Name.text(f"Version {version}", 7,
                        screen_h-23, (70, 70, 70), "helvetica", 15)
        Entry_Name.text("©2021 Aayan Yasin", screen_w -
                        115, screen_h-23, "black", "helvetica", 15)
        pg.display.update()


def enter_6digitCode(uname, email_to_show):

    global collection

    class Entry_Code:
        def __init__(self, x, y, w, h, color):
            self.x = x
            self.y = y
            self.height = h
            self.width = w
            self.color = color

        def place_widget(self):
            pg.draw.rect(window, self.color,
                         (self.x, self.y, self.width, self.height))

        def place_text(self, text):
            font = pg.font.SysFont("comicsansms", self.width+self.height)
            show = font.render(text, True, self.color)
            window.blit(show, (self.x, self.y))

        def place_text_back(self, text):
            font = pg.font.SysFont("helvetica", self.width+self.height)
            show = font.render(text, True, self.color)
            window.blit(show, (self.x, self.y))

        def draw_rect_for_back(self):
            pg.draw.rect(window, self.color,
                         (self.x, self.y, self.width, self.height))

        def Enter_code(self):
            pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_WAIT))
            if int(Code) == int(_6digit_Code):
                change_password_RECOVERY(uname)
            else:
                messagebox.showerror(
                    "Code - JUMP", "The code is incorrect, please try again !")

    active_color = (224, 224, 224)
    entry_title = Entry_Code((screen_w//2)-80, 20, 20, 10, "black")
    entry1 = Entry_Code(200, 100+55, 300, 55, "black")
    entry_text1 = Entry_Code(215+50, 104+55, 16, 16, (30, 30, 30))
    entry_text2 = Entry_Code(245+50, 104+55, 16, 16, (30, 30, 30))
    entry_text3 = Entry_Code(275+50, 104+55, 16, 16, (30, 30, 30))
    entry_text4 = Entry_Code(305+50, 104+55, 16, 16, (30, 30, 30))
    entry_text5 = Entry_Code(335+50, 104+55, 16, 16, (30, 30, 30))
    entry_text6 = Entry_Code(365+50, 104+55, 16, 16, (30, 30, 30))
    button = Entry_Code(200, 200+25, 300, 50, "black")
    button_text = Entry_Code((screen_w//2)-45, 201.5+25, 16, 16, "white")
    entry_info = Entry_Code((screen_w//2)-170, 94, 14, 0, (5, 5, 5))
    buttonBack = Entry_Code(0, 0, 23, 23, (172, 172, 172))
    buttonBack_text = Entry_Code(5, -1, 10, 10, "black")
    check_code = Entry_Code(None, None, None, None, None)
    nums_only = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    active = False
    word = 1
    text1 = "-"
    text2 = "-"
    text3 = "-"
    text4 = "-"
    text5 = "-"
    text6 = "-"

    email_to_show = list(email_to_show)
    new_email = []
    new_email.append(email_to_show[0])
    for Email_to_show_get in range(len(email_to_show)):
        if Email_to_show_get > email_to_show.index("@")-2:
            new_email.append(email_to_show[Email_to_show_get])
        else:
            new_email.append("*")

    email_Main_to_show = str("".join(email_to_show))
    email_Main_to_show_text = str("".join(new_email))

    while True:
        window.fill((224, 224, 224))
        entry2 = Entry_Code(206, 107+55, 288, 40, active_color)
        for events in pg.event.get():
            pos = pg.mouse.get_pos()
            if events.type == pg.QUIT:
                sys.exit()
            if pos[0] > 206 and pos[0] < 495 and pos[1] > 162 and pos[1] < 201:
                pg.mouse.set_cursor(
                    pg.cursors.Cursor(pg.SYSTEM_CURSOR_IBEAM))
            elif pos[0] < 23 and pos[1] < 23 or pos[0] > 200 and pos[0] < 500 and pos[1] > 225 and pos[1] < 273 or pos[0] > 198 and pos[0] < 312 and pos[1] > 281 and pos[1] < 302:
                pg.mouse.set_cursor(
                    pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))
            else:
                pg.mouse.set_cursor(
                    pg.cursors.Cursor(pg.SYSTEM_CURSOR_ARROW))
            if events.type == pg.MOUSEBUTTONDOWN:
                if pos[0] < 23 and pos[1] < 23:
                    asktoleaveforgotpass = messagebox.askquestion(
                        "Jump - Reset Password", "Are you sure you want to go back ?")
                    if asktoleaveforgotpass:
                        Log_In()
                if pos[0] > 198 and pos[0] < 312 and pos[1] > 281 and pos[1] < 302:
                    asktosendcodeagain = messagebox.askquestion(
                        "Jump - Send Code again", "Do you want to get code again ?")
                    if asktosendcodeagain:
                        send_email_func(email_Main_to_show, uname)
                if pos[0] > 206 and pos[0] < 495 and pos[1] > 162 and pos[1] < 201:
                    active = True
                    active_color = "white"
                else:
                    active = False
                    active_color = (224, 224, 224)
                if pos[0] > 200 and pos[0] < 500 and pos[1] > 225 and pos[1] < 273:
                    Code = text1+text2+text3+text4+text5+text6
                    check_code.Enter_code()
            if events.type == pg.KEYDOWN:
                if events.key == pg.K_RETURN:
                    Code = text1+text2+text3+text4+text5+text6
                    check_code.Enter_code()
                key_pressed = pg.key.name(events.key)
                if active:
                    if key_pressed in nums_only:
                        if word == 1:
                            text1 = key_pressed
                        elif word == 2:
                            text2 = key_pressed
                        elif word == 3:
                            text3 = key_pressed
                        elif word == 4:
                            text4 = key_pressed
                        elif word == 5:
                            text5 = key_pressed
                        elif word == 6:
                            text6 = key_pressed
                        word += 1
                        if word > 6:
                            word = 7
                    if key_pressed == "backspace":
                        if word == 2:
                            text1 = "-"
                        elif word == 3:
                            text2 = "-"
                        elif word == 4:
                            text3 = "-"
                        elif word == 5:
                            text4 = "-"
                        elif word == 6:
                            text5 = "-"
                        elif word == 7:
                            text6 = "-"
                        word -= 1
                        if word < 1:
                            word = 1

        entry_title.place_text("Verification")
        entry1.place_widget()
        entry2.place_widget()
        entry_text1.place_text(text1)
        entry_text2.place_text(text2)
        entry_text3.place_text(text3)
        entry_text4.place_text(text4)
        entry_text5.place_text(text5)
        entry_text6.place_text(text6)
        button.place_widget()
        button_text.place_text("Check")
        entry_info.place_text(
            f"Enter 6-digit Code we send to {email_Main_to_show_text}")
        text("Send code again ?", "black", 200, 280, "comicsansms", 14)
        buttonBack.draw_rect_for_back()
        buttonBack_text.place_text_back("<")
        pg.display.update()


def change_password_RECOVERY(name_of_account):
    global collection

    class Entry_Code:
        def __init__(self, x, y, w, h, color):
            self.x = x
            self.y = y
            self.height = h
            self.width = w
            self.color = color

        def place_widget(self):
            pg.draw.rect(window, self.color,
                         (self.x, self.y, self.width, self.height))

        def place_text(self, text):
            font = pg.font.SysFont("comicsansms", self.width+self.height)
            show = font.render(text, True, self.color)
            window.blit(show, (self.x, self.y))

        def place_text_back(self, text):
            font = pg.font.SysFont("helvetica", self.width+self.height)
            show = font.render(text, True, self.color)
            window.blit(show, (self.x, self.y))

        def draw_rect_for_back(self):
            pg.draw.rect(window, self.color,
                         (self.x, self.y, self.width, self.height))

        def Enter_code(self, new_pass):
            pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_WAIT))
            set_or_not = messagebox.askyesno(
                "Jump - Password Set", f"Are you sure you want to set this as your password for {name_of_account} ?")
            if set_or_not:
                collection.find_one_and_update({"name": name_of_account}, {
                                               "$set": {"password": new_pass}})
                Log_In()

    active_color = (224, 224, 224)
    entry_title = Entry_Code((screen_w//2)-70, 20, 20, 10, "black")
    entry1 = Entry_Code(200, 100+55, 300, 55, "black")
    entry_text1 = Entry_Code(215+35, 104+55, 16, 16, (30, 30, 30))
    entry_text2 = Entry_Code(245+35, 104+55, 16, 16, (30, 30, 30))
    entry_text3 = Entry_Code(275+35, 104+55, 16, 16, (30, 30, 30))
    entry_text4 = Entry_Code(305+35, 104+55, 16, 16, (30, 30, 30))
    entry_text5 = Entry_Code(335+35, 104+55, 16, 16, (30, 30, 30))
    entry_text6 = Entry_Code(365+35, 104+55, 16, 16, (30, 30, 30))
    entry_text7 = Entry_Code(395+35, 104+55, 16, 16, (30, 30, 30))
    button = Entry_Code(200, 200+25, 300, 50, "black")
    button_text = Entry_Code((screen_w//2)-45, 201.5+24, 16, 16, "white")
    entry_info = Entry_Code((screen_w//2)-150, 94, 16, 0, (5, 5, 5))
    buttonBack = Entry_Code(0, 0, 23, 23, (172, 172, 172))
    buttonBack_text = Entry_Code(5, -1, 10, 10, "black")
    check_code = Entry_Code(None, None, None, None, None)
    nums_only = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    password_placeholder = ""
    active = False
    word = 1
    text1 = "-"
    text2 = "-"
    text3 = "-"
    text4 = "-"
    text5 = "-"
    text6 = "-"
    text7 = "-"
    text1_Show = ""
    text2_Show = ""
    text3_Show = ""
    text4_Show = ""
    text5_Show = ""
    text6_Show = ""
    text7_Show = ""

    while True:
        window.fill((224, 224, 224))
        entry2 = Entry_Code(206, 107+55, 288, 40, active_color)
        for events in pg.event.get():
            pos = pg.mouse.get_pos()
            if events.type == pg.QUIT:
                sys.exit()
            if pos[0] > 206 and pos[0] < 495 and pos[1] > 162 and pos[1] < 201:
                pg.mouse.set_cursor(
                    pg.cursors.Cursor(pg.SYSTEM_CURSOR_IBEAM))
            elif pos[0] < 23 and pos[1] < 23 or pos[0] > 200 and pos[0] < 500 and pos[1] > 225 and pos[1] < 273 or pos[0] > 506 and pos[0] < 529 and pos[1] > 174 and pos[1] < 193:
                pg.mouse.set_cursor(
                    pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))
            else:
                pg.mouse.set_cursor(
                    pg.cursors.Cursor(pg.SYSTEM_CURSOR_ARROW))
            if pos[0] > 506 and pos[0] < 529 and pos[1] > 174 and pos[1] < 193:
                password_placeholder = "Enter new password"
            else:
                password_placeholder = text1_Show+text2_Show + \
                    text3_Show+text4_Show+text5_Show+text6_Show+text7_Show
            if events.type == pg.MOUSEBUTTONDOWN:
                if pos[0] < 23 and pos[1] < 23:
                    asktoleaveforgotpass = messagebox.askquestion(
                        "Jump - Reset Password", "Are you sure you want to go back ?")
                    if asktoleaveforgotpass:
                        print("Log_In()")
                if pos[0] > 206 and pos[0] < 495 and pos[1] > 162 and pos[1] < 201:
                    active = True
                    active_color = "white"
                else:
                    active = False
                    active_color = (224, 224, 224)
                if pos[0] > 200 and pos[0] < 500 and pos[1] > 225 and pos[1] < 273:
                    Code = text1_Show+text2_Show+text3_Show + \
                        text4_Show+text5_Show+text6_Show+text7_Show
                    check_code.Enter_code(Code)
            if events.type == pg.KEYDOWN:
                if events.key == pg.K_RETURN:
                    Code = text1_Show+text2_Show+text3_Show + \
                        text4_Show+text5_Show+text6_Show+text7_Show
                    check_code.Enter_code(Code)
                key_pressed = pg.key.name(events.key)
                if active:
                    if key_pressed in nums_only or key_pressed in alphabets:
                        if word == 1:
                            text1 = "\u2022"
                            text1_Show = key_pressed
                        elif word == 2:
                            text2 = "\u2022"
                            text2_Show = key_pressed
                        elif word == 3:
                            text3 = "\u2022"
                            text3_Show = key_pressed
                        elif word == 4:
                            text4 = "\u2022"
                            text4_Show = key_pressed
                        elif word == 5:
                            text5 = "\u2022"
                            text5_Show = key_pressed
                        elif word == 6:
                            text6 = "\u2022"
                            text6_Show = key_pressed
                        elif word == 7:
                            text7 = "\u2022"
                            text7_Show = key_pressed
                        word += 1
                        if word > 7:
                            word = 8
                    if key_pressed == "backspace":
                        if word == 2:
                            text1 = "-"
                            text1_Show = ""
                        elif word == 3:
                            text2 = "-"
                            text2_Show = ""
                        elif word == 4:
                            text3 = "-"
                            text3_Show = ""
                        elif word == 5:
                            text4 = "-"
                            text4_Show = ""
                        elif word == 6:
                            text5 = "-"
                            text5_Show = ""
                        elif word == 7:
                            text6 = "-"
                            text6_Show = ""
                        elif word == 8:
                            text7 = "-"
                            text7_Show = ""
                        word -= 1
                        if word < 1:
                            word = 1

        entry_title.place_text("Password")
        entry1.place_widget()
        entry2.place_widget()
        entry_text1.place_text(text1)
        entry_text2.place_text(text2)
        entry_text3.place_text(text3)
        entry_text4.place_text(text4)
        entry_text5.place_text(text5)
        entry_text6.place_text(text6)
        entry_text7.place_text(text7)
        button.place_widget()
        button_text.place_text("Change")
        text("ⓘ", "black", 510, 168, "segoeuisymbol", 20)
        text(password_placeholder, "black", 530, 171, "comicsansms", 15)
        entry_info.place_text(
            f"Enter new 7-digit password for {name_of_account}")
        buttonBack.draw_rect_for_back()
        buttonBack_text.place_text_back("<")
        pg.display.update()


def Log_In():

    def check_login(name, paswd):
        pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_WAIT))
        data = list(collection.find())
        current_name_list_fromDB = []
        for users in data:
            current_name_list_fromDB.append(users["name"])
        if name in current_name_list_fromDB:
            data_dict = collection.find_one({"name": name})
            if data_dict["password"] == paswd:
                names = collection.find({"name": name})
                for namess in names:
                    login_idusr = namess["_id"]
                    pickle.dump(str(login_idusr), open(
                        UserNameSavedFile, "wb"))
                menu()
            else:
                messagebox.showerror(
                    "Jump - Log In", "The password is incorrect.")
        else:
            create_or_not = messagebox.askquestion(
                "Jump - Log In", "Account with this username does not exist, do you want to create one ?")
            if create_or_not:
                sign_up()

    class Entry_Name:
        def __init__(self, x, y, w, h, color):
            self.x = x
            self.y = y
            self.height = h
            self.width = w
            self.color = color

        def place_widget(self):
            pg.draw.rect(window, self.color,
                         (self.x, self.y, self.width, self.height))

        def place_text(self, text):
            font = pg.font.SysFont("comicsansms", self.width+self.height)
            show = font.render(text, True, self.color)
            window.blit(show, (self.x, self.y))

        def text(text, x, y, color, family, size):
            font = pg.font.SysFont(family, size)
            rndFONT = font.render(text, True, color)
            window.blit(rndFONT, (x, y))

    active_colora = (224, 224, 224)
    active_colorb = (224, 224, 224)
    entry_title = Entry_Name((screen_w//2)-60, 20+20, 20, 10, "black")
    entrya1 = Entry_Name(200, 100+15, 300, 55, "black")
    entryb1 = Entry_Name(200, 100+55+30, 300, 55, "black")
    username_placeholder = ""
    password_placeholder = ""
    entry_texta1 = Entry_Name(215+35, 104+15, 16, 16, (30, 30, 30))
    entry_texta2 = Entry_Name(245+35, 104+15, 16, 16, (30, 30, 30))
    entry_texta3 = Entry_Name(275+35, 104+15, 16, 16, (30, 30, 30))
    entry_texta4 = Entry_Name(305+35, 104+15, 16, 16, (30, 30, 30))
    entry_texta5 = Entry_Name(335+35, 104+15, 16, 16, (30, 30, 30))
    entry_texta6 = Entry_Name(365+35, 104+15, 16, 16, (30, 30, 30))
    entry_texta7 = Entry_Name(395+35, 104+15, 16, 16, (30, 30, 30))
    entry_textb1 = Entry_Name(215+35, 104+55+30, 16, 16, (30, 30, 30))
    entry_textb2 = Entry_Name(245+35, 104+55+30, 16, 16, (30, 30, 30))
    entry_textb3 = Entry_Name(275+35, 104+55+30, 16, 16, (30, 30, 30))
    entry_textb4 = Entry_Name(305+35, 104+55+30, 16, 16, (30, 30, 30))
    entry_textb5 = Entry_Name(335+35, 104+55+30, 16, 16, (30, 30, 30))
    entry_textb6 = Entry_Name(365+35, 104+55+30, 16, 16, (30, 30, 30))
    entry_textb7 = Entry_Name(395+35, 104+55+30, 16, 16, (30, 30, 30))
    button = Entry_Name(200, 200+25+45, 300, 50, "black")
    nums_only = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    activea = False
    activeb = False
    worda = 1
    wordb = 1
    texta1 = "-"
    texta2 = "-"
    texta3 = "-"
    texta4 = "-"
    texta5 = "-"
    texta6 = "-"
    texta7 = "-"
    textb1 = "-"
    textb2 = "-"
    textb3 = "-"
    textb4 = "-"
    textb5 = "-"
    textb6 = "-"
    textb7 = "-"
    textb1_Password = "-"
    textb2_Password = "-"
    textb3_Password = "-"
    textb4_Password = "-"
    textb5_Password = "-"
    textb6_Password = "-"
    textb7_Password = "-"

    while True:
        window.fill((224, 224, 224))
        entrya2 = Entry_Name(206, 107+15, 288, 40, active_colora)
        entryb2 = Entry_Name(206, 107+55+30, 288, 40, active_colorb)
        for events in pg.event.get():
            pos = pg.mouse.get_pos()
            if events.type == pg.QUIT:
                sys.exit()
            if pos[0] > 204 and pos[0] < 495 and pos[1] > 191 and pos[1] < 231 or pos[0] > 204 and pos[0] < 493 and pos[1] > 121 and pos[1] < 162:
                pg.mouse.set_cursor(
                    pg.cursors.Cursor(pg.SYSTEM_CURSOR_IBEAM))
            elif pos[0] > 200 and pos[0] < 500 and pos[1] > 270 and pos[1] < 320 or pos[0] > 402 and pos[0] < 500 and pos[1] > 249 and pos[1] < 261 or pos[0] > 198 and pos[0] < 330 and pos[1] > 328 and pos[1] < 341:
                pg.mouse.set_cursor(
                    pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))
            else:
                pg.mouse.set_cursor(
                    pg.cursors.Cursor(pg.SYSTEM_CURSOR_ARROW))
            if pos[0] > 505 and pos[0] < 530 and pos[1] > 132 and pos[1] < 154:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))
                username_placeholder = "Enter Username"
            else:
                username_placeholder = ""
            if pos[0] > 505 and pos[0] < 530 and pos[1] > 202 and pos[1] < 224:
                pg.mouse.set_cursor(pg.cursors.Cursor(pg.SYSTEM_CURSOR_HAND))
                password_placeholder = "Enter Password"
            else:
                password_placeholder = ""
            if events.type == pg.MOUSEBUTTONDOWN:
                if pos[0] > 402 and pos[0] < 500 and pos[1] > 249 and pos[1] < 261:
                    forgot_pass()
                if pos[0] > 198 and pos[0] < 330 and pos[1] > 328 and pos[1] < 341:
                    sign_up()
                if pos[0] > 206 and pos[0] < 493 and pos[1] > 121 and pos[1] < 162:
                    activea = True
                    active_colora = "white"
                else:
                    activea = False
                    active_colora = (224, 224, 224)
                if pos[0] > 206 and pos[0] < 493 and pos[1] > 191 and pos[1] < 231:
                    activeb = True
                    active_colorb = "white"
                else:
                    activeb = False
                    active_colorb = (224, 224, 224)
                if pos[0] > 200 and pos[0] < 500 and pos[1] > 270 and pos[1] < 320:
                    password = textb1_Password+textb2_Password+textb3_Password + \
                        textb4_Password+textb5_Password+textb6_Password+textb7_Password
                    name = texta1+texta2+texta3+texta4+texta5+texta6+texta7
                    if "-" not in name and "-" not in password:
                        check_login(name, password)
                    else:
                        messagebox.showwarrning(
                            "Jump - Log In", f"Fields cannot contain spaces. ")
            if events.type == pg.KEYDOWN:
                if events.key == pg.K_RETURN:
                    password = textb1_Password+textb2_Password+textb3_Password + \
                        textb4_Password+textb5_Password+textb6_Password+textb7_Password
                    name = texta1+texta2+texta3+texta4+texta5+texta6+texta7
                    if "-" not in name and "-" not in password:
                        check_login(name, password)
                    else:
                        messagebox.showwarrning(
                            "Jump - Log In", f"Fields cannot contain spaces. ")
                key_pressed = pg.key.name(events.key)
                if activea:
                    if key_pressed in nums_only or key_pressed in alphabets:
                        if worda == 1:
                            texta1 = key_pressed
                        elif worda == 2:
                            texta2 = key_pressed
                        elif worda == 3:
                            texta3 = key_pressed
                        elif worda == 4:
                            texta4 = key_pressed
                        elif worda == 5:
                            texta5 = key_pressed
                        elif worda == 6:
                            texta6 = key_pressed
                        elif worda == 7:
                            texta7 = key_pressed
                        worda += 1
                        if worda > 7:
                            worda = 8
                    if key_pressed == "backspace":
                        if worda == 2:
                            texta1 = "-"
                        elif worda == 3:
                            texta2 = "-"
                        elif worda == 4:
                            texta3 = "-"
                        elif worda == 5:
                            texta4 = "-"
                        elif worda == 6:
                            texta5 = "-"
                        elif worda == 7:
                            texta6 = "-"
                        elif worda == 8:
                            texta7 = "-"
                        worda -= 1
                        if worda < 1:
                            worda = 1
                if activeb:
                    if key_pressed in nums_only or key_pressed in alphabets:
                        bullets = "\u2022"
                        if wordb == 1:
                            textb1 = bullets
                            textb1_Password = key_pressed
                        elif wordb == 2:
                            textb2 = bullets
                            textb2_Password = key_pressed
                        elif wordb == 3:
                            textb3 = bullets
                            textb3_Password = key_pressed
                        elif wordb == 4:
                            textb4 = bullets
                            textb4_Password = key_pressed
                        elif wordb == 5:
                            textb5 = bullets
                            textb5_Password = key_pressed
                        elif wordb == 6:
                            textb6 = bullets
                            textb6_Password = key_pressed
                        elif wordb == 7:
                            textb7 = bullets
                            textb7_Password = key_pressed
                        wordb += 1
                        if wordb > 7:
                            wordb = 8
                    if key_pressed == "backspace":
                        if wordb == 2:
                            textb1 = "-"
                            textb1_Password = "-"
                        elif wordb == 3:
                            textb2 = "-"
                            textb2_Password = "-"
                        elif wordb == 4:
                            textb3 = "-"
                            textb3_Password = "-"
                        elif wordb == 5:
                            textb4 = "-"
                            textb4_Password = "-"
                        elif wordb == 6:
                            textb5 = "-"
                            textb5_Password = "-"
                        elif wordb == 7:
                            textb6 = "-"
                            textb6_Password = "-"
                        elif wordb == 8:
                            textb7 = "-"
                            textb7_Password = "-"
                        wordb -= 1
                        if wordb < 1:
                            wordb = 1

        entry_title.place_text("Sign In")
        entrya1.place_widget()
        entryb1.place_widget()
        entrya2.place_widget()
        entryb2.place_widget()
        entry_texta1.place_text(texta1)
        entry_texta2.place_text(texta2)
        entry_texta3.place_text(texta3)
        entry_texta4.place_text(texta4)
        entry_texta5.place_text(texta5)
        entry_texta6.place_text(texta6)
        entry_texta7.place_text(texta7)
        entry_textb1.place_text(textb1)
        entry_textb2.place_text(textb2)
        entry_textb3.place_text(textb3)
        entry_textb4.place_text(textb4)
        entry_textb5.place_text(textb5)
        entry_textb6.place_text(textb6)
        entry_textb7.place_text(textb7)
        button.place_widget()
        text("ⓘ", "black", 510, 128, "segoeuisymbol", 20)
        text("ⓘ", "black", 510, 198, "segoeuisymbol", 20)
        text(username_placeholder, "black", 530, 131, "comicsansms", 15)
        text(password_placeholder, "black", 530, 201, "comicsansms", 15)
        Entry_Name.text("Continue", (screen_w//2)-60, 201.5 +
                        25+45.5, "white", "comicsansms", 30)
        Entry_Name.text("Don't have an Account ?",
                        200, 326, "black", "segoeuisymbol", 12)
        Entry_Name.text("Forgot Password ?",
                        402, 247, "black", "segoeuisymbol", 12)
        Entry_Name.text(f"Version {version}", 7,
                        screen_h-23, (70, 70, 70), "helvetica", 15)
        Entry_Name.text("©2021 Aayan Yasin", screen_w -
                        115, screen_h-23, "black", "helvetica", 15)
        pg.display.update()


def Start_Screen():
    global collection
    color = 150

    try:
        logedinornot = pickle.load(open(UserNameSavedFile, "rb"))
    except Exception:
        messagebox.showerror(
            "Jump - Login Error", "There was some error while retrieving data.\nYou need to login again.")
        os.remove(UserNameSavedFile)
        pickle.dump("none", open(UserNameSavedFile, "wb"))
        logedinornot = pickle.load(open(UserNameSavedFile, "rb"))

    perform = True
    error_message = ""
    login_Screen_message = "Loading..."
    login_Screen_message_x, login_Screen_message_y = screen_w/3+80, screen_h/2+115

    while True:
        pg.mixer.music.pause()
        window.fill((150, 150, 150))
        for events2 in pg.event.get():
            pos = pg.mouse.get_pos()
            if events2.type == pg.QUIT:
                quit_game()

        text("J U M P", ((color, color, color)),
             screen_w/3, screen_h/3, "comicsansms", 60)
        text("By Aayan Yasin", ((color, color, color)),
             screen_w/2.4, screen_h/1.8, "comicsansms", 15)
        text(error_message, ((color, color, color)),
             login_Screen_message_x-17, login_Screen_message_y-1, "segoeuisymbol", 16)
        text(login_Screen_message, ((color, color, color)),
             login_Screen_message_x, login_Screen_message_y, "comicsansms", 15)
        color -= 0.3
        if color <= 0:
            color = 0
            if perform:
                try:
                cluster = MongoClient(
                    'mongodb+srv://aayanyasin:A10485766a@cluster0.ez9nx.mongodb.net/Jump?retryWrites=true&w=majority')
                db = cluster["Jump"]
                collection = db["Leader Board"]
                if logedinornot == "none":
                    try:
                        pg.mixer.music.play()
                    except Exception:
                        pass
                    Log_In()
                else:
                    try:
                        pg.mixer.music.play()
                    except Exception:
                        pass
                    menu()
                except Exception:
                    perform = False
                    login_Screen_message_x = screen_w/3-40
                    error_message = "ⓘ"
                    login_Screen_message = "Please make sure you are connected to internet."
                    names = collection.find({"_id": ObjectId(idusr)})
                    for namess in names:
                       status = namess["online"]
                    collection.find_one_and_update({"_id": ObjectId(idusr)}, {"$set": {"online": False}})

        pg.display.update()


if __name__ == "__main__":
    Start_Screen()
