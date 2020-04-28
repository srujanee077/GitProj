from flask import Flask, request, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

app.run()
