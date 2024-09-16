def print_fibonacci(length):
    """
    Prints a list of the Fibonacci sequence up to the given length.

    Parameters:
    length (int): The number of Fibonacci numbers to print.
    """
    if length <= 0:
        print([])
        return

    fibonacci_sequence = [0, 1]
    
    # Generate Fibonacci sequence up to the specified length
    while len(fibonacci_sequence) < length:
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_value)
    
    # Slice the list to ensure it does not exceed the requested length
    fibonacci_sequence = fibonacci_sequence[:length]
    
    # Print the resulting sequence
    print(fibonacci_sequence)
