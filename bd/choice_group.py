import mysql.connector
from bd_connect import mydb, cur

cur: mysql.connector.connection_cext.CMySQLCursor


async def choice_group_name(user_id):
    cur.execute(f'select * from favorite_group where user_id = {user_id}')
    return cur.fetchall()


async def choice_current_group_id(user_id):
    cur.execute(f'select current_group_and_id from favorite_group where user_id = {user_id}')
    return cur.fetchall()