-- 1 часть:
-- 1. Выбрать все заказы из стран France, Austria, Spain
SELECT * FROM orders
WHERE ship_country = 'France' or ship_country = 'Austria' or ship_country = 'Spain';

-- 2. Выбрать все заказы, отсортировать по required_date (по убыванию) и отсортировать по дате отгрузке (по возрастанию)
SELECT * FROM orders
ORDER BY required_date;

-- 3. Выбрать минимальное кол-во  единиц товара среди тех продуктов, которых в продаже более 30 единиц.
SELECT * FROM products
WHERE units_in_stock <= 30
ORDER BY units_in_stock DESC;

-- 4. Выбрать максимальное кол-во единиц товара среди тех продуктов, которых в продаже более 30 единиц.
SELECT * FROM products
WHERE units_in_stock > 30
ORDER BY units_in_stock DESC;

-- 5. Найти среднее значение дней уходящих на доставку с даты формирования заказа в USA
SELECT AVG(required_date - order_date) AS days_delivery FROM orders 
WHERE ship_country = 'USA';

-- 6. Найти сумму, на которую имеется товаров (кол-во * цену) причём таких, которые планируется продавать и в будущем (см. на поле discontinued)
SELECT *, unit_price * units_in_stock AS all_money FROM products 
WHERE discontinued > 0 and units_in_stock > 0;



-- 2 часть:
-- 7. Выбрать все записи заказов в которых наименование страны отгрузки начинается с 'U'
SELECT * FROM orders
WHERE ship_country LIKE 'U%';

-- 8. Выбрать записи заказов (включить колонки идентификатора заказа, идентификатора заказчика, веса и страны отгузки), которые должны быть отгружены в страны имя которых начинается с 'N', отсортировать по весу (по убыванию) и вывести только первые 10 записей.
SELECT order_id, customer_id, freight, ship_country FROM orders
WHERE ship_country LIKE 'N%'
ORDER BY freight DESC LIMIT 10;

-- 9. Выбрать записи работников (включить колонки имени, фамилии, телефона, региона) в которых регион неизвестен
SELECT first_name, last_name, home_phone, region FROM employees
WHERE region IS NULL;

-- 10. Подсчитать кол-во заказчиков регион которых известен
SELECT COUNT(*) FROM orders
WHERE ship_region IS NOT NULL;

-- 11. Подсчитать кол-во поставщиков в каждой из стран и отсортировать результаты группировки по убыванию кол-ва
SELECT country, COUNT(*) FROM suppliers
GROUP BY country
ORDER BY country DESC;

-- 12. Подсчитать суммарный вес заказов (в которых известен регион) по странам, затем отфильтровать по суммарному весу (вывести только те записи где суммарный вес больше 2750) и отсортировать по убыванию суммарного веса.
SELECT ship_region, SUM(freight), COUNT(*) FROM orders
WHERE ship_region IS NOT NULL
GROUP BY ship_region
HAVING SUM(freight) > 2750 ;

-- 13. Выбрать все уникальные страны заказчиков и поставщиков и отсортировать страны по возрастанию
SELECT DISTINCT ship_country FROM orders
ORDER BY ship_country ASC;
SELECT DISTINCT country FROM suppliers
ORDER BY country ASC;

-- 14. Выбрать такие страны в которых "зарегистированы" одновременно и заказчики и поставщики и работники.
-- SELECT country FROM customers
-- UNION
-- SELECT country FROM suppliers
-- UNION
-- SELECT country FROM employees
-- GROUP BY country
-- ORDER BY country ASC;

-- 15. Выбрать такие страны в которых "зарегистированы" одновременно заказчики и поставщики, но при этом в них не "зарегистрированы" работники.
-- SELECT country FROM customers
-- UNION
-- SELECT country FROM suppliers
-- GROUP BY country
-- ORDER BY country ASC;
