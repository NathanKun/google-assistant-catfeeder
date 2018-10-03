from flask import Flask, request, Response
import json
from const import username as u, password as p
import catfeeder

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/feed', methods=['POST'])
def feed():
    auth = request.authorization
    if auth and auth.username == u and auth.password == p:
        catfeeder.main()
        res = {'result': 'OK'}
    else:
        res = {'result': 'Auth failed'}
    return Response(json.dumps(res), mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5678)
