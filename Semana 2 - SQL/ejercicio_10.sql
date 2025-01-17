-- GROUP BY y HAVING: Usando la tabla Ventas, agrupa las ventas por id_producto y calcula la suma total de ingresos por producto. 
-- Muestra solo los productos cuyos ingresos totales sean mayores a 1000.

SELECT * FROM ventas;

SELECT 
	id_producto,
    SUM(cantidad * precio_unitario) AS "Ingresos Totales"
FROM
	ventas
GROUP BY
	id_producto
HAVING
    SUM(cantidad * precio_unitario) > 1000;
