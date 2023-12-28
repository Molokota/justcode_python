-- - Создать таблицу 1 к многим: teacher и groups (преподы и группы)
CREATE TABLE groups (
	groups_id serial PRIMARY KEY,
	language varchar(32) NOT NULL
);

CREATE TABLE teacher (
	teacher_id serial PRIMARY KEY,
	name varchar(32) NOT NULL,
	group_teacher_id int REFERENCES groups(groups_id) NOT NULL
);

INSERT INTO groups (language) VALUES
('JavaScript'),
('Python'),
('С++'),
('C#'),
('PHP'),
('Kotlin');

INSERT INTO teacher (name, group_teacher_id) VALUES
('Алексей Иванов', 2),
('Наталья Козлова', 2),
('Дмитрий Смирнов', 1),
('Елена Петрова', 4),
('Марк Цукерберг', 5),
('Антонина Жарова', 3),
('Игорь Соколов', 5);

-- - Создать таблицу 1 к 1: countries и capitals (страны и столицы)
CREATE TABLE countries (
	countries_id serial PRIMARY KEY,
	countries varchar(32) NOT NULL
);

CREATE TABLE capitals (
	capitals_id serial PRIMARY KEY,
	capitals varchar(32) NOT NULL,
	countries_capitals_id int UNIQUE REFERENCES countries(countries_id) NOT NULL
);

INSERT INTO countries(countries) VALUES
('Китай'),
('Индия'),
('Бразилия'),
('Япония'),
('Франция'),
('Великобритания');

INSERT INTO capitals(capitals, countries_capitals_id) VALUES
('Пекин', 1),
('Нью-Дели', 2),
('Бразилиа', 3),
('Токио', 4),
('Париж', 5),
('Лондон', 6);


-- - Создать таблицу многое ко многим: users и courses (пользователи и курсы)
CREATE TABLE users (
	users_id serial PRIMARY KEY,
	user_name varchar(32) NOT NULL
);

CREATE TABLE courses (
	courses_id serial PRIMARY KEY,
	courses varchar(32) NOT NULL
);

CREATE TABLE users_courses (
	users_id int REFERENCES users(users_id),
	courses_id int REFERENCES courses(courses_id),
	PRIMARY KEY (users_id, courses_id)
);

INSERT INTO users(user_name) VALUES
('Газиза'),
('Павел'),
('Александр'),
('Бауыржан'),
('Бибигуль'),
('Константин');

INSERT INTO courses(courses) VALUES
('JavaScript'),
('Python'),
('С++'),
('C#'),
('PHP'),
('Kotlin');

INSERT INTO users_courses(users_id, courses_id) VALUES
(1, 1),
(1, 5),
(1, 6),
(2, 2),
(3, 6),
(3, 4),
(4, 2),
(4, 1),
(5, 3),
(5, 5),
(6, 3),
(6, 2);