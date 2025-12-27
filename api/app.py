from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "IoT API v1"

@app.route("/sensor")
def sensor():
    return jsonify({"temp": 28, "humidity": 70})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
