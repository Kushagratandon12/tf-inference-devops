import json
from flask import Flask, request


app = Flask(__name__)


@app.route("/import_data", methods=['POST'])
def inferencing():
    data_received = request.json
    print(data_received)
    return 'Data Received', 200


if __name__ == "__main__":
    app.run(debug=True)
