CREATE TABLE Медицинские_документы (
  ID INT PRIMARY KEY,
  Пациент INT NOT NULL,
  Тип_документа VARCHAR(50) NOT NULL,
  Дата_выдачи DATE NOT NULL,
  Врач INT NOT NULL,
  Содержание_документа TEXT,
  FOREIGN KEY (Пациент) REFERENCES Пациент(ID),
  FOREIGN KEY (Врач) REFERENCES Врач(ID)
);
