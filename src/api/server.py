from flask import Flask, redirect, url_for, request, jsonify
import pymysql.cursors
from flask_cors import CORS
from routes.users import users_bp
from routes.recipes import recipes_bp
from routes.goals import goals_bp
from routes.mealplans import mealplans_bp
from routes.create import create_bp
from routes.update import update_bp
from routes.delete import delete_bp

app = Flask(__name__)
app.register_blueprint(users_bp)
app.register_blueprint(recipes_bp)
app.register_blueprint(goals_bp)
app.register_blueprint(mealplans_bp)
app.register_blueprint(create_bp)
app.register_blueprint(update_bp)
app.register_blueprint(delete_bp)
CORS(app)

config = {
    'user': '23FA_dellimorez',
    'password': 'Shout4_dellimorez_GOME',
    'host': 'cmsc508.com',
    'database': '23FA_groups_group27',
    'raise_on_warnings': True
}

page_size = 25 # Number of rows per page

# Security check
@app.before_request
def security_check():
    
    password = request.headers.get('password')  # Extract API key from header
    username = request.headers.get('username')
    
    if request.path == '/create/user':
        return
    if username == None or password == None:
        return jsonify({'message': 'Enter Username and Password'}), 401
    
    cnx = pymysql.connect(host=config['host'],
                        user=config['user'],
                        password=config['password'],
                        database=config['database'],
                        cursorclass=pymysql.cursors.DictCursor)
    
    with cnx:
        with cnx.cursor() as cursor:
                query = f"""
                SELECT *
                FROM users
                WHERE users.username = '{username}';
                """
                
                cursor.execute(query)
                result = cursor.fetchall()
                print(len(result))
                if len(result) != 1:
                    return jsonify({'message': 'Invalid Username/Password'}), 401             

@app.route('/', methods=['GET'])
def default():
    return jsonify({'message': 'Please enter a correct path to access the api'})

if __name__ == '__main__':
    app.run(debug=True)
    
