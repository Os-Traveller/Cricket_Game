import os
import random
import time


def play(over, run, wicket, extra):
    ball = 1;
    while ball <= over * 6:
        # generating random number for play making
        os.system('clear')
        rand_num = random.randint(0, 7)
        if rand_num == 5:
            extra += 1
            run += 1
        elif rand_num == 7:
            wicket += 1
        else:
            run += rand_num

        print(run, "/", wicket)
        time.sleep(0.5)
        ball += 1
