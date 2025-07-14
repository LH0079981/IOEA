from .database import execute_update


def init_db():
    try:
        execute_update("""
            CREATE TABLE IF NOT EXISTS user (
                userId INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR NOT NULL UNIQUE,
                pwd VARCHAR NOT NULL,
                studentId INT,
                teacherId INT
            )
        """)
        print("Database initialized successfully")
    except Exception as e:
        print(f"Database initialization failed: {str(e)}")
