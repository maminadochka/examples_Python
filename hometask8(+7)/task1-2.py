import time

class Auto():
    def __init__(self, auto_brand, auto_age, auto_mark, auto_color = "black", auto_weight = 5):
        self.brand = auto_brand
        self.age = auto_age
        self.mark = auto_mark
        self.color = auto_color
        self.weight = auto_weight

    def move(self):
        print("mooove")

    def birthday(self):
        self.age += 1
        print(f"Today is my birthday! I'm {self.age}")

    def stop(self):
        print("stooop")

    def show_me(self):
        print(f"\nHi! I'm {self.brand}! I'm {self.color} and I weigh {self.weight} tons.")
        self.birthday()
        self.move()
        self.stop()
        #mark

#testing 1 task:
lada_sedan = Auto("BMW", 4, 9)
lada_sedan.move()
lada_sedan.stop()
lada_sedan.birthday()


#2 task:
class Truck(Auto):
    def __init__(self, auto_brand, auto_age, auto_mark, mx_load ,auto_color = "yellow", auto_weight = 15):
        super().__init__(auto_brand, auto_age, auto_mark, auto_color, auto_weight)
        self.max_load = mx_load

    def move(self):
        super().move()
        print("attention!")

    def load(self):
        time.sleep(1)
        print("load...")
        time.sleep(1)

    def show_me(self):
        super().show_me()
        self.load()


class Car(Auto):
    def __init__(self, auto_brand, auto_age, auto_mark, mx_speed, auto_color="blue", auto_weight=4):
    #def __init__(self, auto_brand, auto_age, auto_mark, mx_speed):
        super().__init__(auto_brand, auto_age, auto_mark, auto_color, auto_weight)
        self.max_speed = mx_speed
    
    def move(self):
        super().move()
        print(f"Max speed is {self.max_speed}")

        
tr = Truck("MAZ", 7, 5, 45, "red")
tr.show_me()

my_car = Car("Lamborghini", 1, 10, 90, "green")
my_car.show_me()


