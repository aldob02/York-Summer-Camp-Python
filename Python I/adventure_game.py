health = 3
gold = 0

def start():
    print("You enter the dungeon and follow the path until it splits into a large cavern to the left and a narrow passage to the right. Do you go left or right?")
    action = input()
    if action == "left":
        cavern()
    if action == "right":
        narrow_passage()
    if action == "back":
        leave()

def cavern():
    print("You follow the cavern. There is a massive sleeping dragon in the middle of the floor. To you wake it up, or try to sneak by?")
    action = input()
    if action == "wake":
        wake_dragon()
    if action == "sneak":
        sneak_past_dragon()
    if action == "back":
        start()

def wake_dragon():
    global health
    print("The dragon snaps at you and shoots fire at you.")
    health = health - 1
    if health < 1:
        dead()
    print("Do you fight the dragon or run away?")
    action = input()
    if action == "fight":
        fight_dragon()

def fight_dragon():
    global gold
    print("You defeat the dragon and take its gold!")
    gold = gold + 100
    print("You now have " + str(gold) + " gold.")

def run_from_dragon():
    global health
    print("The dragon bites you as you run away!")
    health = health - 1
    if health < 1:
        dead()
def sneak_past_dragon():
    global gold
    print("You find a little bit of gold")
    gold = gold + 10
    print("You now have " + str(gold) + " gold.")
    
def narrow_passage():
    pass

def dead():
    print("You ran out of health! Game Over. Do you want to play again?")
    answer = input()
    if answer == "Yes":
        start()

def leave():
    print("You left the dungeon with " + str(health) + " health left, and " + str(gold) + " gold.")

start()
