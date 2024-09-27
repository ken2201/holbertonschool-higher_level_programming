# Define a mixin class for swimming behavior
class SwimMixin:
    # Method to represent the swimming ability
    def swim(self):
        print("The creature swims!")

# Define a mixin class for flying behavior
class FlyMixin:
    # Method to represent the flying ability
    def fly(self):
        print("The creature flies!")

# Define the Dragon class that inherits from both SwimMixin and FlyMixin
class Dragon(SwimMixin, FlyMixin):
    # Method to represent the roaring ability specific to a dragon
    def roar(self):
        print("The dragon roars!")

