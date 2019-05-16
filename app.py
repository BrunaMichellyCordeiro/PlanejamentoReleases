import urllib2, json #para pegar os dados da estacao
import time #para o time.sleep()
import serial #para o Arduino
import paho.mqtt.publish as publish #para publicar
import psutil #para configurar o url
import decimal #para converter

def comJSON(jsonurl): #envia todos os dados
	dados = json.loads(jsonurl.read()) #carrega os dados JSON da p�gina j� aberta
	#Arduino
	ard = serial.Serial('/dev/tty96B0', 115200) #inicializa a variavel que receber� os dados do Ardu�no
	#Recebe os dados do Ardu�no
	ardAgua = int(ard.readline().rstrip())
	ardTemp = float(ard.readline().rstrip())
	ardPres = int(ard.readline().rstrip())
	ardUV = float(ard.readline().rstrip())

	print ("\nArduino")
	if ardAgua == 1:
		print ('Molhado')
	else:
		print ('Seco')
	print ('Temperatura:', ardTemp, '*C')
	print ('Pressao:', ardPres, 'Pa')
	print ('Ultra-Violeta:', ardUV, 'lx')

	#Estacao
	print ('\nJSON')
	print ('URL:', jsonurl)
	#Recebe os dados da esta��o
	data = dados['ReturnDataSet'][i]['f_date']
	vel_vento = dados['ReturnDataSet'][i]['sens_aver_6_5']
	umidade = dados['ReturnDataSet'][i]['sens_aver_19_507']

	print ('Data:', data)
	print ('Velocidade do Vento:', vel_vento, 'm/s')
	print ('Umidade do ar:', umidade, '%')

	#CRIA VARIAVEIS AUX
	vel_vento = decimal.Decimal(vel_vento.rstrip())
	umidade  = decimal.Decimal(umidade.rstrip())

	#ENVIA
	channelID = "344243" #Canal criado para o grupo
	apiKey = "1PK9ELK0L4AH8CVP" #C�digo dado pelo ThingSpeak
	#configura��es de comunica��o
	useUnsecuredTCP = True
	useUnsecuredWebsockets = False
	useSSLWebsockets = False
	mqttHost = "mqtt.thingspeak.com"
	if useUnsecuredTCP:
		tTransport = "tcp"
		tPort = 1883
		tTLS = None
	if useUnsecuredWebsockets:
		tTransport = "websockets"
		tPort = 80
		tTLS = None
	if useSSLWebsockets:
		import ssl
		tTransport = "websockets"
		tTLS = {'ca_certs':"/etc/ssl/certs/ca-certificates.crt",'tls_version':ssl.PROTOCOL_TLSv1}
		tPort = 443
	topic = "channels/" + channelID + "/publish/" + apiKey #Cria variavel com o 'caminho' para o canal
	tPayload = "field1=" + str(ardAgua) + "&field2=" + str(ardTemp) + "&field3=" + str(ardPres) + "&field4=" + str(ardUV) + "&field5=" + str(data) + "&field6=" + str(vel_vento) + "&field7=" + str(umidade) #Organiza todas as variaveis em uma String para ser enviado
	print ('Enviando dados')
	try:
		publish.single(topic, payload=tPayload, hostname=mqttHost, port=tPort, tls=tTLS, transport=tTransport) #Envia os dados
		time.sleep(0.5)
		print ('Dados enviados')
	except:
		print ('Erro ao enviar dados')

def semJSON():
	#Arduino
	ard = serial.Serial('/dev/tty96B0', 115200)
	ardAgua = ard.readline().rstrip()
	ardTemp = ard.readline().rstrip()
	ardPres = ard.readline().rstrip()
	ardUV = ard.readline().rstrip()

	print ('\nArduino')
	if ardAgua == 1:
		print ('Molhado')
	else:
		print ('Seco')
	print ('Temperatura:', ardTemp, '*C')
	print ('Pressao:', ardPres, 'Pa')
	print ('Ultra-Violeta:', ardUV, 'lx')

	#ENVIA
	channelID = "344243"
	apiKey = "1PK9ELK0L4AH8CVP"
	useUnsecuredTCP = False
	useUnsecuredWebsockets = True
	useSSLWebsockets = False
	mqttHost = "mqtt.thingspeak.com"
	if useUnsecuredTCP:
		tTransport = "tcp"
		tPort = 1883
		tTLS = None
	if useUnsecuredWebsockets:
		tTransport = "websockets"
		tPort = 80
		tTLS = None
	if useSSLWebsockets:
		import ssl
		tTransport = "websockets"
		tTLS = {'ca_certs':"/etc/ssl/certs/ca-certificates.crt",'tls_version':ssl.PROTOCOL_TLSv1}
		tPort = 443
	topic = "channels/" + channelID + "/publish/" + apiKey
	tPayload = "field1=" + str(ardAgua) + "&field2=" + str(ardTemp) + "&field3=" + str(ardPres) + "&field4=" + str(ardUV)
	print ('Enviando dados')
	try:
		publish.single(topic, payload=tPayload, hostname=mqttHost, port=tPort, tls=tTLS, transport=tTransport)
		time.sleep(0.5)
		print ('Dados enviados')
	except:
		print ('Erro ao enviar dados')

url = "http://www.fieldclimate.com/api/CIDIStationData/GetLast?user_name=facens&user_passw=clima&station_name=002035C0" #Define o URL da esta��o

i = 49 #Para pegar os dados mais atuais da esta��o
j = 0 #Passo do programa


while(1):
	jsonurl = None #Inicializa a varivavel como None
	print ('Passo:', j)
	print ('Atualizando dados')
	try:
		jsonurl = urllib2.urlopen(url, timeout = 5) #tenta abrir o url em no m�ximo 5 segundos
		if jsonurl is not None:
			print ('Dados atualizados')
			comJSON(jsonurl) #Se conseguiu abrir o URL, mostra todos os dados
	except:
		if jsonurl is None:
			print ('Erro ao atualizar dados')
			semJSON() #Se n�o abriu o URL, mostra os dados obtidos localmente (do Arduino)
		pass
	j += 1
	print ('--------------------------------------------------------------------------------------------------------------------------------\n')
	time.sleep(1)