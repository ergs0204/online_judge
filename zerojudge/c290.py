def secret_difference(x):
    sum_odd = 0  # Sum of digits in odd positions
    sum_even = 0  # Sum of digits in even positions

    # Iterate over the digits, with index starting from 0
    for i, digit in enumerate(x_str):
        if i % 2 == 0:
            sum_even += int(digit)  # Even index, but odd position in number
        else:
            sum_odd += int(digit)  # Odd index, but even position in number

    # Calculate the absolute difference
    return abs(sum_odd - sum_even)

# Read the input number
x = input()

# Output the secret difference
print(secret_difference(x))