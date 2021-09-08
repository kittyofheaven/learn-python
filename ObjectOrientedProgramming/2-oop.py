class Hero: #self itu kaya pengganti, ya klo didunianyata kaya aku lah, jadi gaperlu sebut nama
    #misalnya "aku yang lakukan itu", kan sama aja kayak "hazel yang lakukan itu"
    def __init__(self, input_name, input_health, input_roles): #init kaya buat initiate, setiap kali dipanggil bakal langsung nyala
        self.name = input_name
        self.health = input_health
        self.roles = input_roles


hero_1 = Hero('Lord Slowmo Brembo', 1000, "Tank")
hero_2 = Hero('Ngab Rio', 100, 'Assasin')

print(hero_1.__dict__)
print(hero_2.__dict__)
