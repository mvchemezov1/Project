-- При вставке нового пациента отправляем уведомление на email
CREATE TRIGGER send_patient_registration_email
AFTER INSERT ON Пациент
BEGIN
  SELECT send_email(NEW.Email, 'Регистрация пациента', 'Вы успешно зарегистрированы в нашей базе данных.');
END;

-- При обновлении данных пациента отправляем уведомление на email
CREATE TRIGGER send_patient_update_email
AFTER UPDATE ON Пациент
BEGIN
  SELECT send_email(NEW.Email, 'Обновление данных пациента', 'Ваши данные в нашей базе данных были обновлены.');
END;

-- При удалении пациента отправляем уведомление на email и удаляем связанные данные
CREATE TRIGGER delete_related_data_on_patient_delete
BEFORE DELETE ON Пациент
BEGIN
  -- Удаляем связанные данные в других таблицах, например, Прием, Медицинские_документы
  DELETE FROM Прием WHERE Пациент = OLD.ID;
  DELETE FROM Медицинские_документы WHERE Пациент = OLD.ID;

  -- Отправляем уведомление на email
  SELECT send_email(OLD.Email, 'Удаление данных пациента', 'Ваши данные в нашей базе данных были удалены.');
END;