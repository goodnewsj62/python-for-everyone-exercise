# using globals in function could be very useful
# i definitely use to have problems with this when i was starting up writing python
# i wondered why the variable objects outside a function could not be accessed unlike programming language like c++

# a simple example to demonstrate this is
count = 0

def add_number():
    for n in range(10):
        global count
        count += 1

add_number()
print(count)


import html

# you could specify a function to take in number of keyword arguments for example
# the code below takes in keyword arguments for a html tag and also take in the name of tag  and value to create a complete tag
# you can normally do this with the ** before any name of your choice but the most popular name used is kwarg
# eg: **kwarg or **attrs or **foo

def tag_creator(tag_name, value, **kwargs):
    atrr = [f'{key} = "{value}"' for key,value in kwargs.items()] # this is used to create a list of items of key = "value" eg class = "head"
    attr_str = ''.join(atrr) # this turns the list into strings
    tag = '<{head} {attributes} > {value} </{head}>'.format(head = tag_name, attributes = attr_str, value = html.escape(value))
    return tag


print(tag_creator('h3','hey', id = 'head'))