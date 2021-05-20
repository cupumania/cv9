import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
          host="localhost",
          database="_cv9_test",
          user="pras",
          password="prs")

    if conn.is_connected():
        cursor = conn.cursor()
        qry = "SELECT user_id,token,(token_updated_at-token_created_at) AS token_expires FROM users WHERE user_id=1;"
        result = cursor.execute(qry)
        print(result)

except Error as e:
    print("Error while connecting to MySQL:", e)
finally:
    if (conn.is_connected()):
        cursor.close()
        conn.close()
        print("MySQL connection is closed")
