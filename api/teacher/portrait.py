from . import teacher_bp
from flask import jsonify


@teacher_bp.route('/portrait', methods=['GET'])
def get_student_portrait(teacher_id):
    return jsonify({"teacher_id": teacher_id}), 200
