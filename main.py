
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



"""
BLOCKCHAIN CLASS is just an list of blocks, the attributes are chain: the list of linked blocks, difficulty: the level 
of mining and pending transactions: an list of transactions that will be mined by a miner in order to validate them
"""
class Blockchain:
    def __init__(self):
        self.chain = [self.createGenesisBlock()]#CREATING AND ADDING GENESIS BLOCK
        self.difficulty = 4
        self.pendingTransactions = []
        self.reward = 100

    #THE VERY FIRST BLOCK CREATED AUTOMATICALLY BY THE SYSTEM
    def createGenesisBlock(self):
        return Block(datetime.datetime.now().strftime("%d-%m-%Y %H:%M"), [Transaction(None, None, None)])


    #appending transactions to pending transaction attribute
    def createATransaction(self, TRANSACTIONS):
        self.pendingTransactions.append(TRANSACTIONS)


    def getLatestBlock(self):
        return self.chain[-1]


    def miningPendingTransactions(self, MINER_ADDRESS):
        block = Block(datetime.datetime.now().strftime("%d-%m-%Y %H:%M"), self.pendingTransactions)
        #setting previous hash to the value of the Hash of the latest block on the blockchain
        block.setPreviousHash(self.getLatestBlock().getHash())
        #mine the block
        block.mineBlock(self.difficulty)
        #adding this up to the blockchain
        self.chain.append(block)
        #setPending transactions to the reward to the miner
        self.pendingTransactions = [Transaction(None, MINER_ADDRESS, self.reward)]

    def isValid(self):

        for i in range(1, len(self.chain)):
            if(self.chain[i].getPreviousHash() != self.chain[i-1].getHash()):
                return False

            if(self.chain[i].getHash() != self.chain[i].createHash()):
                return False
        return True


    def getBalanceOf(self, ADDRESS):
        balance = 0
        for block in self.chain:
            for ledger in block.getLedger():

                if ADDRESS == ledger.getSenderAddress():
                    balance = balance - ledger.getAmount()
                if ADDRESS == ledger.getReceiverAddress():
                    balance = balance + ledger.getAmount()




        return balance



block = Blockchain()
block.createATransaction(Transaction("felipe", "sara", 50))
block.createATransaction(Transaction("felipe", "sara", 100))
block.miningPendingTransactions("F")
#print(block.chain)

print(block.getBalanceOf("felipe"))





