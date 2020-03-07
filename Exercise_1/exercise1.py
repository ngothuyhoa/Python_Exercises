str = input('Enter String: ')
str1 = input('Enter String 1: ')
index = 0
count = 0

while (index < (len(str) - len(str1) +1)):
    end = index + len(str1)
    if str[index:end] == str1:
        count += 1
    index += 1
    
print('The number of occurrences of \"{}\" in \"{}\" is {}'.format(str1, str, count))