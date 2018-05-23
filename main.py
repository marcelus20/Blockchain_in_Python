
"""
AUTHOR: FELIPE MANTOVANI
DATE: 23/5/2018
PROJECT: RUDMENTARY BLOCKCHAIN IN PYTHON
"""


#importation of the library
import hashlib
import datetime
import json
from typing import Any

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

    #GETTERS
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
pending transactions, the previousHash: pointing to the previous block,  CurrentHash: the hash of the current block
and the nonce that will be increased until the hash problem solve is finished during the mining period of the block
"""

class Block:
    def __init__(self, TIME_STAMP, LEDGER, previousHash =""):
        self.__TIME_STAMP = TIME_STAMP
        self.__LEDGER = LEDGER
        self.__previousHash = previousHash
        self.__nonce = 0
        self.__hash = self.createHash()


    def createHash(self):
        return encrypt(self.__TIME_STAMP, self.__LEDGER, self.__previousHash, self.__nonce)


    #the mine block method gets a dificulty as a parameter, the higher the difficulty the more time is needed to mine the block

    def mineBlock(self, difficulty):

        while self.__hash[0:difficulty] !=difficulty*"0":
            self.__nonce = self.__nonce + 1
            self.__hash = self.createHash()

    # GETTERS

    def getPreviousHash(self):
        return self.__previousHash

    def getNonce(self):
        return self.__nonce

    def getTimeStamp(self):
        return self.__TIME_STAMP

    def getLedger(self):
        return self.__LEDGER

    def getHash(self):
        return self.__hash

    # setter
    def setPreviousHash(self, previousHash):
        self.__previousHash = previousHash
        self.__hash = self.createHash()


    def __str__(self):
        return json.dumps(
            {"Date": self.__TIME_STAMP,
             "Ledger": self.__LEDGER,
             "Previous Hash": self.__previousHash,
             "Hash": self.__hash,
             "nonce": self.__nonce},

            separators=(",", ":"))




