#Exercise 1

def nameupper():
    name = input('Type your name:')
    x = name.upper()
    print(x)

#Exercise 2

def evennumbers(array):
    new_array = [x for x in array if x % 2 == 0]
    print(new_array)

#Exercise 3

def dat_invers(dat_name):
    with open(dat_name, "r") as dat:
        text = dat.readlines()

    for i in text:
        res = i[::-1]
        print(res.strip())

#Exercise 4

import string

def mostfrequentwords(filename):

    with open(filename, 'r') as file:
        text = file.read()
    
    text = text.translate(str.maketrans('','',string.punctuation))
    listofwords = text.lower().split()
    
    dic = dict()
    for i in listofwords:
        if not i in dic:
            dic[i]=1 
        elif i in dic:
            dic[i]+=1

    sorted_dic = sorted(dic.items(), key = lambda x: x[1], reverse=True)

    for i in sorted_dic[:10]:
        print(i)


#Exercise 5

import unicodedata

def cleaner(filename):
    with open(filename, 'r') as file:
        text = file.read()

    print('Original text: \n\"'+ text+ '\"')

    text = text.lower()
    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ASCII', 'ignore').decode('utf-8')

    for i in string.punctuation + '"''':
        text = text.replace(i, ' ' +i+ ' ')

    text = text.split()
    print('\nCleaned text elements: ')
    print(text)

    text = ' '.join(text)
    print('\nCleaned joined text: ')
    print(text)

###########################################################

# Create function that:

s = 'I am a string with an A.'

# 1. Reverse string:

def reverser(string):
    res = string[::-1]
    return print(res)


# 2. How many 'a' and 'A':

def howmany_a_or_A(string):
    count_a, count_A = 0 , 0
    for i in string:
        if i == 'a':
            count_a += 1
        if i == 'A':
            count_A += 1
    return print('Count of \'a\': ', count_a ,'\nCount of \'A\': ', count_A)


# 3. How many vowels (a, e, i, o, u):

def numberofvowels(string):
    count_vowels = 0
    for i in string:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            count_vowels += 1
    return print('Count of vowels is: ', count_vowels)


# 4. Convert to lower case:

def lowercase(string):
    res = string.lower()
    return print(res)


# 5. Convert to upper case:

def lowercase(string):
    res = string.upper()
    return print(res)

