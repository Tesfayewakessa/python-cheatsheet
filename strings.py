#Using python to manipulate strings
'''
python can be used to manipulate strings in several ways

strings can be enclosed in either single quotes '-----' or double quotes "-------"

'\' can be used to escape quotes-------------> like 'can'\t' or "can\'t"

python strings are immutable. They can't be changed.

The built in function len() returns the length of a string.

strings are a bunch methods available for use.

capitalize()    converts the first character to upper case letter
casefold()      converts string into lower case
center()        returns a centered string
count()         returns the number of times a specified value occurs in the string
encode()        retruns an encoded version of the string
endwith()       retruns true if the string ends with the specified value
expandtabs()    sets the tab size of the string
find()          searches the string for the specified value and returns the position where it was found
format()        formats the specified values in string
format_map()    formats specified values in a string
index()         searches the string for specified value and returns the position where is was found
isalnum()       returns true if all characters in the string are alphanumeric
isalpha()       returns true is all characters in the string are alphabets
isascii()       returns true is all characters in the string are ascii characters
isdecimal()     returns true if all characters in the string are decimals
isdigit()       returns true if all characters in the string are digits
isidentifier()  returns true is the string is an identifier
islower()       returns true is all characters in the string are lower case letters
isnumeric()     returns true is all characters in the string are numeric
isprintable()   returns true if all characters in the string are printable
isspace()       returns true if all the chosen characters in the string are whitespaces
istitle()       returns true is the string follows the rules of a title
isupper()       returns true if all characters in the string are all upper case 
join()          converts elements of an iterable into a string
ljust()         returns a left justified version of the string
lower()         converts a tring into lowercase
lstrip()        returns a left trimmed version of a string
maketrans()     returns a translation table to be used in translations
partition()     returns a tuple where the string is parted into three parts
replace()       returns a string where a specified value is replaced with a specified value
rfind()         searches a string for a specified value and returns the last position whereit was found 
rindex()        searches a string for a specified index value and returns the last position whereit was found
rjust()         returns a rightjustified version of a string
rpartition()    returns a tuple where the string is parted into three parts
rsplit()        returns a string at a specified separator, and returns a list
rstrip()        returns a right trimmed version of a string
split()         splits the strin at a specified separator and return a list
splitlines()    splits the string at line breaks and returns a string
startswith()    returns true if the string starts with a specified values
strip()         returns a trimmed version of a string
swapcase()      swaps cases. lower case becomes upper and vise versa
title()         converts the first character of each word to upper case
translate()     returns a translated string
upper()         converts a string into upper
zfill()         fills the string with a specified number of zero values at the beginning
'''
# The basics

'single quotes' #single quoutes
"double qoutes" #double quotes
'can\'t' # use of \' to escape the single quotes
"can't" # just use double cuotes

'Yes, they said!'
"Yes, they said!"
#using the function print will print the result of the string without code
#uses of \n

s = 'Frist line.\nSecond line' 
s# will not print the second line on new . Instead \n is included
print(s) #\n produces new line

#passing raw stringd
print('C:\pathname')
print(r'C:\pathname') # the r before  the quote--------->regular string

#https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals

#string literals

print("""
\usage: python cheatsheat with example [OPTIONS]
    -h   Display this usage message
    -H   print all available help
""")
msg = """
GamePad F710 usage:
Y/A increase/decrease the linear velocity by 20%
B/X increase/decrease the angular velocity by 20%
"""
print(msg)

#string concatination

first_name  = 'Tesfaye'
last_name = 'Wakessa'

full_name = first_name + ' ' + last_name
print(full_name) #prints without quotes

'python''_' 'cheatsheet' ' ' 'with example'

sentence  = ('Y/A increase/decrease the linear velocity by 20%' 
                'B/X increase/decrease the angular velocity by 20%')
#indexing
'''
 +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
 | E | T | H | I | O | P | I | A | N |   | C | O | D | E | R | 
 +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
 0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15
-16                             -8   -7  -6  -5  -4  -3  -2  -1
'''
title = 'ETHIOPIAN CODER'
title.title()
title.capitalize()
title.casefold()
title.istitle()
title.split() #returns a list
title.index(' ') #returns the position at which whitespace occurs

'''
    The rest of  the functions mentioned above can be used in a similar way
'''
title[0]  # character in position 0
title[5]  # character in position 5
title[0:2]  # characters from position 0 (included) to 2 (excluded)
title[2:5]  # characters from position 2 (included) to 5 (excluded)
title[:2]   # character from the beginning to position 2 (excluded)
title[4:]   # characters from position 4 (included) to the end
title[-2:]  # characters from the second-last (included) to the end
title[:2] + title[2:]
assert(title == title[:2]+title[2:])
title[:4] + title[4:]
assert(title == title[:4]+title[4:])

#changing string
title[0] = 'e'

#string length
len(title) 

#Handy built-in functtions
'''
    If we are only interested to  quickly display the output of some varialbles, specially for debugging purposes, 
    we can convert any of the values to a string using repr() and str() functions

    use str() function to represent values which are human-readable 
    use repr() function to generate a value which interpreter readable

    The other handy tool is format()
    The format() method formats the specified values and insert them inside the string's placeholder '{}'

'''
x = 1
y = 200
repr((x,y,('length','width')))
str((x,y,('height','width')))

print('{0} and {1}'.format('length','width'))
print('{0} and {1}'.format('height','width'))
print('x = {0} and y = {1}'.format(x,y))

name  = 'Tesfaye'
f"My name is {name}" # no conversion specified
f"My name is {name!r}" #repr() conversion
f"My name is {repr(name)}"

f"My name is {name!s}" #str() conversion specified

z = 20
value = 2.3445
precision = 3
f"{z:#0x}" # uses integer format specifier and converts 2.3045 to hexadecimal
f"{value:{z}.{precision}}"
foo  = "bar"
f"{foo = }" #white space is preserved
f"{foo = :20}" # returns 20 characters


