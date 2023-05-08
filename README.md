# Instalação do apk do MQTT Dashboard - IoT and Node

1. Baixe e instale o aplicativo Mqtt Dashboard - IoT and Node em seu dispositivo móvel. Este aplicativo é uma ferramenta de cliente MQTT que permite enviar e receber mensagens de tópicos MQTT.
2. Certifique-se de que o broker MQTT esteja em execução na máquina local. 

## Configurações

1. No aplicativo Mqtt Dashboard - IoT and Node, toque no botão de adicionar novo servidor, selecione "MQTT Broker", digite o endereço IP da máquina e a porta do broker MQTT (normalmente, 1883) e toque em "Salvar".
2. Depois de adicionar o broker, toque no botão de adicionar novo dispositivo e selecione o servidor que você acabou de adicionar.
3. Agora, você pode assinar um tópico no broker, digitando o nome do tópico e tocando em "Assinar". Quando uma mensagem for publicada neste tópico, ela será exibida na lista de mensagens recebidas no aplicativo Mqtt Dashboard - IoT and Node. Você também pode publicar uma mensagem em um tópico, tocando no botão "Publicar" no aplicativo Mqtt Dashboard - IoT and Node e digitando o nome do tópico e a mensagem. Quando o cliente estiver inscrito neste tópico, ele receberá a mensagem e imprimirá no console.

# Instalação do broker Mosquitto

1. Baixe o instalador do Mosquitto para Windows a partir do [site oficial](https://mosquitto.org/download/).
2. Execute o instalador e siga as instruções na tela para instalar o Mosquitto no seu sistema.
3. Após a instalação, o Mosquitto será executado como um serviço do Windows. Você pode verificar se o serviço está em execução abrindo o Gerenciador de Serviços do Windows e procurando pelo serviço "Mosquitto Broker" ou pelo comando `netstat -an | find ":1883"` através do prompt.
4. Para testar a conexão MQTT com o Mosquitto, abra outro prompt de comando e digite o seguinte comando: `mosquitto_pub -h localhost -t test -m "hello world"`.Se a mensagem for publicada com sucesso, você verá uma mensagem de confirmação no prompt de comando.
5. Para confirmar que a mensagem foi recebida pelo Mosquitto, abra outro prompt de comando e digite o seguinte comando: `mosquitto_sub -h localhost -t test`. Se a mensagem "hello world" foi publicada com sucesso anteriormente, você deverá vê-la exibida neste prompt de comando.

Agora você pode usar o Mosquitto como um broker MQTT para enviar e receber mensagens de dispositivos MQTT.

# Testando o código
1. Crie um ambiente virtual para instalar as bibliotecas necessárias (sugestão do ambiente no python: `python3 -m venv .venv`).
2. Ative o ambiente (`.venv/Scripts/activate` ou `souce .venv/bin/activate`).
3. Instalando as bibliotecas: `pip install requirements.txt`. Independente da linguagem usada será necessário instalar a biblioteca responsável pela implementação do cliente MQTT (Message Queuing Telemetry Transport). O MQTT é um protocolo de mensagens leve que permite a comunicação entre dispositivos em redes com largura de banda limitada. No python essa biblioteca se chama `paho-mqtt`.
2. O código criado está dentro do diretório `codigos`.
1. Use o código que você quer testar no seu computador e execute-o. O deverá criar uma instância de um cliente MQTT e se conectará ao broker na máquina local usando a porta 1883 (verificar porta).