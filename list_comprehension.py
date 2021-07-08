# List comprehension offers a shorter syntax when you want to create a new list
# based on the value of an existing list

# Usual pattern
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
newList = []

# for x in fruits:
#     if 'a' in x:
#         newList.append(x)

# newList.sort()
# print(newList) 

# List Comprehension pattern
# newList = [each_fruits for each_fruits in fruits if 'a' in each_fruits]

# print(newList)
def getEvenNumbers(y):
    even_Numbers = [x for x in range(y) if x % 2 == 0]
    print(even_Numbers)

def getOddNumbers(y):
    odd_Numbers = [x for x in range(y) if x % 2 == 1]
    print(odd_Numbers)

def printText(x):
    obj = ['even' if i % 2 == 0 else 'odd' for i in range(x)]
    print(obj)

getOddNumbers(20)
getEvenNumbers(20)
printText(20)