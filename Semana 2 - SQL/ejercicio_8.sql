-- Usando la tabla Ventas:
-- id_venta	  id_producto	  cantidad	  precio_unitario
--    1	         1	             2	           700
--    2	         2	             1	           1000
--    3	         3	             4	           300

-- Escribe consultas SQL para:
-- Calcular el total de ingresos generados.
-- Encontrar el producto con el precio más alto.
-- Obtener el promedio de la cantidad vendida.


CREATE TABLE ventas (
	id_venta INT AUTO_INCREMENT PRIMARY KEY,
    cantidad INT NOT NULL,
    precio_unitario FLOAT NOT NULL,
    id_producto INT,
    FOREIGN KEY (id_producto) REFERENCES prodcutos(id_producto)
);

INSERT INTO ventas (cantidad, precio_unitario, id_producto) 
VALUES 
	(2, 700, 1),
    (1, 1000, 2),
    (4, 300, 3);
    
SELECT * FROM ventas;

SELECT 
	SUM(precio_unitario * cantidad) AS "Ingresos Generados"
FROM ventas;


SELECT 
	MAX(precio_unitario) AS "Precio más alto"
FROM ventas;

SELECT
	ROUND(AVG(cantidad)) AS "Promedio ventas"
FROM ventas;
