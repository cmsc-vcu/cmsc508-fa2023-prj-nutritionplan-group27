from flask import Flask, redirect, url_for, request, jsonify, Blueprint
import pymysql.cursors
from dotenv import dotenv_values
from flask_cors import CORS

users_bp = Blueprint('users_bp', __name__)

config = dotenv_values(".env")

page_size = 25

def valid_id(number):
    return number > 0 and number < 8

# Users section
@users_bp.route('/users', methods=['GET'])
def users():
    cnx = pymysql.connect(host=config['host'],
                    user=config['user'],
                    password=config['password'],
                    database=config['database'],
                    cursorclass=pymysql.cursors.DictCursor)
    
    current_page = request.args.get('page', default=1, type=int)
    user_id = request.headers.get('user-id', default=0, type=int)
    direction = "ASC"
    if(request.args.get('direction', default=0, type=int) == 1):
        direction = "DESC"
    
    data = {
        'results': []
    }
    
    with cnx:
        with cnx.cursor() as cursor:
                query = f"""
                SELECT *
                FROM users
                """
                if(user_id != 0):
                    query += f"WHERE users.id = {user_id}"
                query += f"""
                ORDER BY users.id {direction}
                LIMIT {page_size} OFFSET {(current_page - 1) * page_size};"""
                
                try:
                    cursor.execute(query)
                except:
                    return {'error': 'SQL syntax error'}
                result = cursor.fetchall()
                
                if len(result) == page_size:
                    data['next'] = f"{request.base_url}?page={current_page+1}"
                
                for row in result:
                    formattedRow = {
                        'username': row['username'],
                        'id': row['id'],
                        'mealplan-id': row['mealplan_id'],
                        'goal-id': row['goal_id'],
                        'about_me': row['about_me']
                    }
                    data['results'].append(formattedRow)
    return jsonify(data)

@users_bp.route('/users/goals', methods=['GET'])
def sortUsersByGoals():
    cnx = pymysql.connect(host=config['host'],
                    user=config['user'],
                    password=config['password'],
                    database=config['database'],
                    cursorclass=pymysql.cursors.DictCursor)
    
    current_page = request.args.get('page', default=1, type=int)
    goal_id = request.headers.get('goal-id', default=0, type=int)
    mealplan_id = request.headers.get('mealplan-id', default=0, type=int)
    exclude = request.headers.get('exclude', default=False, type=bool)
    direction = "ASC"
    if(request.args.get('direction', default=0, type=int) == 1):
        direction = "DESC"
    
    data = {
        'results': []
    }
    
    with cnx:
        with cnx.cursor() as cursor:
                query = f"""
                SELECT *
                FROM users
                """
                if(goal_id != 0):
                    exclusion = "" if(exclude == False) else "NOT"
                    if(goal_id < 0):
                        query += f"WHERE users.goal_id IS {exclusion} NULL "
                    else:
                        query += f"WHERE {exclusion} users.goal_id = {goal_id} "
                    if(mealplan_id != 0):
                        query += f"AND {exclusion} users.mealplan_id = {mealplan_id}"
                query += f"""
                ORDER BY users.goal_id {direction}
                LIMIT {page_size} OFFSET {(current_page - 1) * page_size};"""
                
                try:
                    cursor.execute(query)
                except pymysql.Error as e:
                    return {'error': f'SQL syntax error {e}'}
                result = cursor.fetchall()
                
                if len(result) == page_size:
                    data['next'] = f"{request.base_url}?page={current_page+1}"
                
                for row in result:
                    formattedRow = {
                        'username': row['username'],
                        'id': row['id'],
                        'mealplan-id': row['mealplan_id'],
                        'goal-id': row['goal_id'],
                        'about_me': row['about_me']
                    }
                    data['results'].append(formattedRow)
    return jsonify(data)

@users_bp.route('/users/mealplans', methods=['GET'])
def sortUsersByMealplans():
    cnx = pymysql.connect(host=config['host'],
                    user=config['user'],
                    password=config['password'],
                    database=config['database'],
                    cursorclass=pymysql.cursors.DictCursor)
    
    current_page = request.args.get('page', default=1, type=int)
    mealplan_id = request.headers.get('mealplan-id', default=0, type=int)
    goal_id = request.headers.get('goal-id', default=0, type=int)
    exclude = request.headers.get('exclude', default=False, type=bool)
    direction = "ASC"
    if(request.args.get('direction', default=0, type=int) == 1):
        direction = "DESC"
    
    data = {
        'results': []
    }
    
    with cnx:
        with cnx.cursor() as cursor:
                query = f"""
                SELECT *
                FROM users
                """
                if(mealplan_id != 0):
                    exclusion = "" if(exclude == False) else "NOT"
                    if(mealplan_id < 0):
                        query += f"WHERE users.mealplan_id IS {exclusion} NULL "
                    else:
                        query += f"WHERE {exclusion} users.mealplan_id = {mealplan_id} "
                    if(goal_id != 0):
                        query += f"AND {exclusion} users.goal_id = {goal_id}"
                query += f"""
                ORDER BY users.mealplan_id {direction}
                LIMIT {page_size} OFFSET {(current_page - 1) * page_size};"""
                
                try:
                    cursor.execute(query)
                except pymysql.Error as e:
                    return {'error': f'SQL syntax error {e}'}
                result = cursor.fetchall()
                
                if len(result) == page_size:
                    data['next'] = f"{request.base_url}?page={current_page+1}"
                
                for row in result:
                    formattedRow = {
                        'username': row['username'],
                        'id': row['id'],
                        'mealplan-id': row['mealplan_id'],
                        'goal-id': row['goal_id'],
                        'about_me': row['about_me']
                    }
                    data['results'].append(formattedRow)
    return jsonify(data)

@users_bp.route('/users/username', methods=['GET'])
def getUserByUsername():
    cnx = pymysql.connect(host=config['host'],
                    user=config['user'],
                    password=config['password'],
                    database=config['database'],
                    cursorclass=pymysql.cursors.DictCursor)
    
    current_page = request.args.get('page', default=1, type=int)
    username = request.headers.get('search', default="")
    direction = "ASC"
    if(request.args.get('direction', default=0, type=int) == 1):
        direction = "DESC"
    
    data = {
        'results': []
    }
    
    with cnx:
        with cnx.cursor() as cursor:
                query = f"""
                SELECT *
                FROM users
                """
                if(username != ""):
                    query += f"WHERE users.username LIKE '%{username}%'"
                query += f"""
                ORDER BY users.username {direction}
                LIMIT {page_size} OFFSET {(current_page - 1) * page_size};"""
                
                try:
                    cursor.execute(query)
                except:
                    return {'error': 'SQL syntax error'}
                result = cursor.fetchall()
                
                if len(result) == page_size:
                    data['next'] = f"{request.base_url}?page={current_page+1}"
                
                for row in result:
                    formattedRow = {
                        'username': row['username'],
                        'id': row['id'],
                        'mealplan-id': row['mealplan_id'],
                        'goal-id': row['goal_id'],
                        'about_me': row['about_me']
                    }
                    data['results'].append(formattedRow)
    return jsonify(data)

@users_bp.route('/users/aboutme', methods=['GET'])
def sortusersByAboutMe():
    cnx = pymysql.connect(host=config['host'],
                    user=config['user'],
                    password=config['password'],
                    database=config['database'],
                    cursorclass=pymysql.cursors.DictCursor)
    
    current_page = request.args.get('page', default=1, type=int)
    search = request.headers.get('aboutme', default="")
    
    direction = "ASC"
    if(request.args.get('direction', default=0, type=int) == 1):
        direction = "DESC"
    
    exclude = request.args.get('exclude', default=False, type=bool)
    
    data = {
        'results': []
    }
    
    with cnx:
        with cnx.cursor() as cursor:
                query = f"""
                SELECT *
                FROM users
                """
                if(search != ""):
                    exclusion = "" if(exclude == False) else "NOT"
                    query += f"WHERE {exclusion} users.about_me LIKE '%{search}%'"
                query+= f"""
                ORDER BY users.about_me {direction}
                LIMIT {page_size} OFFSET {(current_page - 1) * page_size};
                """
                
                try:
                    cursor.execute(query)
                except:
                    return {'error': 'SQL syntax error'}
                result = cursor.fetchall()
                
                if len(result) == page_size:
                    data['next'] = f"{request.base_url}?page={current_page+1}"
                
                for row in result:
                    formattedRow = {
                        'name': row['username'],
                        'about_me': row['about_me'],
                        'mealplan_id': row['mealplan_id'],
                        'goal_id': row['goal_id']
                    }
                    data['results'].append(formattedRow)
                    
    return jsonify(data)