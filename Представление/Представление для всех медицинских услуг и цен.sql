CREATE VIEW V_MedicalServices AS
SELECT 
    У.ID AS Услуга_ID,
    У.Название_услуги AS Название,
    У.Описание_услуги AS Описание,
    У.Цена AS Цена
FROM 
    Медицинские_услуги У;
