from flask import Flask
from dlp import CNF_PATH
from dlp.utils import load_yaml

CNF = load_yaml(CNF_PATH)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"<h1>Welcome to Project {CNF.project_name}!</h1>"

if __name__ == '__main__':
    app.run(debug=True)