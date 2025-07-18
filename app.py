from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    return jsonify({"message": "Received", "data": data}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
