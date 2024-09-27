#!/usr/bin/python3

from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstract base class representing an animal.
    """

    @abstractmethod
    def sound(self) -> str:
        """
        Abstract method to return the sound made by the animal.

        Returns:
            str: The sound made by the animal.
        """
        pass

class Dog(Animal):
    """
    Concrete class representing a dog.
    """

    def sound(self) -> str:
        """
        Returns the sound made by a dog.

        Returns:
            str: The sound "Bark".
        """
        return "Bark"

class Cat(Animal):
    """
    Concrete class representing a cat.
    """

    def sound(self) -> str:
        """
        Returns the sound made by a cat.

        Returns:
            str: The sound "Meow".
        """
        return "Meow"

if __name__ == "__main__":
    # Create instances of Dog and Cat
    dog = Dog()
    cat = Cat()

    # Print the sounds made by the dog and cat
    print(f"Dog says: {dog.sound()}")
    print(f"Cat says: {cat.sound()}")

