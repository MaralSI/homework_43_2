<<<<<<< HEAD
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
    INSERT INTO online_store(name_product, size, price,  productid, photo)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""


CREATE_TABLE_PRODUCT_DETAIL = """
    CREATE TABLE IF NOT EXISTS products_detail
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    productid VARCHAR(255),
    category VARCHAR(255),
    infoproduct VARCHAR(255)
    )
"""

INSERT_DETAIL_PRODUCTS = """
    INSERT INTO products_detail(productid, category, infoproduct)
    VALUES (?, ?, ?)
=======


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

>>>>>>> 3adc3855d84a08f4068db3930f774eb83f99f35a
"""