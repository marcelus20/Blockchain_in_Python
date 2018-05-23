#importation of the library
import hashlib
import datetime



"""
this function will encrypt all the arguments passed and return an a hashing of
all of the parameters converted into strings and incoded
"""
def encrypt(*args):
    string = b""
    for parameter in args:
        string += str(parameter).encode()
    return hashlib.sha256(string).hexdigest()

