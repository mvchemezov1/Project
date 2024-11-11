-- При вставке нового приема отправляем уведомление на email пациенту и врачу
CREATE TRIGGER send_appointment_email
AFTER INSERT ON Прием
BEGIN
  SELECT send_email((SELECT Email FROM Пациент WHERE ID = NEW.Пациент), 'Новый прием', 'У вас назначена новая консультация с врачом.');
  SELECT send_email((SELECT Email FROM Врач WHERE ID = NEW.Врач), 'Новый прием', 'У вас назначена новая консультация с пациентом.');
END;

-- При обновлении данных приема отправляем уведомление на email пациенту и врачу
CREATE TRIGGER send_appointment_update_email
AFTER UPDATE ON Прием
BEGIN
  SELECT send_email((SELECT Email FROM Пациент WHERE ID = NEW.Пациент), 'Обновление приема', 'Ваш прием был обновлен.');
  SELECT send_email((SELECT Email FROM Врач WHERE ID = NEW.Врач), 'Обновление приема', 'Ваш прием был обновлен.');
END;

-- При удалении приема отправляем уведомление на email пациенту и врачу и удаляем связанные данные
CREATE TRIGGER delete_related_data_on_appointment_delete
BEFORE DELETE ON Прием
BEGIN
  -- Удаляем связанные данные в других таблицах, например, Результаты_анализов_и_исследований
  DELETE FROM Результаты_анализов_и_исследований WHERE Прием = OLD.ID;

  -- Отправляем уведомление на email
  SELECT send_email((SELECT Email FROM Пациент WHERE ID = OLD.Пациент), 'Удаление приема', 'Ваш прием был удален.');
  SELECT send_email((SELECT Email FROM Врач WHERE ID = OLD.Врач), 'Удаление приема', 'Ваш прием был удален.');
END;