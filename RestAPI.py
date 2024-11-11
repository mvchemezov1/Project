from flask import Flask, jsonify, request, render_template
import sqlite3

app = Flask(__name__)


# Функция для подключения к базе данных
def get_db_connection():
    conn = sqlite3.connect('C:\\Users\\mikha\\Desktop\\AdminDoc\\admindoc.db')  # Замените на путь к Вашей БД
    conn.row_factory = sqlite3.Row  # позволяет обращаться к столбцам по имени
    return conn


@app.route('/')
def index():
    return render_template('index.html')


# Получить всех пациентов
@app.route('/patients', methods=['GET'])
def view_patients():
    conn = get_db_connection()
    patients = conn.execute('SELECT * FROM Пациент').fetchall()
    conn.close()
    return render_template('patients.html', patients=patients)


# Получить всех врачей
@app.route('/doctors', methods=['GET'])
def view_doctors():
    conn = get_db_connection()
    doctors = conn.execute('SELECT * FROM Врач').fetchall()
    conn.close()
    return render_template('doctors.html', doctors=doctors)


# Получить всех клиник
@app.route('/clinics', methods=['GET'])
def view_clinics():
    conn = get_db_connection()
    clinics = conn.execute('SELECT * FROM Поликлиника_Больница').fetchall()
    conn.close()
    return render_template('clinics.html', clinics=clinics)


# Получить всех приёмов
@app.route('/receptions', methods=['GET'])
def view_receptions():
    conn = get_db_connection()
    receptions = conn.execute('SELECT * FROM Прием').fetchall()
    conn.close()
    return render_template('receptions.html', receptions=receptions)


# Получить всех медуслуг
@app.route('/medservices', methods=['GET'])
def view_medservices():
    conn = get_db_connection()
    medservices = conn.execute('SELECT * FROM Медицинские_услуги').fetchall()
    conn.close()
    return render_template('medservices.html', medservices=medservices)


# Получить всех результатов
@app.route('/results', methods=['GET'])
def view_results():
    conn = get_db_connection()
    results = conn.execute('SELECT * FROM Результаты_анализов_и_исследований').fetchall()
    conn.close()
    return render_template('results.html', results=results)


# Получить всех меддокументов
@app.route('/meddocs', methods=['GET'])
def view_meddocs():
    conn = get_db_connection()
    meddocs = conn.execute('SELECT * FROM Медицинские_документы').fetchall()
    conn.close()
    return render_template('meddocs.html', meddocs=meddocs)


# Получить всех пациентов
@app.route('/app/patients', methods=['GET'])
def get_patients():
    conn = get_db_connection()
    patients = conn.execute('SELECT * FROM Пациент').fetchall()
    conn.close()
    return jsonify([dict(row) for row in patients])


# Получить всех врачей
@app.route('/app/doctors', methods=['GET'])
def get_doctors():
    conn = get_db_connection()
    doctors = conn.execute('SELECT * FROM Врач').fetchall()
    conn.close()
    return jsonify([dict(row) for row in doctors])


# Получить всех клиник
@app.route('/clinics', methods=['GET'])
def get_clinics():
    conn = get_db_connection()
    clinics = conn.execute('SELECT * FROM Поликлиника_Больница').fetchall()
    conn.close()
    return jsonify([dict(row) for row in clinics])


# Получить всех приёмов
@app.route('/receptions', methods=['GET'])
def get_receptions():
    conn = get_db_connection()
    receptions = conn.execute('SELECT * FROM Прием').fetchall()
    conn.close()
    return jsonify([dict(row) for row in receptions])


# Получить всех медуслуг
@app.route('/medservices', methods=['GET'])
def get_medservices():
    conn = get_db_connection()
    medservices = conn.execute('SELECT * FROM Медицинские_услуги').fetchall()
    conn.close()
    return jsonify([dict(row) for row in medservices])


# Получить всех результатов
@app.route('/results', methods=['GET'])
def get_results():
    conn = get_db_connection()
    results = conn.execute('SELECT * FROM Результаты_анализов_и_исследований').fetchall()
    conn.close()
    return jsonify([dict(row) for row in results])


# Получить всех меддокументов
@app.route('/meddocs', methods=['GET'])
def get_meddocs():
    conn = get_db_connection()
    meddocs = conn.execute('SELECT * FROM Медицинские_документы').fetchall()
    conn.close()
    return jsonify([dict(row) for row in meddocs])


# Получить пациента по ID
@app.route('/app/patients/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    conn = get_db_connection()
    patient = conn.execute('SELECT * FROM Пациент WHERE ID = ?', (patient_id,)).fetchone()
    conn.close()
    if patient is None:
        return jsonify({'error': 'Patient not found'}), 404
    return jsonify(dict(patient))


# Получить врача по ID
@app.route('/app/doctors/<int:doctor_id>', methods=['GET'])
def get_doctor(doctor_id):
    conn = get_db_connection()
    doctor = conn.execute('SELECT * FROM Врач WHERE ID = ?', (doctor_id,)).fetchone()
    conn.close()
    if doctor is None:
        return jsonify({'error': 'Doctor not found'}), 404
    return jsonify(dict(doctor))


# Получить поликлинику по ID
@app.route('/app/clinics/<int:clinic_id>', methods=['GET'])
def get_clinic(clinic_id):
    conn = get_db_connection()
    clinic = conn.execute('SELECT * FROM Поликлиника_Больница WHERE ID = ?', (clinic_id,)).fetchone()
    conn.close()
    if clinic is None:
        return jsonify({'error': 'Clinic not found'}), 404
    return jsonify(dict(clinic))


# Получить прием по ID
@app.route('/app/receptions/<int:reception_id>', methods=['GET'])
def get_reception(reception_id):
    conn = get_db_connection()
    reception = conn.execute('SELECT * FROM Прием WHERE ID = ?', (reception_id,)).fetchone()
    conn.close()
    if reception is None:
        return jsonify({'error': 'reception not found'}), 404
    return jsonify(dict(reception))


# Получить медуслугу по ID
@app.route('/app/medservices/<int:medservice_id>', methods=['GET'])
def get_medservice(medservice_id):
    conn = get_db_connection()
    medservice = conn.execute('SELECT * FROM Медицинские_услуги WHERE ID = ?', (medservice_id,)).fetchone()
    conn.close()
    if medservice is None:
        return jsonify({'error': 'medservice not found'}), 404
    return jsonify(dict(medservice))


# Получить результат по ID
@app.route('/app/results/<int:result_id>', methods=['GET'])
def get_result(result_id):
    conn = get_db_connection()
    result = conn.execute('SELECT * FROM Результаты_анализов_и_исследований WHERE ID = ?', (result_id,)).fetchone()
    conn.close()
    if result is None:
        return jsonify({'error': 'result not found'}), 404
    return jsonify(dict(result))


# Получить меддокумент по ID
@app.route('/app/meddocs/<int:meddoc_id>', methods=['GET'])
def get_meddoc(meddoc_id):
    conn = get_db_connection()
    meddoc = conn.execute('SELECT * FROM Медицинские_документы WHERE ID = ?', (meddoc_id,)).fetchone()
    conn.close()
    if meddoc is None:
        return jsonify({'error': 'meddoc not found'}), 404
    return jsonify(dict(meddoc))


# Создать нового пациента
@app.route('/app/patients', methods=['POST'])
def create_patient():
    new_patient = request.get_json()
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO Пациент (Фамилия, Имя, Отчество, Дата_рождения, Пол, Адрес_проживания, Телефон, Email, Полис_ОМС) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
        (new_patient['Фамилия'], new_patient['Имя'], new_patient['Отчество'], new_patient['Дата_рождения'],
         new_patient['Пол'],
         new_patient['Адрес_проживания'], new_patient['Телефон'], new_patient['Email'], new_patient['Полис_ОМС']))
    conn.commit()
    conn.close()
    return jsonify(new_patient), 201


# Создать нового врача
@app.route('/app/doctors', methods=['POST'])
def create_doctor():
    new_doctor = request.get_json()
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO Врач (Фамилия, Имя, Отчество, Специальность, Категория, Адрес_работы, Телефон, Email) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
        (new_doctor['Фамилия'], new_doctor['Имя'], new_doctor['Отчество'], new_doctor['Специальность'],
         new_doctor['Категория'],
         new_doctor['Адрес_работы'], new_doctor['Телефон'], new_doctor['Email']))
    conn.commit()
    conn.close()
    return jsonify(new_doctor), 201


# Создать нового поликлиника
@app.route('/app/clinics', methods=['POST'])
def create_clinic():
    new_clinic = request.get_json()
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO Поликлиника_Больница (Название, Адрес, Телефон, Email, Руководитель]) VALUES (?, ?, ?, ?, ?)',
        (new_clinic['Название'], new_clinic['Адрес'], new_clinic['Телефон'], new_clinic['Email'],
         new_clinic['Руководитель']))
    conn.commit()
    conn.close()
    return jsonify(new_clinic), 201


# Создать нового прием
@app.route('/app/receptions', methods=['POST'])
def create_reception():
    new_reception = request.get_json()
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO Прием (Врач, Пациент, Дата_время_приема, Статус, Диагноз]) VALUES (?, ?, ?, ?, ?)',
        (new_reception['Врач'], new_reception['Пациент'], new_reception['Дата_время_приема'], new_reception['Статус'],
         new_reception['Диагноз']))
    conn.commit()
    conn.close()
    return jsonify(new_reception), 201


# Создать нового Медицинские_услуги
@app.route('/app/medservices', methods=['POST'])
def create_medservice():
    new_medservice = request.get_json()
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO Медицинские_услуги (Название_услуги, Описание_услуги, Цена, Срок_исполнения]) VALUES (?, ?, ?, ?)',
        (new_medservice['Название_услуги'], new_medservice['Описание_услуги'], new_medservice['Цена'], new_medservice['Срок_исполнения']))
    conn.commit()
    conn.close()
    return jsonify(new_medservice), 201


# Создать нового Результаты_анализов_и_исследований
@app.route('/app/results', methods=['POST'])
def create_result():
    new_result = request.get_json()
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO Результаты_анализов_и_исследований (Прием, Услуга, Дата_получения_результата, Время_получения_результата, Результат]) VALUES (?, ?, ?, ?, ?)',
        (new_result['Прием'], new_result['Услуга'], new_result['Дата_получения_результата'], new_result['Время_получения_результата'], new_result['Результат']))
    conn.commit()
    conn.close()
    return jsonify(new_result), 201


# Создать нового Медицинские_документы
@app.route('/app/meddocs', methods=['POST'])
def create_meddoc():
    new_meddoc = request.get_json()
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO Медицинские_документы (Пациент, Тип_документа, Дата_выдачи, Врач, Содержание_документа]) VALUES (?, ?, ?, ?, ?)',
        (new_meddoc['Пациент'], new_meddoc['Тип_документа'], new_meddoc['Дата_выдачи'], new_meddoc['Врач'], new_meddoc['Содержание_документа']))
    conn.commit()
    conn.close()
    return jsonify(new_meddoc), 201


# Обновить информацию о пациенте
@app.route('/patients/<int:patient_id>', methods=['PUT'])
def update_patient(patient_id):
    updated_patient = request.get_json()
    conn = get_db_connection()
    conn.execute(
        'UPDATE Пациент SET Фамилия = ?, Имя = ?, Отчество = ?, Дата_рождения = ?, Пол = ?, Адрес_проживания = ?, Телефон = ?, Email = ?, Полис_ОМС = ? WHERE ID = ?',
        (updated_patient['Фамилия'], updated_patient['Имя'], updated_patient['Отчество'],
         updated_patient['Дата_рождения'], updated_patient['Пол'],
         updated_patient['Адрес_проживания'], updated_patient['Телефон'], updated_patient['Email'],
         updated_patient['Полис_ОМС'], patient_id))
    conn.commit()
    conn.close()
    return jsonify(updated_patient)


# Обновить информацию о враче
@app.route('/app/doctors/<int:doctor_id>', methods=['PUT'])
def update_doctor(doctor_id):
    updated_doctor = request.get_json()
    conn = get_db_connection()
    conn.execute(
        'UPDATE Пациент SET Фамилия = ?, Имя = ?, Отчество = ?, Специальность = ?, Категория = ?, Адрес_работы = ?, Телефон = ?, Email = ? WHERE ID = ?',
        (updated_doctor['Фамилия'], updated_doctor['Имя'], updated_doctor['Отчество'],
         updated_doctor['Специальность'], updated_doctor['Категория'],
         updated_doctor['Адрес_работы'], updated_doctor['Телефон'], updated_doctor['Email'], doctor_id))
    conn.commit()
    conn.close()
    return jsonify(updated_doctor)


# Обновить информацию о поликлинике
@app.route('/app/clinics/<int:clinic_id>', methods=['PUT'])
def update_clinic(clinic_id):
    updated_clinic = request.get_json()
    conn = get_db_connection()
    conn.execute(
        'UPDATE Поликлиника_Больница SET Название = ?, Адрес = ?, Телефон = ?, Email = ?, Руководитель = ? WHERE ID = ?',
        (updated_clinic['Фамилия'], updated_clinic['Имя'], updated_clinic['Отчество'],
         updated_clinic['Специальность'], updated_clinic['Категория'],
         updated_clinic['Адрес_работы'], updated_clinic['Телефон'], updated_clinic['Email'], clinic_id))
    conn.commit()
    conn.close()
    return jsonify(updated_clinic)


# Обновить информацию о прием
@app.route('/app/receptions/<int:reception_id>', methods=['PUT'])
def update_reception(reception_id):
    updated_reception = request.get_json()
    conn = get_db_connection()
    conn.execute(
        'UPDATE Прием SET Врач = ?, Пациент = ?, Дата_время_приема = ?, Статус = ?, Диагноз = ? WHERE ID = ?',
        (updated_reception['Врач'], updated_reception['Пациент'], updated_reception['Дата_время_приема'],
         updated_reception['Статус'], updated_reception['Диагноз'], reception_id))
    conn.commit()
    conn.close()
    return jsonify(updated_reception)


# Обновить информацию о Медицинские_услуги
@app.route('/app/medservices/<int:medservice_id>', methods=['PUT'])
def update_medservice(medservice_id):
    updated_medservice = request.get_json()
    conn = get_db_connection()
    conn.execute(
        'UPDATE Медицинские_услуги SET Название_услуги = ?, Описание_услуги = ?, Цена = ?, Срок_исполнения = ? WHERE ID = ?',
        (updated_medservice['Название_услуги'], updated_medservice['Описание_услуги'], updated_medservice['Цена'],
         updated_medservice['Срок_исполнения'], medservice_id))
    conn.commit()
    conn.close()
    return jsonify(updated_medservice)


# Обновить информацию о Результаты_анализов_и_исследований
@app.route('/app/results/<int:result_id>', methods=['PUT'])
def update_result(result_id):
    updated_result = request.get_json()
    conn = get_db_connection()
    conn.execute(
        'UPDATE Результаты_анализов_и_исследований SET Прием = ?, Услуга = ?, Дата_получения_результата = ?, Время_получения_результата = ?, Результат = ? WHERE ID = ?',
        (updated_result['Прием'], updated_result['Услуга'], updated_result['Дата_получения_результата'],
         updated_result['Время_получения_результата'], updated_result['Результат'], result_id))
    conn.commit()
    conn.close()
    return jsonify(updated_result)


# Обновить информацию о Медицинские_документы
@app.route('/app/meddocs/<int:meddoc_id>', methods=['PUT'])
def update_meddoc(meddoc_id):
    updated_meddoc = request.get_json()
    conn = get_db_connection()
    conn.execute(
        'UPDATE Медицинские_документы SET Пациент = ?, Тип_документа = ?, Дата_выдачи = ?, Врач = ?, Содержание_документа = ? WHERE ID = ?',
        (updated_meddoc['Пациент'], updated_meddoc['Тип_документа'], updated_meddoc['Дата_выдачи'],
         updated_meddoc['Врач'], updated_meddoc['Содержание_документа'], meddoc_id))
    conn.commit()
    conn.close()
    return jsonify(updated_meddoc)


# Удалить пациента
@app.route('/app/patients/<int:patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM Пациент WHERE ID = ?', (patient_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Patient deleted successfully'}), 200


# Удалить врача
@app.route('/app/doctors/<int:doctor_id>', methods=['DELETE'])
def delete_doctor(doctor_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM Врач WHERE ID = ?', (doctor_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Doctor deleted successfully'}), 200


# Удалить поликлинику
@app.route('/app/clinics/<int:clinic_id>', methods=['DELETE'])
def delete_clinic(clinic_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM Поликлиника_Больница WHERE ID = ?', (clinic_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Clinic deleted successfully'}), 200


# Удалить прием
@app.route('/app/receptions/<int:reception_id>', methods=['DELETE'])
def delete_reception(reception_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM Прием WHERE ID = ?', (reception_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Reception deleted successfully'}), 200


# Удалить Медицинские_услуги
@app.route('/app/medservices/<int:medservice_id>', methods=['DELETE'])
def delete_medservice(medservice_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM Медицинские_услуги WHERE ID = ?', (medservice_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Medservice deleted successfully'}), 200


# Удалить Результаты_анализов_и_исследований
@app.route('/app/results/<int:result_id>', methods=['DELETE'])
def delete_result(result_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM Результаты_анализов_и_исследований WHERE ID = ?', (result_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Result deleted successfully'}), 200


# Удалить Медицинские_услуги
@app.route('/app/meddocs/<int:meddoc_id>', methods=['DELETE'])
def delete_meddoc(meddoc_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM Прием WHERE ID = ?', (meddoc_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Meddoc deleted successfully'}), 200


if __name__ == '__main__':
    app.run(host='192.168.0.82', port=3306, debug=True)
