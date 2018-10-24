def validate(hand):
    if hand < 0 or hand > 2:
        return False
    else:
        return True
   #return True

def print_hand(hand, name="GUEST"):
    hands = ["ROCK", "SCISSORS", "PAPER"]
    print(name + " chose " + hands[hand]) 



print("LET'S GET STARTED 'ROCK SCISSORS PAPER' GAME!!")
player_name = input("PUT YOUR NAME HERE:")

print("WHAT WOULD YOU GIVE? (0: ROCK  1: SCISSORS  2: PAPER)")
player_hand = int(input("YOU CHOOSE A NUMBER:"))

if validate(player_hand):
    if player_name == "" :
        print_hand(player_hand)
    else:
        print_hand(player_hand, player_name)
else:
    print("PUT CORRECT NUMBER")