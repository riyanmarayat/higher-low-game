import random

from game_data import data
import art

def call_object():
    object = []
    object1 = random.choice(data)
    object2 = random.choice(data)
    while object1['name'] == object2['name']:
        object1 = random.choice(data)
        object2 = random.choice(data)
    object.append(object1)
    object.append(object2)
    return object

object = call_object()
score = 0
is_player_win = None
is_playing = True
while is_playing:
    print(art.logo)
    if is_player_win == True:
        score += 1
        print(f"You're right! Current score: {score}.")
    elif is_player_win == False:
        print(f"Sorry, that's wrong. Final score: {score}")
        player_input = input("Do you want play game again? Type 'Y' to play again or 'N' to exit: ").lower()
        if player_input == "y":
            object = call_object()
            score = 0
            is_player_win = None
            continue
        else:
            print("\033[2J\033[H", end="", flush=True) #clear console
            break
    else:
        print(f"Current score: {score}.")
    print(f"Compare A: {object[0]['name']}, a {object[0]['description']}, from {object[0]['country']}.")
    print(f"\n{art.vs}")
    print(f"Against B: {object[1]['name']}, a {object[1]['description']}, from {object[1]['country']}.")
    player_input = input("Who has more followers? Type 'A' or 'B': ").lower()
    if int(object[0]['follower_count']) >= int(object[1]['follower_count']):
        answer = "a"
    else:
        answer = "b"

    if answer == player_input:
        is_player_win = True
    else:
        is_player_win = False
    object.pop(0)
    add_object = random.choice(data)
    while object[0] == add_object:
        add_object = random.choice(data)
    object.append(add_object)
    print("\033[2J\033[H", end="", flush=True) #clear console