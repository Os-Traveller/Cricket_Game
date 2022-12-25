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
     
    print("******* Pick Your Two Batter *******\n")
    batter = batting_team["players"]

    i = 0
    while i < len(batter):
        print("[" + str(i) + "] :", batter[i]["name"])
        i += 1

    striker_position = 0
    non_striker_position = 1
    
    # handleing invalid position for any batter
    while(1):        
        striker_position = int(input("\nBatter 1 : "))    
        if striker_position < 0 or striker_position > 10 :
            print("\n\t*** Invaliad Choice, Try Again ***")
            continue
        else:
            break
    
    while(1):
        non_striker_position = int(input("Batter 2: "))
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
    print("\nBall\t Outcome\t Score\t\t Batter")
    
    while over <= total_over:
        # start loop
        # generating random number for play making
        rand_num = random.randint(0, 8)
        
        if free_hit:
            print("\n\t\t*** Free Hit ***\n")

        if rand_num == 5:
            if not free_hit:
                wicket += 1
                batting_team["wicket"] += 1
                batting_team["players"][striker_position]["ball_faced"] += 1
                outcome = "OUT"
                ulility.show_run(ball, outcome, run, wicket, batting_team["players"][striker_position]["name"],
                         batting_team["players"][striker_position]["run"], batting_team["players"][striker_position]["ball_faced"])
            
                ulility.batter_out(striker_position, batting_team)
                
                # finishind innings when team all out
                if wicket == 10:
                    print("\t\t***", batting_team["name"],"All Out!! ***\n")
                    break
                
                # making sure a batsman can not bat twice
                while(1):
                    striker_position = int(input("\nNext Batter : "))
                    if(batting_team["players"][striker_position]["batting"]):
                        print("\n*** A batter can not bat twice ***")
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
            ulility.show_run(ball, outcome, run, wicket, batting_team["players"][striker_position]["name"],
                         batting_team["players"][striker_position]["run"], batting_team["players"][striker_position]["ball_faced"])

        elif rand_num == 8:
            extra += 1
            run += 1
            outcome = "No Ball"
            free_hit = True
            previous_outcome = "No Ball"
            ulility.show_run(ball, outcome, run, wicket, batting_team["players"][striker_position]["name"],
                         batting_team["players"][striker_position]["run"], batting_team["players"][striker_position]["ball_faced"])

        else:
            run += rand_num
            batting_team["players"][striker_position]["ball_faced"] += 1
            batting_team["players"][striker_position]["run"] += rand_num
            outcome = rand_num
            previous_outcome = ""
            if rand_num == 1 or rand_num == 3:
                # swapping batters position
                temp = striker_position
                striker_position = non_striker_position
                non_striker_position = temp
                ulility.show_run(ball, outcome, run, wicket, batting_team["players"][striker_position]["name"],
                         batting_team["players"][striker_position]["run"], batting_team["players"][striker_position]["ball_faced"])

            else:
                ulility.show_run(ball, outcome, run, wicket, batting_team["players"][striker_position]["name"],
                         batting_team["players"][striker_position]["run"], batting_team["players"][striker_position]["ball_faced"])

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
    # end of the function
