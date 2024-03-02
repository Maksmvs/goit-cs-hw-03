from faker import Faker
import psycopg2
import random

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="m1983",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

fake = Faker()

for _ in range(10):
    fullname = fake.name()
    email = fake.email()
    cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))
    conn.commit()

statuses = ['new', 'in progress', 'completed']
for status in statuses:
    try:
        cur.execute("INSERT INTO status (name) VALUES (%s)", (status,))
        conn.commit()
    except psycopg2.IntegrityError:
        conn.rollback()

for _ in range(20):
    title = fake.sentence()
    description = fake.paragraph()
    status_id = random.randint(1, len(statuses))
    user_id = random.randint(1, 10)
    cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)", (title, description, status_id, user_id))
    conn.commit()

cur.close()
conn.close()
