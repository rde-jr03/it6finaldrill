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


#username and password
@auth.verify_password
def verify_password(username, password):
    return username == "ronnie" and password == "2003"

#convert data to xml
def convert_to_xml(data):
    xml = dicttoxml.dicttoxml(data, custom_root='response', attr_type=False)
    dom = parseString(xml)
    return dom.toprettyxml()

def format_response(data):
    response_format = request.args.get('format', 'json').lower()
    if response_format == 'xml':
        xml_data = convert_to_xml
        return make_response(xml_data, 200, {'Content-Type': 'application/xml'})
    else:
        return make_response(jsonify(data), 200)
    
@app.route("/protected")
@auth.login_required
def protected_resource():
    return jsonify({"message": "You are authorized to access this information"})

#Hello World!
@app.route("/")
@auth.login_required
def hello_world():
    return "<p>Hello, World!</p>"


#CREATE
@app.route("/employees", methods=["GET"])
@auth.login_required
def get_employee():
    data = data_fetch("""select * from employees""")
    return make_response(jsonify(data), 200)

#Get employee by id
@app.route("/employees/<int:id>", methods=["GET"])
@auth.login_required
def get_employee_by_id(id):
    data = data_fetch("""select * from employees where employeeNumber = {}""".format(id))
    return make_response(jsonify(data), 200)

#inner join
@app.route("/order/<int:id>/orderdetails", methods=["GET"])
@auth.login_required
def get_order_details(id):
    data = data_fetch(""" select orders.orderNumber, orderdetails.quantityOrdered
                      from orders inner join orderdetails on orders.orderNumber = orderdetails.orderNumber 
                      where orders.orderNumber = 10100;""".format(id))
    return make_response(jsonify(data), 200)



#function to fetch data
def data_fetch(query):
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    return data

if __name__ == "__main__":
    app.run(debug=True)