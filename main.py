from blockchain import Blockchain

b1_transactions={'id':1,'temp_sensor':23.0}
b2_transactions={'id':2,'temp-sensor':25.0}

iot_blockchain=Blockchain()
#iot_blockchain.print_blocks()

iot_blockchain.add_block(b1_transactions)
#iot_blockchain.print_blocks()

iot_blockchain.add_block(b2_transactions)
iot_blockchain.print_blocks()
print(iot_blockchain.validate_chain())
