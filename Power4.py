
def is_power_of_4(number):
# A number is a power of 4 if:
# 1. It's greater than 0
# 2. It's a power of 2 (only one bit is set in binary representation)
# 3. The only set bit is at an even position (0-indexed)

    if number > 0 and (number & (number - 1)) == 0 and (number & 0xAAAAAAAA) == 0:
        return True
    return False

number = int(input("Enter a number: "))

if is_power_of_4(number):
    print("The number is a power of 4")
else:
    print("Number is not power of 4")