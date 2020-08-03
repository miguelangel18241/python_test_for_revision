price = 1000000
has_good_c = True

if has_good_c:
    down_payment = 0.01 * price
else:
    down_payment = 0.02 * price

print (f"Down payment: ${down_payment}")

name = 'What is your name? '
lenth_is = (len(name))

if lenth_is < 3:
    print('Name must be at least 3 characters.')
elif lenth_is > 50 :
    print ('Name can be a max of 50 characters.')
else :
    print('Name looks good.')
