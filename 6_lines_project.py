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

# Calculate the remainder of the third number divided by 6
    remainder3 = num3 % 6



# Display the results upper
upper_lines=print(f"{remainder1}")
if remainder1 == 1:
    print("——————————\n——————————\n——————————\n")
elif remainder1 == 2:
    print("————  ————\n——————————\n——————————\n")
elif remainder1 == 3:
    print("——————————\n————  ————\n——————————\n")
elif remainder1 == 4:
    print("————  ————\n————  ————\n——————————\n")
elif remainder1 == 5:
    print("————  ————\n——————————\n————  ————\n")
elif remainder1 == 6:
    print("————  ————\n——————————\n————  ————\n")
elif remainder1 == 7:
    print("————  ————\n————  ————\n————  ————\n")
elif remainder1 == 8:
    print("————  ————\n————  ————\n————  ————\n")
elif remainder1 == 0:
    print("————  ————\n————  ————\n————  ————\n")


lower_lines=print(f"{remainder2}")
if remainder2 == 1:
    print("——————————\n——————————\n——————————\n")
elif remainder2 == 2:
    print("————  ————\n——————————\n——————————\n")
elif remainder2 == 3:
    print("——————————\n————  ————\n——————————\n")
elif remainder2 == 4:
    print("————  ————\n————  ————\n——————————\n")
elif remainder2 == 5:
    print("————  ————\n——————————\n————  ————\n")
elif remainder2 == 6:
    print("————  ————\n——————————\n————  ————\n")
elif remainder2 == 7:
    print("————  ————\n————  ————\n————  ————\n")
elif remainder2 == 8:
    print("————  ————\n————  ————\n————  ————\n")
elif remainder2 == 0:
    print("————  ————\n————  ————\n————  ————\n")

#Original_6_lines = print(f"{upper_lines}+{lower_lines}")

print(f"The remainder when the third number ({num3}) is divided by 6 is: {remainder3}")
if remainder3 == 1:
    print("- - -")

