-- Crea una tabla categorias con las siguientes columnas:

-- id_categoria: INT, clave primaria, autoincremental.
-- nombre_categoria: VARCHAR(50), no nulo.

-- Agrega una columna id_categoria a la tabla productos como clave foránea y realiza un JOIN para mostrar los productos junto con 
-- su categoría.

CREATE TABLE categorias (
	id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre_categoria VARCHAR(50) NOT NULL
);


INSERT INTO categorias (nombre_categoria) VALUES 
    ('Electrónica'),
    ('Accesorios'),
    ('Periféricos');


ALTER TABLE productos ADD id_categoria INT;

SELECT 
    p.nombre AS producto, 
    c.nombre_categoria AS categoria, 
    p.precio, 
    p.stock
FROM 
    productos p
JOIN 
    categorias c
ON 
    p.id_categoria = c.id_categoria;







