import sqlite3
from db import queries

<<<<<<< HEAD
db = sqlite3.connect("db/online_store.sqlite3")
=======
db = sqlite3.connect("db/product_details.sqlite3")
>>>>>>> 3adc3855d84a08f4068db3930f774eb83f99f35a
cursor = db.cursor()


async def sql_create():
    if db:
<<<<<<< HEAD
        cursor.execute(queries.CREATE_TABLE_NAME_PRODUCTS)
=======
>>>>>>> 3adc3855d84a08f4068db3930f774eb83f99f35a
        cursor.execute(queries.CREATE_TABLE_PRODUCT_DETAILS)
        print('База данных подключена')
    db.commit()

<<<<<<< HEAD

async def sql_insert_store(name_product, size, price, productid, photo):
=======
async def sql_insert_store(name_product, size, price, product_id, category, info_product, photo):
>>>>>>> 3adc3855d84a08f4068db3930f774eb83f99f35a
    cursor.execute(queries.INSERT_STORE, (
        name_product,
        size,
        price,
<<<<<<< HEAD
        productid,
        photo))
    db.commit()


async def sql_insert_detail_products(productid, category, infoproduct):
    cursor.execute(queries.INSERT_DETAIL_PRODUCTS, (
        productid,
        category,
        infoproduct))
=======
        product_id,
        category,
        info_product,
        photo))
>>>>>>> 3adc3855d84a08f4068db3930f774eb83f99f35a
    db.commit()