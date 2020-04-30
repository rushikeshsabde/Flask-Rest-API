from flask import Flask

app = Flask(__name__)

@app.route('/student/<string:name>')
def home(name):
    return {'name':name}, 200

app.run(port=5000)