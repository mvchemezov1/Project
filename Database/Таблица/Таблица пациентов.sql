CREATE TABLE Пациент (
ID INT PRIMARY KEY,
Фамилия VARCHAR(255) NOT NULL,
Имя VARCHAR(255) NOT NULL,
Отчество VARCHAR(255) NOT NULL,
Дата_рождения DATE NOT NULL,
Пол VARCHAR(10) NOT NULL,
Адрес_проживания VARCHAR(255) NOT NULL,
Телефон VARCHAR(20) NOT NULL,
Email VARCHAR(100) NOT NULL,
Полис_ОМС VARCHAR(50) NOT NULL
);
