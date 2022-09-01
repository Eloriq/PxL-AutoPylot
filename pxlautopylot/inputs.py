from random import randint
from time import sleep
from pywinauto import keyboard, mouse


def simulate_key_press(key: str | int):
    keyboard.send_keys("{" + str(key) + " down}")
    sleep(0.196 + randint(0, 20) / 100)


def simulate_key_release(key: str | int):
    keyboard.send_keys("{" + str(key) + " up}")
    sleep(randint(8, 32) / 100)


def simulate_key(key: str | int):
    simulate_key_press(key)
    simulate_key_release(key)


def simulate_click_press(x: int, y: int):
    mouse.move((x, y))
    mouse.press('left', (x, y))
    sleep(0.196 + randint(0, 226) / 1000)


def simulate_click_release(x: int, y: int):
    mouse.move((x, y))
    mouse.release('left', (x, y))
    sleep(randint(83, 329) / 1000)


def simulate_click(x: int, y: int):
    simulate_click_press(x, y)
    simulate_click_release(x, y)


def move_mouse(x: int, y: int):
    mouse.move((x, y))
    sleep(randint(83, 329) / 1000)
