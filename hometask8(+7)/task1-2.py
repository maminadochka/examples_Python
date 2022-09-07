class Auto():
    def __init__(self, auto_color = "black", auto_weight = 5):
        self.brand = ""
        self.age = 0
        self.mark = ""
        self.color = auto_color
        self.weight = auto_weight

    def move(self):
        print("mooove")
        pass

    def birthday(self):
        self.age += 1
        print(self.age)
        pass

    def stop(self):
        print("stooop")
        pass

#testing 1 task:
lada_sedan = Auto()
lada_sedan.move()
lada_sedan.stop()
lada_sedan.age = 5
lada_sedan.birthday()

