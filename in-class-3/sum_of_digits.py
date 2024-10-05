def sum_of_digits(number):
    """
    Returns the sum of the digits of the given integer.
    """
    return sum(int(digit) for digit in str(abs(number)))

if __name__ == "__main__":
    # Test cases
    print(sum_of_digits(356))  # 6
    print(sum_of_digits(4467)) # 22
    print(sum_of_digits(-8920)) # 17
