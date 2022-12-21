import play
import random
import team

team1 = team.team1
team2 = team.team2
over = int(input("Over : "))
toss = random.randint(1, 2)
innings = 1

if toss % 2 == 0:
    team1["batting"] = True
    team2["bolwing"] = True
else:
    team2["batting"] = True
    team1["bowling"] = True

play.play(over, team1, team2)
