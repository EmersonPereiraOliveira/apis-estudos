from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/api/v1/example")
def helloworld():
    return jsonify(hello='world')

@app.route("/api/v1/example", methods = ['GET'])
def helloworld2():
    return jsonify(hello='world', ola='mundo')

@app.route("/api/v1/example", methods = ['GET', 'POST'])
def helloworld3():
    if request.method =="POST":
        content = request.get_json(silent=True)
        print(content['nome'])

    return jsonify(hello='world', ola='mundo3')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True, port=8080)


#@app.route("/api/v1/example", methods = ['GET', 'POST'])
#def helloworld3():
#    if request.method == "POST":
#        content = request.get_json(silent=True)
#        if 'nome' in content.keys():
#            nome = content['nome']
#        else:
#            return jsonify(error='json es mal formado'), 400
#        return jsonify(frase = "Seu nome é " +  nome)
#    elif request.method == "GET":
#        return jsonify(msgm = 'Ok')