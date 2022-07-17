from flask import Flask, jsonify, request, make_response
# from waitress import serve

from model import Data

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def hello():
    return "Hello World"

@app.route('/data', methods=['GET', 'POST', 'DELETE'])
def data():
    try:
        dt = Data()
        values = ()

        if request.method == 'GET':
            id_ = request.args.get('id')
            if id_ :
                query = "SELECT * FROM data WHERE id = %s"
                values = (id_,)
            else:
                query = "SELECT * FROM data"
            data = dt.get_data(query, values)

        elif request.method == 'POST':
            datainput = request.json
            nama = datainput['nama']
            usia = datainput['usia']
            query = "INSERT INTO data(nama, usia) values (%s, %s)"
            values = (nama, usia)
            dt.insert_data(query, values)
            data = [{
                'pesan': 'Berhasil tambah data'
            }]
        else:
            query = "DELETE FROM data WHERE id = %s"
            id_ = request.args.get('id')
            values = (id_,)
            dt.insert_data(query, values)
            data = [{
                'pesan':'Berhasil hapus data'
            }]
    except Exception as e:
        return make_response(jsonify({
            'error': str(e)
        }), 400)
    return make_response(jsonify({
        'data': data
    }), 200)

app.run()
# for production
# serve(app, host='0.0.0.0', port=8080)
