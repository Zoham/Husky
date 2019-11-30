from flask import Flask
from flask import render_template
from flask import request, jsonify

from rasa.nlu.model import Interpreter

app = Flask(__name__)
interpreter = Interpreter.load("./models/nlu")

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/_add_numbers")
def add_numbers():
    query = request.args.get("query", "0", type=str)
    return jsonify(result=askRasa(query))

def askRasa(query):
	reply = interpreter.parse(query)
	print(reply)
	return reply

if __name__ == '__main__':
    app.run()
