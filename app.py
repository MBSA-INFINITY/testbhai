from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def start():
    return "Welcome to the MBSA's Flask Application"

@app.route("/send", methods=['POST'])
def send():
    if request.method == 'POST':
        incoming_data = dict(request.json)
        return incoming_data
