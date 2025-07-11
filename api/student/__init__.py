from flask import Blueprint

student_bp = Blueprint('student', __name__, url_prefix='/api/student/<student_id>')

from . import learningBehavior, portrait
