
"""
AUTHOR: FELIPE MANTOVANI
DATE: 23/5/2018
PROJECT: RUDMENTARY BLOCKCHAIN IN PYTHON
"""


#importation of the library
import hashlib
import datetime
import json



"""
this function will encrypt all the arguments passed and return an a hashing of
all of the parameters converted into strings and incoded
"""
def encrypt(*args):
    string = b""
    for parameter in args:
        string += str(parameter).encode()
    return hashlib.sha256(string).hexdigest()


"""
The Transaction will hold the sender, receiver and the ammount transfered
the attributes will remain private and constants
"""
class Transaction:
    def __init__(self, SENDER_ADDRESS, RECEIVER_ADDRESS, AMMOUNT):
        self.__SENDER_ADDRESS = SENDER_ADDRESS
        self.__RECEIVER_ADDRESS = RECEIVER_ADDRESS
        self.__AMOUNT = AMMOUNT

    def getSenderAddress(self):
        return self.__SENDER_ADDRESS

    def getReceiverAddress(self):
        return self.__RECEIVER_ADDRESS
    def getAmount(self):
        return self.__AMOUNT


    def __str__(self):
        return json.dumps({"sender": self.__SENDER_ADDRESS, "receiver": self.__RECEIVER_ADDRESS, "amount": self.__AMOUNT},
                          separators=(",", ":"))


"""
The block class contains 5 attributes, the timeStamp: when the block has been created, the ledger: list of all 
pending transactions, the previousHash: pointing to the previous block, and CurrentHash: the hash of the current block
"""

class Block:
    def __init__(self, TIME_STAMP, LEDGER):
        self.__TIME_STAMP = TIME_STAMP
        self.__LEDGER = LEDGER



