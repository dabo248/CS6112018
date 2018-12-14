print("\n")
print("PythonExercises-v2 by David Bochan")

print("\n")
print("=== EXERCISE 1 ===")

print("\n")
print("(a) 5 / 3 = " + str(5 / 3))
print("=> with python3 you can receive a float even if you divide two \
integers")

print("\n")
print("(b) 5 % 3 = " + str(5 % 3))
print("=> % is the modulus which divides left hand operand by right hand \
operand and returns remainder")

print("\n")
print("(c) 5.0 / 3 = " + str(5.0 / 3))
print("=> outputs a float number.. there is no difference if a plain 5 or 5.0 \
is used")

print("\n")
print("(d) 5 / 3.0 = " + str(5 / 3.0))
print("=> outputs a float number.. there is no difference if a plain 3 or 3.0 \
is used")

print("\n")
print("(e) 5.2 % 3 = " + str(5.2 % 3))
print("=> % is the modulus which divides left hand operand by right hand \
operand and returns remainder")

print("\n")
print("=== EXERCISE 2 ===")

print("\n")
print("(a) 2000.3 ** 200 = ...")
try:
    print(str(2000.3 ** 200))
except OverflowError as e:
    print("=> The python3 interpreter throws a OverflowError " + str(e))

print("\n")
print("(b) 1.0 + 1.0 - 1.0 = " + str(1.0 + 1.0 - 1.0))
print("=> Addition and substraction of float values which results in another \
float value")

print("\n")
print("(c) 1.0 + 1.0e20 - 1.0e20 = " + str(1.0 + 1.0e20 - 1.0e20))
print("=> 1.0 + 1.0e20 is rounded as close as possible, which is 1.0e20 and \
after substraction of it again it results in 0.0")

print("\n")
print("=== EXERCISE 3 ===")

print("\n")
print("(a) float(123) = " + str(float(123)))
print("=> Takes the integer value 123 as input and casts it to the float \
value 123.0")

print("\n")
print("(b) float('123') = " + str(float('123')))
print("=> Takes the string '123' as input and casts it to the float value \
123.0")

print("\n")
print("(c) float('123.23') = " + str(float('123.23')))
print("=> Takes the string '123.23' as input and casts it to the float value \
123.23")

print("\n")
print("(d) int(123.23) = " + str(int(123.23)))
print("=> Takes the float 123.23 as input and casts it to the integer value \
123")

print("\n")
print("(e) int('123.23') = ...")
try:
    int('123.23')
except ValueError as e:
    print("=> The int() function can't cast a string to float to int and thus \
throws a ValueError (" + str(e) + ")")

print("\n")
print("(f) int(float('123.23')) = " + str(int(float(123.23))))
print("=> As we cast the string to float first, we can use it as a input to \
the int() function and receive a integer")

print("\n")
print("(g) str(12) = " + str(12))
print("=> Takes the integer 12 as input and casts it to the string '12'")

print("\n")
print("(h) str(12.2) = " + str(12.2))
print("=> Takes the float 12.2 as input and casts it to the string '12.2'")

print("\n")
print("(i) bool('a') = " + str(bool('a')))
print("=> Because an actual value (the character 'a') is passed to the bool() \
function, True is returned")

print("\n")
print("(j) bool(0) = " + str(bool(0)))
print("=> The boolean value False equals 0 in python, thus False is returned")

print("\n")
print("(k) bool(0.1) = " + str(bool(0.1)))
print("=> Because a value != 0 is provided in the bool() function, \
it returns True")

print("\n")
print("=== EXERCISE 4 ===")

print("\n")
print("range(5) = {}".format(range(5)))
print("=> range(5) returns a sequence of integers from 0 to 4. for i in \
range(5) is consequently iterating over the sequence of integers")

print("\n")
print("type(range(5)) = {}".format(type(range(5))))
print("=> The type function returns an object's class. For range(5) the class \
range is returned")

print("\n")
print("=== EXERCISE 5 ===")

print("\n")

def div_by_number(numbers_list, max_found):
    number_found = 0
    x = 1

    while number_found < max_found:
        for number in numbers_list:
            if x % number == 0:
                print(x)
                number_found = number_found + 1
        
        x = x + 1
    
numbers_list = [5, 7, 11]
print("div_by_number({}, 20)\n".format(numbers_list))
div_by_number(numbers_list, 20)

print("\n")
print("=== EXERCISE 6 ===")

print("\n")
print("(a) & (b)\n")

def is_prime(n):
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5

    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    
    return True

print("is_prime(0) = {}\n".format(is_prime(0)))
print("is_prime(1) = {}\n".format(is_prime(1)))
print("is_prime(3) = {}\n".format(is_prime(3)))
print("is_prime(7) = {}\n".format(is_prime(7)))
print("is_prime(8) = {}\n".format(is_prime(8)))
print("is_prime(112331) = {}".format(is_prime(112331)))

def primes_up_to(n):

    primes = []

    for i in range(0, n):
        if is_prime(i):
            primes.append(i)

    return primes

print("\n(c) primes_up_to(100) = {}".format(primes_up_to(100)))

def first_primes(n):

    primes = []
    i = 0

    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
            
        i = i + 1

    return primes

print("\n(d) first_primes(12) = {}".format(first_primes(12)))

print("\n")
print("=== EXERCISE 7 ===")

print("\n")
print("(a) print_elements(elements_list)\n")

def print_elements(elements):
    for element in elements:
        print(element)

elements_list = [12, "abc", 92.2, "hello"]

print_elements(elements_list)

print("\n(b) print_elements_reverse(elements_list)\n")

def print_elements_reverse(elements):
    for element in elements[::-1]:
        print(element)

print_elements_reverse(elements_list)

print("\n(c) len_elements(elements_list)\n")

def len_elements(elements):
    count = 0

    for _ in elements:
        count = count + 1

    return count

print("len_elements(elements_list) = {}".format(len_elements(elements_list)))

print("\n")
print("=== EXERCISE 8 ===")

a = [12, "abc", 92.2, "hello"]

print("\n")
print("(a) a = {}".format(a))

print("\n(b) b = a")

b = a

print("\n(c) b[1] = 'changed'")

b[1] = "changed"

print("\n(d) a = {}".format(a))
print("=> b is binding to the same object as a, so when b[1] was changed \
a[1] also shows the change")

print("\n(e) c = a[:]")

c = a[:]

print("\n(f) c[2] = 'also changed'")

c[2] = "also changed"

print("\n(g) a = {}".format(a))
print("=> A copy of the list a was created with a[:] and assigned to c, thus \
a[2] did not change when c[2] changed")

def set_first_elem_to_zero(l):
    if len(l) > 0:
        l[0] = 0

    return l

numbers = [12, 21, 214, 3]

print("\n...")

print("\nnumbers = {}".format(numbers))
print("set_first_elem_to_zero(numbers) = \
{}".format(set_first_elem_to_zero(numbers)))
print("numbers = {}".format(numbers))
print("=> The original list also changed, even though we did not assign \
the returned list to it (same binding)")

print("\n")
print("=== EXERCISE 9 ===")

elements = [[1,3], [3,6]]

print("\n")
print("elements = {}".format(elements))

flat_list = lambda l: [element for sublist in l for element in sublist]

print("flat_list(elements) = {}".format(flat_list(elements)))

print("\n")
print("=== EXERCISE 10 ===")

import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.01)
s = np.sin(t - 2) ** 2 * np.e ** (-t ** 2)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='x', ylabel='y',
       title='Exercise 10')
plt.show()

print("\n")
print("See Figure_1.png")

print("\n")
print("=== EXERCISE 11 ===")

def product_iteration(numbers):
    product = 0

    if len(numbers) > 0:
        product = numbers.pop()

        for number in numbers:
            product = product * number

    return product

from functools import reduce 

def product_recursive(numbers):
    if len(numbers) > 0:
        return reduce((lambda x, y: x * y), numbers)
    else:
        return 0

numbers = [21, 12, 10, 128, 2]
empty_list = []

print("\n")
print("product_iteration(numbers) = {}".format(product_iteration(numbers)))
print("product_iteration(empty_list) = \
{}".format(product_iteration(empty_list)))

numbers = [21, 12, 10, 128, 2]

print("\n")
print("product_recursive(numbers) = {}".format(product_recursive(numbers)))
print("product_recursive(empty_list) = \
{}".format(product_recursive(empty_list)))

print("\n")
print("=== EXERCISE 12 ===")

print("\n\nGood to know!")

print("\n")
print("=== EXERCISE 13 ===")

def read_file(filename):
    with open(filename, 'r') as myfile:
        data=myfile.read().replace('\n', '')

    return data

file_content = read_file("emails.txt")

print("\n\nread_file('emails.txt')\n\n{}".format(file_content))

import re

def extract_email(string):
    match = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', string)

    return match

print("\nextract_email(file_content)\
\n\n{}".format(extract_email(file_content)))