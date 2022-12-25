import play
import random
import team

team1 = team.team1
team2 = team.team2

while(1):
    over = int(input("\n\tOver : "))
    if over > 0:
        break
    else:
        print("\n\t*** Over should be greater than 0 ***")
    
toss = random.randint(1, 2)
innings = 1

if toss % 2 == 0:
    team1["batting"] = True
    team2["bolwing"] = True
else:
    team2["batting"] = True
    team1["bowling"] = True

play.play(over, team1, team2)
