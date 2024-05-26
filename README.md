**CRUD REST API with MySQL, Testing, and XML/JSON Output**

**Project Overview:**
This project demonstrates the implementation of a CRUD (Create, Read, Update, Delete) REST API using Flask with a MySQL database backend. The API supports basic authentication, and responses can be formatted in either JSON or XML.

**GitHub Repository:**
https://github.com/rde-jr03/it6finaldrill.git

**Libraries Used:**
**Flask:** A micro web framework for Python.
**Flask-MySQLdb:** A Flask extension that allows interaction with a MySQL database.
**Flask-HTTPAuth:** A Flask extension for adding basic authentication to routes.
**dicttoxml:** A Python library for converting dictionaries to XML format.

**Installation:**
**Clone the repository:**
git clone https://github.com/rde-jr03/it6finaldrill.git
cd it6finaldrill

**Create a virtual environment and activate it:**
python -m venv venv
source venv/bin/activate

**Install the required libraries:**
pip install Flask Flask-MySQLdb Flask-HTTPAuth dicttoxml

**Configure MySQL:**
Ensure you have a MySQL server running and update the database credentials in the app.config section of the code.

**Configuration:**
**Update the following configuration settings in the code according to your MySQL server setup:**
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "classicmodels"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

**Running the Application:
Start the Flask development server:**
python app.py

**API Endpoints:**
**Authentication:**
The API uses basic authentication. Use the following credentials:
Username: ronnie
Password: 2003

**Endpoints:**
- Protected Resource
URL: /protected
Method: GET
Description: Returns a message indicating the user is authorized.

**Hello World:**
URL: /
Method: GET
Description: Returns a "Hello, World!" message.

**Get All Employees:**
URL: /employees
Method: GET
Description: Fetches all employee records.

**Get Employee by ID:**
URL: /employees/<int:id>
Method: GET
Description: Fetches a specific employee record by ID.

**Get Order Details:**
URL: /order/<int:id>/orderdetails
Method: GET
Description: Fetches order details for a specific order ID.

**Add Order:**
URL: /orders
Method: POST
Description: Adds a new order. The request must be in JSON format with the following fields: orderNumber, orderDate, requiredDate, shippedDate, status, comments, customerNumber.

**Update Order:**
URL: /orders/<int:orderNumber>
Method: PUT
Description: Updates an existing order. The request must be in JSON format with the following fields: orderDate, requiredDate, shippedDate, status, comments, customerNumber.

**Delete Order:**
URL: /orders/<int:id>
Method: DELETE
Description: Deletes an order by ID.

**Response Formats:**
**JSON (default):** The API responds with JSON by default.
**XML:** To receive responses in XML format, add the query parameter format=xml to the request URL.

