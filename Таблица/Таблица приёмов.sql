CREATE TABLE Прием (
  ID INT PRIMARY KEY,
  Врач INT NOT NULL,
  Пациент INT NOT NULL,
  Дата_и_время_приема DATETIME NOT NULL,
  Статус INT NOT NULL,
  Диагноз VARCHAR(255),
  FOREIGN KEY (Врач) REFERENCES Врач(ID),
  FOREIGN KEY (Пациент) REFERENCES Пациент(ID),
  FOREIGN KEY (Статус) REFERENCES Статус(ID)
);
