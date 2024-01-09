-- 1. Найти заказчиков, не сделавших ни одного заказа. Вывести имя заказчика и order_id.
SELECT customers.contact_name, orders.order_id
FROM customers
JOIN orders ON customers.customer_id = orders.customer_id
WHERE orders.order_id IS NULL;
-- Не смог вывести, получется пустой список в первом задании

-- 2. Переписать предыдущий запрос, использовав симметричный вид джойна (подсказка: речь о LEFT и RIGHT).
SELECT contact_name, order_id  FROM  customers
LEFT JOIN orders ON orders.customer_id = customers.customer_id
WHERE orders.order_id IS NULL;

SELECT contact_name, order_id FROM  orders
RIGHT JOIN customers ON customers.customer_id = orders.customer_id
WHERE orders.order_id IS NULL;