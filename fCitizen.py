class Citizen:
  def __init__(self, wealth=0, dirty_near_houses=0, dirty_far_houses=0, clean_near_houses=0, clean_far_houses=0):
    self.wealth = wealth
    self.dirty_near_houses = dirty_near_houses
    self.dirty_far_houses = dirty_far_houses
    self.clean_near_houses = clean_near_houses
    self.clean_far_houses = clean_far_houses

  def earn_income(self):
    self.wealth += 5

  def clean_house(self, dist):
    if self.dirty_near_houses < 1 and self.dirty_far_houses < 1:
      print("No houses to clean! No action taken")
    else:
      if dist == "dirty-near":
        self.dirty_near_houses -= 1
        self.clean_near_houses += 1
      if dist == "dirty-far":
        self.dirty_far_houses -= 1
        self.clean_far_houses += 1

  def move_house(self, status):
    if self.dirty_near_houses < 1 and self.clean_near_houses < 1:
      print("No houses to move! No action taken")
    else:
      if status == "dirty-near":
        self.dirty_near_houses -= 1
        self.dirty_far_houses += 1
      if status == "clean-n":
        self.clean_near_houses -= 1
        self.clean_far_houses += 1

  def build_house(self, house_type):
    if house_type == "dirty-near":
      self.wealth -= 2
      self.dirty_near_houses += 1
    if house_type == "dirty-far":
      self.wealth -= 6
      self.dirty_far_houses += 1
    if house_type == "clean-near":
      self.wealth -= 4
      self.clean_near_houses += 1
    if house_type == "clean-far":
      self.wealth -= 7
      self.clean_far_houses += 1

  def destroy_unit(self, house_type):
    if house_type == "dirty-near":
      #increase flooder's wealth
      self.dirty_near_houses -= 1
    if house_type == "dirty-far":
      #increase flooder's wealth
      self.dirty_far_houses -= 1
    if house_type == "clean-near":
      #increase flooder's wealth
      self.clean_near_houses -= 1
    if house_type == "clean-far":
      #increase flooder's wealth
      self.clean_far_houses -= 1