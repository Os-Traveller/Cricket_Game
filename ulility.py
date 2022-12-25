def show_run(ball, outcome, run, wicket, batter_name, batter_run, ball_faced):
    if run < 10:
        if outcome == "No Ball":
            print(ball, "\t", outcome, "\t", run, "/", wicket, "\t\t",
                  batter_name, "[Run:", batter_run, "* Balls :", str(ball_faced) + "]")
        else:
            print(ball, "\t", outcome, "\t\t", run, "/", wicket, "\t\t",
                  batter_name, "[Run:", batter_run, "* Balls :", str(ball_faced) + "]")
    else:
        if outcome == "No Ball":
            print(ball, "\t", outcome, "\t", run, "/", wicket, "\t",
                  batter_name, "[Run:", batter_run, "* Balls :", str(ball_faced) + "]")
        else:
            print(ball, "\t", outcome, "\t\t", run, "/", wicket, "\t",
                  batter_name, "[Run:", batter_run, "* Balls :", str(ball_faced) + "]")


def batter_out(position, batting_team):
    batting_team["players"][position]["out"] = True
    batter_name = batting_team["players"][position]["name"]
    batter_run = batting_team["players"][position]["run"]
    ball_faced = batting_team["players"][position]["ball_faced"]
    
    print("\n\tWicket !!",
          batter_name, "* Run :", batter_run, "* Ball Faced",
          ball_faced,"* SR :", round(batter_run/ball_faced * 100, 2), "\n")
    
    batter = batting_team["players"]
    i = 0
    while(i < len(batter)):
        if(not batter[i]["batting"]):
            print("[" + str(i) + "] :", batter[i]["name"])
        i += 1
    
    
def score_card(team):
    print(team["ball"])