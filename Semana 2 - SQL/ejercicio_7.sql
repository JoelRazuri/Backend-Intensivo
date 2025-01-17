CREATE DATABASE tienda;
USE tienda;
-- Dadas las siguientes tablas:
-- Productos:
-- id_producto	nombre_producto	 id_categoria
--    1	             Laptop	          1
--    2	             Smartphone	      2
--    3	             Televisor	      3

-- Categorías:
-- id_categoria	   nombre_categoria
--    1	             Electrónica
--    2	             Tecnología
--    3	             Entretenimiento

-- Escribe una consulta que devuelva el nombre del producto junto con el nombre de su categoría usando un INNER JOIN.

CREATE TABLE categorias(
	id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre_categoria VARCHAR(100) NOT NULL
);


CREATE TABLE prodcutos(
	id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre_producto VARCHAR(100) NOT NULL,
    id_categoria INT,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
);


INSERT INTO categorias (nombre_categoria) VALUES
	("Electrónica"),
    ("Tecnología"),
    ("Entretenimiento");


INSERT INTO prodcutos (nombre_producto, id_categoria) VALUES
	("Laptop", 1),
    ("Smartphone", 1),
    ("Televisor", 2),
    ("PC de Escritorio", 1),
    ("Iphone XS", 2),
    ("Play Station 5", 3);


SELECT 
	p.nombre_producto AS producto,
    c.nombre_categoria AS categoria
FROM 
	prodcutos p
INNER JOIN
	categorias c
ON 
	p.id_categoria = c.id_categoria;


