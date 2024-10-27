from hashlib import sha256

transactions = ["Daní le envia 5 a Luis",
                "Luis le envia 3 a Aida",
                "Luis le envia 2 a Mauro"]

# data = "#".join(transactions)

# transactions_hash = sha256(data.encode()).hexdigest()

# print(transactions_hash)

class Block:
    def __init__(self, previous_hash, data):
        self.previous_hash = previous_hash
        self.data = data
        self.nonce = 0

    def hash(self):
        info = "#".join(self.data) + self.previous_hash + str(self.nonce)
        return sha256(info.encode()).hexdigest()
    

class BlockChain:

    difficulty = 8


    def __init__(self):
        self.chain = []

    def add(self, block):
        self.chain.append(block)

    def mine(self, block):
        while True:
            if (block.hash()[:self.difficulty] == "0"*self.difficulty):
                self.add(block)
                break
            else:
                block.nonce += 1


block_chain = BlockChain()

b1 = Block("0"*64, transactions)
print("Hash bloque 1: ",b1.hash())

block_chain.mine(b1)
print("Hash final: ", block_chain.chain[0].hash())
print("Valor del nonce: ", block_chain.chain[0].nonce)


# b2 = Block(b1.hash(), transactions)
# print("Hash bloque 2: ",b2.hash())