CREATE_TABLE_NAME_PRODUCTS = """
    CREATE TABLE IF NOT EXISTS online_store
    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name_product VARCHAR(255),
    size VARCHAR(255),
    price VARCHAR(255), 
    product_id INTEGER,
    photo TEXT
    )
"""

INSERT_STORE = """
    INSERT INTO online_store(name_product, size, price, product_id, photo)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""


CREATE_TABLE_PRODUCT_DETAILS = """
    CREATE TABLE IF NOT EXISTS product_details
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id VARCHAR(255),
    category VARCHAR(255),
    info_product VARCHAR(255)
    )
"""

INSERT_DETAIL_PRODUCTS = """
    INSERT INTO product_detailS(product_id, category, info_product)
    VALUES (?, ?, ?)
"""

CREATE_TABLE_COLLECTION_PRODUCTS = """
    CREATE TABLE IF NOT EXISTS collection_products
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id VARCHAR(255),
    collection VARCHAR(255)
    )
"""

INSERT_DETAIL_PRODUCTS = """
    INSERT INTO collection_products(product_id, collection_products)
    VALUES (?, ?)
"""