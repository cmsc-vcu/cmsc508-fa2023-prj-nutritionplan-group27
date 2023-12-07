from flask import Flask, redirect, url_for, request, jsonify, Blueprint
import pymysql.cursors
from flask_cors import CORS

delete_bp = Blueprint('delete_bp', __name__)

config = {
    'user': '23FA_dellimorez',
    'password': 'Shout4_dellimorez_GOME',
    'host': 'cmsc508.com',
    'database': '23FA_groups_group27',
    'raise_on_warnings': True
}

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
            
            cursor.execute(query)
            result = cursor.fetchall()
            
            print(result)
        cnx.commit()
    
    return {'results': 'User deleted successfully'}