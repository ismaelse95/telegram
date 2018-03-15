import requests
import sys
 
id = "229470654"
 
token = "532491620:AAG00ZgtTxBjLnMwFEVHbAQRmhDnh6uIAuI"
 
url = "https://api.telegram.org/bot" + token + "/sendMessage"
params = {
'chat_id': id,
 
'text' : "Prueba"
}
 
requests.post(url, params=params)