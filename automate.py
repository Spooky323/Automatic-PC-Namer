import pyautogui as auto
import keyboard
import time;
num = 1;
branch = "ATH"
file = open("list.txt",'r')
vlan = file.readline()
pc = "PC{0}-{1}-{2}".format(num,vlan,branch)
while True:
    if keyboard.is_pressed('f9'):
        pos = auto.position()
        auto.click()
        auto.click(715,216)
        auto.click(970,310)
        auto.click()
        auto.click()
        auto.write(pc)
        auto.click(1291,179)
        num += 1
        if num == 9:
            num = 1
            vlan = file.readline()
        pc = "PC{0}-{1}-{2}".format(num,vlan,branch)
        auto.moveTo(pos)
