import pandas as pd
import requests
import json
import random

sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app'

df = pd.read_csv('SDW2023.csv')
user_ids = df['UserID'].tolist()
print(user_ids)

def get_user(id):
  response = requests.get(f'{sdw2023_api_url}/users/{id}')
  return response.json() if response.status_code == 200 else None

users = [user for id in user_ids if (user := get_user(id)) is not None]


df_messages = pd.read_csv('MensagensMKT.csv', delimiter=";")
msgs = df_messages["Mensagem"].tolist()

def generate_news(user):
  random_msg = random.choice(msgs)
  return random_msg

for user in users:
  print(user["id"])
  msg = generate_news(user)
  user['news'].append({
    "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
    "description2": f"{user['name']}, {msg}",
  })
  print(json.dumps(user, indent=2))
