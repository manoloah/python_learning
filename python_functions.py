## How to define functions in python

def hello(user_name):
    print('Hi '+ user_name + '!')


import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'

r= random.randint(1,5)
fortune = getAnswer(r)
print(fortune)

# Variables can be local within functions and global outside functions
spam = 'global bacon'
bacon = 'global bacon'
def spam_loc():
    bacon = 'local bacon'
    return bacon

#but also local variables within programs can be declared global

def spam_glob():
    global bacon
    return bacon

print(spam_loc())
print(spam)
print(spam_glob())


#How to run over errors (example an error that could ocurr but you still want code to continue running)
#Example:
#def math_error(divide_by):
    #result= 42/divide_by
    #return result
#print(math_error(0))

def math_error(divide_by):
    try:
        result= 42/divide_by
    except ZeroDivisionError:
        print('division by zero')
print(math_error(0))
