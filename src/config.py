from os import environ
import telegram
from flask import Flask

PORT = int(environ.get('PORT', '5000'))
BMCAT_HOST = environ['BM_CAT_HOST']
BMCAT_PORT = int(environ.get('BM_CAT_PORT', '8443'))
WEBHOOK_LISTEN = '0.0.0.0'
WEBHOOK_URLBASE = "https://%s:%s" % (BMCAT_HOST, BMCAT_PORT)

BMCAT_APIKEY = environ['BM_CAT_API_KEY']
WEBHOOK_URLPATH = "/%s" % BMCAT_APIKEY

BMCAT_SSLCERT_PATH = environ['BM_CAT_SSL_CERTIFICATE_PATH']
BMCAT_PRIVATEKEY_PATH = environ['BM_CAT_PRIVATE_KEY_PATH']

app = Flask(__name__)

global bot
bot = telegram.Bot(token=BMCAT_APIKEY)
