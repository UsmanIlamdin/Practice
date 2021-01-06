/*
SOLO learn DATABASE SQL tutorials
*/

-- SELECT * FROM `customers`
-- DISPLAY ALL TABLES AVIALABLE IN DATABASE
SHOW TABLES;
SELECT * FROM `offices`;

--Select all office in USA country
SELECT * FROM `offices`
WHERE  country='USA';

--Show  list of city and country 
-- whose offices in Tokyo
SELECT city , country
FROM `offices`
WHERE  city = 'Tokyo';
--Show with limit of 2
SELECT DISTINCT territory
FROM `offices` 
LIMIT 2;

--display cradit data with ordered form
SELECT  * 
FROM `customers`
ORDER BY creditLimit DESC;

SELECT * 
FROM `customers`;

SELECT  * 
FROM `customers`
ORDER BY  customerNumber DESC , customerName ASC;


SELECT * 
FROM `products`
WHERE buyPrice BETWEEN 20 AND 50;


SELECT * 
FROM `products` 
WHERE buyPrice IN (34.00,20.00);


SELECT * 
FROM `products` 
WHERE buyPrice IN (34.00)
OR
buyPrice > 90.00;


-- concatenate the customer colums
SELECT CONCAT(productName , '+',productLine)
FROM `products`;

SELECT *
FROM `employees`;

SELECT CONCAT(UPPER(firstName) ,'--' , UPPER(lastName))
FROM `employees` ;

SELECT *
FROM `orderdetails`;