import time

def introduction():
    print("Welcome to the Mysterious Forest Adventure!")
    print("You find yourself standing at the edge of a dense forest.")
    print("Legend has it that a valuable treasure is hidden deep within.")
    print("Your mission is to find the treasure and return safely.")
    print()

def choose_path():
    print("Which path will you choose?")
    print("1. Take the left path.")
    print("2. Take the right path.")
    choice = input("Enter your choice (1 or 2): ")
    print()
    return choice

def explore_left_path():
    print("You chose the left path.")
    print("You encounter a river blocking your way.")
    print("What will you do?")
    print("1. Swim across the river.")
    print("2. Look for a bridge.")
    choice = input("Enter your choice (1 or 2): ")
    print()
    return choice

def explore_right_path():
    print("You chose the right path.")
    print("You come across a cave entrance.")
    print("What will you do?")
    print("1. Enter the cave.")
    print("2. Continue along the path.")
    choice = input("Enter your choice (1 or 2): ")
    print()
    return choice

def swim_river():
    print("You decide to swim across the river.")
    print("You struggle against the current but manage to reach the other side.")
    print("You continue deeper into the forest.")
    print()
    return "swim"

def find_bridge():
    print("You search for a bridge and find one nearby.")
    print("You cross the bridge and continue your journey.")
    print()
    return "bridge"

def enter_cave():
    print("You cautiously enter the dark cave.")
    print("As you venture deeper, you see a glimmer of light.")
    print("You approach the light and find the treasure!")
    print("Congratulations! You have found the treasure and won the game.")
    print()
    return "treasure"

def continue_along_path():
    print("You decide to continue along the path.")
    print("You journey deeper into the forest.")
    print()
    return "continue"

def main():
    introduction()
    path_choice = choose_path()
    
    if path_choice == "1":
        left_choice = explore_left_path()
        if left_choice == "1":
            outcome = swim_river()
        else:
            outcome = find_bridge()
    else:
        right_choice = explore_right_path()
        if right_choice == "1":
            outcome = enter_cave()
        else:
            outcome = continue_along_path()
    
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
