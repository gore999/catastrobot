import telepot
import time
import requests

#manejador de mensajes
def handle(msg):
    chat_id=msg['chat']['id']
    latitud=msg['location']['latitude']
    longitud=msg['location']['longitude']
   #print('el comando es: '+comando)
    consulta="http://ovc.catastro.meh.es/ovcservweb/ovcswlocalizacionrc/ovccoordenadas.asmx/Consulta_RCCOOR?SRS=EPSG:4326&Coordenada_X="+str(longitud)+"&Coordenada_Y="+str(latitud)
    respuesta = requests.get(consulta)
    texto=str(respuesta.content)
    print(texto)
    parte1=texto[texto.find("<pc1>")+5:texto.find("</pc1>")]
    parte2 = texto[texto.find("<pc2>") + 5:texto.find("</pc2>")]
    direccion=texto[texto.find("<ldt>") + 5:texto.find("</ldt>")]
    bot.sendMessage(chat_id, str(latitud) + " , " + str(longitud))
    if(texto.find("<pc1>")<0):
        bot.sendMessage(chat_id, "No hay referencia catastral para ese punto.")
    else:

        bot.sendMessage(chat_id,parte1+parte2)
        bot.sendMessage(chat_id, direccion)
bot=telepot.Bot("1038379101:AAGE54hpNSe7VOthfAqR56btiddTY4FjLpk")
bot.message_loop(handle)
while(True):
    time.sleep(10)