def lightning_hash(data): #Example hash function
    return data + '*' #star and plus is asterix for as return value #for generate unique hash #Lightning Version Blockhain #Suffix start in 1 for hashing data 
    
class Block: #Primarily Storage unit
    #Function method / define method. #Have parameter is self and have atributes data,hash and last hash :
    def __init__(self,data,hash,last_hash):
        self.data = data #data field is block is soaring #Create argument self, self is calling self block class
        self.hash = hash #hash field is unique value generated for the block based al the blocks
        self.last_hash = last_hash #last_hash field is 
foo_block = Block('foo_data','foo_hash','foo_last_hash') #field block instance #Calling block class

#print(foo_block.data) #Relationship arguments #Output is foo_data
#print(foo_block.hash)
#print(foo_block.last_hash)

class Blockchain():
    def __init__(self):
        #Set to a block instance
        genesis = Block('gen_data','gen_hash','gen_last_hash')
        
        #Create field
        self.chain = [genesis] #Create pair of brackets #Brackets List
    def add_block(self,data):
        #Set arguments for find very last block
        last_hash = self.chain[-1].hash #hash values access #Brackets list final
        hash = lightning_hash(data + last_hash)
        block = Block(data,hash,last_hash)
        self.chain.append(block) #for passing blocks on class block
foo_blockchain = Blockchain()
foo_blockchain.add_block('one') #data block menjadi sring
foo_blockchain.add_block('two')
foo_blockchain.add_block('three')

#looping blockchain one block at time
for block in foo_blockchain.chain:
    #attribute better than before #for writing three seperate line
    #for dictionary representation
    #turn block into a key value collection
    print(block.__dict__) #Create a key value collection all block atributes
    
    


        
    
        
