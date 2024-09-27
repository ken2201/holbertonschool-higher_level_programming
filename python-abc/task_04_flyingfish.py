# Define a class called Fish
class Fish:
    # Method to represent the swimming behavior of a fish
    def swim(self):
        print("The fish is swimming")

    # Method to represent the habitat of a fish
    def habitat(self):
        print("The fish lives in water")

# Define a class called Bird
class Bird:
    # Method to represent the flying behavior of a bird
    def fly(self):
        print("The bird is flying")

    # Method to represent the habitat of a bird
    def habitat(self):
        print("The bird lives in the sky")

# Define a class called FlyingFish that inherits from both Fish and Bird
class FlyingFish(Fish, Bird):
    # Override the fly method to represent the flying behavior of a flying fish
    def fly(self):
        print("The flying fish is soaring!")

    # Override the swim method to represent the swimming behavior of a flying fish
    def swim(self):
        print("The flying fish is swimming!")

    # Override the habitat method to represent the habitat of a flying fish
    def habitat(self):
        print("The flying fish lives both in water and the sky!")

