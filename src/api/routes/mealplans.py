from flask import Flask, redirect, url_for, request, jsonify, Blueprint
import pymysql.cursors
import os
from flask_cors import CORS

mealplans_bp = Blueprint('mealplans_bp', __name__)

from dotenv import dotenv_values
config = dotenv_values(".env")

page_size = 25

@mealplans_bp.route('/mealplans', methods=['GET'])
def mealplan():
    cnx = pymysql.connect(host=config['host'],
                        user=config['user'],
                        password=config['password'],
                        database=config['database'],
                        cursorclass=pymysql.cursors.DictCursor)
    
    current_page = request.args.get('page', default=1, type=int)
    direction = "ASC"
    if(request.args.get('direction', default=0, type=int) == 1):
        direction = "DESC"
        
    mealplan_id = request.headers.get('mealplan-id', default=0)
    
    data = {
        'results': []
    }
    
    with cnx:
        with cnx.cursor() as cursor:
                query = f"""
                SELECT *
                FROM mealplans
                """
                if(mealplan_id != 0):
                    query+=f"WHERE mealplans.id = {mealplan_id}"
                query+=f"""
                ORDER BY mealplans.id {direction}
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
                        'name': row['name'],
                        'id': row['id']
                    }
                    data['results'].append(formattedRow)
                                            
    return jsonify(data)

@mealplans_bp.route('/mealplans/recipe', methods=['GET'])
def getMealplan():
    cnx = pymysql.connect(host=config['host'],
                        user=config['user'],
                        password=config['password'],
                        database=config['database'],
                        cursorclass=pymysql.cursors.DictCursor)

    current_page = request.args.get('page', default=1, type=int)
    mealplan_id = request.headers.get('mealplan-id', default=0)
    
    if mealplan_id == 0:
        return jsonify({'error': 'Please enter a mealplan_id in the arguments'}), 401
    
    recipe = request.headers.get('search', default=None)

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
                FROM recipes
                JOIN mealplanRecipes ON recipes.id = mealplanRecipes.recipe_id
                WHERE mealplanRecipes.mealplan_id = {mealplan_id}
                """
                
                if recipe != None:
                    query += f"AND recipes.name LIKE '%{recipe}%'"
                    
                query += f"""
                ORDER BY recipes.name {direction}
                LIMIT {page_size} OFFSET {(current_page - 1) * page_size};
                """
                print(query)
                
                try:
                    cursor.execute(query)
                except:
                    return {'error': 'SQL syntax error'}
                result = cursor.fetchall()
                if len(result) == page_size:
                    data['next'] = f"{request.base_url}?page={current_page+1}"
                
                for row in result:
                    formattedRow = {
                        'name': row['name'],
                        'ingredients': row['ingredients'],
                        'instructions': row['instructions'],
                        'nutrition': row['nutrition']
                    }
                    data['results'].append(formattedRow)
                                            
    return jsonify(data)

@mealplans_bp.route('/mealplans/popularity', methods=['GET'])
def sortMealplansByPopularity():
    cnx = pymysql.connect(host=config['host'],
                        user=config['user'],
                        password=config['password'],
                        database=config['database'],
                        cursorclass=pymysql.cursors.DictCursor)
    
    current_page = request.args.get('page', default=1, type=int)
    direction = "DESC"
    if(request.args.get('direction', default=0, type=int) == 1):
        direction = "ASC"
    
    exclude = request.args.get('exclude', default=False, type=bool)
    mealplan_id = request.headers.get('mealplan-id', default=0)
    goal_id = request.headers.get('goal-id', default=0)
    
    data = {
        'results': []
    }
    
    with cnx:
        with cnx.cursor() as cursor:
                query = f"""
                SELECT m.id AS mealplan_id, m.name, COALESCE(popular_mealplans.mealplan_count, 0) AS times_used
                FROM mealplans m
                JOIN(
                    SELECT mealplan_id, count(mealplan_id) as mealplan_count
                    FROM users
                """
                if(goal_id != 0):
                    exclusion = "" if(exclude == False) else "NOT"
                    query += f"WHERE {exclusion} users.goal_id = {goal_id}"
                query+=f"""
                    GROUP BY mealplan_id
                    ORDER BY mealplan_count {direction}
                    LIMIT {page_size} OFFSET {(current_page - 1) * page_size}
                ) AS popular_mealplans
                ON m.id = popular_mealplans.mealplan_id
                """
                if(mealplan_id != 0):
                    query += f"WHERE m.id = {mealplan_id}"
                query+=f"""
                ORDER BY times_used {direction};
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
                        'name': row['name'],
                        'times_used': row['times_used']
                    }
                    data['results'].append(formattedRow)
                                            
    return jsonify(data)