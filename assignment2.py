Python 3.3.3 (v3.3.3:c3896275c0f6, Nov 18 2013, 21:18:40) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #append() : adds element at the end of the list.
>>> l1 = [1,2,3,4,"uma"]
>>> l1.append("me")
>>> l1
[1, 2, 3, 4, 'uma', 'me']
>>> # clear() : rremoves all the element from the list.
>>> l1.clear()
>>> l1
[]
>>> l1 = [1, 2, 3, 4, 'uma', 'me']
>>> l1
[1, 2, 3, 4, 'uma', 'me']
>>> l2.copy(l1)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    l2.copy(l1)
NameError: name 'l2' is not defined
>>> l2 = l1.copy()
>>> l2
[1, 2, 3, 4, 'uma', 'me']
>>> #copy : returns the copy of the list.
>>> #count :returns the number of element with specified value.
>>> l1.count()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    l1.count()
TypeError: count() takes exactly one argument (0 given)
>>> l3 = l1.count()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    l3 = l1.count()
TypeError: count() takes exactly one argument (0 given)
>>> l3 = l1.count("4")
>>> l3
0
>>> # extend():adds element at the end,in the current list.
>>> l4 = ["yes",5,6,7,8]
>>> l5 = l1.extend(l4)
>>> l5
>>> l5
>>> l1.extend(l4)
>>> l1
[1, 2, 3, 4, 'uma', 'me', 'yes', 5, 6, 7, 8, 'yes', 5, 6, 7, 8]
>>> #index(): returns the index of first element with specified value.
>>> l1.index()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    l1.index()
TypeError: index() takes at least 1 argument (0 given)
>>> l1.index("yes")
6
>>> #insert : inserts value at the specified index.
>>> l1.insert(1,"orange")
>>> l1
[1, 'orange', 2, 3, 4, 'uma', 'me', 'yes', 5, 6, 7, 8, 'yes', 5, 6, 7, 8]
>>> #pop : removes the element at specified position
>>> l1.pop(1)
'orange'
>>> l1
[1, 2, 3, 4, 'uma', 'me', 'yes', 5, 6, 7, 8, 'yes', 5, 6, 7, 8]
>>> #reverse(): reverses the order of the list.
>>> l1.reverse()
>>> l1
[8, 7, 6, 5, 'yes', 8, 7, 6, 5, 'yes', 'me', 'uma', 4, 3, 2, 1]
>>> l1.reverse()
>>> l1
[1, 2, 3, 4, 'uma', 'me', 'yes', 5, 6, 7, 8, 'yes', 5, 6, 7, 8]
>>> #remove : removes the first element.
>>> l1.remove()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    l1.remove()
TypeError: remove() takes exactly one argument (0 given)
>>> l1.remove(0)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    l1.remove(0)
ValueError: list.remove(x): x not in list
>>> l1.remove("0")
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    l1.remove("0")
ValueError: list.remove(x): x not in list
>>> l1.remove("yes")
>>> l1
[1, 2, 3, 4, 'uma', 'me', 5, 6, 7, 8, 'yes', 5, 6, 7, 8]
>>> # sort() : sorts the list
>>> l1.sort()
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    l1.sort()
TypeError: unorderable types: str() < int()
>>> l6 = l1.sort()
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    l6 = l1.sort()
TypeError: unorderable types: str() < int()
>>> 
