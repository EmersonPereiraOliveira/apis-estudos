from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api/v1/example")
def helloworld():
    return jsonify(hello='world')


app.run(host='0.0.0.0', debug = True, port=8080)