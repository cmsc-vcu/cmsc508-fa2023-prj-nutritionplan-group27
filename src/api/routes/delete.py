from flask import Flask, redirect, url_for, request, jsonify, Blueprint
import pymysql.cursors
import os
from flask_cors import CORS

delete_bp = Blueprint('delete_bp', __name__)

from dotenv import dotenv_values
config = dotenv_values(".env")

@delete_bp.route('/delete/user', methods=['GET'])
def deleteUser():
    cnx = pymysql.connect(host=config['host'],
                    user=config['user'],
                    password=config['password'],
                    database=config['database'],
                    cursorclass=pymysql.cursors.DictCursor)
    
    username = request.headers.get('username', default=None)
    password = request.headers.get('password', default=None)
    
    with cnx:
        with cnx.cursor() as cursor:
            query=f"""
            DELETE FROM
            users
            WHERE username = '{username}';
            """
            
            try:
                cursor.execute(query)
            except:
                return {'error': 'SQL syntax error'}
            result = cursor.fetchall()
            
            print(result)
        cnx.commit()
    
    return {'results': 'User deleted successfully'}