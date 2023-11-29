from flask import Flask, redirect, url_for, request, jsonify
import pymysql.cursors
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

config = {
  'user': '23FA_dellimorez',
  'password': 'Shout4_dellimorez_GOME',
  'host': 'cmsc508.com',
  'database': '23FA_groups_group27',
  'raise_on_warnings': True
}

page_size = 25 # Number of rows per page

@app.route('/recipes', methods=['GET'])
def recipes():
    cnx = pymysql.connect(host=config['host'],
                    user=config['user'],
                    password=config['password'],
                    database=config['database'],
                    cursorclass=pymysql.cursors.DictCursor)
    
    current_page = request.args.get('page', default=1, type=int)
    
    data = {
        'results': []
    }
    
    with cnx:
        with cnx.cursor() as cursor:
                query = f"""
                SELECT *
                FROM recipes
                LIMIT {page_size} OFFSET {(current_page - 1) * page_size};
                """
                
                cursor.execute(query)
                result = cursor.fetchall()
                
                if len(result) == page_size:
                    print(len(result))
                    data['next'] = f"{request.base_url}?page={current_page+1}"
                
                for row in result:
                    formattedRow = {
                        'name': row['name'],
                        'ingredients': row['ingredients'],
                        'instructions': row['instructions'],
                        'nutrition': row['nutrition']
                    }
                    print(formattedRow)
                    data['results'].append(formattedRow)
                                              
    return jsonify(data)

@app.route('/recipes/<recipe>', methods=['GET'])
def searchRecipe(recipe):
    cnx = pymysql.connect(host=config['host'],
                        user=config['user'],
                        password=config['password'],
                        database=config['database'],
                        cursorclass=pymysql.cursors.DictCursor)
  
    current_page = request.args.get('page', default=1, type=int)
    
    data = {
        'results': []
    }
    
    with cnx:
        with cnx.cursor() as cursor:
                query = f"""
                SELECT * 
                FROM recipes 
                WHERE name LIKE '%{recipe}%' 
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
                        'nutrition': row['nutrition']
                    }
                    print(formattedRow)
                    data['results'].append(formattedRow)
                                              
    return jsonify(data)

@app.route('/mealplans/<mealplan>/<recipe>', methods=['GET'])
def searchMealplans(mealplan, recipe):
    cnx = pymysql.connect(host=config['host'],
                        user=config['user'],
                        password=config['password'],
                        database=config['database'],
                        cursorclass=pymysql.cursors.DictCursor)

    current_page = request.args.get('page', default=1, type=int)
    
    data = {
        'results': []
    }
    
    with cnx:
        with cnx.cursor() as cursor:
                query = f"""
                SELECT *
                FROM recipes
                JOIN mealplanRecipes ON recipes.id = mealplanRecipes.recipe_id
                WHERE mealplanRecipes.mealplan_id = {mealplan}
                AND recipes.name LIKE '%{recipe}%'
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
                        'nutrition': row['nutrition']
                    }
                    print(formattedRow)
                    data['results'].append(formattedRow)
                                              
    return jsonify(data)

@app.route('/mealplans/<mealplan>', methods=['GET'])
def getMealplan(mealplan):
    cnx = pymysql.connect(host=config['host'],
                        user=config['user'],
                        password=config['password'],
                        database=config['database'],
                        cursorclass=pymysql.cursors.DictCursor)

    current_page = request.args.get('page', default=1, type=int)
    
    data = {
        'results': []
    }
    
    with cnx:
        with cnx.cursor() as cursor:
                query = f"""
                SELECT *
                FROM recipes
                JOIN mealplanRecipes ON recipes.id = mealplanRecipes.recipe_id
                WHERE mealplanRecipes.mealplan_id = {mealplan}
                LIMIT {page_size} OFFSET {(current_page - 1) * page_size};
                """
                
                cursor.execute(query)
                result = cursor.fetchall()
                if len(result) == page_size:
                    print(len(result))
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

@app.route('/mealplans', methods=['GET'])
def mealplan():
    cnx = pymysql.connect(host=config['host'],
                        user=config['user'],
                        password=config['password'],
                        database=config['database'],
                        cursorclass=pymysql.cursors.DictCursor)
    
    current_page = request.args.get('page', default=1, type=int)
    
    data = {
        'results': []
    }
    
    with cnx:
        with cnx.cursor() as cursor:
                query = f"""
                SELECT *
                FROM mealplans
                LIMIT {page_size} OFFSET {(current_page - 1) * page_size};
                """
                
                cursor.execute(query)
                result = cursor.fetchall()
                
                if len(result) == page_size:
                    print(len(result))
                    data['next'] = f"{request.base_url}?page={current_page+1}"
                
                for row in result:
                    formattedRow = {
                        'name': row['name'],
                        'id': row['id']
                    }
                    print(formattedRow)
                    data['results'].append(formattedRow)
                                              
    return jsonify(data)

@app.route('/goals', methods=['GET'])
def goals():
    cnx = pymysql.connect(host=config['host'],
                        user=config['user'],
                        password=config['password'],
                        database=config['database'],
                        cursorclass=pymysql.cursors.DictCursor)
    
    current_page = request.args.get('page', default=1, type=int)
    
    data = {
        'results': []
    }
    
    with cnx:
        with cnx.cursor() as cursor:
                query = f"""
                SELECT *
                FROM goals
                LIMIT {page_size} OFFSET {(current_page - 1) * page_size};
                """
                
                cursor.execute(query)
                result = cursor.fetchall()
                
                if len(result) == page_size:
                    print(len(result))
                    data['next'] = f"{request.base_url}?page={current_page+1}"
                
                for row in result:
                    formattedRow = {
                        'name': row['name'],
                        'id': row['id'],
                        'description': row['description']
                    }
                    print(formattedRow)
                    data['results'].append(formattedRow)
                                              
    return jsonify(data)

@app.route('/users', methods=['GET'])
def users():
    cnx = pymysql.connect(host=config['host'],
                    user=config['user'],
                    password=config['password'],
                    database=config['database'],
                    cursorclass=pymysql.cursors.DictCursor)
    
    current_page = request.args.get('page', default=1, type=int)
    
    data = {
        'results': []
    }
    
    with cnx:
        with cnx.cursor() as cursor:
                query = f"""
                SELECT *
                FROM users
                LIMIT {page_size} OFFSET {(current_page - 1) * page_size};
                """
                
                cursor.execute(query)
                result = cursor.fetchall()
                
                if len(result) == page_size:
                    print(len(result))
                    data['next'] = f"{request.base_url}?page={current_page+1}"
                
                for row in result:
                    formattedRow = {
                        'username': row['username'],
                        'id': row['id'],
                        'mealplan_id': row['mealplan_id']
                    }
                    print(formattedRow)
                    data['results'].append(formattedRow)
                                              
    return jsonify(data)

@app.route('/users/<user_id>', methods=['GET'])
def getUserById(user_id):
    cnx = pymysql.connect(host=config['host'],
                    user=config['user'],
                    password=config['password'],
                    database=config['database'],
                    cursorclass=pymysql.cursors.DictCursor)
    
    current_page = request.args.get('page', default=1, type=int)
    
    data = {
        'results': []
    }
    
    with cnx:
        with cnx.cursor() as cursor:
                query = f"""
                SELECT *
                FROM users
                WHERE users.id = {user_id}
                LIMIT {page_size} OFFSET {(current_page - 1) * page_size};
                """
                
                cursor.execute(query)
                result = cursor.fetchall()
                
                if len(result) == page_size:
                    print(len(result))
                    data['next'] = f"{request.base_url}?page={current_page+1}"
                
                for row in result:
                    formattedRow = {
                        'username': row['username'],
                        'id': row['id'],
                        'mealplan_id': row['mealplan_id']
                    }
                    print(formattedRow)
                    data['results'].append(formattedRow)
                                              
    return jsonify(data)

@app.route('/users/username/<username>', methods=['GET'])
def getUserByUsername(username):
    cnx = pymysql.connect(host=config['host'],
                    user=config['user'],
                    password=config['password'],
                    database=config['database'],
                    cursorclass=pymysql.cursors.DictCursor)
    
    current_page = request.args.get('page', default=1, type=int)
    
    data = {
        'results': []
    }
    
    with cnx:
        with cnx.cursor() as cursor:
                query = f"""
                SELECT *
                FROM users
                WHERE users.username LIKE '%{username}%'
                LIMIT {page_size} OFFSET {(current_page - 1) * page_size};
                """
                
                cursor.execute(query)
                result = cursor.fetchall()
                
                if len(result) == page_size:
                    print(len(result))
                    data['next'] = f"{request.base_url}?page={current_page+1}"
                
                for row in result:
                    formattedRow = {
                        'username': row['username'],
                        'id': row['id'],
                        'mealplan_id': row['mealplan_id']
                    }
                    print(formattedRow)
                    data['results'].append(formattedRow)
                                              
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
    
