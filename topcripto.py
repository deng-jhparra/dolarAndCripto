"""
************************************************************************
* Author = @alexbonella                                                *
* Date = '15/09/2022'                                                  *
* Description = Envio de mensajes Twilio con Python                    *
************************************************************************
"""

import os
from twilio.rest import Client
import twilio_config as config
from time import sleep
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import requests
from bs4  import BeautifulSoup
from tqdm import tqdm
from datetime import datetime
from utilcripto import request_cripto, obtener_cripto, create_df, send_message

datos = create_df(request_cripto())

# Send Message
message_id = send_message(config.TWILIO_ACCOUNT_SID,
                          config.TWILIO_AUTH_TOKEN,
                          config.PHONE_NUMBER,
                          datos)


print('Mensaje Enviado con exito ' + message_id)