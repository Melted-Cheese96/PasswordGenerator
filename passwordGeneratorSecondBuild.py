from time import sleep
import random
import pyperclip

possibleResponses = ['Y', 'y', 'Yes', 'yes']



def PasswordGenerator(difficulty):
    newPassword = ''
    global alphabet
    if difficulty.lower() == 'easy':
        for passw in range(1,5):
            newPassword += random.choice(alphabet)
        print('Password generated')
        print(newPassword)
        print('Copy to clipboard?')
        copy = input()
        if copy.lower() in possibleResponses:
            pyperclip.copy(newPassword)
            print('Item has been copied to clipboard!')
        elif copy.lower() == 'no':
            print('Item has not been copied to clipboard')
        else:
            print('Error, did you type something wrong?')

    elif difficulty.lower() == 'medium':
        for passw in range(1,11):
            newPassword += random.choice(alphabet)
        print('password has been generated')
        print(newPassword)
        print('Copy to clipboard?')
        copy = input()
        if copy.lower() in possibleResponses:
            pyperclip.copy(newPassword)
        else:
            print('Item not copied')

    elif difficulty.lower() == 'hard':
        for passw in range(1,22):
            newPassword += random.choice(alphabet)
        print('Password generated')
        print(newPassword)
        print('Copy to clipboard?')
        copy = input()
        if copy.lower() in possibleResponses:
            pyperclip.copy(newPassword)
            print('Item has been copied to your clipboard!')


alphabet = 'abcdefghijklmnopqrstuvwxyz'
numbers = 12346



print("Enter the difficulty of your password, you can choose from 'easy', 'medium' and 'hard'")
option1 = input()
print('Generating password')
PasswordGenerator(option1)

