import pymysql
from pymysql.cursors import DictCursor

from .config import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB


def get_db_connection():
    """获取数据库连接"""
    return pymysql.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB,
        cursorclass=DictCursor
    )


def execute_query(query, params=None, fetch_one=False):
    """执行查询并返回结果"""
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params or ())
            if fetch_one:
                return cursor.fetchone()
            return cursor.fetchall()
    finally:
        conn.close()


def execute_update(query, params=None):
    """执行更新操作并返回影响的行数"""
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            affected_rows = cursor.execute(query, params or ())
            conn.commit()
            return affected_rows
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()
