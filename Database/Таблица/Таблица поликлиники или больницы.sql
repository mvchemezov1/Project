CREATE TABLE Поликлиника_Больница (
ID INT PRIMARY KEY,
Название VARCHAR(255) NOT NULL,
Адрес VARCHAR(255) NOT NULL,
Телефон VARCHAR(20) NOT NULL,
Email VARCHAR(100) NOT NULL,
Руководитель INT NOT NULL,
FOREIGN KEY (Руководитель) REFERENCES Врач(ID)
);