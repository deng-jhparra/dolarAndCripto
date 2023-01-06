"""
************************************************************************
* Author = @jesusparra                                             *
* Date = '06/01/2023'                                                  *
* Description = Envio de mensajes Twilio con Python                    *
************************************************************************
"""

import os
from twilio.rest import Client
import twilio_config as config
import time
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import requests
from tqdm import tqdm
from datetime import datetime
from utilidades import request_dolar, obtener_valores, send_message

datos = obtener_valores (request_dolar())

# Send Message
message_id = send_message(config.TWILIO_ACCOUNT_SID, 
                          config.TWILIO_AUTH_TOKEN,
                          config.PHONE_NUMBER,
                          datos)

print('Mensaje Enviado con exito ' + message_id)