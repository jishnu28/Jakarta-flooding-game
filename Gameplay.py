from fGovernment import Government
from fCitizen import Citizen
from fFlooder import Flooder
from PIL import Image


citizen_team = Citizen()
industry_team = Citizen()
flooding_team = Flooder()
government_team = Government()
round_number = 1

def view_current_state():
    print ("\n\n******************Round {}******************\n".format(round_number))
    print("Citizen Team:-------------------------------\n")
    print("- Wealth: {}\n".format(citizen_team.wealth))
    print("- Dirty-near houses: {}\n".format(citizen_team.dirty_near_houses))
    print("- Dirty-far houses: {}\n".format(citizen_team.dirty_far_houses))
    print("- Clean-near houses: {}\n".format(citizen_team.clean_near_houses))
    print("- Clean-far houses: {}\n".format(citizen_team.clean_far_houses))

    print("Industry Team:-------------------------------\n")
    print("- Wealth: {}\n".format(industry_team.wealth))
    print("- Dirty-near factories: {}\n".format(industry_team.dirty_near_houses))
    print("- Dirty-far factories: {}\n".format(industry_team.dirty_far_houses))
    print("- Clean-near factories: {}\n".format(industry_team.clean_near_houses))
    print("- Clean-far factories: {}\n".format(industry_team.clean_far_houses))
    
    print("Government Team:----------------------------\n")
    print("- Current party: {}\n".format(government_team.active_party))
    print("- Current policy: {}\n".format(government_team.active_policy))

    print("Flooding Team:------------------------------\n")
    print("- Wealth: {}\n".format(flooding_team.wealth))
    print("- Houses taken: {}\n".format(flooding_team.houses))

def move_enactor(command) -> None:
    player_char = command[0] # Citizen, Industry
    move_type = command[1] # Build, Destroy, Clean, Move
    recipient = command[2]
    num_of_units = int(command[3]) # Single digit int
    descriptor = command[4:] # "dirty-near", "dirty-far", "clean-near", "clean-far"

    if player_char == "C":
        if move_type == "B": # Build houses
            for i in range(num_of_units):
                citizen_team.build_house(descriptor)
        if move_type == "M": # Move houses
            for i in range(num_of_units):
                citizen_team.move_house(descriptor)
        if move_type == "C": #Clean houses
            for i in range(num_of_units):
                citizen_team.clean_house(descriptor)
    
    if player_char == "I":
        if move_type == "B": # Build houses
            for i in range(num_of_units):
                industry_team.build_house(descriptor)
        if move_type == "M": # Move houses
            for i in range(num_of_units):
                industry_team.move_house(descriptor)
        if move_type == "C": #Clean houses
            for i in range(num_of_units):
                industry_team.clean_house(descriptor)

    if player_char == "F":
        if move_type == "D": # Destroy units
            if recipient == "C":
                for i in range(num_of_units):
                    citizen_team.destroy_unit(descriptor)
            if recipient == "I":
                for i in range(num_of_units):
                    citizen_team.destroy_unit(descriptor)

    # G team does not have to take actions every round so handle separately



print("\n\nPlayers created. Let the games begin!\n")

while round_number < 12:
    # Citizen team earns 5 tokens at the start of every round
    citizen_team.earn_income()
    industry_team.earn_income()

    # Flooding team earns income at the start of every round -- NOT immediately after citizen move, so that delay helps C, I teams
    for i in range(citizen_team.dirty_near_houses):
        flooding_team.earn_income(4) # (2,1,1,0) * 2
    for i in range(citizen_team.dirty_far_houses):
        flooding_team.earn_income(2)
    for i in range(citizen_team.clean_near_houses):
        flooding_team.earn_income(2)

    view_current_state()

    # Have a specific section on elections depending on round number-----------------------------------------
    if round_number == 1 or (round_number%4) == 0:
        img = Image.open("Election.png")
        img.show()
        print("Election round! Time to campaign.")
        winning_party = input("Enter the name of the winning party:")
        government_team.elect_into_power(winning_party)
        new_policy = input("Enter the title of the new policy implemented:")
        government_team.set_policy(new_policy)



    # Government's action
    token_amt = int(input("Enter policy's token amount for this round:"))
    flooding_team.pay_for_policy(token_amt)

    # Citizen's action
    citizen_command = input("Enter Citizen team's move:")
    """
    Examples:
    CB!2dirty-near = Citizen Build 2 dirty-near houses
    FDC1clean-near = Flooder Destroy 1 clean-near house
    FP!4! = Flooder pay 4 for policy

    Input breakdown:
    Char 0 = Playing team
    Char 1 = Action
    Char 2 = Recipient of action
    Char 3 = number of units for action
    Rest of string = Unit descriptor
    """
    move_enactor(citizen_command)
    view_current_state()

    # Citizen's action
    industry_command = input("Enter Industry team's move:")
    """
    Examples:
    CB!2dirty-near = Citizen Build 2 dirty-near houses
    FDC1clean-near = Flooder Destroy 1 clean-near house
    FP!4! = Flooder pay 4 for policy

    Input breakdown:
    Char 0 = Playing team
    Char 1 = Action
    Char 2 = Recipient of action
    Char 3 = number of units for action
    Rest of string = Unit descriptor
    """
    move_enactor(industry_command)
    view_current_state()

    # Flooder's action
    flooder_command = input("Enter Flooding team's move:")
    move_enactor(flooder_command)

    round_number += 1
