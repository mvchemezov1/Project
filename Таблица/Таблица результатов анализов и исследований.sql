CREATE TABLE Результаты_анализов_и_исследований (
  ID INT PRIMARY KEY,
  Прием INT NOT NULL,
  Услуга INT NOT NULL,
  Дата_получения_результата DATETIME NOT NULL,
  время_получения_результата DATETIME NOT NULL,
  Результат TEXT,
  FOREIGN KEY (Прием) REFERENCES Прием(ID),
  FOREIGN KEY (Услуга) REFERENCES Медицинские_услуги(ID)
);
