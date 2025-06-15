#get 2 numbers from the user
first_number = float(input("enter first number"))
second_number = float(input("enter second number"))

#show available operators
print('1. addition (+)')
print('2. subtraction (-)')
print('3. multiplication (+)')
print('4. division (+)')

#get users's choice
choice = input('enter your choice (1/2/3/4):')

#if statement to perform calculations based on choice

if choice == '1':
    result = first_number + second_number
    print(f'Result: {first_number} + {second_number} = {result}')
elif choice == '2':
    result = first_number - num2
    print(f"Result: {first_number} - {second_number} = {result}")

elif choice == '3':
    result = first_number * second_number
    print(f"Result: {first_number} * {second_number} = {result}")

elif choice == '4':
    if second_number == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = first_number / second_number
        print(f"Result: {first_number} / {second_number} = {result}")

else:
    print("Invalid input. Please select 1, 2, 3, or 4.")