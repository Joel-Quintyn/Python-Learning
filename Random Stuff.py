"""
    TODO: Encryption Program
"""
mystring = 'iloveyou'

for letter in mystring:
    x = ord(letter) + 2
    print("{} - {} {}".format(ord(letter), letter, x))
