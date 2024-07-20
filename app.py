from flask_cors import CORS
from flask import *
import importlib
import glob
import sys
import os

def list_files(pattern='./**/*', recursive=True):
    files = glob.glob(pattern, recursive=recursive)
    return files


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

current_directory = os.path.join(os.path.dirname(__file__), "./routes/")

for filename in os.listdir(current_directory):
    if filename.endswith('.py') and filename != '__init__.py':
        module_name = filename[:-3]
        try:
            importlib.import_module(f"routes.{module_name}", package=__name__)
        except Exception as e:
            print(f"Plugin '{module_name}' encountered an error while loading: '{e}'")


app.run("0.0.0.0", 5000, debug=True, ssl_context="adhoc")