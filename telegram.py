import requests
import sys
 
id = "id"
 
token = "api"
 
url = "https://api.telegram.org/bot" + token + "/sendMessage"
params = {
'chat_id': id,
 
'text' : "Prueba"
}
 
requests.post(url, params=params)