# 1. Define the id of next variables:
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

print(id(int_a), id(str_b), id(set_c), id(lst_d), id(dict_e))
# 9790688 139912523504368 139912523690048 139912523458560 139912525345216

# 2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d.append(4)
lst_d.append(5)
print(id(lst_d))
# 139912523458560

# 3. Define the type of each object from step 1.
print(type(int_a), type(str_b), type(set_c), type(lst_d), type(dict_e))
#<class 'int'> <class 'str'> <class 'set'> <class 'list'> <class 'dict'>

# 4*. Check the type of the objects by using isinstance
print(isinstance(int_a, int))
print(isinstance(str_b, str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict))

#String formatting:
#Replace the placeholders with a value:
#"Anna has ___ apples and ___ peaches."
#5. With .format and curly braces {}
amount_apples = 3
amount_peaches = 'has no'
print('Anna has {} apples and {} peaches.'.format(amount_apples,amount_peaches))
# Anna has 3 apples and has no peaches.

#6. By passing index numbers into the curly braces.
print('Anna has {0} apples and {1} peaches.'.format(amount_apples,amount_peaches))
# Anna has 3 apples and has no peaches.

#7. By using keyword arguments into the curly braces.
print('Anna has {amount_apples} apples and {amount_peaches} peaches.'.format(amount_apples = 3, amount_peaches = 2))
# Anna has 3 apples and 2 peaches.

#8*. With indicators of field size (5 chars for the first and 3 for the second)
print('Anna has {0:5} apples and {1:3} peaches.'.format(amount_apples,amount_peaches))
# Anna has     3 apples and has no peaches.

#9. With f-strings and variables
print(f'Anna has {amount_apples} apples and {amount_peaches} peaches.')
# Anna has 3 apples and has no peaches.

#10. With % operator
print('Anna has %s apples and %s peaches' % (amount_apples, amount_peaches))
# Anna has 3 apples and has no peaches

#11*. With variable substitutions by name (hint: by using dict)
print('Anna has %(amount_apples)s apples and %(amount_peaches)s peaches' % {'amount_apples' : 1, 'amount_peaches' : 2})
# Anna has 1 apples and 2 peaches

#12. Convert (1) to list comprehension
lst_comprehension = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(lst_comprehension)
# [0, 1, 16, 9, 256, 25, 1296, 49, 4096, 81]

#13. Convert (2) to regular for with if-else
lst = []

for num in range(10):
    if num % 2 == 0:
        lst.append(num // 2)
    else:
        lst.append(num * 10)
print(lst)
# [0, 10, 1, 30, 2, 50, 3, 70, 4, 90]

#14. Convert (3) to dict comprehension.
d_comprehension = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(d_comprehension)
# {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

#15*. Convert (4) to dict comprehension.
d_comprehension_4 = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(d_comprehension_4)
# {1: 1, 2: 4.0, 3: 9, 4: 8.0, 5: 25, 6: 12.0, 7: 49, 8: 16.0, 9: 81, 10: 20.0}

#16. Convert (5) to regular for with if.
dict = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict[x] = x**3
print(dict)
# {0: 0, 2: 8, 4: 64, 6: 216, 8: 512}

#17*. Convert (6) to regular for with if-else.
dict_2 = {}
for x in range(10):
    if x**3 % 4 == 0:
        dict_2[x] = x**3
    else:
        dict_2[x] = x
print(dict_2)
# {0: 0, 1: 1, 2: 8, 3: 3, 4: 64, 5: 5, 6: 216, 7: 7, 8: 512, 9: 9}

#18. Convert (7) to lambda function
foo = lambda x, y: x if x < y else y

#19*. Convert (8) to regular function
def foo_1(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y

#20. Sort lst_to_sort from min to max
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort))
# [1, 5, 13, 15, 18, 24, 33, 55]

#21. Sort lst_to_sort from max to min
print(sorted(lst_to_sort, reverse=True))
# [55, 33, 24, 18, 15, 13, 5, 1]

#22. Use map and lambda to update the lst_to_sort by multiply each element by 2
print(list(map(lambda x: x * 2, lst_to_sort)))
# [10, 36, 2, 48, 66, 30, 26, 110]

#23*. Raise each list number to the corresponding number on another list:
list_A = [2, 3, 4]
list_B = [5, 6, 7]
print(list(map(lambda x, y: x + y, list_A, list_B)))
# [7, 9, 11]

# 24. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
print(list(filter(lambda x: x % 2 == 1, lst_to_sort)))
# [5, 1, 33, 15, 13, 55]

# 25. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
print(list(filter(lambda x: x < 0, range(-10, 10))))
# [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

# 26*. Using the filter function, find the values that are common to the two lists:
list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]
print(list(filter(lambda x: x in list_1, list_2)))
# [2, 3, 5, 7]
