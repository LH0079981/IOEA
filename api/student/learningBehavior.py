from . import student_bp
from flask import jsonify


@student_bp.route('/learningBehavior', methods=['GET'])
def learningBehavior(student_id):
    return jsonify({"student_id": student_id, "learningHour": 134679}), 200
