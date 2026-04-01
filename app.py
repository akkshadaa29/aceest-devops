from flask import Flask, request, jsonify

app = Flask(__name__)

# dummy data (in-memory)
clients = []

#  Endpoint 1: GET all clients
@app.route('/clients', methods=['GET'])
def get_clients():
    return jsonify(clients)

#  Endpoint 2: ADD client
@app.route('/clients', methods=['POST'])
def add_client():
    data = request.get_json()
    
    if not data.get("name"):
        return jsonify({"error": "Name is required"}), 400

    clients.append(data)
    return jsonify({"message": "Client added successfully"}), 201


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
