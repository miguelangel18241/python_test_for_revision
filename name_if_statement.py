name = input('What is your name? ')
lenth_is = (len(name))

if lenth_is < 3:
    print('Name must be at least 3 characters.')
    print('Try again.')
    
elif lenth_is > 50 :
    print ('Name can be a max of 50 characters.')
else :
    print('Name looks good.')
