from flask import request, jsonify
from werkzeug.security import check_password_hash

from . import auth_bp
from database.database import execute_query


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    name = data.get('name')
    pwd = data.get('pwd')

    if not name or not pwd:
        return jsonify({"success": 0, "error": "Missing parameters"}), 400

    try:
        # 获取用户信息
        user = execute_query(
            "SELECT userId, pwd,studentId,teacherId FROM user WHERE name = %s",
            (name,),
            fetch_one=True
        )

        # 对比用户名和密码
        if user and check_password_hash(user['pwd'], pwd):
            return jsonify(
                {"success": 1, "userId": user['userId'], "studentId": user['studentId'],
                 "teacherId": user['teacherId']}), 200
        elif not user:
            return jsonify({"success": 0, "error": "Username does not exist"}), 200
        else:
            return jsonify({"success": 0, "error": "Password incorrect"}), 200

    except Exception as e:
        return jsonify({"success": 0, "error": str(e)}), 500
