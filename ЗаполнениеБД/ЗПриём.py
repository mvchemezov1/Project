import sqlite3
from faker import Faker
import random
from datetime import datetime, timedelta

# Создание подключения к базе данных SQLite (или подключение к существующей)
conn = sqlite3.connect('AdminDoc.db')
cursor = conn.cursor()

# Создание экземпляра Faker
fake = Faker('ru_RU')

# SQL-запрос для вставки данных
insert_query = '''
INSERT INTO appointments (patient_id, doctor_id, appointment_date, status)
VALUES (?, ?, ?, ?);
'''

# Получаем список всех пациентов для генерации appointments
cursor.execute('SELECT id FROM users WHERE role = "пациент";')
patients = [row[0] for row in cursor.fetchall()]

# Получаем список всех врачей
cursor.execute('SELECT id FROM doctors;')
doctors = [row[0] for row in cursor.fetchall()]

# Генерация и вставка 5000 записей
for _ in range(5000):
    patient_id = random.choice(patients)
    doctor_id = random.choice(doctors)
    appointment_date = fake.date_time_between(start_date='-30d', end_date='+30d')  # Генерация даты

    # Проверка статуса на основе даты
    if appointment_date < datetime.now():
        status = 'Завершённый'
    elif appointment_date >= datetime.now():
        status = random.choice(['Подтверждённый', 'Отменённый'])

    cursor.execute(insert_query, (patient_id, doctor_id, appointment_date, status))

# Сохранение изменений и закрытие подключения
conn.commit()
conn.close()

print("5000 записей успешно сгенерировано!")