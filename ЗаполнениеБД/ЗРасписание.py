import sqlite3
from datetime import timedelta

from faker import Faker
import random

# Создание подключения к базе данных SQLite (или подключение к существующей)
conn = sqlite3.connect('AdminDoc.db')
cursor = conn.cursor()

# Создание экземпляра Faker
fake = Faker('ru_RU')

# SQL-запрос для вставки данных
insert_query = '''
INSERT INTO schedules (doctor_id, start_time, end_time)
VALUES (?, ?, ?);
'''

# Получаем список всех врачей для генерации расписания
cursor.execute('SELECT id FROM doctors;')
doctors = [row[0] for row in cursor.fetchall()]

# Генерация и вставка 10,000 записей
for _ in range(10000):
    doctor_id = random.choice(doctors)
    start_time = fake.date_time_this_month()
    end_time = start_time + timedelta(hours=random.randint(3, 5))  # Продолжительность приема от 1 до 3 часов

    # Проверяем наличие записей о приемах для данного врача
    cursor.execute('SELECT COUNT(*) FROM appointments WHERE doctor_id = ? AND appointment_date BETWEEN ? AND ?;',
                   (doctor_id, start_time, end_time))
    has_appointment = cursor.fetchone()[0] > 0

    cursor.execute(insert_query, (doctor_id, start_time, end_time))

# Сохранение изменений и закрытие подключения
conn.commit()
conn.close()

print("10,000 записей успешно сгенерировано в таблице schedules!")