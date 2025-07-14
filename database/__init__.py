from .database import execute_update


def init_db():
    try:
        execute_update("""
            CREATE TABLE IF NOT EXISTS user (
                userId INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL UNIQUE,
                pwd VARCHAR(255) NOT NULL,
                studentId INT,
                teacherId INT
            )
        """)
        # print("Database initialized successfully")
    except Exception as e:
        print(f"Database initialization failed: {str(e)}")
