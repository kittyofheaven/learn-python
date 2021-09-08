class Hero: 
    #class variable
    jumlah = 0
    def __init__(self, input_name, input_health, input_roles): 
        #instance Variable
        self.name = input_name
        self.health = input_health
        self.roles = input_roles
        Hero.jumlah += 1 #untuk panggil class variable dan setiap ada init akan ditambah 1
        print('membuat hero dengan nama', input_name)
        
class Tower:
    jumlah = 0
    def __init__(self, input_health, input_attack):
        print("menciptakan Tower")
        self.health = input_health
        self.attack = input_attack
        Tower.jumlah += 1

hero_1 = Hero('Lord Slowmo Brembo', 1000, "Tank")
hero_2 = Hero('Ngab Rio', 100, 'Assasin')
print(Hero.jumlah)

tower_1 = Tower(1000, 25)
print(Tower.jumlah)
