"""
Author : MOHD ZULFADZLI BIN AB JALIL

This code will demonstrate a to-do app backend with APIs.
* Assuming the to-do app is having an admin that was set as permanent user.
* The app only need access token (Authentication) when calling for APIs, accessing to-do list.
* Assuming the functionality is only to demonstrate the back-end of the app and maintain simplicity.

To execute this program simply look for README file for more details explanation.

"""
from flask import Flask, jsonify, request, session
from datetime import timedelta
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from pymongo import MongoClient
from dotenv import load_dotenv
import os
# initiate env
load_dotenv()

app = Flask(__name__)
app.secret_key = "todoapp"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)
client = MongoClient(os.environ.get("MONGODB_URI"))
app.db = client.todoapp

users = {"todoapp@gmail.com": "mypass123"}
# todos = []
# completions = []


@app.route('/')
def home():
    """
    Home page for the app. Checking for the user in the session.

    :return: message to indicate the user already login or not authorized.
    """
    if 'username' in session:
        username = session['username']
        return jsonify({'message': 'You are already logged in', 'username': username})
    else:
        resp = jsonify({'message': 'Unauthorized'})
        resp.status_code = 401
        return resp


@app.route('/login', methods=['POST'])
def login():
    """
    To login, POST Username and Password in JSON format.

    :return: message successfully login if the request sent are correct Username and Password and followed format
    else return 400 (Bad Request).
    """
    _json = request.json
    _username = _json['username']
    _password = _json['password']
    # validate the received values
    if _username and _password:
        if users.get(_username) == _password:
            access_token = create_access_token(identity=_username)
            session['username'] = _username
            return jsonify({
                'message': 'You are logged in successfully',
                'access_token': access_token
            })
        else:
            resp = jsonify({'message': 'Bad Request - invalid username or password'})
            resp.status_code = 400
            return resp
    else:
        resp = jsonify({'message': 'Bad Request - invalid credendtials'})
        resp.status_code = 400
        return resp


@app.route('/logout')
def logout():
    """
    To logout from the application and cancel authorization.

    :return: message successfully logout.
    """
    if 'username' in session:
        session.pop('username', None)
    return jsonify({'message': 'You successfully logged out'})


@app.route("/add", methods=["POST"])
@jwt_required()
def add_todo():
    """
    To add to-do from the list.

    :return: response message added if to-do not exist in list
    else return 400 (Bad Request) or 401 (Unauthorized).
    """
    if 'username' in session:
        _json_todo = request.json
        _todo = _json_todo['todo']
        todos = [x["name"] for x in app.db.todos.find()]
        if _todo not in todos:
            # todos.append(_todo)
            app.db.todos.insert_one(
                {"name": _todo}
            )
            return jsonify({'message': 'Successfully added to do into list'})
        else:
            resp = jsonify({'message': 'Bad Request - invalid key or already exist in the list'})
            resp.status_code = 400
            return resp
    else:
        resp = jsonify({'message': 'Unauthorized'})
        resp.status_code = 401
        return resp


@app.route("/listall", methods=["POST", "GET"])
@jwt_required()
def list_all_todo():
    """
    To list all to-do from the existed list.

    :return: response the list for all to-do from the existed list.
    """
    todo_with_mark = []
    todos = [x["name"] for x in app.db.todos.find()]
    completions = [x["name"] for x in app.db.completions.find()]
    for i in todos:
        if i in completions:
            todo_with_mark.append(i + " [X]")
        else:
            todo_with_mark.append(i + " [ ]")
    return jsonify({'todos': todo_with_mark})


@app.route("/complete", methods=["POST"])
@jwt_required()
def complete():
    """
    To mark to-do from the list if existed.

    :return: response message marked if to-do exist in list
    else return 400 (Bad Request) or 401 (Unauthorized).
    """
    if 'username' in session:
        _json = request.json
        _tomark = _json['tomark']
        todos = [x["name"] for x in app.db.todos.find()]
        if _tomark in todos:
            # completions.append(_tomark)
            app.db.completions.insert_one(
                {"name": _tomark}
            )
            return jsonify({'message': 'Marked as Completed'})
        else:
            resp = jsonify({'message': 'Bad Request - invalid key or not exist in the list'})
            resp.status_code = 400
            return resp
    else:
        resp = jsonify({'message': 'Unauthorized'})
        resp.status_code = 401
        return resp


@app.route('/deltodo', methods=['DELETE'])
@jwt_required()
def delete_todo():
    """
    To delete to-do from the list if existed.

    :return: response message successfully deleted if to-do exist in list
    else return 400 (Bad Request) or 401 (Unauthorized).
    """
    if 'username' in session:
        _json_todo = request.json
        _todelete = _json_todo['todelete']
        todos = [x["name"] for x in app.db.todos.find()]
        completions = [x["name"] for x in app.db.completions.find()]
        if _todelete in todos:
            # todos.remove(_todelete)
            app.db.todos.delete_one(
                {"name": _todelete}
            )
            if _todelete in completions:
                app.db.completions.delete_one(
                    {"name": _todelete}
                )
            return jsonify({'message': 'Todo deleted'})
        else:
            resp = jsonify({'message': 'Bad Request - invalid key or not exist in  the list'})
            resp.status_code = 400
            return resp
    else:
        resp = jsonify({'message': 'Unauthorized'})
        resp.status_code = 401
        return resp


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
