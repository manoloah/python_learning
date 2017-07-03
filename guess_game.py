import random


def guess(answer_number):
    for guess_tries in range (1,7):
        print('What is your guess?')
        guess_number = int(raw_input())
        if answer_number>guess_number:
            print('your guess is to low')
        elif answer_number<guess_number:
            print('your guess is to high')
        else:
            break
    if answer_number==guess_number:
        print('You guessed correctly after '+str(guess_tries)+ 'tries')
    if answer_number!=guess_number:
        print('I am sorry you are not a good guesser')

upper_limit = 10
lower_limit = 0

answer_number = random.randint(0,10)
print('My number is between '+ str(upper_limit)+' and '+str(lower_limit))
result = guess(answer_number)
print(result)
