import os
import numpy as np
from pandas import array
import colorama
from colorama import Fore, Back, Style
colorama.init()
import json

blank = Fore.RED + Back.GREEN + " " + Style.RESET_ALL


class buildings():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.village_name = "village"
        self.color = Fore.RED + Back.GREEN


class Townhall():
    def __init__(self, x, y, village1):
        self.x = x
        self.y = y
        self.width = 3
        self.height = 4
        self.x1 = x - 1
        self.y1 = y - 2
        self.array = village1.array
        self.back_array = village1.back_array
        self.color = Fore.RED + Back.LIGHTGREEN_EX
        self.health = 100
        self.make_townhall()
        self.destroyed = False

    def make_townhall(self):
        for i in range(self.height):
            for j in range(self.width):
                self.array[self.y1+i][self.x1+j] = self.color + \
                    "T" + Style.RESET_ALL
                self.back_array[self.y1+i][self.x1+j] = "1"

    def reduce_health(self, damage,replay):
        self.health -= damage
        if self.health < 100 and self.health > 50:
            self.color = Back.LIGHTGREEN_EX + Fore.BLACK
            self.make_townhall()
        elif self.health <= 50 and self.health > 20:
            self.color = Back.LIGHTYELLOW_EX + Fore.BLACK
            self.make_townhall()
        elif self.health <= 20 and self.health > 0:
            self.color = Back.RED + Fore.BLACK
            self.make_townhall()
        elif self.health <= 0:
            self.destroy(replay)

    def get_health(self):
        return self.health

    def destroy(self,replay):
        self.destroyed = True
        for i in range(self.height):
            for j in range(self.width):
                self.array[self.y1+i][self.x1+j] = blank
                self.back_array[self.y1+i][self.x1+j] = " "
        
        # input file name
        

    def reduce_health_1(self, damage):
        self.health -= damage
        if self.health < 100 and self.health > 50:
            self.color = Back.LIGHTGREEN_EX + Fore.BLACK
            self.make_townhall()
        elif self.health <= 50 and self.health > 20:
            self.color = Back.LIGHTYELLOW_EX + Fore.BLACK
            self.make_townhall()
        elif self.health <= 20 and self.health > 0:
            self.color = Back.RED + Fore.BLACK
            self.make_townhall()
        elif self.health <= 0:
            self.destroy_1()
    
    def destroy_1(self):
        self.destroyed = True
        for i in range(self.height):
            for j in range(self.width):
                self.array[self.y1+i][self.x1+j] = blank
                self.back_array[self.y1+i][self.x1+j] = " "

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    


class Huts():
    def __init__(self, x, y, village1, hut_number):
        self.x = x
        self.y = y
        self.width = 2
        self.height = 2
        self.health = 100
        self.x1 = x - 1
        self.y1 = y - 1
        self.array = village1.array
        self.back_array = village1.back_array
        self.color = Fore.RED + Back.LIGHTGREEN_EX
        self.num = hut_number
        self.make_huts()
        self.destroyed = False

    def make_huts(self):
        for i in range(self.height):
            for j in range(self.width):
                self.array[self.y1+i][self.x1+j] = self.color + \
                    "H" + Style.RESET_ALL
                self.back_array[self.y1+i][self.x1+j] = self.num

    def reduce_health(self, damage):
        self.health -= damage
        if self.health < 100 and self.health > 50:
            self.color = Back.LIGHTGREEN_EX + Fore.BLACK
            self.make_huts()
        elif self.health <= 50 and self.health > 20:
            self.color = Back.LIGHTYELLOW_EX + Fore.BLACK
            self.make_huts()
        elif self.health <= 20 and self.health > 0:
            self.color = Back.RED + Fore.BLACK
            self.make_huts()
        elif self.health <= 0:
            self.destroy()

    def get_health(self):
        return self.health

    def destroy(self):
        self.destroyed = True
        for i in range(self.height):
            for j in range(self.width):
                self.array[self.y1+i][self.x1+j] = blank
                self.back_array[self.y1+i][self.x1+j] = " "
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y


class Cannons():
    def __init__(self, x, y, village1, cannon_number):
        self.x = x
        self.y = y
        self.width = 2
        self.height = 2
        self.x1 = x - 1
        self.y1 = y - 1
        self.health = 100
        self.damage = 5
        self.array = village1.array
        self.back_array = village1.back_array
        self.color = Fore.RED + Back.LIGHTGREEN_EX
        self.num = cannon_number
        self.make_Cannon()
        self.destroyed = False

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def make_Cannon(self):
        for i in range(self.height):
            for j in range(self.width):
                self.array[self.y1+i][self.x1+j] = self.color + \
                    "C" + Style.RESET_ALL
                self.back_array[self.y1+i][self.x1+j] = self.num

    def reduce_health(self, damage):
        self.health -= damage
        if self.health < 100 and self.health > 50:
            self.color = Back.LIGHTGREEN_EX + Fore.BLACK
            self.make_Cannon()
        elif self.health <= 50 and self.health > 20:
            self.color = Back.LIGHTYELLOW_EX + Fore.BLACK
            self.make_Cannon()
        elif self.health <= 20 and self.health > 0:
            self.color = Back.RED + Fore.BLACK
            self.make_Cannon()
        elif self.health <= 0:
            self.destroy()

    def get_health(self):
        return self.health

    def destroy(self):
        self.destroyed = True
        for i in range(self.height):
            for j in range(self.width):
                self.array[self.y1+i][self.x1+j] = blank
                self.back_array[self.y1+i][self.x1+j] = " "

    def attack(self):
        for i in range(10):
            for j in range(10):
                if (self.back_array[self.y1-5+i][self.x1-5+j] == "K"):
                    self.color = Fore.BLACK + Back.WHITE
                    return "K"

    def get_damage(self):
        return self.damage


class wall():
    def __init__(self, x, y, village1, count):
        self.x = x
        self.y = y
        self.width = 1
        self.height = 1
        self.x1 = x - 1
        self.y1 = y - 2
        self.array = village1.array
        self.back_array = village1.back_array
        self.color = Fore.RED + Back.BLACK
        self.health = 100
        self.back_array[x][y] = count
        self.array[x][y] = self.color + 'w' + Style.RESET_ALL
    
    def make_huts(self):
        for i in range(self.height):
            for j in range(self.width):
                self.array[self.y1+i][self.x1+j] = self.color + \
                    "H" + Style.RESET_ALL
                self.back_array[self.y1+i][self.x1+j] = self.num

    def reduce_health(self, damage, count):
        self.health -= damage
        if self.health <= 100 and self.health > 50:
            self.color = Back.LIGHTGREEN_EX + Fore.BLACK
            self.back_array[self.x][self.y] = count
            self.array[self.x][self.y] = self.color + 'w' + Style.RESET_ALL
        elif self.health <= 50 and self.health > 20:
            self.color = Back.LIGHTYELLOW_EX + Fore.BLACK
            self.back_array[self.x][self.y] = count
            self.array[self.x][self.y] = self.color + 'w' + Style.RESET_ALL
        elif self.health <= 20 and self.health > 0:
            self.color = Back.RED + Fore.BLACK
            self.back_array[self.x][self.y] = count
            self.array[self.x][self.y] = self.color + 'w' + Style.RESET_ALL
        elif self.health <= 0:
            self.destroy()

    def get_health(self):
        return self.health

    def destroy(self):
        for i in range(self.height):
            for j in range(self.width):
                self.array[self.y][self.x] = blank
                self.back_array[self.y][self.x] = " "


    