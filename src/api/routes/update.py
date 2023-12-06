from flask import Flask, redirect, url_for, request, jsonify, Blueprint
import pymysql.cursors
from flask_cors import CORS

update_bp = Blueprint('update_bp', __name__)

config = {
    'user': '23FA_dellimorez',
    'password': 'Shout4_dellimorez_GOME',
    'host': 'cmsc508.com',
    'database': '23FA_groups_group27',
    'raise_on_warnings': True
}

# Create User
@update_bp.route('/update/user', methods=['GET'])
def createUser():
    cnx = pymysql.connect(host=config['host'],
                    user=config['user'],
                    password=config['password'],
                    database=config['database'],
                    cursorclass=pymysql.cursors.DictCursor)
    
    username = request.headers.get('username', default=None)
    password = request.headers.get('password', default=None)
    new_username = request.headers.get('new-username', default=None)
    new_password = request.headers.get('new-password', default=None)
    new_about_me = request.headers.get('new-about_me', default=None)
    new_mealplan = request.headers.get('new-mealplan', default=None)
    new_goal = request.headers.get('new-goal', default=None)
    
    if new_mealplan != None and not new_mealplan.isnumeric():
        return jsonify( {'error': 'Please enter a valid mealplan id for new_mealplan'} )
    elif new_mealplan != None:
        if int(new_mealplan) < 1 or int(new_mealplan) > 7:
            return jsonify( {'error': 'Mealplan id must be between 1-7'} )
    
    if new_goal != None and not new_goal.isnumeric():
        return jsonify( {'error': 'Please enter a valid goal id for new_goal'} )
    elif new_goal != None:
        if int(new_goal) < 1 or int(new_goal) > 6:
            return jsonify( {'error': 'Goal id must be between 1-6'} )
    
    if new_about_me != None and len(new_about_me) > 256:
        return jsonify( {'error': 'new_about_me length should be less than 256 characters'} )
    
    
    
    print(request.headers)
    
    with cnx:
        with cnx.cursor() as cursor:
            if (new_password != None):
                query = f"""
                UPDATE users
                SET password = '{new_password}'
                WHERE users.username = '{username}';
                """
                cursor.execute(query)
            
            if (new_about_me != None):
                query = f"""
                UPDATE users
                SET about_me = '{new_about_me}'
                WHERE username = '{username}';
                """
                cursor.execute(query)
                result = cursor.fetchall()
                print("hello")
            
            if (new_mealplan != None):
                query = f"""
                UPDATE users
                SET mealplan_id = '{new_mealplan}'
                WHERE users.username = '{username}';
                """
                cursor.execute(query)
            
            if (new_goal != None):
                query = f"""
                UPDATE users
                SET goal_id = '{new_goal}'
                WHERE users.username = '{username}';
                """
                cursor.execute(query)
            
            if (new_username != None):
                query = f"""
                SELECT *
                FROM users
                WHERE users.username = '{new_username}';
                """
                
                cursor.execute(query)
                result = cursor.fetchall()
                
                if(len(result) != 0):
                    return jsonify( {'error': 'New Username already taken'} )
                
                query = f"""
                UPDATE users
                SET username = '{new_username}'
                WHERE users.username = '{username}';
                """
                cursor.execute(query)
        
        cnx.commit()
    return jsonify( {'message': 'Account Updated Successfully'} ), 200