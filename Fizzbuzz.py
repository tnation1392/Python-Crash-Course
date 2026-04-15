def fizz_buzz(start, end):
    """
    Print 'Fizz', 'Buzz', or 'FizzBuzz' for numbers in the specified range based on divisibility rules.

    Parameters:
    start (int): The starting number of the range.
    end (int): The ending number of the range.
    """
    if start > end:
        print("Start should be less than or equal to end.")
        return

    for fizzbuzz in range(start, end + 1):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            print("FizzBuzz")
        elif fizzbuzz % 3 == 0:
            print("Fizz")
        elif fizzbuzz % 5 == 0:
            print("Buzz")
        else:
            print(fizzbuzz)


# Example usage
print("From 1 to 10")
fizz_buzz(1, 10)
print("\nFrom 50 to 75")
fizz_buzz(50, 75)
