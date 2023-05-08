import paho.mqtt as mqtt


# executada quando o cliente se conecta ao broker
def on_connect(client, userdata, flags, rc):
    print(f"Conectado. Código:{str(rc)}")

 
# executada quando uma mensagem é recebida
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


def connect_mqtt():
    pet_feeder_id = mqtt.Client("pet_feeder")  # instanciando o cliente MQTT
    pet_feeder_id.on_connect = on_connect
    pet_feeder_id.on_message = on_message
    pet_feeder_id.connect("mqtt.server.com", 1883, 60)





def connect(client):
    client.username_pw_set("user", password="password")
    client.connect("mqtt.server.com", 1883, 60)
