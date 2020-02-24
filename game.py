import glob
import os
import random

import pygame
from pygame.locals import *

import arrow

pygame.mixer.init()

pinyinfiles = list(glob.glob("./resource/pinyin/*.mp3"))


def play_mp3(pinyinfile):
    pygame.mixer.music.load(pinyinfile)
    pygame.mixer.music.play(0)
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(1)


with open("score.csv", "wt") as score:
    while True:
        pinyinfile = random.choice(pinyinfiles)

        while True:
            print("听音")
            play_mp3(pinyinfile)

            correct_answer = os.path.basename(pinyinfile).split(".")[0]

            answer = input("答：")

            if answer.lower() == "r":
                continue

            if answer.lower() == "q":
                print("正确答案", correct_answer)
                break

            score.write(f"{arrow.now().format('YYYY-MM-DD HH:mm:ss')},{correct_answer},{answer}\n")
            score.flush()

            if answer != correct_answer:
                print("错误")
                play_mp3("./resource/incorrect.mp3")
                continue
            else:
                print("正确")
                play_mp3("./resource/correct.mp3")
                break