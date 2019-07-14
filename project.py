"""
Write 2 functions that perform a "Caesar Cipher" on a string.
A Caesar Cypher is a classic example in cryptography wherein
a user encodes a message by using a shift in the alphabet. They give
their key to the decoder, and with that key, the decoder can read the
intended message from apparent gibberish.

Upload code to blackboard as a .txt file.

"""

'''
Write a function with the following description:
    input: a string S consisting of only lower cases letters and empty spaces
    of arbitrary length, and n, an integer;

    output: A string W = T+str(n). T is a string which has been encrypted by
    by replacing each letter in the string s by a letter n letters ahead in the
    alphabet.
    Shifting by z by 1 letter gives a
'''

# Message to Grader:
# All functions give return, to see output print(function)
# I was hoping we covered dictionaries before this project was due,
# dictionaries were the first thing that popped into my head
# to do when writing this code
# Names for things are just letters, too lazy to name them.

def encryption(S, n):

    x = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
         'j':10, 'k': 11, 'l':12, 'm':13, 'n':14, 'o': 15, 'p': 16, 'q': 17, 'r': 18,
         's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    y = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i',
         10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r',
         19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}

    # Use a dictionaries to inter-swap between integers and letters
    l = []
    W = ''

    # l will be where we append the translated code
    # W will be the output in string

    # Iterate through the string to encrypt, careful steps at spaces and n values > 26
    # First made letters integer values, then added n to "shift" down the line
    # new sum of n and letter is then translated back to letter form
    for i in S:
        if i == ' ':
            l.append(i)
        elif x[i] + n >= 26:
                if (x[i] + n ) % 26 == 0:
                    z = (x[i] % 26) + n
                    l.append(y[z])
                else:
                    z = (x[i] + n) % 26
                    l.append(y[z])
        else:
            z = x[i] + n
            l.append(y[z])
        T = ''.join(l)
        W = T + str(n)
    return W

def decryption(W):

    x = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8,
         'j':9, 'k': 10, 'l':11, 'm':12, 'n':13, 'o': 14, 'p': 15, 'q': 16, 'r': 17,
         's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
    y = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i',
         9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r',
         18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}

    # Dictionaries for switching out letters and integers
    # now we have to shift back left from the int at the end of the string
    # shift back left means subtracting so a needs to be 0.

    j = []
    k = []
    l = []

    # j is for finding letters in the decrypted string
    # k is for finding numbers in the encrypted string
    # l is where we append the translated string

    # Iterate to separate letters from integers
    for i in W:
        if i in '0123456789':
            k. append(i)
        else:
            j.append(i)
    j1 = ''.join(j)

    k1 = ''.join(k)
    k2 = int(k1)

    # Iterate through the encrypted message to translate it back, careful steps at spaces and when end integers are high
    for i in j1:
        if i == ' ':
            l.append(i)
        elif x[i] - k2 < 0:
            z = (x[i] - k2) % 26
            l.append(y[z])
        else:
            z = x[i] - k2
            l.append(y[z])
        S = ''.join(l)
    return S

# Just a test function pay no attention
def test():
    a = encryption('hello world', 1)
    b = encryption('zebra', 11)
    c = encryption('zebra', 26)
    d = encryption('zebra', 59)
    e = encryption('zebra', 1000)
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(decryption(a))
    print(decryption(b))
    print(decryption(c))
    print(decryption(d))
    print(decryption(e))
test()
