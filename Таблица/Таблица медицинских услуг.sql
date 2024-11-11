CREATE TABLE Медицинские_услуги (
  ID INT PRIMARY KEY,
  Название_услуги VARCHAR(255) NOT NULL,
  Описание_услуги TEXT NOT NULL,
  Цена DECIMAL(10, 2) NOT NULL,
  Срок_исполнения INT
);
