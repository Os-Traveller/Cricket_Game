import playMaking
import ulility


def play(over, team1, team2):
    # start function
    innings = 1
    target = 0
    
    # finding whose team is batting first
    print("")
    if team1["batting"]:
        print("*******", team1["name"], "batting *******\n")
        playMaking.play_making(over, team1, team2, innings, target)
        target = team1["total_run"] + 1
        print("\n***", team2["name"], "needs", target, "runs of", over, "overs to win ***\n")
        innings = 2
        
        print("*******", team2["name"], "batting *******\n")
        playMaking.play_making(over, team2, team1, innings, target)
        
        # score card
        ulility.score_card(team1)
        ulility.score_card(team2)
        
        # chosing winner
        if team1["total_run"] > team2["total_run"]:
            print("\n\t***",team1["name"],"Won By",team1["total_run"] - team2["total_run"], "run ***\n")
        elif team2["total_run"] > team1["total_run"]:
            print("\n\t***", team2["name"],"Won By", 10 - team2["wicket"], "Wicket ***\n")
        else:
            print("\n\t*** Match Tied ***\n")
        
    else:
        print("*******", team2["name"], "batting *******\n")
        playMaking.play_making(over, team2, team1, innings, target)
        target = team2["total_run"] + 1
        print("\n***", team1["name"], "needs", target, "runs of", over, "overs to win ***\n")
        innings = 2
        
        print("*******", team1["name"], "batting *******\n")
        playMaking.play_making(over, team1, team2, innings, target)
        
        # score card 
        ulility.score_card(team2)
        ulility.score_card(team1)
        
        # chossing winner
        if team2["total_run"] > team1["total_run"]:
            print("\n\t***",team2["name"],"Won By",team2["total_run"] - team1["total_run"], "run ***\n")
        elif team1["total_run"] > team2["total_run"]:
            print("\n\t***", team1["name"],"Won By", 10 - team1["wicket"], "Wicket ***\n")
        else:
            print("\n\t*** Match Tied ***\n")
    # end Function
