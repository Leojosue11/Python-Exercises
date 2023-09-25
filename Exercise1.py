import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)
    return roll

while True:
    players = input("Enter the number of players (1-4): ")
    if players.isdigit():
        players = int(players)
        if players >= 1 and players <= 4 :
            break
        else:
            print("Must be between 1 - 4 players")
            
    else:
        print("Invalid, Insert a number. Try again")      

max_score = 20
player_score = [0 for _ in range(players)]
win = False
real_score = 0

while max(player_score) < max_score :
    
    for player_idx in range(players) :
        print("\nPlayer number", player_idx + 1,  "turn has just started")
        print("Your total score is: ", player_score[player_idx], "\n")
        current_score = 0
        
        while True :  
            should_roll = input("Would you like to roll (y): ")
            if should_roll.lower() != "y" :
                break
            value = roll()
            if value == 1 :
                print("You rolled a 1! Turn done!")
                break
            else:
                current_score += value
                real_score = player_score[player_idx] + current_score
                print("You rolled a: ", value)
                print("Your score is:", current_score)
                if real_score > max_score :
                    print("You have passed the max number, your score will be restarted")
                    player_score[player_idx] = 0
                    current_score = 0
                    break
                elif real_score == max_score :
                    print("you won the game")
                    win = True
                    break
                
        player_score[player_idx] += current_score
        if win == True :
            break
            
max_score = max(player_score)
player_winning = player_score.index(max_score)
print("Player number: ", player_winning + 1 , "is the winner with a score of: ", max_score, "\n" )