from flask import Flask, request, jsonify

app = Flask(__name__)

app.secret_key = 'xyz123'

items = [
    {
        'name':'milk',
        'price':'10$'
    },
    {
        'name':'book',
        'price':'15$'
    },
    {
        'name':'pencil',
        'price':'2$'
    }
]

@app.route('/item/<string:name>', methods=['GET'])
def getItem(name):
    for item in items:
        if item['name']==name:
            return jsonify(item)
    return {'ttem':None}, 404

@app.route('/item',methods=['POST'])
def createItem():
    data = request.get_json()
    item = {'name':data['name'], 'price':data['price']}
    items.append(item)
    return jsonify(item), 201

@app.route('/items', methods=['GET'])
def getItems():
    return jsonify(items), 200

app.run(port=5000, debug=True)
