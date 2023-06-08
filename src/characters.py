import os
import numpy as np
from pandas import array
import colorama
from colorama import Fore, Back, Style
colorama.init()
import json
from buildings import *

blank = Fore.RED + Back.GREEN + " " + Style.RESET_ALL


class characters():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.village_name = "village"
        self.color = Fore.RED + Back.BLACK

    def attack(self, y, x):
        return self.back_array[y][x]

class king(characters):
    def __init__(self, x, y, village1):
        self.x = x
        self.y = y
        self.type = "king"
        self.char = "K"
        self.array = village1.array
        self.back_array = village1.back_array
        self.color = Fore.RED + Back.BLACK
        self.village1 = village1
        self.damage = 10
        self.health = 100
        self.spawn_king(village1)

    def spawn_king(self, village1):
        # if(self.array[self.y+1][self.x] == blank):
        #     self.array[self.y][self.x] = self.color + self.char  + Style.RESET_ALL
        #     self.array[self.y][self.x+1] = self.color + ">"  + Style.RESET_ALL
        village1.array[self.y][self.x] = self.color + \
            self.char + Style.RESET_ALL
        village1.back_array[self.y][self.x] = self.char

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_damage(self):
        return self.damage

    def get_health(self):
        return self.health

    def add_health(self, health):
        self.health = health
        self.health_bar()

    def move_up(self):
        if(self.array[self.y-1][self.x] == blank):
            self.array[self.y][self.x] = blank
            self.back_array[self.y][self.x] = " "
            self.y -= 1
            self.spawn_king(self.village1)

    def move_down(self):
        if(self.array[self.y+1][self.x] == blank):
            self.array[self.y][self.x] = blank
            self.back_array[self.y][self.x] = " "
            self.y += 1
            self.spawn_king(self.village1)

    def move_left(self):
        if(self.array[self.y][self.x-1] == blank):
            self.array[self.y][self.x] = blank
            self.back_array[self.y][self.x] = " "
            self.x -= 1
            self.spawn_king(self.village1)

    def move_right(self):
        if(self.array[self.y][self.x+1] == blank):
            self.array[self.y][self.x] = blank
            self.back_array[self.y][self.x] = " "
            self.x += 1
            self.spawn_king(self.village1)

    def attack(self):
        return self.back_array[self.y][self.x+1]

    def reduce_health(self, damage, replay):
        self.health = self. health - damage
        if self.health < 0:
            self.health = 0
            self.king_death(replay)
        self.health_bar()

    def health_bar(self):
        print("King health: " + str(self.health))
        health_bar = ""
        for i in range(int(self.health/10)):
            if i < 2:
                health_bar += Fore.RED + "██" + Style.RESET_ALL
            elif i < 5:
                health_bar += Fore.LIGHTYELLOW_EX + "██" + Style.RESET_ALL
            elif i <= 10:
                health_bar += Fore.GREEN + "██" + Style.RESET_ALL
        print(health_bar)

    def king_death(self,replay):
        self.array[self.y][self.x] = blank
        self.back_array[self.y][self.x] = " "
        print("King is dead")

        # input file name
        input_file = input('Save game as: ')
        if(input_file == 'q'):
            quit()


        # store input array in a json file in a folder
        with open(input_file + '.json', 'w') as outfile:
            json.dump(replay, outfile)
        quit()

    def king_death_1(self):
        self.array[self.y][self.x] = blank
        self.back_array[self.y][self.x] = " "
        print("King is dead, You lose!!")

    def reduce_health_1(self, damage):
        self.health = self. health - damage
        if self.health < 0:
            self.health = 0
            self.king_death_1()
        self.health_bar()

    def lattack(self, village1, townhall1, hut1, hut2, hut3, hut4, hut5, cannon1, cannon2, wall1):
        dist_x = hut1.get_x() - self.x
        dist_y = hut1.get_y() - self.y
        dist = dist_x**2 + dist_y**2
        if dist <= 25:
            hut1.reduce_health(self.damage)

        dist_x = hut2.get_x() - self.x
        dist_y = hut2.get_y() - self.y
        dist = dist_x**2 + dist_y**2
        if dist <= 25:
            hut2.reduce_health(self.damage)

        dist_x = hut3.get_x() - self.x
        dist_y = hut3.get_y() - self.y
        dist = dist_x**2 + dist_y**2
        if dist <= 25:
            hut3.reduce_health(self.damage)

        dist_x = hut4.get_x() - self.x
        dist_y = hut4.get_y() - self.y
        dist = dist_x**2 + dist_y**2
        if dist <= 25:
            hut4.reduce_health(self.damage)

        dist_x = hut5.get_x() - self.x
        dist_y = hut5.get_y() - self.y
        dist = dist_x**2 + dist_y**2
        if dist <= 25:
            hut5.reduce_health(self.damage)

        dist_x = cannon1.get_x() - self.x
        dist_y = cannon1.get_y() - self.y
        dist = dist_x**2 + dist_y**2
        if dist <= 25:
            cannon1.reduce_health(self.damage)

        dist_x = cannon2.get_x() - self.x
        dist_y = cannon2.get_y() - self.y
        dist = dist_x**2 + dist_y**2
        if dist <= 25:
            cannon2.reduce_health(self.damage)

        dist_x = townhall1.get_x() - self.x
        dist_y = townhall1.get_y() - self.y
        dist = dist_x**2 + dist_y**2
        if dist <= 25:
            townhall1.reduce_health_1(self.damage)

class barbarian(characters):
    def __init__(self, x, y, village1):
        self.x = x
        self.y = y
        self.type = "barbarian"
        self.char = "B"
        self.array = village1.array
        self.back_array = village1.back_array
        self.color = Fore.RED + Back.BLACK
        self.village1 = village1
        self.damage = 10
        self.health = 100
        # self.spawn_barbarian(village1)

    def spawn_barbarian(self, village1):
        # if(self.array[self.y+1][self.x] == blank):
        #     self.array[self.y][self.x] = self.color + self.char  + Style.RESET_ALL
        #     self.array[self.y][self.x+1] = self.color + ">"  + Style.RESET_ALL
        village1.array[self.y][self.x] = self.color + \
            self.char + Style.RESET_ALL
        village1.back_array[self.y][self.x] = self.char

    def get_closest_enemy(self, village1, townhall1, hut1, hut2, hut3, hut4, hut5, cannon1, cannon2, wall1):
        if not hut1.destroyed:
            dist_x = hut1.get_x() - self.x
            dist_y = hut1.get_y() - self.y
            dist1 = dist_x**2 + dist_y**2
        else:
            dist1 = 100000

        if not hut2.destroyed:
            dist_x = hut2.get_x() - self.x
            dist_y = hut2.get_y() - self.y
            dist2 = dist_x**2 + dist_y**2
        else:
            dist2 = 100000

        if not hut3.destroyed:
            dist_x = hut3.get_x() - self.x
            dist_y = hut3.get_y() - self.y
            dist3 = dist_x**2 + dist_y**2
        else:
            dist3 = 100000

        if not hut4.destroyed:
            dist_x = hut4.get_x() - self.x
            dist_y = hut4.get_y() - self.y
            dist4 = dist_x**2 + dist_y**2
        else:
            dist4 = 100000

        if not hut5.destroyed:
            dist_x = hut5.get_x() - self.x
            dist_y = hut5.get_y() - self.y
            dist5 = dist_x**2 + dist_y**2
        else:
            dist5 = 100000
        
        if not cannon1.destroyed:
            dist_x = cannon1.get_x() - self.x
            dist_y = cannon1.get_y() - self.y
            dist6 = dist_x**2 + dist_y**2
        else:
            dist6 = 100000

        if not cannon2.destroyed:
            dist_x = cannon2.get_x() - self.x
            dist_y = cannon2.get_y() - self.y
            dist7 = dist_x**2 + dist_y**2
        else:
            dist7 = 100000

        if not townhall1.destroyed:
            dist_x = townhall1.get_x() - self.x
            dist_y = townhall1.get_y() - self.y
            dist8 = dist_x**2 + dist_y**2
        else:
            dist8 = 100000

        closest = min(dist1, dist2, dist3, dist4, dist5, dist6, dist7, dist8)
        print(closest)
        if closest == dist1:
            structure = hut1
            return hut1
        elif closest == dist2:
            structure = hut2
            return hut2
        elif closest == dist3:
            structure = hut3
            return hut3
        elif closest == dist4:
            structure = hut4
            return hut4
        elif closest == dist5:
            structure = hut5
            return hut5
        elif closest == dist6:
            structure = cannon1
            return cannon1
        elif closest == dist7:
            structure = cannon2
            return cannon2
        elif closest == dist8:
            structure = townhall1
            return townhall1

    def give_damage(self, y, x, village1, townhall1, hut1, hut2, hut3, hut4, hut5, cannon1, cannon2, wall1):
        if self.attack(y,x) == "1":
            townhall1.reduce_health_1(self.get_damage())
        elif self.attack(y,x) == 2:
            hut1.reduce_health(self.get_damage())
        elif self.attack(y,x) == 3:
            hut2.reduce_health(self.get_damage())
        elif self.attack(y,x) == 4:
            hut3.reduce_health(self.get_damage())
        elif self.attack(y,x) == 5:
            hut4.reduce_health(self.get_damage())
        elif self.attack(y,x) == 6:
            hut5.reduce_health(self.get_damage())
        elif self.attack(y,x) == 7:
            cannon1.reduce_health(self.get_damage())
        elif self.attack(y,x) == 8:
            cannon2.reduce_health(self.get_damage())
        elif self.attack(y,x) == range(9,137):
            wall1[self.attack(y,x)-8].reduce_health(self.get_damage(), self.attack())

    def move(self,village1, townhall1, hut1, hut2, hut3, hut4, hut5, cannon1, cannon2, wall1):
        nearest = self.get_closest_enemy(village1, townhall1, hut1, hut2, hut3, hut4, hut5, cannon1, cannon2, wall1)

        if self.x < nearest.x:
            if village1.back_array[self.y][self.x+1] == " " or village1.back_array[self.y][self.x+1] == "B" or village1.back_array[self.y][self.x+1] == "K":
                village1.array[self.y][self.x] = blank
                village1.array[self.y][self.x+1] = self.color + self.char + Style.RESET_ALL
                village1.back_array[self.y][self.x] = ' '
                village1.back_array[self.y][self.x+1] = self.char
                self.x += 1
            else:
                self.give_damage(self.y, self.x+1, village1, townhall1, hut1, hut2, hut3, hut4, hut5, cannon1, cannon2, wall1)
        elif self.x > nearest.x:
            if village1.back_array[self.y][self.x-1] == " " or village1.back_array[self.y][self.x-1] == "B" or village1.back_array[self.y][self.x-1] == "K":
                village1.array[self.y][self.x] = blank
                village1.array[self.y][self.x-1] = self.color + self.char + Style.RESET_ALL
                village1.back_array[self.y][self.x] = ' '
                village1.back_array[self.y][self.x-1] = self.char
                self.x -= 1
            else:
                self.give_damage(self.y, self.x-1, village1, townhall1, hut1, hut2, hut3, hut4, hut5, cannon1, cannon2, wall1)
        elif self.y < nearest.y:
            if village1.back_array[self.y+1][self.x] == " " or village1.back_array[self.y+1][self.x] == "B" or village1.back_array[self.y+1][self.x] == "K":
                village1.array[self.y][self.x] = blank
                village1.array[self.y+1][self.x] = self.color + self.char + Style.RESET_ALL
                village1.back_array[self.y][self.x] = ' '
                village1.back_array[self.y+1][self.x] = self.char
                self.y += 1
            else:
                self.give_damage(self.y+1, self.x, village1, townhall1, hut1, hut2, hut3, hut4, hut5, cannon1, cannon2, wall1)
        elif self.y > nearest.y:
            if village1.back_array[self.y-1][self.x] == " " or village1.back_array[self.y-1][self.x] == "B" or village1.back_array[self.y-1][self.x] == "K":
                village1.array[self.y][self.x] = blank
                village1.array[self.y-1][self.x] = self.color + self.char + Style.RESET_ALL
                village1.back_array[self.y][self.x] = ' '
                village1.back_array[self.y-1][self.x] = self.char
                self.y -= 1
            else:
                self.give_damage(self.y-1, self.x, village1, townhall1, hut1, hut2, hut3, hut4, hut5, cannon1, cannon2, wall1)
    
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_damage(self):
        return self.damage

    def get_health(self):
        return self.health

    def move_up(self):
        if(self.array[self.y-1][self.x] == blank):
            self.array[self.y][self.x] = blank
            self.back_array[self.y][self.x] = " "
            self.y -= 1
            self.spawn_king(self.village1)

    def move_down(self):
        if(self.array[self.y+1][self.x] == blank):
            self.array[self.y][self.x] = blank
            self.back_array[self.y][self.x] = " "
            self.y += 1
            self.spawn_king(self.village1)

    def move_left(self):
        if(self.array[self.y][self.x-1] == blank):
            self.array[self.y][self.x] = blank
            self.back_array[self.y][self.x] = " "
            self.x -= 1
            self.spawn_king(self.village1)

    def move_right(self):
        if(self.array[self.y][self.x+1] == blank):
            self.array[self.y][self.x] = blank
            self.back_array[self.y][self.x] = " "
            self.x += 1
            self.spawn_king(self.village1)

    def reduce_health(self, damage, replay):
        self.health = self. health - damage
        if self.health < 0:
            self.health = 0
            self.king_death(replay)
        self.health_bar()

    def health_bar(self):
        print("King health: " + str(self.health))
        health_bar = ""
        for i in range(int(self.health/10)):
            if i < 2:
                health_bar += Fore.RED + "██" + Style.RESET_ALL
            elif i < 5:
                health_bar += Fore.LIGHTYELLOW_EX + "██" + Style.RESET_ALL
            elif i <= 10:
                health_bar += Fore.GREEN + "██" + Style.RESET_ALL
        print(health_bar)

    def king_death(self,replay):
        self.array[self.y][self.x] = blank
        self.back_array[self.y][self.x] = " "
        print("King is dead")

        # input file name
        input_file = input('Save game as: ')


        # store input array in a json file in a folder
        with open(input_file + '.json', 'w') as outfile:
            json.dump(replay, outfile)
        quit()

    def king_death_1(self):
        self.array[self.y][self.x] = blank
        self.back_array[self.y][self.x] = " "
        print("King is dead")

    def reduce_health_1(self, damage):
        self.health = self. health - damage
        if self.health < 0:
            self.health = 0
            self.king_death_1()
        self.health_bar()
