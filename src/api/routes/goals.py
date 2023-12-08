from flask import Flask, redirect, url_for, request, jsonify, Blueprint
import pymysql.cursors
from flask_cors import CORS

goals_bp = Blueprint('goals_bp', __name__)

config = {
    'user': '23FA_dellimorez',
    'password': 'Shout4_dellimorez_GOME',
    'host': 'cmsc508.com',
    'database': '23FA_groups_group27',
    'raise_on_warnings': True
}

page_size = 25

# Goals section
@goals_bp.route('/goals', methods=['GET'])
def goals():
    cnx = pymysql.connect(host=config['host'],
                        user=config['user'],
                        password=config['password'],
                        database=config['database'],
                        cursorclass=pymysql.cursors.DictCursor)
    
    current_page = request.args.get('page', default=1, type=int)
    direction = "ASC"
    if(request.args.get('direction', default=0, type=int) == 1):
        direction = "DESC"
    
    goal_id = request.headers.get('goal-id', default=0)
    
    data = {
        'results': []
    }
    
    with cnx:
        with cnx.cursor() as cursor:
                query = f"""
                SELECT *
                FROM goals
                """
                if(goal_id != 0):
                    query+=f"WHERE goals.id = {goal_id}"
                query+=f"""
                ORDER BY goals.id {direction}
                LIMIT {page_size} OFFSET {(current_page - 1) * page_size};
                """
                
                cursor.execute(query)
                result = cursor.fetchall()
                
                if len(result) == page_size:
                    data['next'] = f"{request.base_url}?page={current_page+1}"
                
                for row in result:
                    formattedRow = {
                        'name': row['name'],
                        'id': row['id'],
                        'description': row['description']
                    }
                    data['results'].append(formattedRow)
    return jsonify(data)

@goals_bp.route('/goals/name', methods=['GET'])
def sortByGoalName():
    cnx = pymysql.connect(host=config['host'],
                        user=config['user'],
                        password=config['password'],
                        database=config['database'],
                        cursorclass=pymysql.cursors.DictCursor)
    
    current_page = request.args.get('page', default=1, type=int)
    name = request.headers.get('search', default=None)
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
                FROM goals
                """
                if(name != None):
                    print("ball")
                    query+= f"""
                    WHERE goals.name LIKE '%{name}%'
                    """
                query+=f"""
                ORDER BY goals.name {direction}
                LIMIT {page_size} OFFSET {(current_page - 1) * page_size};
                """
                
                cursor.execute(query)
                result = cursor.fetchall()
                
                if len(result) == page_size:
                    data['next'] = f"{request.base_url}?page={current_page+1}"
                
                for row in result:
                    formattedRow = {
                        'name': row['name'],
                        'id': row['id'],
                        'description': row['description']
                    }
                    data['results'].append(formattedRow)
    return jsonify(data)

@goals_bp.route('/goals/popularity', methods=['GET'])
def sortGoalsByPopularity():
    cnx = pymysql.connect(host=config['host'],
                        user=config['user'],
                        password=config['password'],
                        database=config['database'],
                        cursorclass=pymysql.cursors.DictCursor)
    
    current_page = request.args.get('page', default=1, type=int)
    direction = "DESC"
    if(request.args.get('direction', default=0, type=int) == 1):
        direction = "ASC"
        
    
    goal_id = request.headers.get('goal-id', default=0)
    
    data = {
        'results': []
    }
    
    with cnx:
        with cnx.cursor() as cursor:
                query = f"""
                SELECT g.id AS goal_id, g.name, g.description, COALESCE(popular_goals.goal_count, 0) AS times_used
                FROM goals g
                JOIN(
                    SELECT goal_id, count(goal_id) as goal_count
                    FROM users
                    GROUP BY goal_id
                    ORDER BY goal_count {direction}
                    LIMIT {page_size} OFFSET {(current_page - 1) * page_size}
                ) AS popular_goals
                ON g.id = popular_goals.goal_id
                """
                if(goal_id != 0):
                    query += f"WHERE g.id = {goal_id}"
                query+=f"""
                ORDER BY times_used {direction};
                """
                
                cursor.execute(query)
                result = cursor.fetchall()
                
                if len(result) == page_size:
                    data['next'] = f"{request.base_url}?page={current_page+1}"
                
                for row in result:
                    formattedRow = {
                        'name': row['name'],
                        'description': row['description'],
                        'times_used': row['times_used']
                    }
                    data['results'].append(formattedRow)
    return jsonify(data)