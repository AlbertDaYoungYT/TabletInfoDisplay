from flask_cors import CORS
from flask import *
import sys


APPLICATION_ID = sys.argv[-1]

app = Flask(__name__)
CORS(app)

@app.before_request
def RequestOriginCheck():
    if request.remote_addr != "127.0.0.1" and request.args.get('id') != APPLICATION_ID:
        return jsonify({"err": "ID doesn't match for outbound connections"})



@app.route("/")
def Index():
    return "Hello"



app.run("0.0.0.0", 5000, ssl_context="adhoc")