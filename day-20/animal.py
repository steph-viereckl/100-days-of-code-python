class Animal:

    def __init__(self):
        self.num_eyes = 2

    def breathe(self):

       print("Inhale, exhale.")


class Fish(Animal):

    def __init__(self):
        super().__init__()

    def swim(self):
        print("swim")

    def breathe(self):
        # Can also leverage super class method AND add something special
        super().breathe()
        print("doing this under water")

nemo = Fish()
nemo.swim()
nemo.breathe() # Access from super class... and then expand functionality 
eyes = nemo.num_eyes # Access from super class
