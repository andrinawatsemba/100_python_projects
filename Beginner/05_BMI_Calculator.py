weight = float(input('Enter your weight')) #variable prompting the user to input their weight

Hieght = float(input('enter  your hieght')) #variable prompting the user to input their hieght

#using float() because weight and height can include decimal points

bmi = weight/(Hieght**2) #calculating the bmi using it's formular
print(f'your BMI is {bmi}')

#using an if statement to give the user feedback based their bmi

if bmi < 18.5:
    print('category: Under weight')

elif bmi < 25:
    print('category: Normal weight')
elif bmi < 30:
    print('category:overweight')
else:
    print('category:Obese')    
