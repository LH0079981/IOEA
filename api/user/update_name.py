from flask import request, jsonify

from . import user_bp
from database.database import execute_query, execute_update


@user_bp.route('/update_name', methods=['POST'])
def update_name():
    data = request.get_json()
    userid = data.get('userid')
    new_name = data.get('new_name')

    if not userid or not new_name:
        return jsonify({"success": 0, "errr": "Missing parameters"}), 400

    try:
        # 验证用户是否存在
        user = execute_query(
            "SELECT userid,name,pwd FROM user WHERE userid = %s",
            (userid,),
            fetch_one=True
        )

        if not user:
            return jsonify({"success": 0, "error": "User not found"}), 404

        # 检测用户名是否重复
        existing_user = execute_query(
            "SELECT userid,name,pwd FROM user WHERE name = %s",
            (new_name,),
            fetch_one=True
        )

        if existing_user:
            return jsonify({"success": 0, "error": "Duplicate username"}), 200

        affected_rows = execute_update(
            "UPDATE user SET name = %s WHERE userid = %s",
            (new_name, userid)
        )

        return jsonify({"success": 1, "message": "Username updated"}), 200

    except Exception as e:
        return jsonify({"success": 0, "error": str(e)}), 500
