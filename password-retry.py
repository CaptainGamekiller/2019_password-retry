i = 3
while True and i > 0:
    password = input('Please input the password. You have up to 3 attempts: ')
    if password == 'a123456':
        print('Login successful!')
        break  
    else:
        i = i - 1
        print('Incorrect password!')
        if i > 0:
            print('You have', i, 'attempts left.')
