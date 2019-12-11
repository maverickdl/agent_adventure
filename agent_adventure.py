import time
import random
import sys


def print_longpause(statement):
    print(statement)
    time.sleep(3.5)


def print_pause(statement):
    print(statement)
    time.sleep(2)


def intro(agent):
    print_pause("\nIt's 7pm...")
    print_longpause("You are Agent Lebhare of the Weird Secret Agents "
                    "Company\n")
    print_longpause("Tonight is the office Christmas Party at Club Fashion\n")
    print_pause("You have a crush on Agent Wendy...\n")
    print_pause("Your mission... ask for and obtain her number")
    print_pause("But first you'll need a wingman\n")
    print_longpause("You walk around to see who else is still in the office\n")
    print_longpause(f"You stumble upon Agent {agent} who agrees to be "
                    "your wingman...\n")
    print_pause("He doesn't seem particularly motivated just yet...\n")
    print_pause("Nevertheless, you head to the super speedy Agents car")
    print_pause("Amazingly, the Agent car already has preset destinations\n\n")


def drive_to(agent, visits, mood):
    time = 300
    while True:
        time -= 61
        if time <= 0:
            print_pause("\n\nBut.. Oh no.. you took too long figuring "
                        "out what to do!")
            print_pause("Everyone has gone home!")
            end_game("lose")
            break
        print_pause(f"Where would you like to go with Agent {agent}?")
        destination = input(" 'KFC' - Kings Fried Chicken\n"
                            " 'Gym' - Packo's Gym\n"
                            " 'Mars' - Agent Mars' Apartment\n"
                            " 'Club' - Club Fashion\n\n").lower()
        if destination in visits:
            print_pause("You've already been there!")
            print_pause("Try somewhere else...\n")
        elif (destination == "kfc" or destination == "mars" or
              destination == "gym"):
            visits.append(destination)
            location(destination, agent, mood)
        elif destination == "club":
            club(destination, agent, visits, mood)
            break
        else:
            print_pause("That's not a valid destination, please try again")


def location(destination, agent, mood):
    print_pause(f"You input {destination} and you arrive in a flash.\n")
    if agent == "Seps" and destination == "kfc":
        print_pause("Kings Fried Chicken!\n")
        print_pause("Before you know it, Agent Seps jumps out of the car")
        print_pause("He runs into KFC, happy as ever")
        print_longpause("You sit and wait...")
        print_pause("After an hour, Agent Seps comes back brimming with joy")
        print_pause(""""Let's go to the party!" he says""")
        mood.append("motivated")
    elif agent == "Mars" and destination == "mars":
        print_pause("Agent Mars' Apartment!\n")
        print_pause("Before you know it, Agent Mars jumps out of the car.")
        print_longpause("You see him run into his apartment...")
        print_longpause("...'Is he coming back?' You wonder\n")
        print_pause("He runs out with some sort of.... book?")
        print_pause("He walks up to your window and knocks... profusely")
        print_pause("'Ooooh Agent Lebhare, want to read my thesis?'\n")
        print_longpause("Confused, you oblige and pick a random chapter\n")
        print_longpause("...you're reading for a whole hour\n")
        print_pause("Finally, brimming with joy, Agent Mars suggests you "
                    "get to the party")
        mood.append("motivated")
    elif agent == "Whit" and destination == "gym":
        print_pause("Packo's gym!\n")
        print_pause("Before you know it, Agent Whit jumps out of the car.")
        print_longpause("He looks back at you and says 'Come on, lets do "
                        "some sparring'")
        print_longpause("...you agree for some reason")
        print_longpause("\nFinally, an hour later and exhausted, you're "
                        "ready to get going again.")
        print_pause("Thrilled, Agent Whit suggests you get to the party")
        mood.append("motivated")
    else:
        print_pause(f"Agent {agent} looks at you in confusion...\n")
        print_pause(f"Clearly Agent {agent} would prefer to be elsewhere.")
        print_pause("Frustrated, you look back to the destination input.\n")


def club(destination, agent, visits, mood):
    print_pause(f"\nYou arrive at Club Fashion nice and quickly.\n")
    if "motivated" in mood:
        print_pause(f"Agent {agent} is looking ready to be a great wingman.")
        print_pause("Are you ready to go in now?\n")
        enter = input("Enter 'yes' or 'no'?\n")
        if enter == "yes":
            print_pause(f"You enter Club Fashion with Agent {agent}")
            print_longpause("He has a great idea.")
            print_longpause("You sing 'You've Lost That Lovin "
                            "Feeling' to Agent Wendy")
            print_pause("\nShe loves it.")
            print_pause("You get her number!\n")
            end_game("win")
        elif enter == "no":
            print_pause("You chickened out!")
            print_pause(f"Agent {agent} leaves to get a kebab.")
            end_game("lose")
    else:
        print_pause(f"Agent {agent} doesn't look very motivated.")
        print_pause("Are you sure you want to go into the party now?\n")
        enter = input("Enter 'yes' or 'no'?\n")
        if enter == "yes":
            print_pause(f"\nYou head inside with Agent {agent}")
            print_pause(f"You approach Agent Wendy but Agent {agent} "
                        "embarassses you because he's moody")
            print_pause("Agent Wendy walks away rolling her eyes.")
            print_longpause("\nHow embarassing...")
            end_game("lose")
        elif enter == "no":
            print_pause(f"Probably a good idea.  You and Agent {agent} "
                        "head back to the car\n\n")
            drive_to(agent, visits, mood)


def end_game(status):
    if status == "lose":
        print_pause("You failed to complete the mission.")
        print_pause("You lose.")
    elif status == "win":
        print_pause("Well done, you did it!")
        print_pause("You Win!")
    print_pause("GAME OVER\n")
    play_again()


def play_again():
    response = input("Would you like to play again?\n"
                     " Enter 'yes' to play again\n"
                     " Enter 'no' to quit\n").lower()
    if response == "yes":
        play_game()
    elif response == "no":
        print_pause("\nThanks for playing :)")
        print_pause("\nGoodbye!")
        sys.exit(0)
    else:
        print("\nInvalid input\n\n")
        play_again()


def play_game():
    agents = ["Seps", "Mars", "Whit"]
    agent = random.choice(agents)
    visits = []
    mood = []
    intro(agent)
    drive_to(agent, visits, mood)


play_game()
