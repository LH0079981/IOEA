from flask import request, jsonify

from . import user_bp
from database.database import execute_query, execute_update


@user_bp.route('/update_studentId', methods=['POST'])
def update_studentId():
    data = request.get_json()
    userId = data.get('userId')
    studentId = data.get('studentId')
    print(data)

    if not userId or not studentId:
        return jsonify({"success": 0, "error": "Missing parameters"}), 400

    try:
        # 验证用户是否存在
        user = execute_query(
            "SELECT userId FROM user WHERE userId = %s",
            (userId,),
            fetch_one=True
        )

        if not user:
            return jsonify({"success": 0, "error": "User not found"}), 404

        execute_update(
            "UPDATE user SET studentId = %s WHERE userId = %s",
            (studentId, userId)
        )

        return jsonify({"success": 1, "message": "studentId updated"}), 200

    except Exception as e:
        return jsonify({"success": 0, "error": str(e)}), 500
