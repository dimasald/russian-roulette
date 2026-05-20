import random
import time

def start_game():
    print("---Game Started---")

def player_turn():
    global player_hp, bot_hp, turn, bullet_slot, bullet_position
    print(f"Your HP:{player_hp}")
    print(f"Bot HP:{bot_hp}")
    target_choice = input("Enemy or Self? (E or S): ")
    if target_choice == "E":
        print("You are going to shoot bot!")
        time.sleep(2)
        if bullet_slot == bullet_position:
            bot_hp -= 1
            bullet_slot = 1
            print("You got it right!")
            bullet_position = random.randint(1, 6)
            turn = "bot"
        else:
            print("You got it wrong!")
            bullet_slot += 1
            turn = "bot"

    elif target_choice == "S":
        print("You are going to shoot self!")
        time.sleep(2)
        if not bullet_slot == bullet_position:
            bullet_slot += 1
            print("Safe!")
        else:
            player_hp -= 1
            bullet_slot = 1
            print("You got it wrong!")
            bullet_position = random.randint(1, 6)
            turn = "bot"
    else:
        print("Enter a valid choice!")
        
def choose_target(shoot_self ):
    global bot_target_choice, decision
    if decision <= shoot_self:
        return "bot"
    else:
        return "player"

def bot_turn():
    global player_hp, bot_hp, turn, bullet_slot, bullet_position, remaining_slot, chance, decision
    print(f"Your HP:{player_hp}")
    print(f"Bot HP:{bot_hp}")
    print("Bot is thinking...")
    time.sleep(3)
    decision = random.randint(1, 100)
    remaining_slot = 7 - bullet_slot
    chance = 1 / remaining_slot
    if chance <= 1/6:
        bot_target_choice = choose_target(90)
    elif chance <= 2/6:
        bot_target_choice = choose_target(75)
    elif chance <= 3/6:
        bot_target_choice = choose_target(60)
    elif chance <= 4/6:
        bot_target_choice = choose_target(35)
    elif chance <= 5/6:
        bot_target_choice = choose_target(15)
    else:
        bot_target_choice = choose_target(0)
    if bot_target_choice == "player":
        print("Bot is going to shoot you...!")
        time.sleep(2)
        if bullet_slot == bullet_position:
            player_hp -= 1
            bullet_position = random.randint(1, 6)
            bullet_slot = 1
            print("Bot got it right!")
            turn = "player"
            
        else:
            bullet_slot += 1
            print("Bot got it wrong!")
            turn = "player"

    elif bot_target_choice == "bot":
        print("Bot is going to shoot self...!")
        time.sleep(2)
        if not bullet_slot == bullet_position:
            bullet_slot += 1
            print("Bot Safe!")
        else:
            bot_hp -= 1
            bullet_position = random.randint(1, 6)
            bullet_slot = 1
            print("Bot got it wrong!")
            turn = "player"

turn = ["player", "bot"]
turn = random.choice(turn)
bullet_position = random.randint(1, 6)
bullet_slot = 1
player_hp = 3
bot_hp = 3

start_game()

while True:
    if turn == "player":
        player_turn()
    elif turn == "bot":
        bot_turn()
    if bot_hp == 0 or player_hp == 0:
        break


if bot_hp == 0:
    print("You won")
else:
    print("You lose")
