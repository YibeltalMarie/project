
class Animal:
  def __init__(self,f_name,l_name):
    self.first_name = f_name
    self.last_name = l_name
  
  def print(self):
    print(f"Full Name: {self.first_name}:{self.last_name}")