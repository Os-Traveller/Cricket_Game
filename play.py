import playMaking


def play(over, team1, team2):
    # start function
    innings = 1
    target = 0
    # finding whose team is batting first
    if team1["batting"]:
        print("\t\t******* team1 batting *******\n")
        playMaking.play_making(over, team1, team2, innings, target)

    else:
        print("\t\t******* team2 batting *******\n")
        playMaking.play_making(over, team2, team1, innings, target)

    # finding if it's the first innings or second innings
    # end Function
