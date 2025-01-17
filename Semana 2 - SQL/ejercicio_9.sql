-- Subconsultas: Usando las tablas anteriores, escribe una consulta para encontrar los nombres de los productos cuyo precio unitario 
-- sea mayor que el precio promedio de todos los productos.
use tienda;

SELECT * FROM ventas;
SELECT * FROM prodcutos;

SELECT 
	p.nombre_producto AS "Productos mayor al precio promedio",
    v.precio_unitario AS "Precio",
    (SELECT ROUND(AVG(precio_unitario),2) FROM ventas) AS "Precio promedio"
FROM
	prodcutos p
INNER JOIN
	ventas v
ON
	p.id_producto = v.id_producto
WHERE
	v.precio_unitario > (SELECT AVG(precio_unitario) FROM ventas);