# Quick Picks

import random

NUMBERS_PER_LINE = 6
UPPER_LIMIT = 45
LOWER_LIMIT = 1
quick_pick = []

quick_picks_amount = int(input("How many quick picks?: "))

for i in range(quick_picks_amount):
    quick_pick = []
    for j in range(NUMBERS_PER_LINE):
        number = random.randint(LOWER_LIMIT, UPPER_LIMIT)
        while number in quick_pick:
            number = random.randint(LOWER_LIMIT, UPPER_LIMIT)
        quick_pick.append(number)
    quick_pick.sort()
    print(" ".join("{:2}".format(number) for number in quick_pick))


