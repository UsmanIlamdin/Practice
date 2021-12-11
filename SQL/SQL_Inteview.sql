CREATE DATABASE ORG;
SHOW DATABASES;
USE ORG;

CREATE TABLE Worker (
	WORKER_ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	FIRST_NAME CHAR(25),
	LAST_NAME CHAR(25),
	SALARY INT(15),
	JOINING_DATE DATETIME,
	DEPARTMENT CHAR(25)
);

INSERT INTO Worker 
	(WORKER_ID, FIRST_NAME, LAST_NAME, SALARY, JOINING_DATE, DEPARTMENT) VALUES
		(001, 'Monika', 'Arora', 100000, '14-02-20 09.00.00', 'HR'),
		(002, 'Niharika', 'Verma', 80000, '14-06-11 09.00.00', 'Admin'),
		(003, 'Vishal', 'Singhal', 300000, '14-02-20 09.00.00', 'HR'),
		(004, 'Amitabh', 'Singh', 500000, '14-02-20 09.00.00', 'Admin'),
		(005, 'Vivek', 'Bhati', 500000, '14-06-11 09.00.00', 'Admin'),
		(006, 'Vipul', 'Diwan', 200000, '14-06-11 09.00.00', 'Account'),
		(007, 'Satish', 'Kumar', 75000, '14-01-20 09.00.00', 'Account'),
		(008, 'Geetika', 'Chauhan', 90000, '14-04-11 09.00.00', 'Admin');

CREATE TABLE Bonus (
	WORKER_REF_ID INT,
	BONUS_AMOUNT INT(10),
	BONUS_DATE DATETIME,
	FOREIGN KEY (WORKER_REF_ID)
		REFERENCES Worker(WORKER_ID)
        ON DELETE CASCADE
);

INSERT INTO Bonus 
	(WORKER_REF_ID, BONUS_AMOUNT, BONUS_DATE) VALUES
		(001, 5000, '16-02-20'),
		(002, 3000, '16-06-11'),
		(003, 4000, '16-02-20'),
		(001, 4500, '16-02-20'),
		(002, 3500, '16-06-11');


CREATE TABLE Title (
	WORKER_REF_ID INT,
	WORKER_TITLE CHAR(25),
	AFFECTED_FROM DATETIME,
	FOREIGN KEY (WORKER_REF_ID)
		REFERENCES Worker(WORKER_ID)
        ON DELETE CASCADE
);

INSERT INTO Title 
	(WORKER_REF_ID, WORKER_TITLE, AFFECTED_FROM) VALUES
 (001, 'Manager', '2016-02-20 00:00:00'),
 (002, 'Executive', '2016-06-11 00:00:00'),
 (008, 'Executive', '2016-06-11 00:00:00'),
 (005, 'Manager', '2016-06-11 00:00:00'),
 (004, 'Asst. Manager', '2016-06-11 00:00:00'),
 (007, 'Executive', '2016-06-11 00:00:00'),
 (006, 'Lead', '2016-06-11 00:00:00'),
 (003, 'Lead', '2016-06-11 00:00:00');





/*


Use Org database in this file 

*/



 /*
 Q-1. Write an SQL query to fetch “FIRST_NAME” from 
 Worker table using the alias name as <WORKER_NAME>.
 */

 SELECT `worker`.FIRST_NAME as Worker_Name 
 FROM `worker`;

 /*
 Q-2. Write an SQL query to fetch “FIRST_NAME” from Worker 
 table in upper case.
 */
 SELECT UCASE(`worker`.FIRST_NAME) as Worker_Name 
 FROM `worker`;


 /*
 Q-3. Write an SQL query to fetch unique values of DEPARTMENT
from Worker table.
 */

SELECT DISTINCT(`worker`.DEPARTMENT)
FROM `worker`;


/*
Q-4. Write an SQL query to print the first three characters of  
FIRST_NAME from Worker table.
*/

SELECT substring(`worker`.FIRST_NAME,1,3) 
FROM `worker`;

/*
Q-5. Write an SQL query to find the position of the alphabet 
(‘a’) in the first name column ‘Amitabh’ from Worker table.
*/



SELECT POSITION("A" IN first_name) 
FROM worker
WHERE first_name = "Amitabh";




SELECT INSTR(first_name, "A") 
FROM worker 
WHERE first_name = "Amitabh";


/*
Q-6. Write an SQL query to print the FIRST_NAME from 
Worker table after removing white spaces from the right side
*/

SELECT RTRIM(FIRST_NAME)    --   ltrim and rtrim  Lift and Right Trim.
FROM Worker;



/*
Q-7. Write An SQL Query To Print The DEPARTMENT 
From Worker Table After Removing White Spaces From The Left Side.*/
SELECT LTRIM(department) FROM worker;


/*
Q-8. Write An SQL Query That Fetches The Unique Values Of 
DEPARTMENT From Worker Table And Prints Its Length.
*/
SELECT DISTINCT(department), LENGTH(department) AS departmentNameLength 
FROM worker;    



/*
Q-9. Write An SQL Query To Print The FIRST_NAME From Worker 
Table After Replacing ‘A’ With ‘A’.
*/
SELECT REPLACE(first_name, "a", "A") FROM worker;



/*
Q-10. Write An SQL Query To Print The FIRST_NAME And 
LAST_NAME From Worker Table Into A Single Column COMPLETE_NAME. 
A Space Char Should Separate Them.
*/


SELECT CONCAT(`worker`.FIRST_NAME , "||" ,`worker`.LAST_NAME) as NAME
FROM `worker`; 


/*
Q-11. Write An SQL Query To Print All Worker Details 
From The Worker Table Order By FIRST_NAME Ascending.
*/
SELECT * FROM worker ORDER BY first_name ASC;


/*
Q-12. Write An SQL Query To Print All Worker Details From 
The Worker Table Order By FIRST_NAME Ascending And 
DEPARTMENT Descending.
*/




SELECT *
FROM `worker`
ORDER BY `worker`.FIRST_NAME ASC, `worker`.DEPARTMENT DESC;



/*
Q-13. Write An SQL Query To Print Details For Workers With 
The First Name As “Vipul” And “Satish” From Worker Table.
*/



SELECT *
FROM `worker`
WHERE `worker`.FIRST_NAME IN("Vipul" , "Satish");


/*
Q-14. Write An SQL Query To Print Details Of Workers 
Excluding First Names, “Vipul” And “Satish” From Worker Table.
*/


SELECT *
FROM `worker`
WHERE `worker`.FIRST_NAME NOT IN("Vipul" , "Satish");



/*
Q-15. Write An SQL Query To Print Details Of Workers 
With DEPARTMENT Name As “Admin”.
*/

SELECT *
FROM `worker`
WHERE `worker`.DEPARTMENT ="Admin";



/*
Q-16. Write An SQL Query To Print Details Of The Workers 
Whose FIRST_NAME Contains ‘A’.
*/


SELECT * 
FROM worker 
WHERE first_name LIKE "%a%";



/*
Q-17. Write An SQL Query To Print Details Of The Workers 
Whose FIRST_NAME Ends With ‘A’.
*/

SELECT * 
FROM worker 
WHERE first_name LIKE "%a";


/*
Q-18. Write An SQL Query To Print Details Of The Workers 
Whose FIRST_NAME Ends With ‘H’ And Contains Six Alphabets.*/


SELECT * 
FROM worker 
WHERE first_name LIKE "_____a";


/*
Q-19. Write An SQL Query To Print Details Of The Workers 
Whose SALARY Lies Between 100000 And 500000.
*/


SELECT *
FROM `worker`
WHERE `worker`.SALARY BETWEEN 100000 AND 500000;



/*
Q-20. Write An SQL Query To Print Details Of The 
Workers Who Have Joined In Feb’2014.
*/

SELECT * 
FROM worker 
WHERE joining_date LIKE "2014-02%";


SELECT * 
FROM worker 
WHERE year(joining_date) = 2014 AND month(joining_date) = 2;


/*
Q-21. Write An SQL Query To Fetch The Count Of 
Employees Working In The Department ‘Admin’.
*/

SELECT COUNT(`worker`.WORKER_ID) , `worker`.FIRST_NAME, `worker`.DEPARTMENT
FROM `worker`
WHERE `worker`.DEPARTMENT = "Admin"
GROUP BY `worker`.DEPARTMENT;



SELECT COUNT(*) 
FROM worker 
WHERE department = "Admin";



/*
Q-22. Write an SQL query to fetch worker names with 
salaries >= 50000 and <= 100000.
*/


SELECT * 
FROM `worker` 
WHERE `worker`.SALARY  >= 50000 
AND 
`worker`.SALARY <= 100000;




/*
Q-23. Write an SQL query to fetch the no. of workers 
for each department in the descending order.
*/


SELECT COUNT(`worker`.WORKER_ID) , `worker`.FIRST_NAME, `worker`.DEPARTMENT
FROM `worker`
GROUP BY `worker`.DEPARTMENT
ORDER BY COUNT(*) DESC;


/*
Q-24. Write an SQL query to print details of the Workers who are also Managers.
*/


SELECT *
FROM `worker` as W , `title` as T
WHERE W.WORKER_ID = T.WORKER_REF_ID 
AND
T.WORKER_TITLE = "Manager";


/*Q-25. Write an SQL query to fetch duplicate records 
having matching data in some fields of a table.

*/

SELECT WORKER_TITLE, AFFECTED_FROM, COUNT(*)
FROM Title
GROUP BY WORKER_TITLE, AFFECTED_FROM
HAVING COUNT(*) > 1;


/*
Q-26 Write an SQL query to show only odd rows from a table.
*/

SELECT *
FROM `worker`
WHERE MOD(WORKER_ID,2)!=0;

/*
Q-27 Write an SQL query to show only Even rows from a table.
*/

SELECT *
FROM `worker`
WHERE MOD(WORKER_ID,2)=0;





/*
Q-28. Write an SQL query to clone a new table from another table.
*/


  CREATE TABLE worker_clone SELECT * FROM `worker`;

--CREATE TABLE worker_clone LIKE `worker`;
SELECT * 
FROm worker_clone;


/*
Q-29. Write an SQL query to fetch intersecting records of two tables.
*/


SELECT *
FROM `worker` INNER JOIN 
`title` ON `worker`.WORKER_ID = `title`.WORKER_REF_ID;


/*
Q-30. Write an SQL query to show records from one table 
that another table does not have.
*/
SELECT *
FROM `worker` RIGHT JOIN 
`bonus` ON `worker`.WORKER_ID = `bonus`.WORKER_REF_ID;


/*
Q-31. Write an SQL query to show the current date and time.
*/

SELECT CURRENT_TIME();
SELECT CURDATE();


/*
Q-32. Write an SQL query to show the top n (say 10) records of a table.
*/


SELECT *
FROM `worker`
LIMIT 10 ;


/*
Q-33. Write an SQL query to determine the nth (say n=5) 
highest salary from a table.
*/

SELECT *
FROM `worker` W1
WHERE 2=(
	SELECT COUNT(DISTINCT( SALARY))
	FROM `worker` W2
	WHERE W2.SALARY > W1.SALARY

);

/*
Q-34. Write an SQL query to determine the 5th 
highest salary without using TOP or limit method.
*/


SELECT *
FROM `worker` W1
WHERE 4=(
	SELECT COUNT(DISTINCT( W2.SALARY))
	FROM `worker` W2
	WHERE W2.SALARY > W1.SALARY

);



/*
Q-35. Write an SQL query to fetch the list 
of employees with the same salary.
*/


SELECT *
FROM `worker` W1 , `worker` W2
WHERE W1.SALARY = W2.SALARY
AND
	  W1.WORKER_ID !=W2.WORKER_ID;



/*
Q-36. Write an SQL query to show the second highest salary from a table.
*/

SELECT max(`worker`.SALARY) 
FROM `worker` 
WHERE Salary not in (
	SELECT max(Salary) FROM Worker
	);



/*
Q-37. Write an SQL query to show one row twice in results from a table.
*/


SELECT FIRST_NAME, DEPARTMENT 
FROM worker W 
WHERE W.DEPARTMENT='HR' 
UNION ALL
SELECT FIRST_NAME, DEPARTMENT 
FROM Worker W1 
WHERE W1.DEPARTMENT='HR';

/*
Q-38. Write an SQL query to fetch intersecting records of two tables.
*/


SELECT *
FROM `worker` INNER JOIN `bonus`
ON `worker`.WORKER_ID = `bonus`.WORKER_REF_ID;

/*
Write an SQL query to fetch the first 50% records from a table.
*/

	SELECT *
	FROM WORKER
	WHERE WORKER_ID <= (
		SELECT count(WORKER_ID)/2 
		FROM Worker
		);


/*
Q-40. Write an SQL query to fetch the departments 
that have less than five people in it
*/


SELECT * , COUNT(`worker`.WORKER_ID) as 'COUNT OF NUMBER'
FROM `worker`
GROUP BY `worker`.DEPARTMENT
HAVING COUNT(`worker`.WORKER_ID) < 5;



SELECT DEPARTMENT, COUNT(WORKER_ID) as 'Number of Workers' 
FROM Worker 
GROUP BY DEPARTMENT 
HAVING COUNT(WORKER_ID) < 5;


/*
Q-41. Write an SQL query to show all departments along 
with the number of people in there.
*/


SELECT `worker`.DEPARTMENT , COUNT(`worker`.WORKER_ID) as 'COUNT OF NUMBER'
FROM `worker`
GROUP BY `worker`.DEPARTMENT;


/*
Q-42. Write an SQL query to show the last record from a table.
*/


SELECT * 
FROM Worker 
WHERE WORKER_ID = (
	SELECT max(WORKER_ID) 
	FROM Worker);


SELECT * 
FROM `worker`
ORDER BY `worker`.WORKER_ID DESC
LIMIT 1;



/*
Q-43. Write an SQL query to fetch the first row of a table.
*/



SELECT * 
FROM `worker`
LIMIT 1;


/*
Q-44. Write an SQL query to fetch the last five records from a table.
*/


SELECT * 
FROM `worker`
ORDER BY `worker`.WORKER_ID DESC
LIMIT 5;




/*
Q-45. Write an SQL query to print the name of employees 
having the highest salary in each department.
*/



SELECT `worker`.DEPARTMENT, `worker`.FIRST_NAME , MAX(`worker`.SALARY)
FROM `worker`
GROUP BY `worker`.DEPARTMENT;




SELECT t.DEPARTMENT,t.FIRST_NAME,t.Salary 
FROM(
	SELECT max(Salary) as TotalSalary,DEPARTMENT 
	FROM Worker 
	GROUP BY DEPARTMENT) as TempNew 
	Inner Join Worker t on TempNew.DEPARTMENT=t.DEPARTMENT 
 	and TempNew.TotalSalary=t.Salary;


/*
Q-46. Write an SQL query to fetch three max salaries from a table.
*/

SELECT DISTINCT(`worker`.SALARY), `worker`.FIRST_NAME 
FROM `worker`
ORDER BY `worker`.SALARY DESC
LIMIT 3;




