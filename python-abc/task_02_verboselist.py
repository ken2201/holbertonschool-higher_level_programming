#!/usr/bin/python3

# Define a class VerboseList that inherits from the built-in list class
class VerboseList(list):

    # Override the append method to add an item and print a message
    def append(self, item):
        # Call the superclass's append method to add the item
        super().append(item)
        # Print a message indicating the item has been added
        print(f"Added [{item}] to the list.")

    # Override the extend method to add multiple items and print a message
    def extend(self, iterable):
        # Convert the iterable to a list
        items = list(iterable)
        # Call the superclass's extend method to add the items
        super().extend(items)
        # Print a message indicating the number of items added
        print(f"Extended the list with [{len(items)}] items.")

    # Override the remove method to remove an item and print a message
    def remove(self, item):
        # Print a message indicating the item has been removed
        print(f"Removed [{item}] from the list.")
        # Call the superclass's remove method to remove the item
        super().remove(item)

    # Override the pop method to remove and return an item and print a message
    def pop(self, index=-1):
        # Get the item at the specified index
        item = self[index]
        # Print a message indicating the item has been popped
        print(f"Popped [{item}] from the list.")
        # Call the superclass's pop method to remove and return the item
        return super().pop(index)

