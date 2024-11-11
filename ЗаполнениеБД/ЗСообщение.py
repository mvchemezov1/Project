import sqlite3
import random
from datetime import datetime, timedelta

# Соединяемся с базой данных (если она не существует, создастся пустая база)
conn = sqlite3.connect('AdminDoc.db')
cursor = conn.cursor()

# Предполагается, что таблица appointments уже создана и заполнена.
# Пример структуры таблицы appointments
# CREATE TABLE "appointments" (
#     "id" INTEGER PRIMARY KEY AUTOINCREMENT,
#     "patient_id" INTEGER NOT NULL,
#     "status" TEXT NOT NULL CHECK (status IN ('confirmed', 'canceled')),
#     "appointment_date" DATETIME NOT NULL
# );

# Получаем все подтвержденные и отмененные приемы
cursor.execute("SELECT patient_id, status, appointment_date FROM appointments")
appointments = cursor.fetchall()

# Проверяем, что есть приемы для заполнения уведомлений
if appointments:
    for i in range(10000):
        # Случайный выбор приема
        appointment = random.choice(appointments)
        patient_id, status, appointment_date = appointment

        if status == 'Подтверждённый':
            message = f"Ваш прием назначен на {appointment_date}."
        elif status == 'Отменённый':
            message = f"Ваш прием на {appointment_date} отменен."
        elif status == 'Завершённый':
            message = f"Ваш прием на {appointment_date} завершён."


        # Вставка уведомления в таблицу
        cursor.execute("""
            INSERT INTO notifications (user_id, message, notification_date, is_read)
            VALUES (?, ?, ?, ?)
        """, (patient_id, message, datetime.now(), False))

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()