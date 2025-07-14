from flask import request, jsonify
from werkzeug.security import generate_password_hash

from . import auth_bp
from database.database import execute_query, execute_update


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data.get('name')
    pwd = data.get('pwd')

    if not name or not pwd:
        return jsonify({"success": 0, "error": "Missing parameters"}), 400

    try:
        # 检查用户名是否存在
        existing_user = execute_query(
            "SELECT userId FROM user WHERE name = %s AND status = 1",
            (name,),
            fetch_one=True
        )

        if existing_user:
            return jsonify({"success": 0, "error": "Duplicate username"}), 200

        # 生成密码哈希
        hashed_pwd = generate_password_hash(pwd)

        # 插入新用户
        execute_update(
            "INSERT INTO user (status, name, pwd) VALUES (1, %s, %s)",
            (name, hashed_pwd)
        )

        # 获取新用户ID
        new_user = execute_query(
            "SELECT userId FROM user WHERE name = %s AND status = 1",
            (name,),
            fetch_one=True
        )
        return jsonify({"success": 1, "userId": new_user['userId']}), 201

    except Exception as e:
        return jsonify({"success": 0, "error": str(e)}), 500
