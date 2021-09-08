class Hero: #template
    pass


hero_1 = Hero() #object
hero_2 = Hero()

hero_1.name = "sniper"
hero_1.health = 100

hero_2.name = "ucup"
hero_2.health = 1000

print(hero_1.__dict__)
print(hero_1.name)
