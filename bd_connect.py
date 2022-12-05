from psycopg2 import connect
from config import host, user, password, database, port

try:
    mydb = connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=int(port)
    )
    cur = mydb.cursor()
except Exception as e:
    print(port)
    print(host)
    print(user)
    print(password)
    print(database)
    print(e)