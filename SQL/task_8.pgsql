-- Вывести продукты количество которых в продаже меньше самого малого среднего 
-- количества продуктов в деталях заказов (группировка по product_id). 
-- Результирующая таблица должна иметь колонки product_name и units_in_stock

SELECT DISTINCT product_name, units_in_stock  FROM products 
JOIN order_details USING (product_id)
WHERE order_details.quantity < (SELECT AVG(quantity) FROM order_details);


-- Вывести все товары (уникальные названия продуктов), которых заказано 
-- ровно 10 единиц (конечно же, это можно решить и без подзапроса).

SELECT DISTINCT product_name FROM products 
JOIN order_details USING (product_id)
WHERE order_details.quantity = 10

