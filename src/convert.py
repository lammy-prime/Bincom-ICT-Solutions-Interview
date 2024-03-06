import random

def generate_binary_and_convert():
    # Generate a random 4-digit binary number as a string
    binary_str = ''.join(str(random.randint(0, 1)) for _ in range(4))
    # Convert the binary string to a decimal (base 10) number
    decimal_number = int(binary_str, 2)
    
    print(f"Generated binary number: {binary_str}")
    print(f"Decimal (base 10) equivalent: {decimal_number}")

generate_binary_and_convert()
