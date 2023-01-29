from flask import Flask, jsonify, request
import json, random

app = Flask(__name__)

#funções internas (usadas nas funções da API):
def randomID(dicionario):
    id = random.randint(0, len(dicionario["frases"]) - 1)
    return id

def ler_JSON():
    with open("api_frases/frases.json", "r", encoding='utf-8') as arq:
        myJson = json.load(arq)
        return myJson

def adicionar_no_JSON(frase):
    myJson = ler_JSON()
    myJson["frases"].append(frase)
    with open("api_frases/frases.json", "w", encoding='utf-8') as arq:
        json.dump(myJson, arq, ensure_ascii=False)

def procurar_frase(arquivo_JSON, id:int):
    fraseJSON = arquivo_JSON["frases"][id]
    print(fraseJSON)
    return fraseJSON

def deletar_frase(arquivo_JSON, id):
    del arquivo_JSON["frases"][id]
    with open("api_frases/frases.json", "w", encoding='utf-8') as arq:
        json.dump(arquivo_JSON, arq, ensure_ascii=False)    

#funções da API em si:

#consultar frases aleatorias
@app.route('/frasesaleatorias', methods=['GET'])
def obterFrase():
    arquivoJSON = ler_JSON()
    id = randomID(arquivoJSON)
    frase = procurar_frase(arquivoJSON, id)
    return jsonify(frase)

#adicionar frases
@app.route('/novafrase', methods=['POST'])
def adicionarFrase():
    novaFrase = request.get_json()
    adicionar_no_JSON(novaFrase)
    return jsonify("Frase adicionada")

#pegar todas as frases
@app.route('/pegartodas', methods=['GET'])
def pegarTodas():
  arquivo = ler_JSON()
  return jsonify(arquivo)

#deletar frases por id
@app.route('/deletarfrase', methods=['POST'])
def excluirFrase():
    id = int(request.get_json())
    arquivoJSON = ler_JSON()
    if id > -1 and id < len(arquivoJSON["frases"]):
        deletar_frase(arquivoJSON, id)
        return jsonify(f"Frase de id '{id}' deletada")
    else:
        return jsonify(f"O id {id} é inválido ou inexistente. Tente novamente.")

    
#iniciar a API
app.config['JSON_AS_ASCII'] = False
app.run(port=5000, host='0.0.0.0', debug=True)