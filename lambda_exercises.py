''' 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = list(filter(lambda x: (x % 2 == 0), list1))
odd = list(filter(lambda x: (x % 2 == 1), list1))

print(even)
print(odd)

''' 2)
find which days of the week have exactly 6 characters.
'''

weekdays = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']
print(list(filter(lambda x: len(x) == 6, weekdays)))

''' 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']
'''
list2 = ['orange', 'red', 'green', 'blue', 'white', 'black']
print(list(filter(lambda x: (x != 'orange' and x != 'black'), list2)))

''' 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 '''
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]

print(list(filter(lambda x: x not in list2, list1)))

''' 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

'''
list1 = ['red', 'black', 'white', 'green', 'orange']
print(list(filter(lambda x: 'ack' in x, list1)))
print(list(filter(lambda x: 'abc' in x, list1)))


''' 6)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
'''

str1 = "Hello8world"
#str1 = "HELLO"
#str1 = "hello"

password_return = (lambda x: any(i.isupper() for i in x) and any(i.islower() for i in x) and any(i.isdigit() for i in x) and len(x) >= 8)
print(password_return(str1))


''' 7)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''

original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
sorted_scores = sorted(original_scores, key=lambda x: x[1])

print(sorted_scores)