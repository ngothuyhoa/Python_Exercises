listItem = {'iphone': 10, 'samsung': 20, 'oppo': 0}
tmp=0
while (tmp == 0):
    item = input('Enter item need check: ')
    if(item != ''):
        if item in listItem and listItem[item] > 0:
            print('{} items vailable'.format(listItem[item]) )
        else:
            print('Out of stock!')
    else:
        tmp = 1