import csv 
import json
import requests
from typing import List, Dict, Iterator

# with é uma função context manager que gera abre e fecha recursos automaticamente evitando erros 
# with vai abrir o arquivo vendas e guarda-lo em file para podermos manipula-lo
with open("sales.csv", newline='') as file:
    reader: Iterator = csv.reader(file)

    sales: List[Dict[str, str]] = [] # lista sales para guardar os dados estruturados
 
    keys: List[str] = ["id", "product", "quantity", "price"] # lista das chaves que mortar o dicionário

    for row in reader:
        # print(row)
        # zip(keys, row) monta os elementos do dicionário, junta "row" com "keys
        # print(dict(zip(keys, row)))
        sales.append(dict(zip(keys, row))) # sales.append adiciona cada elemento do dicionário na lista sales

    print(sales)


with open("sales.json", "w") as json_file: # cria ou sobrescreve um aquivo json de nome sales.json
    json.dump(sales, json_file) # joga o que tem na lista sales dento de json_file, transfere a informação pra um aquivo json

    for sale in sales:
        # response pega o feedback de quando mandamos os dados para a API falsa
        # o link se refere a API
        # json=sale converte os dados para json para que a API possa recebe-los
        response = requests.post("https://jsonplaceholder.typicode.com/posts", json=sale) 
        print(response.status_code)
        print(response.text)