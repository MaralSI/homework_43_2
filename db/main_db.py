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


async def sql_insert_store(name_product, size, price, productid, photo):
    cursor.execute(queries.INSERT_NAME_PRODUCTS, (
        name_product,
        size,
        price,
        productid,
        photo))
    db.commit()


async def sql_insert_detail_products(productid, category, infoproduct):
    cursor.execute(queries.INSERT_PRODUCT_DETAILS, (
        productid,
        category,
        infoproduct))
    db.commit()
    
async def sql_insert_collection_products(productid, collection):
    cursor.execute(queries.INSERT_COLLECTION_PRODUCTS, (
        productid,
        collection))
    db.commit()
    
    