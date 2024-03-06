def fibonacci_sum(n):
    # Initialize the first two Fibonacci numbers and the sum
    a, b = 0, 1
    sum_seq = 0
    # Loop to generate and sum the first n Fibonacci numbers
    for _ in range(n):
        sum_seq += a  # Add the current number to the sum
        a, b = b, a + b  # Update values of a and b for next Fibonacci number
    return sum_seq

# Sum the first 50 Fibonacci numbers
n = 50
total_sum = fibonacci_sum(n)
print(f"The sum of the first {n} Fibonacci numbers is: {total_sum}")
