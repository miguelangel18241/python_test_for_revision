course = '''
Good morning,

Thanks for your email, we will get back to you as soon as we can.

Regards,

Miguel
CEO
'''

test2 = (course[:])
test3 = (test2 * 100)

name = 'Jennifer'
last = 'Perez'
msg = name + ' ' + last
print (msg)

message = f'{name} [{last}] is a coder.'
print (message)

message2 = name + (name[0])+ 'is a coder'
print (message2)

lastMessage = f'{name} [{last}] is a coder'
print (lastMessage)

nombre = input('What is your name? ')
apellido = input("What is your last name? ")
message3 = f'Hola {nombre} {apellido}, you are on the right way! '
print (message3)


course1 = '''
Good morning,

Thanks for your email, we will get back to you as soon as we can.

Regards,

Miguel
CEO
'''
lenght_is = (len(course1))
message = f'This email contains {lenght_is} letters.'

print (message)
