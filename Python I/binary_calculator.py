def binary_to_decimal(binary_number):
    return int(binary_number, 2)

def decimal_to_binary(decimal_number):
    return bin(decimal_number)

def add_binary_numbers(binary_number_1, binary_number_2):
    decimal_number_1 = int(binary_number_1, 2)
    decimal_number_2 = int(binary_number_2, 2)
    decimal_sum = decimal_number_1 + decimal_number_2
    binary_sum = bin(decimal_sum)
    return binary_sum

def subtract_binary_numbers(binary_number_1, binary_number_2):
    decimal_number_1 = int(binary_number_1, 2)
    decimal_number_2 = int(binary_number_2, 2)
    decimal_difference = decimal_number_1 - decimal_number_2
    binary_difference = bin(decimal_difference)
    return binary_difference

def multiply_binary_numbers(binary_number_1, binary_number_2):
    decimal_number_1 = int(binary_number_1, 2)
    decimal_number_2 = int(binary_number_2, 2)
    decimal_product = decimal_number_1 * decimal_number_2
    binary_product = bin(decimal_product)
    return binary_product

def divide_binary_numbers(binary_number_1, binary_number_2):
    decimal_number_1 = int(binary_number_1, 2)
    decimal_number_2 = int(binary_number_2, 2)
    decimal_quotient = decimal_number_1 // decimal_number_2
    binary_quotient = bin(decimal_quotient)
    return binary_quotient

def bit_shift_left(binary_number, shift_number):
    decimal_number = int(binary_number, 2)
    decimal_shifted = decimal_number << shift_number
    binary_shifted = bin(decimal_shifted)
    return binary_shifted

def bit_shift_right(binary_number, shift_number):
    decimal_number = int(binary_number, 2)
    decimal_shifted = decimal_number >> shift_number
    binary_shifted = bin(decimal_shifted)
    return binary_shifted

# extra challenges for students with experience with python

def factorial(binary_number):
    decimal_number = int(binary_number, 2)
    f=1
    for i in range(1,decimal_number+1):
        f = f * i
    binary_f = bin(f)
    return binary_f

def is_even(binary_number):
    if(binary_number[len(binary_number)-1] == '0'):
        return True
    else:
        return False

print(decimal_to_binary(12))
print(binary_to_decimal("0b11000"))
print(add_binary_numbers("0b101", "0b101"))
print(subtract_binary_numbers("0b1010", "0b1000"))
print(multiply_binary_numbers("0b11", "0b101"))
print(divide_binary_numbers("0b1010", "0b10"))
print(bit_shift_left("0b1110101", 3))
print(bit_shift_right("0b1100101", 3))
print(factorial("0b101"))
print(is_even("0b1101"))
print(is_even("0b1000"))
