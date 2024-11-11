-- При вставке новой услуги отправляем уведомление на email администратора
CREATE TRIGGER send_service_registration_email
AFTER INSERT ON Медицинские_услуги
BEGIN
  SELECT send_email('admin@example.com', 'Новая медицинская услуга', 'Новая медицинская услуга была добавлена в нашу базу данных.');
END;

-- При обновлении данных услуги отправляем уведомление на email администратора
CREATE TRIGGER send_service_update_email
AFTER UPDATE ON Медицинские_услуги
BEGIN
  SELECT send_email('admin@example.com', 'Обновление медицинской услуги', 'Данные медицинской услуги в нашей базе данных были обновлены.');
END;

-- При удалении услуги отправляем уведомление на email администратора и удаляем связанные данные
CREATE TRIGGER delete_related_data_on_service_delete
BEFORE DELETE ON Медицинские_услуги
BEGIN
  -- Удаляем связанные данные в других таблицах, например, Результаты_анализов_и_исследований
  DELETE FROM Результаты_анализов_и_исследований WHERE Услуга = OLD.ID;

  -- Отправляем уведомление на email
  SELECT send_email('admin@example.com', 'Удаление медицинской услуги', 'Данные медицинской услуги в нашей базе данных были удалены.');
END;