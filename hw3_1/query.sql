--1.Отримати всі завдання певного користувача
SELECT * 
FROM tasks 
WHERE user_id = 5;

--2.Вибрати завдання за певним статусом
SELECT * 
FROM tasks 
WHERE status_id = (
    SELECT id 
    FROM status 
    WHERE name = 'new'
);

--3.Оновити статус конкретного завдання
UPDATE tasks
SET status_id = (
    SELECT id
    FROM status
    WHERE name = 'in progress'
)
WHERE id = 3;

--4.Отримати список користувачів, які не мають жодного завдання
SELECT *
FROM users
WHERE id NOT IN (
    SELECT DISTINCT user_id
    FROM tasks
);

--5.Додати нове завдання для конкретного користувача
INSERT INTO tasks (title, description, status_id, user_id)
VALUES ('Perform testing of new features', 'Summarize the results and identify any issues discovered during testing', 1, 1);

--6.Видалити конкретне завдання
DELETE FROM tasks
WHERE id = 1; -- наприклад

--7.Знайти користувачів з певною електронною поштою
SELECT * 
FROM users 
WHERE email LIKE '%b%' AND email LIKE '%@example.com';

--8.Оновити ім'я користувача
UPDATE users
SET fullname = 'BOB MARLEY'
WHERE id = 1;

--9.Отримати кількість завдань для кожного статусу
SELECT status.name AS status_name, COUNT(*) AS task_count
FROM tasks
JOIN status ON tasks.status_id = status.id
GROUP BY status.name;

--10.Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти
SELECT tasks.*
FROM tasks
JOIN users ON tasks.user_id = users.id
WHERE users.email LIKE '%@example.com';

--11.Отримати список завдань, що не мають опису
SELECT *
FROM tasks
WHERE description IS NULL OR description = '';

--12.Вибрати користувачів та їхні завдання, які є у статусі 'in progress'
SELECT users.fullname, tasks.title
FROM users
INNER JOIN tasks ON users.id = tasks.user_id
INNER JOIN status ON tasks.status_id = status.id
WHERE status.name = 'in progress';

--13.Отримати користувачів та кількість їхніх завдань
SELECT users.fullname, COUNT(tasks.id) AS task_count
FROM users
LEFT JOIN tasks ON users.id = tasks.user_id
GROUP BY users.fullname;



































