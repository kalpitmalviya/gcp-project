from flask import Flask
app = Flask(__name__)

@app.route('/')
def testing():
    return 'Hello, from Flask !!'