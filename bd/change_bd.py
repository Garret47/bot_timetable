import psycopg2
from bd_connect import mydb, cur
from .choice_group import choice_group_name

cur: mysql.connector.connection_cext.CMySQLCursor


async def insert_group_name(user_id, group):
    cur.execute(f'insert into favorite_group values ({user_id}, "{group}")')
    mydb.commit()


async def update_group_name(user_id, groups, group=None):
    if group:
        cur.execute(
            f'update favorite_group set group_name = concat("{groups}", " ", "{group}") where user_id={user_id}')
    else:
        cur.execute(
            f'update favorite_group set group_name = "{groups}" where user_id={user_id}')
    mydb.commit()


async def delete_group_name(user_id):
    cur.execute(f'delete from favorite_group where user_id = {user_id};')
    mydb.commit()


async def update_group_current_id(user_id, group_id, name_group):
    cur.execute(f'update favorite_group set current_group_and_id = concat("{group_id}", " ", "{name_group}") '
                f'where user_id={user_id}')
    mydb.commit()