from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/service-b', methods=['GET'])
def service_b():
    return jsonify({'message': 'Hello from Service B'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)