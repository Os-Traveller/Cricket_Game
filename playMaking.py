import random
import time


def play_making(total_over, batting_team, bowling_team, innings, target):
    # start function
    over = 1
    ball = 1
    wicket = 0
    extra = 0
    run = 0
    batting_position = [0, 1]
    strike_position = 0
    last_batter_position = 1
    outcome = ""
    print("Run\t Outcome\t Score\t\t Batter")
    while over <= total_over:
        # start loop
        # generating random number for play making
        rand_num = random.randint(0, 8)
        if rand_num == 5:
            wicket += 1

        elif rand_num == 7:
            extra += 1
            run += 1
            outcome = "Wide"
            previous_outcome = "Wide"

        elif rand_num == 8:
            extra += 1
            run += 1
            outcome = "No Ball"
            previous_outcome = "No Ball"

        else:
            run += rand_num
            outcome = rand_num
            previous_outcome = ""

        # fixing white space
        if run < 10:
            if outcome == "No Ball":
                print(ball, "\t", outcome, "\t", run, "/", wicket, "\t\t",
                      batting_team["players"][strike_position]["name"])
            else:
                print(ball, "\t", outcome, "\t\t", run, "/", wicket, "\t\t",
                      batting_team["players"][strike_position]["name"])
        else:
            if outcome == "No Ball":
                print(ball, "\t", outcome, "\t", run, "/", wicket, "\t",
                      batting_team["players"][strike_position]["name"])
            else:
                print(ball, "\t", outcome, "\t\t", run, "/", wicket, "\t",
                      batting_team["players"][strike_position]["name"])

        time.sleep(0.2)

        if previous_outcome == "":
            ball += 1
            if ball > 6:
                over += 1
                ball = 1
        # end loop

    # end of the function
