import sqlite3
from faker import Faker
import random

# Создание подключения к базе данных SQLite (или подключение к существующей)
conn = sqlite3.connect('AdminDoc.db')
cursor = conn.cursor()

# Создание экземпляра Faker
fake = Faker('RU_ru')

# Возможные роли
roles = ['пациент', 'доктор', 'админ']

# SQL-запрос для вставки данных
insert_query = '''
INSERT INTO users (username, password, role, full_name, email, phone)
VALUES (?, ?, ?, ?, ?, ?);
'''

# Генерация и вставка 100 записей
for _ in range(10000):
    username = fake.unique.user_name()
    password = fake.password()
    role = random.choice(roles)
    full_name = fake.name()
    email = fake.unique.email()
    phone = fake.phone_number()

    cursor.execute(insert_query, (username, password, role, full_name, email, phone))

# Сохранение изменений и закрытие подключения
conn.commit()
conn.close()

print("100 записей успешно сгенерировано!")