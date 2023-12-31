from flask import Flask, redirect, url_for, request, jsonify, Blueprint
import pymysql.cursors
import os
from flask_cors import CORS

create_bp = Blueprint('create_bp', __name__)

from dotenv import dotenv_values
config = dotenv_values(".env")

# Create User
@create_bp.route('/create/user', methods=['GET'])
def createUser():
    cnx = pymysql.connect(host=config['host'],
                    user=config['user'],
                    password=config['password'],
                    database=config['database'],
                    cursorclass=pymysql.cursors.DictCursor)
    
    username = request.args.get('username', default=None)
    password = request.args.get('password', default=None)
    
    if username == None or password == None:
        return jsonify( {'error': 'Please enter the desired username and password as arguments'} )
    
    with cnx:
        with cnx.cursor() as cursor:
            query = f"""
            SELECT *
            FROM users
            WHERE users.username = '{username}';
            """
            
            try:
                cursor.execute(query)
            except:
                return {'error': 'SQL syntax error'}
            result = cursor.fetchall()
            
            if(len(result) != 0):
                return jsonify( {'error': 'Username already taken'} )
            
            query = f"""
            insert into `users`
            (`username`, `password`) 
            values ("{username}", "{password}");
            """
            
            try:
                cursor.execute(query)
            except:
                return {'error': 'SQL syntax error'}
            result = cursor.fetchall()
            print(result)
        
        cnx.commit()
    return jsonify( {'message': 'Account Created Successfully'} ), 200

# Create Recipe
@create_bp.route('/create/recipe', methods=['GET'])
def createRecipe():
    cnx = pymysql.connect(host=config['host'],
                    user=config['user'],
                    password=config['password'],
                    database=config['database'],
                    cursorclass=pymysql.cursors.DictCursor)
    
    name = request.headers.get('recipe-name')
    calories = request.headers.get('recipe-calories')
    ingredients = request.headers.get('recipe-ingredients')
    instructions = request.headers.get('recipe-instructions')
    
    if not name or not calories or not ingredients or not instructions:
        return jsonify( {'error': 
            'Please enter values for name, calories, ingredients, and instructions in the header file'} )
    
    with cnx:
        with cnx.cursor() as cursor:            
            query = f"""
            insert into `recipes`
            (`name`, `calories`, `ingredients`, `instructions`) 
            values ("{name}", "{calories}", "{ingredients}", "{instructions}");
            """
            
            try:
                cursor.execute(query)
            except:
                return {'error': 'SQL syntax error'}
            result = cursor.fetchall()
        
        cnx.commit()
    return jsonify( {'message': 'Recipe Created Successfully'} ), 200
