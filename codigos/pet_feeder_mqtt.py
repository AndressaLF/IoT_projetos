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
client.connect(broker_address, port=port, keepalive=keepalive)  # conectando ao broker MQTT

# Tópicos utilizados

sensor_set_topic = "sensor_infra/set"
sensor_state_topic = "sensor_infra/state"


# configuração inicial

animal_presence = False
sensor_presenca = 0  # (0 ou 1)
state = "OFF"


# Executa quando o cliente se conectar ao servidor MQTT

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe(sensor_state_topic)  # inscrição do cliente no tópico state do sensor
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
    
    
# Executada quando o cliente MQTT recebe uma mensagem do servidor MQTT

def on_message(client, userdata, message):
    global state
    
    if message.topic == sensor_state_topic:  
        state = str(message.payload)  # (ON ou OFF)
            
        if state == "ON":
            client.publish(sensor_state_topic, "ON!")
            alimentar_pet()
        else:
            client.publish(sensor_state_topic, "OFF!")
    

# Lógica para tratamento dos dados do sensor de presença

def detectar_presenca_pet():
    if sensor_presenca == 1:
        return True
    else:
        return False


# Chamando as funções de conexão e mensagem

client.on_connect = on_connect
client.on_message = on_message


# Simulando a detecção de presença do animal

while True:
    # Verificando a presença do animal
    animal_presente = detectar_presenca_pet()

    if animal_presente:
        alimentar_pet()

    # Aguardando um intervalo antes de verificar a presença novamente
    time.sleep(10)
