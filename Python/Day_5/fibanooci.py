def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence
num_terms = int(input("Enter the number of terms: "))
fib_sequence = fibonacci_sequence(num_terms)
print(f"Fibonacci sequence up to {num_terms} terms: {fib_sequence}")