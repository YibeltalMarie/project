
class Name:
  def __init__(self,f_name,l_name):
    self.first_name = f_name
    self.last_name = l_name
  
  def print(self):
    print(f"Full Name: {self.first_name}:{self.last_name}")

name1 = Name("Yibeltal","Marie")
name2 = Name("Temesgen","Marie")
print(name1.first_name)
print(name2.last_name)
name1.print()
name2.print()
