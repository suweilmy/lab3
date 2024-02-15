numbers = []


for i in range(10):
    try:
        num = float(input(f"Enter value {i + 1}: "))
        numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter a valid number.")


largest = numbers[0]


for num in numbers:
    if num > largest:
        largest = num

print(f"The largest number entered is: {largest}")