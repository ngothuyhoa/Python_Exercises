import math

edge1 = input('Enter the first edge: ')
while (edge1.isalpha() or edge1 == ''):
    edge1 = input('Wrong!! Enter the first edge is Digit: ')
    
edge2 = input('Enter the second edge: ')
while (edge2.isalpha() or edge2 == ''):
    edge2 = input('Wrong!! Enter the second edge is Digit: ')
    
edge1 = float(edge1)
edge2 = float(edge2)
hypotenuse = math.sqrt(pow(edge1, 2) + pow(edge2, 2))
area = (edge1*edge2)/2
print('Hypotenuse length is : {} \nArea of the triangle is : {}'.format(hypotenuse, area))
