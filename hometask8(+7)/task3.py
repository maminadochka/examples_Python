class Weapon():
    def __init__(self, barrel_size=0):
        self.barrel = barrel_size

    def __gt__(self, other):
        print("Wich barrel is bigger?")
        print("My barrel is", self.barrel)
        print("Other barrel is", other.barrel)
        return self.barrel > other.barrel

    def __sub__(self, other):
        print("My barrel is", self.barrel)
        print("Other barrel is", other.barrel)
        return self.barrel - other.barrel

    def load(self):
        raise NotImplemented

    def shoot(self):
        raise NotImplemented


class Gun(Weapon):
    def shoot(self):
        print("BANG!*******************")


class Rifle(Weapon):
    def shoot(self):
        print("BAAANG!!!")


class MiniGun(Gun, Rifle):
    def shoot(self):
        print("\n")
        for i in range(5):
            super().shoot()


gun = Gun(5.9)
rifle = Rifle(10)
minigun = MiniGun()

#print(rifle > gun)

print(rifle - gun)

print("\n")
for curr_gun in [gun, rifle, minigun]:
    curr_gun.shoot()