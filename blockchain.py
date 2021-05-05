#Blockchain class 

from block import Block

class Blockchain:
    def __init__(self):
        self.chain=[] #Empty chain
        self.unconfirmed_transactions=[]
        self.genesis_block()

    #define genesis block
    def genesis_block(self):
        transactions=[]
        genesis_block=Block(transactions,"0")
        genesis_block.generate_hash()
        self.chain.append(genesis_block)

    #define add block upon request
    def add_block(self,transactions):
        previous_hash=(self.chain[len(self.chain)-1]).hash
        new_block=Block(transactions,previous_hash)
        new_block.generate_hash() #current hash
        proof=self.proof_of_work(new_block)
        self.chain.append(new_block)
        return proof,new_block

    #define a function to print chain
    def print_blocks(self):
        for i in range(len(self.chain)):
            current=self.chain[i]
            print("Block {} {} ".format(i,current))
            current.print_block()

    # function to validate the chain
    def validate_chain(self):
        for i in range(1,len(self.chain)):
            current_block=self.chain[i]
            previous_block=self.chain[i-1]
            if(current_block.hash!=current_block.generate_hash()):
                print('Malpractice found in the block {0}'.format(i))
                return False
            if(current_block.previous_hash!=previous_block.generate_hash()):
                print('Malpractice found with previous block {0}'.format(i-1))
                return False
        return True
    
    # Proof of Work function
    def proof_of_work(self,block,difficulty=2):
        proof=block.generate_hash()
        while proof[0:difficulty]!='0'*difficulty:
            block.nonce+=1
            proof=block.generate_hash()
        block.nonce=0
        return proof