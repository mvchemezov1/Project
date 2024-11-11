-- При вставке нового документа отправляем уведомление на email пациенту и врачу
CREATE TRIGGER send_document_email
AFTER INSERT ON Медицинские_документы
BEGIN
  SELECT send_email((SELECT Email FROM Пациент WHERE ID = NEW.Пациент), 'Новый медицинский документ', 'У вас есть новый медицинский документ.');
  SELECT send_email((SELECT Email FROM Врач WHERE ID = NEW.Врач), 'Новый медицинский документ', 'У вашего пациента есть новый медицинский документ.');
END;

-- При обновлении данных документа отправляем уведомление на email пациенту и врачу
CREATE TRIGGER send_document_update_email
AFTER UPDATE ON Медицинские_документы
BEGIN
  SELECT send_email((SELECT Email FROM Пациент WHERE ID = NEW.Пациент), 'Обновление медицинского документа', 'Ваш медицинский документ был обновлен.');
  SELECT send_email((SELECT Email FROM Врач WHERE ID = NEW.Врач), 'Обновление медицинского документа', 'Медицинский документ вашего пациента был обновлен.');
END;

-- При удалении документа отправляем уведомление на email пациенту и врачу
CREATE TRIGGER delete_document_email
BEFORE DELETE ON Медицинские_документы
BEGIN
  -- Отправляем уведомление на email
  SELECT send_email((SELECT Email FROM Пациент WHERE ID = OLD.Пациент), 'Удаление медицинского документа', 'Ваш медицинский документ был удален.');
  SELECT send_email((SELECT Email FROM Врач WHERE ID = OLD.Врач), 'Удаление медицинского документа', 'Медицинский документ вашего пациента был удален.');
END;