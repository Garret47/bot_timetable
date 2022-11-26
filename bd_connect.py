from mysql.connector import connect
from config import host, user, password, database

try:
    mydb = connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    cur = mydb.cursor()
except Exception as e:
    print(e)