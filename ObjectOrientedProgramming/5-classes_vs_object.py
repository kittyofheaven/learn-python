print('done')

#this is class
class Fighters: 
  #__init__ is a method
  def __init__ (self, name, health, attack) :  #this is like initiation
    self.name = name
    self.health = health
    self.attck = attack

shiro = Fighters('shironeko', 10000, 700) #shiro is an object

print(shiro.name)
print(shiro.attck)
