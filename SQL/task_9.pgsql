-- -- Создать базу данных со следующими таблицами:
-- DROP DATABASE univer_2;
-- CREATE DATABASE UNIVER_2;

-- -- -  Таблица 'settings' с полями
CREATE TABLE settings (
id_settings INT PRIMARY KEY,
on_off_notifications BOOLEAN DEFAULT TRUE,
theme_black_white_grey VARCHAR(64)
);

-- -- - Таблица 'accounts' с полями:
CREATE TABLE accounts (
id_accounts INT PRIMARY KEY,
id_settings INT,
creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
update_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (id_settings) REFERENCES settings (id_settings)
);


-- -- - Таблица 'students' с полями:
CREATE TABLE students (
id_students INT PRIMARY KEY,
id_accounts INT,
creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
update_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
first_name VARCHAR(64) NOT NULL,
last_name VARCHAR(64) NOT NULL,
birth_data DATE,
gender  VARCHAR(64) NOT NULL,
activity BOOLEAN DEFAULT TRUE,
FOREIGN KEY (id_accounts) REFERENCES accounts (id_accounts)
);

-- -- - Таблица 'courses' с полями:
CREATE TABLE courses (
id_courses INT PRIMARY KEY,
id_students INT,
creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
update_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
course_name VARCHAR(64) NOT NULL,
description_course VARCHAR(1000),
date_start_course DATE,
date_end_course DATE CHECK (date_end_course > date_start_course),
FOREIGN KEY (id_students) REFERENCES students (id_students)
);

-- -- - Таблица 'teachers' с полями:
CREATE TABLE teacher (
id_teacher INT PRIMARY KEY,
id_accounts INT,
id_courses INT,
creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
update_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
first_name VARCHAR(64) NOT NULL,
last_name VARCHAR(64) NOT NULL,
birth_data DATE CHECK (birth_data < '2006-01-01'),
gender  VARCHAR(64) NOT NULL,
activity BOOLEAN DEFAULT TRUE,
FOREIGN KEY (id_accounts) REFERENCES accounts (id_accounts),
FOREIGN KEY (id_courses) REFERENCES courses (id_courses)
);

-- -- - Связи в базе:
-- --     - Таблица 'students' и таблица 'accounts' - One to One
-- --     - Таблица 'teachers' и таблица 'accounts' - One to One
-- --     - Таблица 'accounts' и таблица 'settings' - One to One
-- --     - Таблица 'courses' и таблица 'students' - Many to Many
-- --     - Таблица 'teachers' и таблица 'courses' - One to Many
    
-- -- -  Таблица 'settings'
insert into settings (id_settings, on_off_notifications, theme_black_white_grey) values (1, false, 'Puce');
insert into settings (id_settings, on_off_notifications, theme_black_white_grey) values (2, false, 'Pink');
insert into settings (id_settings, on_off_notifications, theme_black_white_grey) values (3, true, 'Pink');
insert into settings (id_settings, on_off_notifications, theme_black_white_grey) values (4, false, 'Crimson');
insert into settings (id_settings, on_off_notifications, theme_black_white_grey) values (5, true, 'Maroon');
insert into settings (id_settings, on_off_notifications, theme_black_white_grey) values (6, false, 'Violet');
insert into settings (id_settings, on_off_notifications, theme_black_white_grey) values (7, true, 'Blue');
insert into settings (id_settings, on_off_notifications, theme_black_white_grey) values (8, false, 'Teal');
insert into settings (id_settings, on_off_notifications, theme_black_white_grey) values (9, false, 'Mauv');
insert into settings (id_settings, on_off_notifications, theme_black_white_grey) values (10, true, 'Blue');
-- -- - Таблица 'accounts'
insert into accounts (id_accounts, id_settings) values (1, 1);
insert into accounts (id_accounts, id_settings) values (2, 2);
insert into accounts (id_accounts, id_settings) values (3, 3);
insert into accounts (id_accounts, id_settings) values (4, 4);
insert into accounts (id_accounts, id_settings) values (5, 5);
insert into accounts (id_accounts, id_settings) values (6, 6);
insert into accounts (id_accounts, id_settings) values (7, 7);
insert into accounts (id_accounts, id_settings) values (8, 8);
insert into accounts (id_accounts, id_settings) values (9, 9);
insert into accounts (id_accounts, id_settings) values (10, 10);

-- -- - Таблица 'students'
insert into students (id_students, id_accounts, first_name, last_name, birth_data, gender, activity) values (1, 1, 'Jethro', 'Moseley', '24.9.1991', 'Male', true);
insert into students (id_students, id_accounts, first_name, last_name, birth_data, gender, activity) values (2, 2, 'Maud', 'McDunlevy', '11.10.1997', 'Female', true);
insert into students (id_students, id_accounts, first_name, last_name, birth_data, gender, activity) values (3, 3, 'Guido', 'Gelly', '24.9.1991', 'Male', true);
insert into students (id_students, id_accounts, first_name, last_name, birth_data, gender, activity) values (4, 4, 'Aldon', 'Hellwing', '16.1.2003', 'Male', false);
insert into students (id_students, id_accounts, first_name, last_name, birth_data, gender, activity) values (5, 5, 'Alyda', 'Duckers', '12.5.2000', 'Female', true);
insert into students (id_students, id_accounts, first_name, last_name, birth_data, gender, activity) values (6, 6, 'Eziechiele', 'McGoogan', '26.9.1985', 'Male', true);
insert into students (id_students, id_accounts, first_name, last_name, birth_data, gender, activity) values (7, 7, 'Mauricio', 'Ferreri', '27.5.1999', 'Male', false);
insert into students (id_students, id_accounts, first_name, last_name, birth_data, gender, activity) values (8, 8, 'Kaleb', 'Manjot', '16.8.1989', 'Male', false);
insert into students (id_students, id_accounts, first_name, last_name, birth_data, gender, activity) values (9, 9, 'Boyce', 'Millyard', '2.9.1987', 'Male', false);
insert into students (id_students, id_accounts, first_name, last_name, birth_data, gender, activity) values (10, 10, 'Ibby', 'Pergens', '31.5.2004', 'Female', false);

-- -- - Таблица 'courses'
insert into courses (id_courses, id_students, course_name, description_course, date_start_course, date_end_course) values (1, 1, 'Luxembourgish', 'Nam dui. Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis. Ut at dolor quis odio consequat varius. Integer ac leo. Pellentesque ultrices mattis odio. Donec vitae nisi. Nam ultrices, libero non mattis pulvinar, nulla pede ullamcorper augue, a suscipit nulla elit ac nulla. Sed vel enim sit amet nunc viverra dapibus.', '2024/04/25', '2024/07/05');
insert into courses (id_courses, id_students, course_name, description_course, date_start_course, date_end_course) values (2, 2, 'Oriya', 'Proin interdum mauris non ligula pellentesque ultrices. Phasellus id sapien in sapien iaculis congue. Vivamus metus arcu, adipiscing molestie, hendrerit at, vulputate vitae, nisl. Aenean lectus. Pellentesque eget nunc. Donec quis orci eget orci vehicula condimentum. Curabitur in libero ut massa volutpat convallis. Morbi odio odio, elementum eu, interdum eu, tincidunt in, leo. Maecenas pulvinar lobortis est. Phasellus sit amet erat.', '2023/12/04', '2024/08/03');
insert into courses (id_courses, id_students, course_name, description_course, date_start_course, date_end_course) values (3, 3, 'Montenegrin', 'Morbi porttitor lorem id ligula. Suspendisse ornare consequat lectus. In est risus, auctor sed, tristique in, tempus sit amet, sem.', '2023/11/24', '2024/08/05');
insert into courses (id_courses, id_students, course_name, description_course, date_start_course, date_end_course) values (4, 4, 'Ndebele', 'Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Duis faucibus accumsan odio. Curabitur convallis. Duis consequat dui nec nisi volutpat eleifend. Donec ut dolor. Morbi vel lectus in quam fringilla rhoncus.', '2024/03/01', '2024/08/19');
insert into courses (id_courses, id_students, course_name, description_course, date_start_course, date_end_course) values (5, 5, 'Belarusian', 'Duis ac nibh. Fusce lacus purus, aliquet at, feugiat non, pretium quis, lectus. Suspendisse potenti. In eleifend quam a odio. In hac habitasse platea dictumst.', '2024/02/24', '2024/07/18');
insert into courses (id_courses, id_students, course_name, description_course, date_start_course, date_end_course) values (6, 6, 'Azeri', 'Integer ac neque. Duis bibendum. Morbi non quam nec dui luctus rutrum. Nulla tellus. In sagittis dui vel nisl. Duis ac nibh. Fusce lacus purus, aliquet at, feugiat non, pretium quis, lectus. Suspendisse potenti. In eleifend quam a odio. In hac habitasse platea dictumst.', '2024/01/05', '2024/06/30');
insert into courses (id_courses, id_students, course_name, description_course, date_start_course, date_end_course) values (7, 7, 'Bosnian', 'Nulla facilisi. Cras non velit nec nisi vulputate nonummy. Maecenas tincidunt lacus at velit. Vivamus vel nulla eget eros elementum pellentesque. Quisque porta volutpat erat.', '2024/01/11', '2024/10/07');
insert into courses (id_courses, id_students, course_name, description_course, date_start_course, date_end_course) values (8, 8, 'Albanian', 'Mauris lacinia sapien quis libero. Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum. Integer a nibh. In quis justo. Maecenas rhoncus aliquam lacus. Morbi quis tortor id nulla ultrices aliquet. Maecenas leo odio, condimentum id, luctus nec, molestie sed, justo. Pellentesque viverra pede ac diam. Cras pellentesque volutpat dui.', '2023/11/11', '2024/08/09');
insert into courses (id_courses, id_students, course_name, description_course, date_start_course, date_end_course) values (9, 9, 'Dutch', 'Maecenas pulvinar lobortis est.', '2024/04/23', '2024/06/17');
insert into courses (id_courses, id_students, course_name, description_course, date_start_course, date_end_course) values (10, 10, 'Mongolian', 'Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus vestibulum sagittis sapien. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Etiam vel augue. Vestibulum rutrum rutrum neque. Aenean auctor gravida sem. Praesent id massa id nisl venenatis lacinia.', '2024/03/08', '2024/08/25');

-- -- - Таблица 'teachers'
insert into teacher (id_teacher, id_accounts, id_courses, first_name, last_name, birth_data, gender, activity) values (1, 1, 1, 'Fee', 'Storah', '1989/10/23', 'Male', true);
insert into teacher (id_teacher, id_accounts, id_courses, first_name, last_name, birth_data, gender, activity) values (2, 2, 2, 'Clarice', 'Abercromby', '1987/10/18', 'Female', false);
insert into teacher (id_teacher, id_accounts, id_courses, first_name, last_name, birth_data, gender, activity) values (3, 3, 3, 'Danie', 'Himpson', '1974/07/04', 'Male', false);
insert into teacher (id_teacher, id_accounts, id_courses, first_name, last_name, birth_data, gender, activity) values (4, 4, 4, 'Randie', 'Sargeant', '1983/07/09', 'Male', false);
insert into teacher (id_teacher, id_accounts, id_courses, first_name, last_name, birth_data, gender, activity) values (5, 5, 5, 'Ade', 'Aspy', '1980/01/19', 'Male', false);
insert into teacher (id_teacher, id_accounts, id_courses, first_name, last_name, birth_data, gender, activity) values (6, 6, 6, 'Eydie', 'Lonie', '1993/04/22', 'Female', false);
insert into teacher (id_teacher, id_accounts, id_courses, first_name, last_name, birth_data, gender, activity) values (7, 7, 7, 'Galina', 'Songhurst', '1999/04/03', 'Female', false);
insert into teacher (id_teacher, id_accounts, id_courses, first_name, last_name, birth_data, gender, activity) values (8, 8, 8, 'Arluene', 'Lozano', '1989/03/31', 'Female', false);
insert into teacher (id_teacher, id_accounts, id_courses, first_name, last_name, birth_data, gender, activity) values (9, 9, 9, 'Rutger', 'Nother', '1994/10/17', 'Male', false);
insert into teacher (id_teacher, id_accounts, id_courses, first_name, last_name, birth_data, gender, activity) values (10, 10, 10, 'Alejandro', 'Prahl', '1987/11/10', 'Male', false);
