# An iterator is an object that contains a countable number of values.
# An object that can be iterated upon. meanimg that you can traverse through all the values.
# Technically in python, an iterator is an object which implements the iterator protocol which consists of the method iter() and next()

# Simole iterators

#  - list
my_list = [1, 2, 3]

for i in [1, 2, 3, 4]:
    print(i)

my_iter = iter(my_list)

print(my_list)
print(my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))


