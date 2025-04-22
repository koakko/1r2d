from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route('/api/hello')
def hello():
    return jsonify({'message': 'Hello from the Backend!'})

if __name__ == '__main__':
    app.run(debug=True, host='192.168.0.182', port=5000)