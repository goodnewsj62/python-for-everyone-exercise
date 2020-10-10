''' Exercise: Change the socket program socket1.py to prompt the user
for the URL so it can read any web page. You can use split('/') to
break the URL into its component parts so you can extract the host
name for the socket connect call. Add error checking using try and
except to handle the condition where the user enters an improperly
formatted or non-existent URL.

*you could use: data.pr4e.org 80 as input to test
*and use: romeo.txt as sub

from: Python for Everybody
Exploring Data Using Python 3
Charles R. Severance
'''

import socket

# test_info_url : data.pr4e.org
#

url = input('Enter non http (eg data.pr4e.org) url then a space and a port: ')
url_port = url.split()

if len(url_port) > 1:
    try:
        info_url = (url_port[0] , int(url_port[1]))
    except:
        print('Enter an integer')
else:
    raise IndexError('must enter a url and an integer')

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(info_url)
except:
    print('NO connection')
try:
    reqst = input('Enter sub url (eg data.pr4e.org/romeo.txt) if any: ')
    cmd = 'GET http://' + ''.join(url_port[0]) + '/' + reqst + ' HTTP/1.0\r\n\r\n'
    cmd = cmd.encode()
    mysock.sendall(cmd)

    count = 0

    while True:
        data = mysock.recv(1000)
        if len(data) < 1:
            break
        count += len(data)
        print(data.decode().rstrip())

    print('Here is the total size of data---', count)
except OSError:
    print('There was no connection!')
except:
    print('You have entered the wrong sub!')





'''
Exercise 2: Change your socket program so that it counts the number
of characters it has received and stops displaying any text after it has
shown 3000 characters. The program should retrieve the entire docu-
ment and count the total number of characters and display the count
of the number of characters at the end of the document.

*you could use: data.pr4e.org 80 as input to test
*and use: romeo.txt as sub

from: Python for Everybody
Exploring Data Using Python 3
Charles R. Severance
'''

url = input('Enter non http (eg data.pr4e.org) url then a space and a port: ')
url_port = url.split()
li = list()

if len(url_port) > 1:
    try:
        info_url = (url_port[0] , int(url_port[1]))
    except:
        print('Enter an integer')
else:
    raise IndexError('must enter a url and an integer')



try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(info_url)
except:
    print('NO connection')

try:
    reqst =  input('Enter sub url (eg romeo.txt) if any: ')
    #
    cmd = 'GET http:/'+''.join(url_port[0]) + '/' + reqst+' HTTP/1.0\r\n\r\n'
    cmd = cmd.encode()
    mysock.send(cmd)

    count = 0
    received = b''

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        count += len(data)
        received = data.decode()
        words = received.split()
        for word in words:
            li.append(word)


    #to remove most of the headers uncomment the two lines below
    #x = li.index('Content-Type:')
    #del li[:x]
    prnt = ''
    for each in li[:3000]:
        hold = ''.join(each)
        prnt += hold + ' '

    print(prnt)


    print('Here is the total size of data---', count)
    print('Here is the numbers of characters: ', len(li))
except OSError:
    print('There was no connection!')
except:
    print('You have entered the wrong sub!')


from urllib import request,parse,error


'''
Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving
the document from a URL, (2) displaying up to 3000 characters, and
(3) counting the overall number of characters in the document. Don’t
worry about the headers for this exercise, simply show the first 3000
characters of the document contents.
'''

input_url = input("Enter the url of the txt document: ")
url = ''
count = 0
hold_char = list()

input_url = input_url.strip()
if input_url[-4] == '.':
    url = input_url
else:
    raise AttributeError('Please enter a valid site that ends with \".foo\"')



try:
    data = request.urlopen(url)
    data = data.read().decode()
    # parse characters into list if its not up to 3000
    for each in data:
        each = each.strip()

        if each == ' ': # append white space without counting
            hold_char.append(each)
        else:
            hold_char.append(each)
            count += 1

except:
    print('connection error')

str_ = ''
for each in hold_char[:3000]:
    if each == '':
        str_ += ' '
    str_ += each

print(count)
print(str_)

#'http://data.pr4e.org/romeo.txt

'''
Exercise 4: Change the urllinks.py program to extract and count para-
graph (p) tags from the retrieved HTML document and display the
count of the paragraphs as the output of your program. Do not display
the paragraph text, only count them. Test your program on several
small web pages as well as some larger web pages.
'''


from bs4 import BeautifulSoup
import ssl

count = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url eg(https://www.python.org/): ')
url = url.strip()

html = request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('p')
for tag in tags:
    count += 1

print("number of p tags: ", count)


"""
Exercise 5: (Advanced) Change the socket program so that it only shows
data after the headers and a blank line have been received. Remember
that recv receives characters (newlines and all), not lines.
"""


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysock.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

hold_data = b""
while True:
    data = mysock.recv(512)
    if len(data) < 1: break

    hold_data += data

index = hold_data.find(b'\r\n\r\n')
important_data = hold_data[index + 4:]

print(important_data.decode(),end='')
mysock.close()