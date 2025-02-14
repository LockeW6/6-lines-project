# Get three three-digit numbers as input from the user
# Ensure input is valid and is converted to integers
num1 = int(input("Enter the first three-digit number: "))
num2 = int(input("Enter the second three-digit number: "))
num3 = int(input("Enter the third three-digit number: "))

if not (100 <= num1 <= 999 and 100 <= num2 <= 999 and 100 <= num3 <= 999):
    print("Please enter valid three-digit number！")

    num1 = int(input("Enter the first three-digit number: "))
    num2 = int(input("Enter the second three-digit number: "))
    num3 = int(input("Enter the third three-digit number: "))
else:
# Calculate the remainder of the first two numbers divided by 8
    remainder1 = num1 % 8
    remainder2 = num2 % 8
    remainder3 = num3 % 6

yin = "————  ————"
yang = "——————————"

def upper(remainder1):
    if remainder1 == 1:
        return f"{yang}\n{yang}\n{yang}"
    elif remainder1 == 2:
        return f"{yin}\n{yang}\n{yang}"
    elif remainder1 == 3:
        return f"{yang}\n{yin}\n{yang}"
    elif remainder1 == 4:
        return f"{yin}\n{yin}\n{yang}"
    elif remainder1 == 5:
        return f"{yang}\n{yang}\n{yin}"
    elif remainder1 == 6:
        return f"{yin}\n{yang}\n{yin}"
    elif remainder1 == 7:
        return f"{yang}\n{yin}\n{yin}"
    elif remainder1 == 8 or remainder1 == 0:
        return f"{yin}\n{yin}\n{yin}"

def lower(remainder2):
    if remainder2 == 1:
        return f"{yang}\n{yang}\n{yang}"
    elif remainder2 == 2:
        return f"{yin}\n{yang}\n{yang}"
    elif remainder2 == 3:
        return f"{yang}\n{yin}\n{yang}"
    elif remainder2 == 4:
        return f"{yin}\n{yin}\n{yang}"
    elif remainder2 == 5:
        return f"{yang}\n{yang}\n{yin}"
    elif remainder2 == 6:
        return f"{yin}\n{yang}\n{yin}"
    elif remainder2 == 7:
        return f"{yang}\n{yin}\n{yin}"
    elif remainder2 == 8 or remainder2 == 0:
        return f"{yin}\n{yin}\n{yin}"

original_upper = upper(remainder1)
original_lower = lower(remainder2)
Original_6_lines = original_upper + "\n" + original_lower
print("Original 6 lines：")
print(Original_6_lines)

def change(change, remainder3):
    if remainder3 == 0:
        return change

    lines = change.strip().splitlines() 
    index = len(lines) - remainder3

    if lines[index] == yin:
        lines[index] = yang
    elif lines[index] == yang:
        lines[index] = yin

    return "\n".join(lines) + "\n"

Changed_6_lines = change(Original_6_lines, remainder3)
print("Changed 6 lines：")
print(Changed_6_lines)