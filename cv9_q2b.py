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
        qry = "SELECT a.user_id,name,institution_name,entry_type FROM users a "
        qry += "LEFT JOIN user_balance b ON a.user_id = b.user_id "
        qry += "GROUP BY institution_name, user_id;"

        result = cursor.execute(qry)
        print(result)

except Error as e:
    print("Error while connecting to MySQL:", e)
finally:
    if (conn.is_connected()):
        cursor.close()
        conn.close()
        print("MySQL connection is closed")
