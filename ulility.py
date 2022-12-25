def show_run(over, ball, outcome, run, wicket, batter_name, batter_run, ball_faced):
    over_str = str(over - 1) + "." + str(ball)
    player_str = batter_name + " [Run : " + str(batter_run) + " Ball : " + str(ball_faced) + " ]"
    
    print("\t" + formatter(over_str, 10) + formatter(str(outcome), 10) + formatter(str(run) + "/" + str(wicket), 10) + player_str)


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
            print("\t[" + str(i) + "] :", batter[i]["name"])
        i += 1
    
 
def formatter(content, total_space):
    temp_str = content
    i = 1
    while(i <= total_space - len(content)):
        temp_str += " "
        i += 1
        
    return temp_str
     
    
def score_card(team):
    print("\n\t\t\t *****", team["name"], "*****\n")
    print("\t" + formatter("Player Name", 20) + formatter("Run", 8) + formatter("Ball", 8), "Strike Rate\n")
    
    batters = team["players"]
    i = 0
    while(i < len(batters)):
        if batters[i]["batting"]:
            name = batters[i]["name"]
            run = batters[i]["run"]
            ball = batters[i]["ball_faced"]
            
            strike_rate = 0.0
            if ball > 0:
                strike_rate = round(run * 100 / ball, 2)
                
            print("\t" + formatter(name, 20) + formatter(str(run), 8) + formatter(str(ball), 8), strike_rate)
        
        # condition ends
        i += 1
    # loop ends
    team_ball = team["ball"]
    over = str(int(team_ball / 6))
    over += "." + str(team_ball % 6)
    extra = team["extra"]
    total_run = team["total_run"]
    wicket = team["wicket"]
    
    print("\n\tOver :", over, "\tExtra :", extra, "\tTotal :", total_run, "/", wicket, "\n")
    
    