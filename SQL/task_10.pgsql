-- Созадть индекс в таблице курсов
ADD COLUMN iin VARCHAR(12);
CREATE UNIQUE INDEX iin_index on courses (iin);


-- Сгрупировать студентов по курсам и кол-во студентов
SELECT students.first_name, students.last_name, courses.id_courses, COUNT(students.id_students) AS total_students FROM students
JOIN courses ON courses.id_courses = students.id_students
GROUP BY students.first_name, students.last_name, courses.id_courses;


-- - Сгрупировать преподов по кол-ву курсов
SELECT first_name, last_name, id_courses, COUNT(id_courses) AS total_courses FROM teacher
GROUP BY first_name, last_name, id_courses;


-- ДЗ. Попрактиковаться с JOIN-ми между таблицами:
-- - Вытащить один курс со всеми студентами
SELECT courses.course_name, students.first_name, students.last_name FROM courses
JOIN students ON students.id_students = courses.id_courses
WHERE courses.course_name = 'Bosnian';

-- - Препода с его курсами
SELECT teacher.first_name, teacher.last_name, courses.course_name FROM courses
JOIN teacher ON courses.id_courses = teacher.id_courses
WHERE teacher.first_name = 'Alejandro' and  teacher.last_name = 'Prahl';
