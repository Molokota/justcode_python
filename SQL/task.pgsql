-- 1) Создать таблицу publisher
-- publisher_id - уникальный идентификатор
-- name - название публикации
-- city - город (НЕОБЯЗАТЕЛЬНОЕ ПОЛЕ)

CREATE TABLE publisher 
(
    publisher_id int PRIMARY KEY,
    name varchar(64) NOT NULL,
    city varchar(64)
);

INSERT INTO publisher VALUES
(1, 'Новое литературное обозрение', NULL),
(2, 'Эксмо', 'Санкт-Петербург'),
(3, 'АСТ', 'Казань'),
(4, 'Рипол Классик', NULL),
(5, 'МИФ', 'Казань'),
(6, 'Центрполиграф', 'Самара'),
(7, 'Альпина Паблишер', NULL), 
(8, 'Азбука-Аттикус', 'Казань'),
(9, 'Детгиз', 'Ростов-на-Дону'),
(10, 'Московский Рабочий', 'Владивосток');


-- 2) Создать таблицу book с полями:
-- book_id - уникальный идентификатор
-- author - автор книги
-- title - название книги
-- page_count - сколько страниц в книге (НЕОБЯЗАТЕЛЬНОЕ ПОЛЕ)

CREATE TABLE book 
(
    book_id int PRIMARY KEY,
    author varchar(64) NOT NULL,
    title varchar(64) NOT NULL,
    page_count int 
);

INSERT INTO book VALUES 
(1, 'Лев Толстой', 'Приключения в космосе', 200),
(2, 'Абай Кунанбаев', 'Тайны древнего леса', 150),
(3, 'Алексей Смирнов', 'Загадочный город', NULL),
(4, 'Лев Толстой', 'В поисках времени', 400),
(5, 'Андрей Новиков',  'Стратегии программирования', 200),
(6, 'Абай Кунанбаев',  'Тайные знания веков', 280),
(7, 'Дмитрий Лебедев',  'Путеводитель по новым технологиям', 150),
(8, 'Лев Толстой',  'Любовь под парусами', 230),
(9, 'Сергей Краснов',  'Энциклопедия науки и исследований', NULL),
(10, 'Абай Кунанбаев',  'Секреты кулинарии великих шеф-поваров', 100);

-- DROP TABLE book;
-- DROP TABLE publisher;

-- 3) Выполнить выборку из таблицы публикаторов
-- - С уникальными городами
SELECT DISTINCT city FROM publisher 
WHERE NOT city = 'NULL'

-- 4) Выполнить выборку из таблицы книги:
-- - Где кол-во страниц не превышает 250
SELECT * FROM book
WHERE page_count <= 250;

-- - Где автор это Абай Кунанбаев И кол-во страниц не первышает 150
SELECT * FROM book
WHERE author = 'Абай Кунанбаев' and page_count <= 150;

-- Посчитать кол-во книг где автор Лев Толстой
SELECT COUNT(*) FROM book
WHERE author = 'Лев Толстой';
