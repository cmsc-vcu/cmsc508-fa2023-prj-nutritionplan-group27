from flask import Flask, redirect, url_for, request, jsonify, Blueprint
import pymysql.cursors
from flask_cors import CORS

recipes_bp = Blueprint('recipes_bp', __name__)

config = {
  'user': '23FA_dellimorez',
  'password': 'Shout4_dellimorez_GOME',
  'host': 'cmsc508.com',
  'database': '23FA_groups_group27',
  'raise_on_warnings': True
}

page_size = 25

# Recipe section 
@recipes_bp.route('/recipes', methods=['GET'])
def recipes():
    cnx = pymysql.connect(host=config['host'],
                    user=config['user'],
                    password=config['password'],
                    database=config['database'],
                    cursorclass=pymysql.cursors.DictCursor)
    
    current_page = request.args.get('page', default=1, type=int)
    
    direction = "ASC"
    if(request.args.get('direction', default=0, type=int) == 1):
        direction = "DESC"
    
    recipe = request.args.get('name', default="")
    
    exclude = request.args.get('exclude', default=False, type=bool)
    
    data = {
        'results': []
    }
    
    with cnx:
        with cnx.cursor() as cursor:
                query = f"""
                SELECT *
                FROM recipes
                """
                if(recipe != ""):
                    exclusion = "" if(exclude == False) else "NOT"
                    query += f"WHERE {exclusion} recipes.name LIKE '%{recipe}%'"
                query += f"""
                ORDER BY recipes.id {direction}
                LIMIT {page_size} OFFSET {(current_page - 1) * page_size};
                """
                
                cursor.execute(query)
                result = cursor.fetchall()
                
                if len(result) == page_size:
                    data['next'] = f"{request.base_url}?page={current_page+1}"
                
                for row in result:
                    formattedRow = {
                        'name': row['name'],
                        'ingredients': row['ingredients'],
                        'instructions': row['instructions'],
                        'nutrition': row['calories']
                    }
                    data['results'].append(formattedRow)
    return jsonify(data)

@recipes_bp.route('/recipes/name', methods=['GET'])
def sortRecipesByName():
    cnx = pymysql.connect(host=config['host'],
                    user=config['user'],
                    password=config['password'],
                    database=config['database'],
                    cursorclass=pymysql.cursors.DictCursor)
    
    current_page = request.args.get('page', default=1, type=int)
    recipe = request.args.get('name', default="")
    
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
                FROM recipes
                """
                if(recipe != ""):
                    exclusion = "" if(exclude == False) else "NOT"
                    query += f"WHERE {exclusion} recipes.name LIKE '%{recipe}%'"
                query+= f"""
                ORDER BY recipes.name {direction}
                LIMIT {page_size} OFFSET {(current_page - 1) * page_size};
                """
                
                cursor.execute(query)
                result = cursor.fetchall()
                
                if len(result) == page_size:
                    data['next'] = f"{request.base_url}?page={current_page+1}"
                
                for row in result:
                    formattedRow = {
                        'name': row['name'],
                        'ingredients': row['ingredients'],
                        'instructions': row['instructions'],
                        'nutrition': row['calories']
                    }
                    data['results'].append(formattedRow)
                                              
    return jsonify(data)

@recipes_bp.route('/recipes/id', methods=['GET'])
def searchRecipeById():
    cnx = pymysql.connect(host=config['host'],
                        user=config['user'],
                        password=config['password'],
                        database=config['database'],
                        cursorclass=pymysql.cursors.DictCursor)
  
    current_page = request.args.get('page', default=1, type=int)
    
    recipe_id = request.args.get('id', default=0, type=int)
    
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
                FROM recipes
                """
                if(recipe_id != 0):
                    exclusion = "" if(exclude == False) else "NOT"
                    query += f"WHERE {exclusion} recipes.id = {recipe_id}"
                query+= f"""
                ORDER BY recipes.id {direction}
                LIMIT {page_size} OFFSET {(current_page - 1) * page_size};
                """
                cursor.execute(query)
                result = cursor.fetchall()
                if len(result) == page_size:
                    data['next'] = f"{request.base_url}?page={current_page+1}"
                
                for row in result:
                    formattedRow = {
                        'name': row['name'],
                        'ingredients': row['ingredients'],
                        'instructions': row['instructions'],
                        'nutrition': row['calories']
                    }
                    data['results'].append(formattedRow)
                    
                if(recipe_id != 0):
                    query = f"""
                    SELECT name 
                    FROM mealplans
                    JOIN mealplanRecipes ON mealplans.id = mealplanRecipes.mealplan_id
                    WHERE mealplanRecipes.recipe_id = {recipe_id} 
                    LIMIT {page_size} OFFSET {(current_page - 1) * page_size};
                    """
                    cursor.execute(query)
                    result = cursor.fetchall()
                    
                    for row in result:
                        data['results'].append(row['name'])
                                              
    return jsonify(data)

@recipes_bp.route('/recipes/calories', methods=['GET'])
def sortRecipesByNutrition():
    cnx = pymysql.connect(host=config['host'],
                    user=config['user'],
                    password=config['password'],
                    database=config['database'],
                    cursorclass=pymysql.cursors.DictCursor)
    
    current_page = request.args.get('page', default=1, type=int)
    recipe = request.args.get('name', default="")
    
    direction = "ASC"
    if(request.args.get('direction', default=0, type=int) == 1):
        direction = "DESC"
    
    exclude = request.args.get('exclude', default=False, type=bool)
    
    limit = request.args.get('limit', default=999999, type=int)
    
    greater_than = request.args.get('greater_than', default=False, type=bool)
    
    symbol = '>' if greater_than else '<'
    
    if greater_than and limit == 999999:
        limit = 0
    
    data = {
        'results': []
    }
    
    with cnx:
        with cnx.cursor() as cursor:
                query = f"""
                SELECT *
                FROM recipes
                """
                if(recipe != ""):
                    exclusion = "" if(exclude == False) else "NOT"
                    query += f"WHERE {exclusion} recipes.name LIKE '%{recipe}%'"
                query+= f"""
                WHERE recipes.calories {symbol} {limit}
                ORDER BY recipes.calories {direction}
                LIMIT {page_size} OFFSET {(current_page - 1) * page_size};
                """
                
                cursor.execute(query)
                result = cursor.fetchall()
                
                if len(result) == page_size:
                    data['next'] = f"{request.base_url}?page={current_page+1}"
                
                for row in result:
                    formattedRow = {
                        'name': row['name'],
                        'ingredients': row['ingredients'],
                        'instructions': row['instructions'],
                        'nutrition': row['calories']
                    }
                    data['results'].append(formattedRow)
                                              
    return jsonify(data)

@recipes_bp.route('/recipes/ingredients', methods=['GET'])
def sortRecipesByIngredients():
    cnx = pymysql.connect(host=config['host'],
                    user=config['user'],
                    password=config['password'],
                    database=config['database'],
                    cursorclass=pymysql.cursors.DictCursor)
    
    current_page = request.args.get('page', default=1, type=int)
    ingredient = request.args.get('ingredient', default="")
    
    direction = "ASC"
    if(request.args.get('direction', default=0, type=int) == 1):
        direction = "DESC"
    
    exclude = request.args.get('exclude', default=False, type=bool)
    
    limit = request.args.get('limit', default=999999, type=int)
    
    data = {
        'results': []
    }
    
    with cnx:
        with cnx.cursor() as cursor:
                query = f"""
                SELECT *
                FROM recipes
                """
                if(ingredient != ""):
                    exclusion = "" if(exclude == False) else "NOT"
                    query += f"WHERE {exclusion} recipes.ingredients LIKE '%{ingredient}%'"
                query+= f"""
                ORDER BY recipes.name {direction}
                LIMIT {page_size} OFFSET {(current_page - 1) * page_size};
                """
                
                cursor.execute(query)
                result = cursor.fetchall()
                
                if len(result) == page_size:
                    data['next'] = f"{request.base_url}?page={current_page+1}"
                
                for row in result:
                    formattedRow = {
                        'name': row['name'],
                        'ingredients': row['ingredients'],
                        'instructions': row['instructions'],
                        'nutrition': row['calories']
                    }
                    data['results'].append(formattedRow)
                                              
    return jsonify(data)

# TODO: Add Update, Insert, and Delete functionality