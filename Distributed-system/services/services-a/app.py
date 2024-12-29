from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/service-a', methods=['GET'])
def service_a():
    return jsonify({'message': 'Hello from Service A'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)