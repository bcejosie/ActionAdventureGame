import time
import sys

freddy_name = "Freddy"
trust = 2
supplies = 1

def TypeText(textToType):
      for chars in textToType:
            sys.stdout.write(chars)
            sys.stdout.flush()
            time.sleep(.03)

TypeText("The back garden seemed unusually appealing today, so you head over even though the air feels sub-zero.\nThe chilling air soothes you just for a second, your muscles relax for the first time this day.")
time.sleep(1)
TypeText("\nThe potato plants are wilting a little, though, and so are the courgettes. When was the last time you watered them?")

time.sleep(1)

invalid_input = True

if trust == 4 and trust != 3 and trust != 2 and trust != 1:
    TypeText("\nThe doctor could help out maybe; put them to work and have them show their worth?")
    time.sleep(1)
    player_input = int(input("\nSelect 1 to water crops with Juniper, 2 to speak with Freddy"))

    while invalid_input == True:
        match player_input:
            case 1:
                TypeText("You go to water the crops.")
                invalid_input = False
                break

            case 2:
                TypeText(f"You go to speak with {freddy_name}.")
                invalid_input = False
                break
    
            case _:
                print("Invalid input. Please enter 1 or 2.")
                player_input = int(input("Select 1 to water crops with Juniper, 2 to speak with Freddy"))
                invalid_input = True
                break

elif trust == 3 and trust !=2 and trust != 4 and trust != 1:
    TypeText("\nBut you also have to check on the fences, you don’t want another determined visitor to scale them now do you?\n")
    time.sleep(1)
    player_input = int(input("\nSelect 1 to water crops, 2 check on fences"))

    while invalid_input == True:

        match player_input:
            case 1:
                TypeText("You go to water the crops.")
                invalid_input = False
                break

            case 2:
                TypeText("You go to check on the fences.")
                invalid_input = False
                break

            case _:
                print("Invalid input. Please enter 1 or 2.")
                player_input = int(input("Select 1 to water crops, 2 check on fences"))
                invalid_input = True
                break

elif trust == 2 and trust != 3 and trust != 4 and trust != 1:
    TypeText(f"\nBut maybe you should talk to {freddy_name} about what happened today. You don’t want them to stay upset with you.\n")
    time.sleep(1)
    player_input = int(input(f"Select 1 to water crops, 2 to speak with {freddy_name}"))
    
    while invalid_input == True:

        match player_input:
            case 1:
                TypeText("You call  out of the house to help you out.\nThey don’t respond so you call yet again.")
                time.sleep(1)
                TypeText("\nThis time they come out to join you in the garden.\n You water the crops side by side in silence in silence.\n +1 supplies")
                supplies = supplies + 1
                print(f"Supplies now = {supplies}")
                invalid_input = False
                break

            case 2:
                TypeText(f"\n You call {freddy_name} out of the house." "\nIt's a good idea to talk over what happened today and how you've acted." f"\nYou’re able to explain your reasoning to {freddy_name}.")
                time.sleep(2)
                TypeText(f"\nIt’s not as if Juniper was an obvious threat, but neither of you knew her." "\nThe outside world has all gone crazy so it’s not as if you can trust just anyone.")
                time.sleep(2)
                TypeText(f"\nThankfully, {freddy_name} get’s it." "\nThey were just upset that they could’ve missed out on a unique opportunity.\n And they trust in you grows a little. +1 Trust.")
                time.sleep(2)
                trust = trust + 1
                print(f"\nTrust now = {trust}")
                invalid_input = False
                break

            case _:
                print("Invalid input. Please enter 1 or 2.")
                player_input = int(input("Select 1 to water crops, 2 to speak with Freddy"))
                invalid_input =True
                break
