from flask import Flask, jsonify, request, make_response

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def hello():
    data = [{
        'Nama' : 'Galih',
        'Pekerjaan' : 'Web Engineer',
        'Pesan' : 'Hello World'
    }]
    return make_response(jsonify({'data' : data}), 200)

app.run()