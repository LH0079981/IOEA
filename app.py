from flask import Flask
from flask_cors import CORS

from database import init_db
from api.auth import auth_bp
from api.user import user_bp
from api.student import student_bp
from api.teacher import teacher_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)
app.register_blueprint(student_bp)
app.register_blueprint(teacher_bp)

if __name__ == '__main__':
    # init_db()
    app.run(host='0.0.0.0', port=3000, debug=True)
