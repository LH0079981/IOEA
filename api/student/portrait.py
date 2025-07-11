from . import student_bp
from flask import jsonify


@student_bp.route('/portrait', methods=['GET'])
def get_student_portrait(student_id):

    return jsonify({"student_id": student_id}), 200
