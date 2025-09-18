import mysql.connector  # type: ignore

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        database="product_db",
        user="root",
        password="kol@mind1"
    )
    return conn

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            price DECIMAL(10,2) NOT NULL,
            stock INT NOT NULL
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()







'''import mysql.connector #type: ignore

def get_connection():
    conn = mysql.connector.connect(
        host='localhost',
        database="product_db",
        user="root",
        password="root"
    )
    return conn


CREATE DATABASE product_db;
USE product_db;
 
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10,2),
    stock INT
);
'''
