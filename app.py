from flask import Flask, jsonify, request
stores = [
    {
        'name':'Costco',
        'items':[
            {
                'name':'chicken',
                'price':12.00
            }
        ]
    }
]

app = Flask(__name__)
#tell what will be requested

#post will be used to recieve date here and get sends data here
#app.route is get by default
@app.route('/store',methods =['POST'])
def create_store():
    requested_data = request.get_json()   #json data is recieved here
    new_store = {
        'name':requested_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)

#the name in string:name needs to match name in get emthod
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name']==name:
            return jsonify(store)
    return jsonify({'message':'store not found'})


@app.route('/store/<string:name>/item',methods=['POST'])
def create_item(name):
    request_data = request.jsonify()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name':request_data['name'],
                'price':request_data['price']
            }

    store['items'] .append(new_item)
    return jsonify(new_item)
