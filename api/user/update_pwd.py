from flask import request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash

from . import user_bp
from database.database import execute_query, execute_update


@user_bp.route('/update_pwd', methods=['POST'])
def update_pwd():
    data = request.get_json()
    userId = data.get('userId')
    old_pwd = data.get('old_pwd')
    new_pwd = data.get('new_pwd')

    if not userId or not old_pwd or not new_pwd:
        return jsonify({"success": 0, "error": "Missing parameters"}), 400

    try:
        # 验证用户是否存在
        user = execute_query(
            "SELECT userId,name,pwd FROM user WHERE userId = %s",
            (userId,),
            fetch_one=True
        )

        if not user:
            return jsonify({"success": 0, "error": "User not found"}), 404

        # 验证旧密码
        if not check_password_hash(user['pwd'], old_pwd):
            return jsonify({"success": 0, "error": "Invalid old password"}), 401

        # 生成新密码哈希
        new_hashed_pwd = generate_password_hash(new_pwd)

        # 更新密码
        execute_update(
            "UPDATE user SET pwd = %s WHERE userId = %s",
            (new_hashed_pwd, userId)
        )

        return jsonify({"success": 1, "message": "Password updated"}), 200

    except Exception as e:
        return jsonify({"success": 0, "error": str(e)}), 500
