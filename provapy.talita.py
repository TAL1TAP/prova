from flask import Flask, app , request
from flask.json import jsonify
import json

app = Flask(__name__)

ListaReceitas = [
    {
           "Título" : "Pudim" ,
           "Lista de ingrediente": [
            "3 ovos"
            "300 gm de manteiga"
            "4 colheres de sopa de Açucar"
            "2 latas de Leite condensado"
            "3 xícaras de chá de leite"
            ],
            "modo de preparo" : "para preprar, basta misturar todos os ingredientes, logo após, levá-lo ao forno em banho maria"
            "Rendimento" "Rende 5 fatias"
       },
    ]
@app.route("/rotaApirest", methods= ["POST","GET"])
def Cadastro ():
    if request.method == "GET"
    elif request.method == "POST":
    newRec= json.loads(request.date)
    ListaReceitas.append(newRec)
    return jsonify({
        "menssagem" : "Cadastrado",
        "newValue": newRec

    })
@app.route('/rotaApirest/<int:indice>', methods=[ 'GET', 'PUT', 'DELETE'])
def cadastroID(indice):
    try:
        ListaReceitas[indice]
    except IndexError:
        message= 'Receita ID {} Não encontrada' .format(indice)
        return jsonify ({
            "message": "Updated!",
            "newValue":"newRec"

        })
@app.rout('/rotaApirest/<int:indice>', methods=['GET','PUT','DELETE'])
def cadastroID(indice):
    try:
        ListaReceitas[indice]
    except IndexError:
         message = 'Recfeita ID {} Não Encontrada'.format(indice)
         return jsonify({
              "message":message,
              "status" "Error!"
         })
    if request.method == 'GET':
        return ListaReceitas[indice]

    elif request.method == 'PUT':

        newValue =json.loads(request.data)

    ListaReceitas[indice]= newValue
    return jsonify({
        "message": "Updated!",
        "newVlue": newValue
    })
    elif request.method=='DELETE'
    print(indice)
    ListaReceitas.pop(indice)
    return jsonify({
        "message": "DELETED!",
        "arryAtual": ListaReceitas
        })
    if __name__=='__main__':
        app.run(debug=true)









