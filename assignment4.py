Python 3.3.3 (v3.3.3:c3896275c0f6, Nov 18 2013, 21:18:40) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Dictionary
>>> #clear() : removes all the data
>>> people = {'name':"ram",'age':"30",'hobby':"badminton"}
>>> people.clear()
>>> people
{}
>>> people = {'name':"ram",'age':"30",'hobby':"badminton"}

>>> people
{'name': 'ram', 'hobby': 'badminton', 'age': '30'}
>>> # copy(): returns a copy of dictionary.
>>> x = people.copy
>>> x
<built-in method copy of dict object at 0x01D90BE8>
>>> x = people.copy()
>>> x
{'name': 'ram', 'hobby': 'badminton', 'age': '30'}
>>> # fromkeys() : returns a dictionary with specified key and values
>>> x = {'key1','key2','key3'}
>>> y= {'0'}
>>> final = dict.fromkeys(x,y)
>>> final
{'key2': {'0'}, 'key3': {'0'}, 'key1': {'0'}}
>>> #get() :fetches the value from he dictionary.
>>> people.get("age")
'30'
>>> #itens(): returns a list of tuple containing key -value pair.
>>> people.items()
dict_items([('name', 'ram'), ('hobby', 'badminton'), ('age', '30')])
>>> #keys : returns a lis containing dictionary keys.
>>> people.keys()
dict_keys(['name', 'hobby', 'age'])
>>> #values : returns values of the dictionary.
>>> people.values()
dict_values(['ram', 'badminton', '30'])
>>> #pop; removes the element with specified key.
>>> people.pop("age")
'30'
>>> people
{'name': 'ram', 'hobby': 'badminton'}
>>> #update : updates the key-value pair.
>>> people.update('age':"56")
SyntaxError: invalid syntax
>>> people.update({'age':"65"})
>>> people
{'name': 'ram', 'hobby': 'badminton', 'age': '65'}
>>> 
