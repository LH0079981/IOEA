from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash

from database.database import execute_query
from . import auth_bp


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    name = data.get('name')
    pwd = data.get('pwd')

    if not name or not pwd:
        return jsonify({"pass": 0, "error": "Missing parameters"}), 400

    try:
        # 获取用户信息
        user = execute_query(
            "SELECT userid, pwd FROM user WHERE name = %s",
            (name,),
            fetch_one=True
        )
        # 对比用户名和密码
        if user and check_password_hash(user['pwd'], pwd):
            return jsonify({"pass": 1, "userid": user['userid']}), 200
        elif not user:
            return jsonify({"pass": 0, "error": "Username does not exist"}), 200
        else:
            return jsonify({"pass": 0, "error": "Password incorrect"}), 200

    except Exception as e:
        return jsonify({"pass": 0, "error": str(e)}), 500
