import mysql.connector
import time
import os

DB_HOST = os.getenv("DB_HOST", "db")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "root")
DB_NAME = os.getenv("DB_NAME", "cerveceria")

TABLES = [
    """
    CREATE TABLE IF NOT EXISTS tipos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS categorias (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS proveedores (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        telefono VARCHAR(50),
        direccion VARCHAR(200),
        email VARCHAR(100)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS productos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        precio DECIMAL(10,2) NOT NULL,
        tipo_id INT NOT NULL,
        categoria_id INT NOT NULL,
        proveedor_id INT,
        FOREIGN KEY (tipo_id) REFERENCES tipos(id),
        FOREIGN KEY (categoria_id) REFERENCES categorias(id),
        FOREIGN KEY (proveedor_id) REFERENCES proveedores(id)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS usuarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(100) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL
    );
    """,
    """
    INSERT IGNORE INTO usuarios (username, password)
    VALUES ('admin', '$2b$12$eVvxI8pGgAb9YSEuxsjj0O6XglN6E466zvWXTmFRrM8Nl1N8MPmFi');
    """
]

def create_database():
    for i in range(10):
        try:
            conn = mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD
            )
            cursor = conn.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            conn.close()
            return
        except:
            print("Esperando a MySQL...")
            time.sleep(3)

def init_tables():
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = conn.cursor()
    for t in TABLES:
        cursor.execute(t)
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_database()
    init_tables()
    print("Base de datos lista ✔️")
