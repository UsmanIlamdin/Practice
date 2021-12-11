/*
Write a query in SQL to find the minimum and maximum number from the integer column:
*/
SELECT MIN(dnumber) as Minimun_Vale, MAX(dnumber) as Maximum_Value
FROM `department`;



/*
Write a query to access the first record from the SQL table?
*/

SELECT * 
FROM `department`
LIMIT 1;


--Write a query to access the last record from the table?

SELECT  LAST(`department`.dnumber)
FROM `department`;
--Write a query in Structured Query Language to view the current date and time.

SELECT GETDATE();  

SELECT SYSDATETIME();


