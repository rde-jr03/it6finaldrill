from flask import Flask, make_response, jsonify, request, abort
from flask_mysqldb import MySQL
from flask_httpauth import HTTPBasicAuth
import dicttoxml
from xml.dom.minidom import parseString

app = Flask(__name__)
auth = HTTPBasicAuth()

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "classicmodels"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

#Hello World!
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)