import sqlite3

DB_NAME = 'products.db'

def create_database():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            link TEXT NOT NULL UNIQUE,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    connection.commit()
    connection.close()

def save_product(title, link, description):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("""
        INSERT OR IGNORE INTO products
        (title, link, description)
        VALUES (?, ?, ?)
    """, (title, link, description))
    connection.commit()
    connection.close()


def get_products():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("""
        SELECT id, title, link, description, created_at
        FROM products
        ORDER BY id DESC
    """)
    products = cursor.fetchall()
    connection.close()
    return products
create_database()