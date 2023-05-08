import paho.mqtt.client as mqtt
import time

# Dados de conexão com o broker MQTT
broker_address = "broker.mqtt.com"
port = 1883
keepalive = 60

# Tópicos MQTT para controle do ar condicionado
set_topic = "arcondicionado/set"
status_topic = "arcondicionado/status"

# Variáveis de controle do ar condicionado
temperatura = 25
ligado = False


# Função callback para quando o cliente se conecta ao broker
def on_connect(client, userdata, flags, rc):
    print("Conectado ao broker com resultado: " + str(rc))

    # Inscrevendo-se no tópico de status para receber atualizações
    client.subscribe(status_topic)


# Função callback para quando o cliente recebe uma mensagem
def on_message(client, userdata, msg):
    global temperatura, ligado

    # Verificando se a mensagem recebida é para atualizar a temperatura
    if msg.topic == set_topic + "/temperatura":
        temperatura = float(msg.payload)

    # Verificando se a mensagem recebida é para ligar/desligar o ar condicionado
    elif msg.topic == set_topic + "/ligado":
        ligado = True if msg.payload == b"1" else False

    # Atualizando o status do ar condicionado
    client.publish(
        status_topic, "temperatura: {}, ligado: {}".format(temperatura, ligado))


# Criando uma instância do cliente MQTT
client = mqtt.Client()

# Configurando as funções de callback
client.on_connect = on_connect
client.on_message = on_message

# Conectando-se ao broker MQTT
client.connect(broker_address, port=port, keepalive=keepalive)

# Iniciando a thread de rede do cliente MQTT
client.loop_start()

# Simulando o envio de mensagens para o ar condicionado
while True:
    # Alterando a temperatura do ar condicionado
    temperatura += 1
    client.publish(set_topic + "/temperatura", temperatura)

    # Ligando/desligando o ar condicionado
    ligado = not ligado
    client.publish(set_topic + "/ligado", "1" if ligado else "0")

    # Aguardando um segundo
    time.sleep(1)
