import random
import time
import ulility


def play_making(total_over, batting_team, bowling_team, innings, target):
    # start function
    over = 1
    ball = 1
    wicket = 0
    extra = 0
    run = 0
     
    print("\t******* Pick Your Two Batter *******\n")
    batter = batting_team["players"]

    i = 0
    while i < len(batter):
        print("\t[" + str(i) + "] :", batter[i]["name"])
        time.sleep(0.05)
        i += 1

    striker_position = 0
    non_striker_position = 1
    
    # handleing invalid position for any batter
    while(1):        
        striker_position = int(input("\n\tBatter 1 : "))    
        if striker_position < 0 or striker_position > 10 :
            print("\n\t*** Invaliad Choice, Try Again ***")
            continue
        else:
            break
    
    while(1):
        non_striker_position = int(input("\tBatter 2: "))
        if non_striker_position < 0 or non_striker_position > 10:
            print("\n\t*** Invaliad Choice, Try Again ***")
            continue
        else:
            break
            
    # making sure a batter can't bat twice
    batting_team["players"][striker_position]["batting"] = True
    batting_team["players"][non_striker_position]["batting"] = True
    
    previous_outcome = ""
    free_hit = False
    formatter = ulility.formatter
    print("\n\t" + formatter("Over", 10) + formatter("Outcome", 10) + formatter("Run", 10), "Player\n")
    
    # games starts here 
    while over <= total_over:
        # start loop
        # generating random number for play making
        rand_num = random.randint(0, 8)
        
        if free_hit:
            print("\n\t*** Free Hit ***\n")

        if rand_num == 5:
            if not free_hit:
                wicket += 1
                batting_team["wicket"] += 1
                batting_team["players"][striker_position]["ball_faced"] += 1
                outcome = "OUT"
                
                # necessary variables
                player_name = batting_team["players"][striker_position]["name"]
                players_run = batting_team["players"][striker_position]["run"]
                player_ball = batting_team["players"][striker_position]["ball_faced"]
                
                ulility.show_run(over, ball, outcome, run, wicket, player_name, players_run, player_ball)
            
                ulility.batter_out(striker_position, batting_team)
                
                # finishind innings when team all out
                if wicket == 10:
                    print("\t\t***", batting_team["name"],"All Out!! ***\n")
                    break
                
                # making sure a batsman can not bat twice
                while(1):
                    striker_position = int(input("\n\tNext Batter : "))
                    if(batting_team["players"][striker_position]["batting"]):
                        print("\n\t*** A batter can not bat twice ***")
                        continue
                    else:
                        break
                    
                print("")
                batting_team["players"][striker_position]["batting"] = True
                
        elif rand_num == 7:
            extra += 1 
            run += 1
            outcome = "Wide"
            previous_outcome = "Wide"
            
            # necessary variables
            player_name = batting_team["players"][striker_position]["name"]
            players_run = batting_team["players"][striker_position]["run"]
            player_ball = batting_team["players"][striker_position]["ball_faced"]
            
            ulility.show_run(over, ball, outcome, run, wicket, player_name, players_run, player_ball)

        elif rand_num == 8:
            extra += 1
            run += 1
            outcome = "No Ball"
            free_hit = True
            previous_outcome = "No Ball"
            
            # necessary variables
            player_name = batting_team["players"][striker_position]["name"]
            players_run = batting_team["players"][striker_position]["run"]
            player_ball = batting_team["players"][striker_position]["ball_faced"]
            
            ulility.show_run(over, ball, outcome, run, wicket, player_name, players_run, player_ball)

        else:
            run += rand_num
            batting_team["players"][striker_position]["ball_faced"] += 1
            batting_team["players"][striker_position]["run"] += rand_num
            outcome = rand_num
            previous_outcome = ""
            if rand_num == 1 or rand_num == 3:
                # necessary variables
                player_name = batting_team["players"][striker_position]["name"]
                players_run = batting_team["players"][striker_position]["run"]
                player_ball = batting_team["players"][striker_position]["ball_faced"]
                
                # swapping batters position
                temp = striker_position
                striker_position = non_striker_position
                non_striker_position = temp
                
                ulility.show_run(over, ball, outcome, run, wicket, player_name, players_run, player_ball)

            else:
                # necessary variables
                player_name = batting_team["players"][striker_position]["name"]
                players_run = batting_team["players"][striker_position]["run"]
                player_ball = batting_team["players"][striker_position]["ball_faced"]
                
                ulility.show_run(over, ball, outcome, run, wicket, player_name, players_run, player_ball)

        # fixing white space
        time.sleep(0.05)
        if previous_outcome != "No Ball" and free_hit:
            free_hit = False

        if previous_outcome == "":
            ball += 1
            batting_team["ball"] += 1
            if ball > 6:
                print("\n\t*** Over :", over, "finished ***\n")
                over += 1
                ball = 1
                # swaping batter's position after over is finished 
                temp = striker_position
                striker_position = non_striker_position
                non_striker_position = temp
                if over < total_over:
                    # checking if last over
                    print("\t*** Starting over", over, "***\n")
        # all out 
        # target chase 
        if innings == 2:
            if run > target:
                break
        # end loop
    batting_team["total_run"] = run
    batting_team["extra"] = extra
    # end of the function
