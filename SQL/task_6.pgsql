--  Доделать практику
-- -- Создать функцию по подсчету количества продуктов по данным поставщика
CREATE OR REPLACE FUNCTION get_quantity(id INTEGER) RETURNS BIGINT AS $$
    SELECT COUNT(*) FROM products
    WHERE supplier_id = id;
$$ LANGUAGE SQL;

SELECT * FROM get_quantity(24);


-- Создать функцию которая показывает заказы за определенный период
CREATE OR REPLACE FUNCTION get_quantity(d_order DATE) RETURNS SETOF orders AS $$
    SELECT * FROM orders
    WHERE order_date = d_order;
$$ LANGUAGE SQL;

SELECT * FROM get_quantity('1996-07-08'::date);

-- ДЗ
-- -- - Создать функцию, которая принимает на вход имя сотрудника и возвращает всю информацию о нем из таблицы employees
CREATE OR REPLACE FUNCTION employees_first_name(first_name_1 VARCHAR) RETURNS SETOF employees AS $$
    SELECT * FROM employees
    WHERE first_name = first_name_1;
$$ LANGUAGE SQL;

SELECT * FROM employees_first_name('Nancy')


-- - Создайте функцию, которая принимает на вход идентификатор сотрудника и новое имя, а затем обновляет имя в таблице employees
CREATE OR REPLACE FUNCTION update_employees(employees_id INT, employees_first_name VARCHAR) RETURNS void as $$
    UPDATE employees
    SET first_name = employees_first_name
    WHERE employee_id = employees_id
$$ LANGUAGE SQL;

SELECT update_employees(9, 'ooooooo');

