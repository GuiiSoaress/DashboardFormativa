from flask import Flask, jsonify, render_template
import requests
from flask_cors import CORS
import random
import time 
from configdb import conectar
from datetime import datetime, timezone

API_KEY = "X8PFUG78LVKXAV4"

def salvar_banco(temperatura, umidade, entry):
    agora = datetime.now(timezone.utc)
    data_hora = agora.strftime("%Y-%m-%dT%H:%M:%SZ")
    
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO dados (data_hora, temperatura, umidade, entry)  VALUES ( %s, %s, %s, %s)",
        (data_hora, temperatura, umidade, entry)
    )

    conexao.commit()

    cursor.close()
    conexao.close()
    print("Salvo no banco de dados")

def enviar_dados(temperatura, umidade):
    
    url = f"https://api.thingspeak.com/update?api_key={API_KEY}&field1={temperatura}&field2={umidade}"
    
    resposta = requests.get(url)
    
    print("Temperatura:", temperatura, "°C")
    print("Umidade:", umidade, "%")
    
    print("Resposta da API:", resposta.text)
    
    print("-------------------------------")
    
    entry = int(resposta.text)

    if (entry > 0 ):
        salvar_banco(temperatura, umidade, entry)
    else:
        print("Erro ao enviar dados ao thingSpeak")


while True:
    temperatura = round(random.uniform(20, 30), 2)
    umidade = round(random.uniform(50, 70), 2)
    
    enviar_dados(temperatura, umidade)
    
    time.sleep(15)