from flask import Flask, jsonify, request, make_response
# from waitress import serve

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def hello():
    return "Hello World"

app.run()
# for production
# serve(app, host='0.0.0.0', port=8080)
