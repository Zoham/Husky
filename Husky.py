from flask import Flask
#from flask_ngrok import run_with_ngrok
from flask import render_template

app = Flask(__name__)
#run_with_ngrok(app)  # Start ngrok when app is run

@app.route("/")
def hello():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
