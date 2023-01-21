class Flooder:
    def __init__(self, wealth=0, houses=0):
        self.wealth = wealth
        self.houses = 0
    
    def flood_one_house(self, player, house_type):
        player.destroy_unit(house_type)
        if house_type == "dirty-near":
            self.wealth -= 2
            self.houses += 1
        if house_type == "dirty-far":
            self.wealth -= 6
            self.houses += 1
        if house_type == "clean-near":
            self.wealth -= 4
            self.houses += 1
        if house_type == "clean-far":
            self.wealth -= 7
            self.houses += 1
    
    def earn_income(self, amount):
        self.wealth += amount
        # No income earnt for clean-far houses
    
    def pay_for_policy(self, token_amount):
        self.wealth -= token_amount