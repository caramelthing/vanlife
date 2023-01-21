#! /usr/bin/env python3

import random

def lucky8ball(crazynumber):
    if crazynumber == 1:
        return "white mirrors"
    elif crazynumber == 2:
        return "green mirrors"
    elif crazynumber == 3:
        return "One white and one green mirror"
    elif crazynumber == 4:
        return "mirrors same colour as the wheels"

print(lucky8ball(random.randint(1,4)))