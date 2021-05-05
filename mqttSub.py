# mqtt_blockchain
import paho.mqtt.client as mqtt
from blockchain import Blockchain

#create a client object
client=mqtt.Client()

#connect with broker
client.connect('broker.hivemq.com',1883)
print('Broker Connected')

#subscribe on the topic
client.subscribe('madblocks')

mqtt_blockchain = Blockchain() # Block0
mqtt_blockchain.print_blocks()

#create a notification function
def notification(client,userdata,msg):
        t=(msg.payload)
        print(t) # t - sensory data
        mqtt_blockchain.add_block(t)
        mqtt_blockchain.print_blocks()
        print(mqtt_blockchain.validate_chain())
        # send this data to blockchain

# configure our notification function
client.on_message=notification                                                                                 
client.loop_forever()