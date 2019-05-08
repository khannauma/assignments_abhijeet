Python 3.3.3 (v3.3.3:c3896275c0f6, Nov 18 2013, 21:18:40) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> salute= "morning"
>>> salute.upper()
'MORNING'
>>> # casefold() : converts string to lowercase
>>> fruit = "APPLES"
>>> fruit.casefold()
'apples'
>>> #count() : returns the number of times a particular value occurs in string.
>>> word ="mississippi"
>>> word.count("s")
4
>>> structure = "Structure"
>>> # index() : returns the specified position/value of the string.
>>> structure = "Structure"
>>> structure.index("c")
4
>>> structure.index("r")
2
>>> #isalnum(): returns TRUE if all the characters in the string are alphanumeric.
>>> str = "string1"
>>> str.isalnum()
True
>>> #isalpha() : returns TRUE if all the characters are alphabets.
>>> str.isalpha()
False
>>> #isidentifier() : returns TRUE if the string is an identifier.
>>> str = "testing123"
>>> str.isidentifier()
True
>>> #lower() : returns a string where all characters are lower case.
>>> str = "ThiS iS REAL"
>>> str.lower()
'this is real'
>>> #replace : replaces the value in the string.
>>> str = "I like apples."
>>> str.replace
<built-in method replace of str object at 0x018C8C00>
>>> str.replcae("apples","strawberries")
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    str.replcae("apples","strawberries")
AttributeError: 'str' object has no attribute 'replcae'
>>> x = str.replace("apples","strawberries")
>>> print (x)
I like strawberries.
>>> #swapcase : swaps the cases .
>>> str = "SwaP thIs String"
>>> str.swapcase()
'sWAp THiS sTRING'
>>> #zfill : adds 0 in the begining untill it reaches the defined length.
>>> str = "300"
>>> z = str.zfill(5)
>>> print(z)
00300
>>> 
