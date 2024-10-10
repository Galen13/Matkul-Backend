from flask import Flask, jsonify, request, make_response

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/karyawan', methods=['GET', 'POST', 'PUT', 'DELETE'])
def karyawan():
    try:
        if request.method == 'GET':
            data = [{
                'Nama' : 'Galih GET',
                'Pekerjaan' : 'Web Engineer',
                'Usia' : '27',
            }]
        elif request.method == 'POST':
            data = [{
                'Nama' : 'Galih POST',
                'Pekerjaan' : 'Web Engineer',
                'Usia' : '27',
            }]
        elif request.method == 'PUT':
            data = [{
                'Nama' : 'Galih PUT',
                'Pekerjaan' : 'Web Engineer',
                'Usia' : '27',
            }]
        else:
            data = [{
                'Nama' : 'Galih DELETE',
                'Pekerjaan' : 'Web Engineer',
                'Usia' : '27',
            }]
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 400)
    return make_response(jsonify({'data': data}), 200)

app.run()