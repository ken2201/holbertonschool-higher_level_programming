class CountedIterator:
    # Constructor method to initialize the iterator and counter
    def __init__(self, iterable):
        # Initialize the iterator with the provided iterable
        self.iterator = iter(iterable)
        # Initialize the counter to zero
        self.counter = 0

    # Method to make the object itself an iterator
    def __iter__(self):
        # Return the iterator object itself
        return self

    # Method to get the next item from the iterator
    def __next__(self):
        try:
            # Get the next item from the iterator
            item = next(self.iterator)
            # Increment the counter
            self.counter += 1
            # Return the item
            return item
        except StopIteration:
            # Raise StopIteration if there are no more items
            raise StopIteration

    # Method to get the current count of items iterated
    def get_count(self):
        # Return the current value of the counter
        return self.counter

