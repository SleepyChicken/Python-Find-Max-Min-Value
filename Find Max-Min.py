'''
        Written by SleepyChicken
'''

number = []                                         # list of number

X = None

while X != 'e' :
    X = input("") 
    if X.isdigit() == True :
        number.append(int(X))
    elif X == 'e' :
        print('You entered '+ str(len(number)) +' number')
        print(number)

if number[0] > number[1] :
    max = number[0]
    min = number[1]
elif number[0] < number[1] :
    max = number[1]
    min = number[0]
elif number[0] == number[1] :
    max = number[1]
    min = number[1]

for i in range(0, len(number)) :                  # loop to find maximum value
    if i == range(len(number)) :
        break
    elif number[i] > max :
        max = number[i]

for i in range(0, len(number)) :                  # loop to find maximum value
    if i == range(len(number)) :
        break
    elif number[i] < min :
        min = number[i]

print('maximum value is '+str(max))
print('minimum value is '+str(min))