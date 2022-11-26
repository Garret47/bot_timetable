import mysql.connector
from bd_connect import mydb, cur
from .choice_group import choice_group_name

cur: mysql.connector.connection_cext.CMySQLCursor


async def insert_group_name(user_id, group):
    cur.execute(f'insert into favorite_group values ({user_id}, "{group}")')
    mydb.commit()


async def update_group_name(user_id, groups, group):
    cur.execute(f'update favorite_group set group_name = concat("{groups[0][1]}", " ", "{group}") where user_id={user_id}')
    mydb.commit()
