# Импортируем необходимые библиотеки
from flask import Flask, request, redirect, url_for, render_template, flash, session, jsonify
import sqlite3
from datetime import datetime, timedelta
import os
import bcrypt

# Создаем приложение Flask
app = Flask(__name__)

# Указываем путь к базе данных
DATABASE = 'C:\\Users\\mikha\\Desktop\\AdminDoc\\AdminDoc.db'

# Устанавливаем секретный ключ для сессий
app.secret_key = os.urandom(24)

# Функция для подключения к базе данных
def get_db():
    # Подключаемся к базе данных
    conn = sqlite3.connect(DATABASE)
    # Устанавливаем фабрику строк для получения результатов запросов
    conn.row_factory = sqlite3.Row
    return conn

# Маршрут для главной страницы
@app.route('/')
def index():
    # Возвращаем шаблон главной страницы
    return render_template('index.html')

# Маршрут для страницы записей на прием
@app.route('/appointments')
def show_appointments():
    # Возвращаем шаблон страницы записей на прием
    return render_template('appointments.html')

# Маршрут для страницы авторизации
@app.route('/login')
def slogin():
    # Возвращаем шаблон страницы авторизации
    return render_template('login.html')

# Маршрут для страницы регистрации
@app.route('/register')
def sregister():
    # Возвращаем шаблон страницы регистрации
    return render_template('register.html')

# Маршрут для страницы расписания
@app.route('/schedule')
def sshedule():
    # Подключаемся к базе данных
    with get_db() as conn:
        # Выполняем запрос для получения списка врачей и их специальностей
        doctors = conn.execute('''
            SELECT d.*, u.full_name, u.role, s.name AS specialty, sda.symptom, sda.specialty
            FROM doctors d
            JOIN users u ON d.user_id = u.id
            JOIN specialties s ON d.specialty = s.name
            JOIN SymptomsDoctorAdvice sda ON s.name = sda.specialty
        ''').fetchall()

        # Выполняем запрос для получения списка специальностей
        specialties = conn.execute("SELECT id, name FROM specialties").fetchall()

        # Возвращаем шаблон страницы расписания с данными врачей и специальностей
        return render_template('schedule.html', doctors=doctors, specialties=specialties)

# Маршрут для обработки регистрации
@app.route('/register', methods=['GET', 'POST'])
def register():
    # Если метод запроса POST
    if request.method == 'POST':
        # Получаем данные из формы регистрации
        username = request.form['username']
        password = request.form['password'].encode('utf-8')
        full_name = request.form['full_name']
        email = request.form['email']

        # Хэшируем пароль
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

        # Подключаемся к базе данных
        with get_db() as conn:
            try:
                # Выполняем запрос для добавления нового пользователя
                conn.execute('''
                    INSERT INTO users (username, password, role, full_name, email)
                    VALUES (?,?,?,?,?)
                ''', (username, hashed_password, 'пациент', full_name, email))
                # Выводим сообщение об успешной регистрации
                flash('Регистрация прошла успешно!', 'uccess')
                # Перенаправляем на главную страницу
                return redirect(url_for('index'))
            except sqlite3.IntegrityError:
                # Выводим сообщение об ошибке при регистрации
                flash('Пользователь с таким именем или email уже существует.', 'error')
            finally:
                # Коммитим изменения
                conn.commit()
        # Закрываем соединение с базой данных
        conn.close()

        # Возвращаем шаблон страницы регистрации
        return render_template('register.html')

# Маршрут для обработки авторизации
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Если метод запроса POST
    if request.method == 'POST':
        # Получаем данные из формы авторизации
        username = request.form['username']
        password = request.form['password'].encode('utf-8')

        # Подключаемся к базе данных
        with get_db() as conn:
            # Выполняем запрос для проверки пользователя
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE username =?', (username,))
            user = cursor.fetchone()

        # Если пользователь найден и пароль верный
        if user and bcrypt.checkpw(password, user[2]):
            # Сохраняем id пользователя в сессии
            session['user_id'] = user[0]
            # Перенаправляем на главную страницу
            return redirect(url_for('index'))
        else:
            # Возвращаем сообщение о неверном имени пользователя или пароле
            return 'Неверное имя пользователя или пароль', 401

    # Возвращаем шаблон страницы авторизации
    return render_template('login.html')

# Маршрут для страницы профиля пользователя
@app.route('/dashboard')
def dashboard():
    # Если пользователь авторизован
    if 'user_id' in session:
        # Возвращаем сообщение с id пользователя
        return f'Добро пожаловать! Ваш ID пользователя: {session["user_id"]}'
    # Если пользователь не авторизован, перенаправляем на страницу авторизации
    return redirect(url_for('login'))

# Функция для получения списка врачей по симптомам
def get_doctors(symptom):
    # Подключаемся к базе данных
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    # Выполняем запрос для получения списка врачей по симптомам
    query = '''
        SELECT specialty
        FROM SymptomsDoctorAdvice
        WHERE symptom LIKE?
    '''
    cursor.execute(query, ('%' + symptom + '%',))
    specialtys = cursor.fetchall()

    # Возвращаем список врачей
    return [specialty[0] for specialty in specialtys]

# Маршрут для страницы помощи
@app.route('/help')
def fer():
    # Возвращаем шаблон страницы помощи
    return render_template('docser.html')

# Маршрут для поиска врачей по симптомам
@app.route('/search', methods=['GET'])
def search():
    # Получаем симптом из запроса
    symptom = request.args.get('symptom')
    # Преобразуем симптом в строчные буквы
    doctors = get_doctors(symptom.lower())
    # Возвращаем список врачей в формате JSON
    return jsonify(doctors)

# Маршрут для записи на прием
@app.route('/api/appointments', methods=['POST'])
def appointment():
    # Получаем данные из запроса
    data = request.get_json()
    # Получаем id пациента из сессии
    patient_id = session["user_id"]
    # Получаем id врача из запроса
    doctor_id = data.get('doctor_id')
    # Получаем дату и время приема из запроса
    date = data.get('date')
    appointment_date = data.get('appointment_date')
    # Устанавливаем статус записи на прием
    status = "Подтверждённый"

    # Подключаемся к базе данных
    with get_db() as conn:
        # Выполняем запрос для проверки записи на прием
        cursor = conn.cursor()
        check_appointment_query = """
            SELECT COUNT(*)
            FROM appointments
            WHERE patient_id =? AND appointment_date =?
        """
        cursor.execute(check_appointment_query, (patient_id, appointment_date))
        count = cursor.fetchone()[0]

        # Если запись на прием уже существует
        if count:
            # Возвращаем сообщение об ошибке
            return jsonify({'message': 'У Вас уже есть запись на это время'}), 400

        # Если записи на прием нет, добавляем новую запись
        cursor.execute("""
            INSERT INTO appointments (patient_id, doctor_id, date, appointment_date, status)
            VALUES (?,?,?,?,?)
        """, (patient_id, doctor_id, date, appointment_date, status))

    # Коммитим изменения
    conn.commit()
    # Закрываем соединение с базой данных
    cursor.close()

    # Возвращаем сообщение об успешной записи на прием
    return jsonify({'message': 'Запись успешно добавлена'}), 201

# Маршрут для получения доступных слотов приема
@app.route('/api/slots', methods=['GET'])
def get_slots():
    # Получаем id врача и дату из запроса
    doctor_id = request.args.get('doctorId', type=int)
    slot_date_str = request.args.get('date')

    # Подключаемся к базе данных
    conn = get_db()
    cursor = conn.cursor()

    # Выполняем запрос для получения доступных слотов приема
    appointments_query = """
        SELECT appointment_date
        FROM appointments
        WHERE doctor_id =?
    """
    cursor.execute(appointments_query, (doctor_id,))
    appointments = [appointment['appointment_date'] for appointment in cursor.fetchall()]

    # Генерируем доступные слоты приема
    slots = []
    starting_time = datetime.strptime('09:00:00', '%H:%M:%S')
    ending_time = datetime.strptime('17:00:00', '%H:%M:%S')
    current_time = starting_time
    while current_time < ending_time:
        appointment_time_str = (datetime.strptime(slot_date_str, '%Y-%m-%d') + timedelta(hours=current_time.hour, minutes=current_time.minute)).strftime('%Y-%m-%d %H:%M:%S')
        if appointment_time_str not in appointments:
            slots.append({
                "appointment_date": appointment_time_str
            })
        current_time += timedelta(minutes=30)

    # Возвращаем доступные слоты приема
    return slots

# Маршрут для получения записей на прием пациента
@app.route('/api/appointments/user', methods=['GET'])
def get_user_appointments():
    # Получаем id пациента из сессии
    patient_id = session["user_id"]

    # Подключаемся к базе данных
    with get_db() as conn:
        # Выполняем запрос для получения записей на прием пациента
        appointments_query = """
            SELECT doctor_id, date, appointment_date, status
            FROM appointments
            WHERE patient_id =?
        """
        cursor = conn.cursor()
        cursor.execute(appointments_query, (patient_id,))
        appointments = cursor.fetchall()

    # Преобразуем результаты в список словарей
    result = [{
        "doctor_id": appointment['doctor_id'],
        "date": appointment['date'],
        "appointment_date": appointment['appointment_date'],
        "status": appointment['status']
    } for appointment in appointments]

    # Возвращаем записи на прием пациента
    return jsonify(result)

# Запускаем приложение
if __name__ == '__main__':
    app.run(debug=True)