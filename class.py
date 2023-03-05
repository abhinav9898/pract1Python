class Person:
    def __init__(self, name, age):
        self.name= name
        self.age= age

    def talk(self):
        print(f"Hi my is {self.name} and I'm {self.age}")


person1= Person("Abhinav", 25)

person2= Person("Prerana", 29)

person1.talk()
person2.talk()

