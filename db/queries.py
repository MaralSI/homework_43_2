

CREATE_TABLE_PRODUCT_DETAILS = """
    CREATE TABLE IF NOT EXISTS product_details
    (id INTERGER PRIMARY KEY AUTOINTEGER,
    name_product VARCHAR(255),
    size VACHAR(255)
    price VACHAR(255)
    photo TEXT
    product_id INTEGER
    category VACHAR(255)
    info_product TEXT
    )
"""


INSERT_STORE = """
   INSERT_INFO online_store(name_product, size, price, product_id, category, info_product, photo)
    VALUES(?, ?, ?, ?, ?, ?, ?)

"""