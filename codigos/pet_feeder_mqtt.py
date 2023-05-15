# importação das bibliotecas
import paho.mqtt as mqtt
import time


# Informações necessárias para se conectar ao Broker MQTT

broker_address = "test.mosquitto.org"  # endereço do servidor MQTT
port = 1883  # porta usada para conexão
keepalive = 60  # tempo máx(s) que o cliente deve esperar entre as mensagens
user = 'petfeeder'


# Tópicos utilizados controlar e obter informações do sensor de presença

sensor_set_topic = "sensor_infra/set"
sensor_state_topic = "sensor_infra/state"


# configuração inicial

sensor_presenca = 0
state = "OFF"

# Instanciando o cliente MQTT 

client = mqtt.Client(user)
client.connect(broker_address, port, keepalive)  # conectando ao broker MQTT


# Executa quando o cliente se conectar ao servidor MQTT

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe(sensor_state_topic)  # inscrição do cliente no tópico state do sensor
        print("Conexão bem-sucedida! Inscrito no tópico de state.")
    else:
        print(f"Falha na conexão. Código de resultado: {rc}")


# Executada quando o cliente MQTT recebe uma mensagem do servidor MQTT

def on_message(client, userdata, message):

    global animal_presence, state
    
    if message.topic == sensor_state_topic:  
        state = str(message.payload)  # (ON ou OFF)
            
        if state == "ON":
            alimentar_pet()
        else:
            state == "OFF"
            
            
def alimentar_pet():
    print("Alimentando o pet...")
    client.publish(
        sensor_set_topic, "Pet Alimentado")
    client.publish(
        sensor_state_topic, "OFF!")  # atualiza o state do sensor -> (topic/payload)


# Lógica para tratamento dos dados do sensor de presença

def detectar_presenca_pet():
    if sensor_presenca == 1:
        return True
    else:
        return False


# Simulando a detecção de presença do animal

while True:
    # Verificando a presença do animal
    animal_presente = detectar_presenca_pet()

    if animal_presente:
        alimentar_pet()

    # Aguardando um intervalo antes de verificar a presença novamente
    time.sleep(10)
    

# chamando as funções de conexão e mensagem

client.on_connect = on_connect
client.on_message = on_message