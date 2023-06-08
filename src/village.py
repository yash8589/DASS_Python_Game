import os
import numpy as np
from pandas import array
import colorama
from colorama import Fore, Back, Style
colorama.init()


class village():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.village_name = "village"
        self.color = Fore.RED + Back.GREEN
        self.init_array()

    def init_array(self):
        self.array = [[" " for i in range(self.x)] for j in range(self.y)]
        self.back_array = [[" " for i in range(self.x)] for j in range(self.y)]
        self.make_border()

    def make_border(self):
        for i in range(self.x):
            for j in range(self.y):
                self.array[j][i] = self.color + " "+ Style.RESET_ALL

        for i in range(self.x):
            self.array[0][i] = self.color+"X"+Style.RESET_ALL
            self.array[self.y-1][i] = self.color+"X"+Style.RESET_ALL

        for j in range(self.y):
            self.array[j][0] = self.color+"X"+Style.RESET_ALL
            self.array[j][self.x-1] = self.color + "X"+    Style.RESET_ALL

        

        # make border for back_array
        for i in range(self.x):
            for j in range(self.y):
                self.back_array[j][i] =" "
        for i in range(self.x):
            self.back_array[0][i] = "-"
            self.back_array[self.y-1][i] = "-"
        for j in range(self.y):
            self.back_array[j][0] = "|"
            self.back_array[j][self.x-1] = "|"
        

    def print_array(self):
        os.system('clear')
        for i in range(self.y):
            for j in range(self.x):
                print(self.array[i][j], end="")
            print("")

    def print_back_array(self):
        for i in range(self.y):
            for j in range(self.x):
                print(self.back_array[i][j], end="")
            print("")
        
            