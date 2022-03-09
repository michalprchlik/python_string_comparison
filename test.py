#!/bin/python3

import timeit
name = 'Eric'
age = 74

print(timeit.timeit("""name = "Eric"
age = 74
'%s is %s.' % (name, age)""", number = 10000))

print(timeit.timeit("""name = "Eric"
age = 74
'{} is {}.'.format(name, age)""", number = 10000))

print(timeit.timeit("""name = "Eric"
age = 74
f'{name} is {age}.'""", number = 10000))

print(timeit.timeit("""name = "Eric"
age = 74
'name + "is" + str(age).'""", number = 10000))
