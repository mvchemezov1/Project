-- При вставке новой поликлиники или больницы отправляем уведомление на email руководителя
CREATE TRIGGER send_hospital_registration_email
AFTER INSERT ON Поликлиника_Больница
BEGIN
  SELECT send_email((SELECT Email FROM Врач WHERE ID = NEW.Руководитель), 'Регистрация поликлиники/больницы', 'Новая поликлиника/больница была зарегистрирована в нашей базе данных.');
END;

-- При обновлении данных поликлиники или больницы отправляем уведомление на email руководителя
CREATE TRIGGER send_hospital_update_email
AFTER UPDATE ON Поликлиника_Больница
BEGIN
  SELECT send_email((SELECT Email FROM Врач WHERE ID = NEW.Руководитель), 'Обновление данных поликлиники/больницы', 'Данные поликлиники/больницы в нашей базе данных были обновлены.');
END;

-- При удалении поликлиники или больницы отправляем уведомление на email руководителя и удаляем связанные данные
CREATE TRIGGER delete_related_data_on_hospital_delete
BEFORE DELETE ON Поликлиника_Больница
BEGIN
  -- Удаляем связанные данные в других таблицах, например, Прием
  DELETE FROM Прием WHERE Врач = OLD.Руководитель;

  -- Отправляем уведомление на email
  SELECT send_email((SELECT Email FROM Врач WHERE ID = OLD.Руководитель), 'Удаление данных поликлиники/больницы', 'Данные поликлиники/больницы в нашей базе данных были удалены.');
END;