class Hero:

    jumlah = 0
    __privatejumlah = 0

    def __init__(self,name,health):
        self.name = name
        self.health = health

        self.__private = "private"
        self.__protected = "protected"

Aprilia = Hero("Aprilia",100)

print(Aprilia.__dict__)
print(Hero.__dict__)
print(Hero.__privatejumlah)