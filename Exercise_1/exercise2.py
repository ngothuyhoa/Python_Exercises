celsius = input('Enter Celsius is Digit: ')

while (celsius.isalpha() or celsius == ''):
    celsius = input('Wrong!! Please enter celsius is digit: ')

fahrenheit = (float(celsius)*9)/5 +32

print('{}C = {}F'.format(celsius, fahrenheit))