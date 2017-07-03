#lists: matrix[row][column], row 1 starts at index o
#lists can have negative indexes:

list = ['potter','rooney','scholes']
print(list[-1]) # outputs the last value in list
#slices of lists list[startitem:enditem-1]
print(list[0:3])

i = 5
for i in range(4):
    print(i+1)

#to iterate over a list of values
for i in range(len(list)):
    print(list[i])

#assigning variables from a lists:
player_1,player_2,player_3 = list
print(player_3)
list.insert(4,'ronaldo') #append does the same but adds it at the end, remove()
print(list)
list.sort()
print(list)
list.sort(reverse=True)

#Many of the things you can do with lists can also be done with strings: indexing; slicing; and using them with for loops, with len(), and with the in and not in operators. To see this, enter the following into the interactive shell
name = 'Sophie' #tupple is treating a string as a list (example below)
for i in name:
    print('****'+i+'****')

#But the main way that tuples are different from lists is that tuples, like strings, are immutable
