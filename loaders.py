import sys
import time, random
from os import system
from termcolor import colored, cprint

def game_start_message(color = 'green') :
    system("cls")
    print("[====== Entering the Game ======]\n")
    cprint(" Please wait, checking data ...\n", color, file=sys.stderr)
    print("[===============================]")
    time_sleep(1, 3), system("cls")

def player_loading() :
    system("cls")
    print("[== Preparing ==]\n")
    cprint(" Please wait ...\n", 'green', file=sys.stderr)
    print("[===============]")  
    time_sleep(1, 3), system("cls")

def loading_message(color = 'green') :
    system("cls")
    print("[==============================]\n")
    cprint(" Please wait, checking data ...\n", color, file=sys.stderr)
    print("[==============================]")
    time_sleep(1, 3), system("cls")

def loading_message_tips(color = 'green') :
    system("cls")
    print("[==============================]\n")
    cprint(" --Tips: Happy New year 2k20--\n", color, file=sys.stderr)
    cprint(" Please wait, checking data ...\n", color, file=sys.stderr)
    print("[==============================]")
    time_sleep(1, 3), system("cls")

def time_sleep(min_val, max_val, clear = False) :
    if clear :
        sleep = time.sleep(random.randint(min_val, max_val)), system("cls")
        return sleep

    sleep = time.sleep(random.randint(min_val, max_val))
    return sleep

def error_message(color = 'red') :
    cprint("\n\nThere went error, closing the game", color, file=sys.stderr)
    