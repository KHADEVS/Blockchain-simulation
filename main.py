import hashlib
import time
import random
import string


CRYPTOCURRENCIES = ["Bitcoin", "Ethereum", "Ripple", "Litecoin", "Cardano", "Polkadot", "Solana", "Dogecoin", "Shiba Inu", "Avalanche"]

class Transaction:
    def __init__(self, sender, recipient, amount, cryptocurrency):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.cryptocurrency = cryptocurrency

    def __repr__(self):
        return f"{self.sender} -> {self.recipient}: {self.amount} {self.cryptocurrency}"

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", time.time(), "Genesis Block", self.calculate_hash(0, "0", time.time(), "Genesis Block"))

    def calculate_hash(self, index, previous_hash, timestamp, data):
        value = f"{index}{previous_hash}{timestamp}{data}"
        return hashlib.sha256(value.encode()).hexdigest()

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, transactions):
        latest_block = self.get_latest_block()
        new_index = latest_block.index + 1
        new_timestamp = time.time()
        new_hash = self.calculate_hash(new_index, latest_block.hash, new_timestamp, str(transactions))
        new_block = Block(new_index, latest_block.hash, new_timestamp, str(transactions), new_hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != self.calculate_hash(current_block.index, current_block.previous_hash, current_block.timestamp, current_block.data):
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

def generate_random_address():
    
    return "0x" + ''.join(random.choices(string.hexdigits.lower(), k=40))

if __name__ == "__main__":
    blockchain = Blockchain()

    while True:
       
        transaction1 = Transaction(
            generate_random_address(),
            generate_random_address(),
            random.randint(1, 100),
            random.choice(CRYPTOCURRENCIES)
        )
        transaction2 = Transaction(
            generate_random_address(),
            generate_random_address(),
            random.randint(1, 100),
            random.choice(CRYPTOCURRENCIES)
        )

        
        print(f"Transaction 1: {transaction1}")
        print(f"Transaction 2: {transaction2}")

       
        blockchain.add_block([transaction1, transaction2])

       
        latest_block = blockchain.get_latest_block()
        print(f"Index: {latest_block.index}, Transactions: {latest_block.data}, Hash: {latest_block.hash}")

 
        print("Is blockchain valid?", blockchain.is_chain_valid())

       
        time.sleep(5)