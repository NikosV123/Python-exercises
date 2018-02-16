# -*- coding: utf-8 -*-
from random import randrange
the_rest_of_the_numbers = []
player = []
all_players = []
number_of_numbers_to_take_for_win = 0
finish = 0
for i in range (1,81):
    the_rest_of_the_numbers.append(i)
for j in range (0,100):
    for k in range (1,6):
        player.append(randrange(1,81))
    all_players.append(player)
    player = []
for h in range (0,999):
    while(1==1):
        if (len(the_rest_of_the_numbers) != 0):
            take = randrange(len(the_rest_of_the_numbers))
            take = the_rest_of_the_numbers.pop(take - 1)
        number_of_numbers_to_take_for_win = number_of_numbers_to_take_for_win + 0.001
        for y in range (0,100):
            if take in all_players[y]:
                if (len(all_players[y]) > 1):
                    all_players[y].remove(take)
                else:
                    finish = 1
                    break
        if (finish == 1):
            finish = 0
            break
    the_rest_of_the_numbers = []
    for i in range (1,81):
        the_rest_of_the_numbers.append(i)
print number_of_numbers_to_take_for_win
