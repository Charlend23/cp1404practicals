# TODO: Use f-string formatting to produce the output:
print(f"{year} {name} for about ${cost:,.2f}")

# TODO: Using a for loop with the range function and f-string formatting,
numbers = (1, 19, 123, 456, -25)

for i, number in enumerate(numbers, 1):
    print(f"Number {i} is {number:5}")
# produce the following right-aligned output (DO NOT use a list):
# 2 ^ 0 is    1
# 2 ^ 1 is    2
# 2 ^ 2 is    4
# 2 ^ 3 is    8
# 2 ^ 4 is   16
# 2 ^ 5 is   32
# 2 ^ 6 is   64
# 2 ^ 7 is  128
# 2 ^ 8 is  256
# 2 ^ 9 is  512
# 2 ^10 is 1024