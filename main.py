from flask import Flask
import json
from flask import request
from flask_swagger_ui import get_swaggerui_blueprint
import info
app = Flask(__name__)

SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = "http://localhost:3003/"
  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "CUSTOMER API REST",
    },
)

# Register blueprint at URL
# (URL must match the one given to factory function above)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


@app.route("/")
def home():
    return json.dumps(info.info)
@app.route("/v1/customers", methods=['GET'])
def getAllCustomers():
    return {
        "msm": "Request Success"
    }

@app.route("/v1/customer/<id>", methods=['GET'])
def getOneCustomer(id):
    return {
        "id": id,
        "msm": "Request Success"
    }

@app.route("/v1/new/customer", methods=['POST'])
def saveOneCustomer():
    values = request.get_json()
    return {
        "msm": "Request Success",
        "username": values['username'],
        "nombres": values['nombres'],
        "apellidos": values['apellidos'],
        "email": values['email']
    }

@app.route("/v1/edit/customer/<id>", methods=['PUT'])
def editOneCustomer(id):
    return {
        "id": id,
        "msm": "Request Success"
    }

@app.route("/v1/delete/customer/<id>", methods=['DELETE'])
def DeleteOneCustomer(id):
    return {
        "id": id,
        "msm": "Request Success"
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port="3003", debug=True)