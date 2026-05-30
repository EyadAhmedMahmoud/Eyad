
import time
import random


def main():
    total_score = 0
    print("Welcome to the adventure game!")
    time.sleep(2)
    print("Would you like to enter or quit?")
    time.sleep(2)

    while True:
        choices = input("Enter \"enter\" to start or \"quit\" to exit: ").lower()
        if choices == "enter":
            total_score += 10
            print("You have been given 10 points for starting the game.")
            time.sleep(2)
            print("You are now ready to begin your adventure!")
            time.sleep(2)
            break
        elif choices == "quit":
            print("Thanks for playing!")
            time.sleep(2)
            print("Do you want to play again?")
            time.sleep(2)
            while True:
                last_choice = input("Enter \"yes\" to continue, or \"no\" to end: ").lower()
                if last_choice == "yes":
                    return True
                elif last_choice == "no":
                    print("Thanks for playing!")
                    time.sleep(2)
                    print("Exiting the game...")
                    time.sleep(4)
                    return False
                else:
                    print("Invalid choice. Please try again.")
                    time.sleep(2)
        else:
            print("Invalid choice. Please try again.")
            time.sleep(2)

    weapons = ["dagger", "sword", "bow and arrow", "magic staff"]
    weapon = random.choice(weapons)
    print("You have been randomly assigned a weapon.")
    time.sleep(2)
    print(f"You got a: {weapon}")
    time.sleep(2)
    print("You find yourself standing in an open field ")
    time.sleep(2)
    print("filled with grass and yellow wildflowers.")
    time.sleep(2)
    print("Rumor has it that a wicked fairie is somewhere around here.")
    time.sleep(2)
    print("It has been terrifying the nearby village.")
    time.sleep(2)
    print("You must find the fairie and defeat it to save the village.")
    time.sleep(2)
    print("In front of you is a house.")
    time.sleep(2)
    print("To your right is a dark cave.")
    time.sleep(2)
    print(f"In your hand, you hold your trusty {weapon}.")
    time.sleep(2)
    user_name = input("Enter your name: ")
    print(f"Hello, {user_name}!")
    time.sleep(2.5)
    print("What would you like to do?")
    time.sleep(2)
    print("Would you like to go into the house ")
    time.sleep(2)
    print("or explore the cave?")
    time.sleep(2)
    print("Or would you like to wander around the field?")
    time.sleep(2)
    while True:
        choice2 = input("Enter \"house\", \"cave\", or \"field\": ").lower()
        if choice2 == "house":
            total_score = handle_house(total_score, weapon)
            break
        elif choice2 == "cave":
            total_score = handle_cave(total_score)
            break
        elif choice2 == "field":
            print("You wander around the field aimlessly.")
            total_score -= 5
            break
        else:
            print("Invalid choice. Please try again.")

    print(f"Your final score is: {total_score}")
    print("Game Over!")
    time.sleep(3)
    print("Do you want to play again?")
    time.sleep(2)
    while True:
        last_choice = input("Enter \"yes\" to continue, or \"no\" to end: ").lower()
        if last_choice == "yes":
            return True
        elif last_choice == "no":
            print("Thanks for playing!")
            time.sleep(4)
            return False
        else:
            print("Invalid choice. Please try again.")
            time.sleep(2)


def handle_house(total_score, weapon):
    print("You approach the house.")
    time.sleep(2)

    print("It's a small cottage with a thatched roof.")
    time.sleep(2)

    print("The door is slightly ajar.")
    time.sleep(2)

    while True:
        choice3 = input("Enter \"enter\" to go inside, or \"leave\" to go back to the field: ").lower()
        if choice3 == "enter":
            print("You enter the house and find it empty.")
            time.sleep(2)
            print("Suddenly, a wicked fairie appears!")
            time.sleep(2)

            while True:
                choice4 = input("Enter \"fight\" to fight the fairie, or \"run\" to escape: ").lower()
                if choice4 == "fight":
                    total_score = fight_fairie(total_score, weapon)
                    break
                elif choice4 == "run":
                    print("You run back outside and escape safely.")
                    total_score += 5
                    print("You gain 5 points for escaping safely.")
                    time.sleep(2)
                    print("You can either go back to the field or explore the cave.")
                    break
                else:
                    print("Invalid choice. Please try again.")
            break
        elif choice3 == "leave":
            print("You leave the house and go back to the field.")
            total_score += 2
            break
        else:
            print("Invalid choice. Please try again.")

    return total_score


def handle_cave(total_score):
    print("You cautiously enter the dark cave.")
    time.sleep(2)

    print("Inside the cave, you find a treasure chest!")
    time.sleep(2)

    print("You open the chest and find 100 gold coins!")
    total_score += 100
    print("You gain 100 points for finding the treasure.")
    time.sleep(2)

    print("You leave the cave and return to the field.")
    
    return total_score


def fight_fairie(total_score, weapon):
    print(f"You bravely fight the fairie with your {weapon}.")
    time.sleep(2)

    if weapon in ["sword", "magic staff"]:
        print(f"With your {weapon}, you easily defeat the fairie!")
        total_score += 50
        print("You gain 50 points for defeating the fairie.")
        time.sleep(2)
        print("Congratulations, you saved the village!")
    else:
        if random.randint(1, 10) > 5:
            print("You defeated the fairie!")
            total_score += 50
            print("You gain 50 points for defeating the fairie.")
            time.sleep(2)
            print("Congratulations, you saved the village!")
        else:
            print("The fairie was too powerful. You have been defeated.")
            total_score -= 20
            time.sleep(2)
            print("Game over.")
    
    return total_score


if __name__ == "__main__":
    while main():
        pass
