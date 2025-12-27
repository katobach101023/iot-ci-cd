from flask import Flask, request, jsonify
app = Flask(__name__)

data = {"temperature": 0, "humidity": 0}

@app.route("/iot", methods=["POST"])
def post():
    global data
    data = request.json
    return {"status": "ok"}

@app.route("/iot")
def get():
    return jsonify(data)

app.run(host="0.0.0.0", port=5000)
