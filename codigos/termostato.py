import paho.mqtt.client as mqtt

# Define o nome do cliente MQTT
client_name = "termostato"

# Define o tópico MQTT para receber as mensagens de temperatura
temp_topic = "casa/termostato/temperatura"

# Define o tópico MQTT para enviar mensagens de controle do termostato
ctrl_topic = "casa/termostato/controle"

# Define o valor inicial da temperatura
temperatura = 25.0


# Função para estabelecer a conexão com o broker MQTT
def on_connect(client, userdata, flags, rc):
    print("Conectado ao broker com sucesso! Código de retorno: ", str(rc))
    # Inscreve-se no tópico para receber mensagens de temperatura
    client.subscribe(temp_topic)


# Função para receber as mensagens de temperatura
def on_message(client, userdata, msg):
    global temperatura
    temperatura = float(msg.payload)
    print("Temperatura atual: ", temperatura)


# Função para enviar mensagens de controle do termostato
def enviar_controle():
    global temperatura
    if temperatura > 28.0:
        print("Enviando mensagem para ligar o ar-condicionado")
        client.publish(ctrl_topic, "ligar_ar")
    elif temperatura < 20.0:
        print("Enviando mensagem para ligar o aquecedor")
        client.publish(ctrl_topic, "ligar_aquecedor")


# Cria a instância do cliente MQTT
client = mqtt.Client(client_name)

# Define as funções de callback
client.on_connect = on_connect
client.on_message = on_message

# Conecta ao broker MQTT
client.connect("test.mosquitto.org", 1883, 60)

# Inicia o loop para receber mensagens e enviar o controle do termostato
client.loop_start()

# Loop principal
while True:
    enviar_controle()