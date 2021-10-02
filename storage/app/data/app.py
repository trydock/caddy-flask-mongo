from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return os.environ['APPCONFIG_MONGODB_ADMINUSERNAME']

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
