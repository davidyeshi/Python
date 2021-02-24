# Strings are indexed in python

# Hello World :D
print('Hello World')

# Print new line with \n
print('Hello \n World')

# Check the length of string
len('Hello World')

# Assign string and print object
s = 'Hello'
print(s)

# Checking elements in string
s[0]
s[1]

# We can use a : to perform slicing which grabs everything
# up to a designated point

# GRab everything past the first term
s[1:]

# Grab everything upto the 3rd index
s[:3]

#Everything
s[:]

# We can use negative indexing to go backwards
# Last letter (one index behind 0 so it loops back around
s[-1]

# Grab everything but the last letter
s[:-1]

# We can also use index and slice notation to grab elements of a sequence by a
# specified step size (the default is 1). For instance we can use two colons in
# a row and then a number specifying the frequency to grab elements. For example

# Grab everything but go in steps size of 1
s[::1]

# Grab everything but go in steps size of 2
s[::2]


# ## String properties
# Its important to note that strings have an important property known as immutability. 
# This means that once a a string is created, the elements within 
# it cannot be changed or replaced

# example
s[0] = 'x'

# concatenate strings!
s + ' concatenate'

# we can reassign s completely though
s = s + ' concatenate'

# we can use the multiplication symbol to create repetition
letter = 'z'
letter * 10


# ## Basic Built-in String methods
#
# Objects in python usually have built-in methods. These methods are functions
# inside the object that can perform actions or commands of the object itself

# Some examples

# Upper case a string
s.upper()

# Lower Case a string
s.lower()

# Split a string by blank space (this is the default)
s.split()

# Split by a specific element
s.split('c')

# There are many more methods, go to google lol

# ## Print Formatting

# We can use the .format() method to add formattted objects to printed string statements.
# example
'Insert another string with curly brackets: {}'.format('The inserted string')

# Other examples

print('This is a string with an {p}'.format(p = 'insert'))

# Multiple items
print('One: {p}, Two: {p}, Three: {p}'.format(p="Hi!"))

# Several objects
print('Object 1: {a}, Object 2: {b}, Object 3: {c}'.format(a=1, b='two', c=12.3))