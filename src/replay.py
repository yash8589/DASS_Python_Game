# from characters import *
# from input import *
# from buildings import *
# from village import *
# import os
# import numpy as np
# from pandas import array
# import colorama
# from colorama import Fore, Back, Style
# colorama.init()
# import json
# import time

# village1 = village(80, 40)

# # take input file as input
# input_file = input("Enter saved game name: ")

# # import array from saved json file
# with open(input_file + '.json') as json_file:
#     replay = json.load(json_file)

# townhall1 = Townhall(40, 20, village1)

# hut1 = Huts(25, 15, village1, 2)
# hut2 = Huts(55, 15, village1, 3)
# hut3 = Huts(40, 10, village1, 4)
# hut4 = Huts(30, 25, village1, 5)
# hut5 = Huts(50, 25, village1, 6)

# cannon1 = Cannons(35, 20, village1, 7)
# cannon2 = Cannons(45, 20, village1, 8)

# king1 = king(10, 20, village1)

# for inp in replay:
   
#     time.sleep(0.1)
#     if(inp == 'q'):
#         break
#     if(inp == 'b'):
#         village1.print_back_array()
#     if(inp == 'w'):
#         king1.move_up()
#     if(inp == 's'):
#         king1.move_down()
#     if(inp == 'a'):
#         king1.move_left()
#     if(inp == 'd'):
#         king1.move_right()
#     if(inp == ' '):
#         if king1.attack() == "1":
#             townhall1.reduce_health_1(king1.get_damage())
#         elif king1.attack() == 2:
#             hut1.reduce_health(king1.get_damage())
#         elif king1.attack() == 3:
#             hut2.reduce_health(king1.get_damage())
#         elif king1.attack() == 4:
#             hut3.reduce_health(king1.get_damage())
#         elif king1.attack() == 5:
#             hut4.reduce_health(king1.get_damage())
#         elif king1.attack() == 6:
#             hut5.reduce_health(king1.get_damage())
#         elif king1.attack() == 7:
#             cannon1.reduce_health(king1.get_damage())
#         elif king1.attack() == 8:
#             cannon2.reduce_health(king1.get_damage())

#     if(cannon1.attack() == "K" and cannon2.attack == "K"):
#         king1.reduce_health_1(cannon1.get_damage() + cannon2.get_damage())
#     elif(cannon1.attack() == "K" or cannon2.attack() == "K"):
#         king1.reduce_health_1(cannon1.get_damage())
#     os.system('clear')
#     print("King's Coordinates", king1.attack())
    
    

#     village1.print_array()
#     print(king1.health_bar())

from itertools import count
from characters import *
from input import *
from buildings import *
from village import *
import os
import numpy as np
from pandas import array
import colorama
from colorama import Fore, Back, Style
colorama.init()

input_file = input("Enter saved game name: ")

# import array from saved json file
with open(input_file + '.json') as json_file:
    replay = json.load(json_file)

village1 = village(80, 40)

townhall1 = Townhall(40, 20, village1)

# barbarians
barbarian1 = barbarian(10,25,village1)
barbarian2 = barbarian(5,35,village1)
barbarian3 = barbarian(15,2,village1)
barbarians = [barbarian1,barbarian2,barbarian3]
barbarians_spawned = [False, False, False]


hut1 = Huts(25, 15, village1, 2)
hut2 = Huts(55, 15, village1, 3)
hut3 = Huts(40, 10, village1, 4)
hut4 = Huts(30, 25, village1, 5)
hut5 = Huts(50, 25, village1, 6)

cannon1 = Cannons(35, 20, village1, 7)
cannon2 = Cannons(45, 20, village1, 8)

wall1 = []
count1 = 8

b1, b2, b3 = False, False, False


# for j in range(20,60):
#     wall1.append(wall(5,j,village1, count1))
#     count1 += 1

# for j in range(5,30):
#     wall1.append(wall(j,20,village1, count1))
#     count1 += 1

# for j in range(20, 60):
#     wall1.append(wall(30,j,village1, count1))
#     count1 += 1

# for j in range(5,30):
#     wall1.append(wall(j,59,village1, count1))
#     count1 += 1

import time

king1 = king(10, 20, village1)



sleep_time = 0.5

for inp in replay:
    time.sleep(0.1)
    replay.append(inp)
    if(inp == 'q'):
        break
    if(inp == 'b'):
        village1.print_back_array()
        time.sleep(sleep_time)
    if(inp == 'w'):
        king1.move_up()
        time.sleep(sleep_time)
    if(inp == 's'):
        king1.move_down()
        time.sleep(sleep_time)
    if(inp == 'a'):
        king1.move_left()
        time.sleep(sleep_time)
    if(inp == 'd'):
        king1.move_right()
        time.sleep(sleep_time)
    if(inp == 'r'):             # rage spell
        sleep_time = 0
    if(inp == 'h'):             # heal spell
        curr = king1.get_health()
        if(curr < 100):
            new = curr + (curr*1.5)
            if(new > 100):
                new = 100
        king1.add_health(new)
    if(inp == '1'):
        unspawned = -1
        for i in range(len(barbarians)):
            if(barbarians_spawned[i] == False):
                unspawned = i
                break
        if unspawned == -1:
            continue
        barbarians[unspawned].x = 10
        barbarians[unspawned].y = 25
        barbarians[unspawned].spawn_barbarian(village1)
        structure = barbarian1.get_closest_enemy(village1, townhall1, hut1, hut2, hut3, hut4, hut5, cannon1, cannon2, wall1)
        barbarians_spawned[unspawned] = True
    if(inp == '2'):
        unspawned = -1
        for i in range(len(barbarians)):
            if(barbarians_spawned[i] == False):
                unspawned = i
                break
        if unspawned == -1:
            continue
        barbarians[unspawned].x = 5
        barbarians[unspawned].y = 35
        barbarians[unspawned].spawn_barbarian(village1)
        structure = barbarian1.get_closest_enemy(village1, townhall1, hut1, hut2, hut3, hut4, hut5, cannon1, cannon2, wall1)
        barbarians_spawned[unspawned] = True
    if(inp == '3'):
        unspawned = -1
        for i in range(len(barbarians)):
            if(barbarians_spawned[i] == False):
                unspawned = i
                break
        if unspawned == -1:
            continue
        barbarians[unspawned].x = 15
        barbarians[unspawned].y = 2
        barbarians[unspawned].spawn_barbarian(village1)
        structure = barbarian1.get_closest_enemy(village1, townhall1, hut1, hut2, hut3, hut4, hut5, cannon1, cannon2, wall1)
        barbarians_spawned[unspawned] = True
    if(inp == 'l'):
        king1.lattack(village1, townhall1, hut1, hut2, hut3, hut4, hut5, cannon1, cannon2, wall1)
    if(inp == ' '):
        if king1.attack() == "1":
            townhall1.reduce_health(king1.get_damage(), replay)
        elif king1.attack() == 2:
            hut1.reduce_health(king1.get_damage())
        elif king1.attack() == 3:
            hut2.reduce_health(king1.get_damage())
        elif king1.attack() == 4:
            hut3.reduce_health(king1.get_damage())
        elif king1.attack() == 5:
            hut4.reduce_health(king1.get_damage())
        elif king1.attack() == 6:
            hut5.reduce_health(king1.get_damage())
        elif king1.attack() == 7:
            cannon1.reduce_health(king1.get_damage())
        elif king1.attack() == 8:
            cannon2.reduce_health(king1.get_damage())
        elif king1.attack() == range(9,137):
            wall1[king1.attack()-8].reduce_health(king1.get_damage(), king1.attack())
        time.sleep(sleep_time)

    if(cannon1.attack() == "K" and cannon2.attack == "K"):
        king1.reduce_health(cannon1.get_damage() + cannon2.get_damage(),replay)
    elif(cannon1.attack() == "K" or cannon2.attack() == "K"):
        king1.reduce_health(cannon1.get_damage(),replay)


    for i, val in enumerate(barbarians_spawned):
        if val:
            barbarians[i].move(village1, townhall1, hut1, hut2, hut3, hut4, hut5, cannon1, cannon2, wall1)


    os.system('clear')



    print("King's Attack Coordinates", king1.attack())
    # print("wall 58", wall1[50].get_health())
       
    village1.print_array()
    print(king1.health_bar()) 
    
    if(townhall1.get_health() == 0 and hut1.get_health() == 0 and hut2.get_health() == 0 and hut3.get_health() == 0 and hut4.get_health() == 0 and hut5.get_health() == 0 and cannon1.get_health() == 0 and cannon2.get_health() == 0):
        print("You Win!")
        quit()

