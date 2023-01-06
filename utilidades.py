"""
************************************************************************
* Author = @jesusparra                                             *
* Date = '06/01/2023'                                                  *
* Description = Envio de mensajes Twilio con Python                    *
************************************************************************
"""

import pandas as pd
from twilio.rest import Client
import twilio_config as config
import time
from datetime import datetime
import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

def request_dolar():

    url_dolar = 'https://us-central1-api-dolar.cloudfunctions.net/apiDolar/dolarToday'

    try :
        response = requests.get(url_dolar).json()
    except Exception as e:
        print(e)

    return response

def obtener_valores (response):

    fecha = response['_timestamp']['fecha']
    dolar = response['USD']['dolartoday']
    dolarbcv = response['USD']['sicad2']
    dolarbitcoin = response['USD']['localbitcoin_ref']

    return fecha, dolar,dolarbcv,dolarbitcoin

def send_message(TWILIO_ACCOUNT_SID, 
                 TWILIO_AUTH_TOKEN, 
                 PHONE_NUMBER, 
                 datos):

    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN

    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body='dolartoday       '+ datos[0]+'\n\n\n'+'*DOLARTODAY BsS '+str(datos[1])+'\n'+'*DOLAR BCV BsS '+str(datos[2])+'\n'+'*DOLAR BITCOIN BsS '+str(datos[3])+'\n',
                        from_= PHONE_NUMBER,
                        to = '+584245590953'
                    )

    return message.sid