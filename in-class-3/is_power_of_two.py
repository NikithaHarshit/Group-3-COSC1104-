def is_power_of_two(number):
   
    # Returns True if the number is a power of 2, otherwise False.
    
    if number < 1:
        return False
    return (number & (number - 1)) == 0

if __name__ == "__main__":
    # Test cases
    print(is_power_of_two(1))    # True, since 2^0 = 1
    print(is_power_of_two(2))    # True, since 2^1 = 2
    print(is_power_of_two(4))    # True, since 2^2 = 4
    print(is_power_of_two(10))   # False, not a power of 2
    print(is_power_of_two(16))   # True, since 2^4 = 16
    print(is_power_of_two(18))   # False, not a power of 2
