# iter() and next()
#
# Write a function simulate_for_loop(iterable) that manually uses iter() and next() to replicate what a for loop does (catch StopIteration with try/except).
# Test it on a list, a string, and a range object.
# Print each value with its index.
def simulate_for_loop(iterable):
    # 1. Get an 
    iterator = iter(iterable)
    index = 0

    # 2. Infinite loop to continuously fetch the next item
    while True:
        try:
            # 3. Request the next item
            value = next(iterator)
            print(f"Index {index}: {value}")
            index += 1
        except StopIteration:
            # 4. Stop when the iterator runs out of items
            break


# --- Tests ---

print("--- Testing on a List ---")
simulate_for_loop(["apple", "banana", "cherry"])

print("\n--- Testing on a String ---")
simulate_for_loop("Python")

print("\n--- Testing on a Range ---")
simulate_for_loop(range(5, 10))
#
# Custom Iterator — __iter__ and __next__
#
# Write a custom iterator class EvenNumbers(start, count) that yields 'count' even numbers starting from 'start'.
# Use __iter__ and __next__.
# Demonstrate with a for loop and with manual next() calls.
# Verify that __iter__ returns self.
