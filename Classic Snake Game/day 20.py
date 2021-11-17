import time
class Animal:
    def __init(self):
        self.num_eyes=2


    def breathe(self):
        for i in range(1,3):
            print("Inhale")
            time.sleep(1)
            print("Exhale")



class Fish(Animal):
    def __init__(self):
        super().__init__()
    def breathe(self):
        super().breathe()
        print("Doing Underwater")

    def swim(self):
        print("Moving Water")


nemo=Fish()
nemo.breathe()
