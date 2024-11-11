-- При вставке нового врача отправляем уведомление на email
CREATE TRIGGER send_doctor_registration_email
AFTER INSERT ON Врач
BEGIN
  SELECT send_email(NEW.Email, 'Регистрация врача', 'Вы успешно зарегистрированы в нашей базе данных.');
END;

-- При обновлении данных врача отправляем уведомление на email
CREATE TRIGGER send_doctor_update_email
AFTER UPDATE ON Врач
BEGIN
  SELECT send_email(NEW.Email, 'Обновление данных врача', 'Ваши данные в нашей базе данных были обновлены.');
END;

-- При удалении врача отправляем уведомление на email и удаляем связанные данные
CREATE TRIGGER delete_related_data_on_doctor_delete
BEFORE DELETE ON Врач
BEGIN
  -- Удаляем связанные данные в других таблицах, например, Прием, Поликлиника_Больница, Медицинские_документы
  DELETE FROM Прием WHERE Врач = OLD.ID;
  DELETE FROM Поликлиника_Больница WHERE Руководитель = OLD.ID;
  DELETE FROM Медицинские_документы WHERE Врач = OLD.ID;

  -- Отправляем уведомление на email
  SELECT send_email(OLD.Email, 'Удаление данных врача', 'Ваши данные в нашей базе данных были удалены.');
END;