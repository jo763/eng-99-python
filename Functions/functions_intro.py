# DON'T
# Repeat
# Yourself

# def print_something(string_to_print):
#     print(f"{string_to_print} has been printed")
#
# print_something("Potato")

# def tri_multiply(*args):
#     total = 1
#     for num in args:
#         total *= num
#     return total/2
#
# print(tri_multiply(2,4,6))


# def addition (num1, num2):
#     return num1 + num2
# def subtraction (num1, num2):
#     return num1 - num2
# def multiplication (num1, num2):
#     return num1 * num2
# def division (num1, num2):
#     return num1 / num2
#
# print(addition(10,5))
# print(subtraction(10,5))
# print(multiplication(10,5))
# print(division(10,5))




print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1
# A1a:
def find_divisors(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors
#print(find_divisors(12))

print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function)
# A1b:
# -------------------------------------------------------------------------------------- #
def factor_of_each_other(num1, num2):
    x = find_divisors(num1)
    y = find_divisors(num2)
    if num1 in y or num2 in x:
        return True
    else:
        return False
print(factor_of_each_other(3,12))
print(factor_of_each_other(12,3))
print(factor_of_each_other(11,3))

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
# A2a:

def alphabet_position(letter):
    letter.lower()
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    pos = alphabet.index(letter)
    return pos +1

print(alphabet_position("c"))

print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14
# A2b:
def id_creation(name):
    id = ''
    for letter in name:
        id += str(alphabet_position(letter)-1)
    return id

print(id_creation("bob"))

print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)
# A2c:
# -------------------------------------------------------------------------------------- #
def password_creation(name):
    id = id_creation(name)
    sum = 0
    for character in id:
        sum += int(character)
    password = int(id) - sum
    return password

print(password_creation("bob"))

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.
# A3a:
def prime_checker(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

print(prime_checker(5))
print(prime_checker(5))
print(prime_checker(12))

print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit
# A3b:
# -------------------------------------------------------------------------------------- #
def prime_checker2(number):
    if type(number) not in [int]:
        print("Number is not a integer")
        return
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

print(prime_checker2(5))
print(prime_checker2(5))
print(prime_checker2(12))
print(prime_checker2('x'))
print(prime_checker2(True))



