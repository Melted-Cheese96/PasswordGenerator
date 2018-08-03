import random
from time import sleep 
import pyperclip


newPassword = [] 


alphabet = 'abcdefghijklmnopqrstuvwxyz'
numbers = 1243453457833

newPassword = '' 

def PasswordGenerator(levelOfSecurity):
    global newPassword
    if levelOfSecurity.lower() == 'easy':
        for num in range(1,5):
            newPassword += random.choice(alphabet)
        print('password generated.')
        print(str(newPassword))
        copy = input('Copy to clipboard?')
        if copy == 'yes':
            strver = str(newPassword)
            pyperclip.copy(strver)
            print('Copied to clipboard!')
        elif copy == 'no':
            pass
        else:
            print('Error')
    elif levelOfSecurity.lower() == 'medium':
        for num in range(1,11):
            newPassword.append(random.choice(alphabet))
            newPaassword.append(numbers)
        print('Password generated')
        print(str(newPassword))
    elif levelOfSecurity.lower() == 'hard':
        for num in range(1,22):
            newPassword.append(random.choice(alphabet))
            newPassword.append(numbers)
        print('Password generated!')
        print(str(newPassword).strip('[]'))
        

passwordsec = input('Enter difficulty of password')
print('You have entered {}'.format(passwordsec))
PasswordGenerator(passwordsec)
