import mysql.connector

def get_db_connection():
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root@123',
        database='moviedb',
        auth_plugin='mysql_native_password',
    )
    return db
