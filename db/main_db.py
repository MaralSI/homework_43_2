import sqlite3
from db import queries

db = sqlite3.connect("db/product_details.sqlite3")
cursor = db.cursor()


async def sql_create():
    if db:
        cursor.execute(queries.CREATE_TABLE_PRODUCT_DETAILS)
        print('База данных подключена')
    db.commit()

async def sql_insert_store(name_product, size, price, product_id, category, info_product, photo):
    cursor.execute(queries.INSERT_STORE, (
        name_product,
        size,
        price,
        product_id,
        category,
        info_product,
        photo))
    db.commit()