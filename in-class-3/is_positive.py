def is_positive(number):

    # Returns True if the number is positive, otherwise False.

    if number > 0:
        print(f"{number} is positive.")
        return True
    elif number < 0:
        print(f"{number} is negative.")
        return False
    else:
        print(f"{number} is zero.")
        return False  # Ensure the function returns False for zero

if __name__ == "__main__":
    # Test cases
    print(is_positive(10.5))  # True, positive
    print(is_positive(-3.14))  # False, negative
    print(is_positive(0))     # False, zero
