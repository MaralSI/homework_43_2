import sqlite3
from db import queries

db = sqlite3.connect("db/online_store.sqlite3")
cursor = db.cursor()


async def sql_create():
    if db:
        cursor.execute(queries.CREATE_TABLE_NAME_PRODUCTS)
        cursor.execute(queries.CREATE_TABLE_PRODUCT_DETAILS)
        cursor.execute(queries.CREATE_TABLE_COLLECTION_PRODUCTS)
        print('База данных подключена')
    db.commit()


async def sql_insert_store(name_product, size, price, product_id, photo):
    cursor.execute(queries.INSERT_NAME_PRODUCTS, (
        name_product,
        size,
        price,
        product_id,
        photo))
    db.commit()


async def sql_insert_detail_products(product_id, category, info_product):
    cursor.execute(queries.INSERT_PRODUCT_DETAILS, (
        product_id,
        category,
        info_product))
    db.commit()
    
async def sql_insert_collection_products(product_id, collection):
    cursor.execute(queries.INSERT_COLLECTION_PRODUCTS, (
        product_id,
        collection))
    db.commit()
    
    