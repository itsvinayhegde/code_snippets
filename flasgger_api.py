import hmac
# from flasgger import Swagger
# from flask import Flask, request, jsonify
# from flask_jwt import JWT, jwt_required, current_identity, JWTError

class User(object):
    def __init__(self, user_id, username, password):
        self.id = user_id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id=%s)" % self.id
    
users = [User(1, 'vinay', 'vinay@123')]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and hmac.compare_digest(user.password.encode('utf-8'), password.encode('utf-8')):
        return user
    
def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret'
app.config['SWAGGER'] = {
    'title': 'Swagger JWT authentication App',
    'uiversion': 3,
}
app.config['JWT_AUTH_URL_RULE'] = '/api/auth'
app.config['JWT_AUTH_HEADER_NAME'] = 'Jwtauthorization'
app.config['JWT_AUTH_HEADER_NAME'] = 'Bearer'

swag = Swagger(app,
               template={
                   'swagger': '2.0.0',
                   'info':{
                       'title': 'Swagger Authentication app',
                       'version': '1.0',
                   },
                   'consumes':['application/x-www-form-urlencoded',],
                   'produces': ['appliaction/json',]
               },
            )

def jwt_request_handler():
    auth_header_name = app.config['JWT_AUTH_HEADER_NAME']
    auth_header_value = request.headers.get(auth_header_name,None)
    auth_header_prefix = app.config['JWT_AUTH_HEADER_NAME']
    
    if not auth_header_value:
        return
    
    parts = auth_header_value.split()
    