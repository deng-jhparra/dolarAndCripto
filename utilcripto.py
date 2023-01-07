"""
************************************************************************
* Author = @jesusparra                                                *
* Date = '06/01/2023'                                                  *
* Description = Envio de mensajes Twilio con Python                    *
************************************************************************
"""

import pandas as pd
from twilio.rest import Client
import twilio_config as config
import time
from tqdm import tqdm
from datetime import datetime
import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

def request_cripto():

    url_currency = 'https://data.binance.com/api/v3/ticker/24hr'

    try :
        response = requests.get(url_currency).json()
    except Exception as e:
        print(e)

    return response

def obtener_cripto(response,i):

    cripto = response[i]['symbol']
    preciocambio = float(response[i]['priceChange'])
    porcpreciocambio = float(response[i]['priceChangePercent'])
    mediaprecio = response[i]['weightedAvgPrice']
    preciocierre = response[i]['prevClosePrice']
    precio = response[i]['lastPrice']
    ultimacantidad = float(response[i]['lastQty'])
    volumen = response[i]['volume']
    capital = response[i]['quoteVolume']

    return cripto, preciocambio, porcpreciocambio, mediaprecio, preciocierre, precio, ultimacantidad, volumen, capital

def create_df (response):

    datos = []

    for i in tqdm(range(len(response))):
        datos.append(obtener_cripto(response,i))
        time.sleep(0.001)
    
    col = ['Cripto','Cambio','Variacion','Media','Cierre','Precio','Ultima Cantidad','Volumen','Capitalizacion']
    df = pd.DataFrame(datos,columns=col)
    df = df.sort_values(by = 'Media',ascending = False)
    datos = df[(df['Variacion']>0) & (df['Ultima Cantidad']>28.0)]
    datos = datos[['Cripto','Cambio','Variacion']]
    datos.set_index('Cripto',inplace = True)
    
    return datos.head(10)

def send_message(TWILIO_ACCOUNT_SID, 
                 TWILIO_AUTH_TOKEN, 
                 PHONE_NUMBER, 
                 datos):

    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN

    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body='\nTop 10 de Criptomonedas :' + '\n\n' + str(datos),
                        from_= PHONE_NUMBER,
                        to = '+584245590953'
                    )

    return message.sid
