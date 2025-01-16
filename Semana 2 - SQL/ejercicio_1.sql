-- 1. Crear una base de datos llamada tienda_online.
-- 2. Crea una tabla productos con las siguientes columnas: id, nombre, precio, stock.
-- 3. Inserta al menos 5 registros en la tabla productos. 


-- 1. 
CREATE DATABASE tienda_online;
USE sql_avanzado;


-- 2. 
CREATE TABLE productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL
);


-- 3. 
INSERT INTO productos (nombre, precio, stock)
VALUES 
    ('Laptop', 1200.50, 5),
    ('Mouse', 25.00, 50),
    ('Teclado', 75.00, 20),
    ('Monitor', 300.00, 10),
    ('Cargador', 45.00, 15);

