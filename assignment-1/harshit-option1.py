#Author name- Harshit Sonik
# Date: 11-10-2024
# Description: A program that checks if a number is prime, finds nearby primes, and lists divisors if the number is not prime.

def is_prime(num):
   #Check if a number is prime.
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_previous_prime(num):
    #check the nearest prime number before the given number.
    for i in range(num - 1, 1, -1):
        if is_prime(i):
            return i
    return None

def find_next_prime(num):
    #check the nearest prime number after the given number.
    i = num + 1
    while True:
        if is_prime(i):
            return i
        i += 1

def get_divisors(num):
    #Returns a list of divisors of number.
    divisors = [i for i in range(2, num) if num % i == 0]
    return divisors

def main():
    while True:
        user_input = input("Please enter the number to check: ")
        if not user_input.isdigit() or int(user_input) <= 0:
            print("That is not a positive whole number. Try again.\n")
            continue
        else:
            num = int(user_input)
            break

    previous_prime = find_previous_prime(num)
    next_prime = find_next_prime(num)

    if previous_prime:
        print(f"The prime number before {num} is {previous_prime}.")
    else:
        print(f"There is no prime number before {num}.")
    
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        divisors = get_divisors(num)
        print(f"{num} is not prime. Its factors are {', '.join(map(str, divisors))}.")
    
    print(f"The prime number after {num} is {next_prime}.")

    input("\nPress Enter to exit the program..")

if __name__ == "__main__":
    main()
