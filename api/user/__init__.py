from flask import Blueprint

user_bp = Blueprint('user', __name__, url_prefix='/api/user')

from . import update_name,update_pwd,update_studentId,update_teacherId