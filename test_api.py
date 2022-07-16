from urllib.request import HTTPBasicAuthHandler
import requests
from requests.auth import HTTPBasicAuth

# resp = requests.get("http://127.0.0.1:8000/api/users_register_login/" ,params={"user_id":1} , auth=HTTPBasicAuth("admin", "admin"))
# print(resp.json())

# resp = requests.post("http://127.0.0.1:8000/api/users_register_login/", data={
#                      "user_id": 2, "first_name": "Mobin", "last_name": "Atashi", "username": "Phoenix"}, auth=HTTPBasicAuth("admin", "admin"))
# print(resp.json())

resp = requests.put("http://127.0.0.1:8000/api/users_register_login/", data={
    "user_id": 2, "is_deleted": True}, auth=HTTPBasicAuth("admin", "admin"))
print(resp.json())

# resp = requests.get("http://127.0.0.1:8000/api/users_list/", auth=HTTPBasicAuth("admin", "admin"))
# print(resp.json())

# resp = requests.post("http://127.0.0.1:8000/api/users_list/",data={"is_deleted": False} ,auth=HTTPBasicAuth("admin", "admin"))
# print(resp.json())

# resp = requests.get("http://127.0.0.1:8000/api/users_list/", auth=HTTPBasicAuth("admin", "admin"))
# print(resp.json())