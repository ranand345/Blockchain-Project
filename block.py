# Block Class

from datetime import datetime
from hashlib import sha256

class Block:
    def __init__(self,transactions,previous_hash,nonce=0):
        self.timestamp=datetime.now()
        self.transactions=transactions
        self.previous_hash=previous_hash
        self.nonce=nonce
        self.hash=self.generate_hash()
    
    def print_block(self):
        print("Timestamp:",self.timestamp)
        print("Transactions:",self.transactions)
        print("Current hash:",self.hash)
        print("Previous hash:",self.previous_hash)

    def generate_hash(self):
        blockContents=str(self.timestamp)
        blockContents+=str(self.transactions)
        blockContents+=str(self.previous_hash)
        blockContents+=str(self.nonce)
        block_hash=sha256(blockContents.encode())
        return block_hash.hexdigest()