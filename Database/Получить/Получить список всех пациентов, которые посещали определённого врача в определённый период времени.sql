SELECT * FROM Пациент WHERE ID IN (SELECT Пациент FROM Прием WHERE Врач =? AND Дата_и_время_приема BETWEEN? AND?);