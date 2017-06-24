#Loops & imports
import random, sys
user_age = 0
while user_age < 5:
    print('You are still younger than 5')
    user_age = user_age +1

user_name = ''
while user_name != 'your name':
    print('What is your name?')
    user_name = raw_input()
print('Your name is not your name')
##he first line creates an infinite loop; it is a while loop whose condition is always True. (The expression True, after all, always evaluates down to the value True.) The program execution will always enter the loop and will exit it only when a break statement is executed. (An infinite loop that never exits is a common programming bug.)

while True:
     print('Please type your name.')
     user_name = raw_input()
     if user_name == 'your name':
         break
print('Thank you!')

while True:
    print('Who are you?')
    name = raw_input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = raw_input()
    if password == 'swordfish':
        break
print('Access granted.')

print('what is your name five times?')
user_name = raw_input()
for i in range(5):
    print(user_name + str(i))

total = 0
num = 1
for num in range(101):
    total = total + num
print(total)
num = 0
for num in range(0,10,1):
    total = total + num
print(total)

#import modules example
total = random.randint(1,10)
total = str(total)
print('your random number is '+ total)
