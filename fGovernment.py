#import Flooder

class Government:
    def __init__(self, active_party="No election yet", active_policy="No policy implemented"):
        self.active_party = active_party # Of Class = Politician
        self.active_policy = active_policy
    
    def elect_into_power(self, winning_party):
        self.active_party =  winning_party
    
    def set_policy(self, new_policy):
        self.active_policy = new_policy

    """
    def enact_policy(player, token_amount):
        player.pay_for_policy(token_amount)
    """