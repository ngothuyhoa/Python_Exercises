#firt: The user will choose whether to add the list or not
# Enter 1 to add item to list or Enter any key to ignore
#then: Enter item need check, program stop when item entered is ''

listItem = ['iphone', 'samsung', 'oppo']
choose = input('Please choose one:\nEnter 1 to add item to list\nEnter any key to ignore\n')

if choose == '1':
    listItem += list(input('Enter list item: ').split(','))
    
tmp = 0
while (tmp == 0):
    item = input('Enter item need check: ')
    if(item != ''):
        if item in listItem:
            print('Available')
        else:
            print('Out of stock!')
    else:
        tmp = 1