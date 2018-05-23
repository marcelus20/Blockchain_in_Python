# Blockchain_in_Python
This Project is a python version of the MantovaCoin blockChain available at this link: https://github.com/marcelus20/MANTOVACOIN-blockchain-

<h3>This blockchain uses the criptography used in bitcoin blockchain, the SHA-256</h3>



This simulates a blockchain and its features such as:
<ul>

<li>Coins Transfer bettween users</li>
<li>The Users are based on a public address that could be any string for testing porpuses</li>
<li>Mining blocks with a certain level of difficulty</li>
<li>possibility of checking the balance of each public address</li>

</ul>


<h3>How to change the difficulty</h3>
Go to Blockchain class and change the attribute difficulty value.
<h1>WARNING</h1>
It is recomended to use the difficulty level between 0 and 5, because higher than 5
may take several minutes to mine the block and the CPU may work harder for the Hash problem solving process

<h3>How to instantiate the the blockchain</h3>
<p background="grey">
<code>myBlockchain = Blockchain()</code>
</p>

<h3> Making transactions </h3>
<code>myBlockchain.createATransaction(Transaction(fromAddress, toAddress, ammount))</code>

<h3> mining the block </h3>
<code>myBlockchain.miningPendingTransactions(minerAddress)</code>
The minerAddress is passed as a parameter because the system will reward the miner with 100 coins for every block mined.
PS: miner balance will be update always on the following mining

<h3> Checking the balance of a given address </h3>
<code>myBlockchain.getBalanceOf(address)</code>

<h3> Checking integrity of the blockchain (if it has not been tampered with)</h3>
<code>myBlockchain.isValid()</code>


<h3> How to print the whole blockchain </h3>
<code>print("This blockchain has not been tampered with: "+str(myBlockchain.isValid()))</code>
PS: Depending on the console, the json printing may not be pretty
