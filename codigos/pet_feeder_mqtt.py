# importação das bibliotecas
import paho.mqtt.client as mqtt
import time

# Informações necessárias para se conectar ao Broker MQTT

broker_address = "test.mosquitto.org"  # endereço do servidor MQTT
port = 1883  # porta usada para conexão
keepalive = 60  # tempo máx(s) que o cliente deve esperar entre as mensagens
user = 'petfeeder'

# Instanciando o cliente MQTT

client = mqtt.Client(user)
# conectando ao broker MQTT
client.connect(broker_address, port=port, keepalive=keepalive)

# Tópicos utilizados

sensor_set_topic = "sensor/sensor_infra/set"
sensor_state_topic = "sensor/sensor_infra/state"
sensor_state_topic_ = "sensor/state"


# configuração inicial

state = "OFF"
set = ""


# Executa quando o cliente se conectar ao servidor MQTT

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        # inscrição do cliente no tópico state do sensor
        client.subscribe(sensor_state_topic)
        print("Conexão bem-sucedida! Inscrito no tópico de state.")
    else:
        print(f"Falha na conexão. Código: {rc}")


# Função executada quando o status foi ON

def alimentar_pet():
    print("Alimentando o pet...")
    client.publish(
        sensor_set_topic, "Pet Alimentado")  # atualiza o state do sensor -> (topic/payload)
    client.publish(
        sensor_state_topic, "OFF!")


# Executada quando o cliente MQTT recebe uma mensagem do servidor/cliente MQTT

def on_message(client, userdata, message):
    
    global state, set

    if message.topic == sensor_state_topic:
        state = str(message.payload)  # (ON ou OFF)

        if state == "ON":
            client.publish(sensor_state_topic, "ON!")
            alimentar_pet()
        else:
            client.publish(sensor_state_topic, "OFF!")


# Chamando as funções de conexão e mensagem

client.on_connect = on_connect
client.on_message = on_message
