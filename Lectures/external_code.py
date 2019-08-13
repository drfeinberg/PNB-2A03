def my_name():
    name = input("What's you're name?")
    print("Your name is ", name)
    return name

class Animals:
    all_animals = []

    def __init__(self):
        self.animal = None

    def input_animals(self):
        self.animal = input("Type your animal here: \n")
        self.all_animals.append(self.animal)
