-- Retrive the distict salary of all `employee`

SElECT DISTINCTROW employee.salary
FROM `employee` ; 

-- Retrive the all salary of all `employee`

SElECT ALL employee.salary
FROM `employee` ; 

-- '''
-- Retrive all the attributes of John B smith
-- '''
SELECT * 
FROM employee as E
WHERE fname = 'John' AND minit = 'B' AND lname = 'Smith' ;

-- '''
-- Retrive Bdate and address attributes of John B smith
-- '''
SELECT bdate , address
FROM employee
WHERE fname = 'John' AND minit = 'B' AND lname = 'Smith' ;

-- Retrive name and address of all `employee` who `works'
-- for reassch `department`

SELECT employee.fname , employee.address
FROM `employee` , `department`
WHERE employee.dno = department.dnumber 
AND
department.dname = 'Research';

USE company;

-- Ambiguous Attribute Names, Aliasing, Renaming, and Tuple Variables
SELECT *
FROM `employee` AS E , `department` AS D
WHERE E.dno = D.dnumber
AND
D.dname = "Research";

-- for every project located in 'Stanford' list prject name 
-- controlling `department` number and `department` manager
-- name , address


SELECT project.pname ,  employee.lname , employee.bdate , employee.address
FROM `employee` , `department` , `project`
WHERE employee.ssn = department.mgrssn 
AND
project.plocation = 'Stafford'
AND
department.dnumber = project.dnum ; 



-- Retrive all the project number in which 
-- lname = smith work either employess or as an 
-- worker

-- this query retrive all pnumber in which SMith work as an 
-- manager
SELECT DISTINCT(project.pnumber) , project.pname
FROM `employee` , `department` , `project`
WHERE employee.ssn = department.mgrssn 
AND 
department.dnumber = project.dnum
AND
employee.lname = 'Smith'   

UNION 
-- this query will return all pnumber in which smith work as an worker
SELECT DISTINCT(project.pnumber)  , project.pname
FROM `employee` , `works_on` , `project`
WHERE employee.ssn = works_on.essn 
AND
employee.lname = 'Smith'
AND
project.dnum = works_on.pno 
; 


-- select the employees who have addres Houston, TX

SELECT employee.fname , employee.minit , employee.lname
FROM `employee`
WHERE employee.address LIKE "% Houston, TX%" 
;


--find all `employee` who are born in 1950s
SELECT `employee`.fname , `employee`.bdate
FROM `employee`
WHERE employee.bdate LIKE "%195_______%";

--employee working on productX increase salary by 
--10 percent
SELECT `employee`.fname , `employee`.salary , (`employee`.salary)*1.1 as Inscreased_Salary
FROM `employee`  , `project` , `works_on`
WHERE `employee`.ssn = `works_on`.essn AND `works_on`.pno = `project`.pnumber
AND `project`.pname = "ProductX";

-- Retrive the name of `employee` whose work in 
-- `department` 5 and salary between 30k and 40k

SELECT employee.fname,employee.lname,employee.salary
FROM `employee`
WHERE employee.dno = 5
AND 
(employee.salary BETWEEN 30000 AND 40000);
--using and option              
SELECT employee.fname,employee.lname,employee.salary
FROM `employee`
WHERE employee.dno = 5
AND 
(employee.salary >= 30000 
AND 
employee.salary <=40000)
ORDER BY employee.fname  , employee.salary DESC;

-- Retrive the name of `employee` who  have same `dependent`
-- has his fname

SELECT employee.fname ,employee.lname 
FROM `employee` , `dependent`
WHERE employee.ssn = dependent.essn 
AND employee.fname = dependent.dependent_name ; 

-- Retrive the name of employee who have no    
-- `dependent` 


SELECT employee.fname , employee.lname
FROM `employee`
WHERE NOT EXISTS (
    SELECT *
    FROM `dependent`
    WHERE employee.ssn = dependent.essn 
);


-- Retrieve the social security numbers of 
-- all employees who work on project number 1, 
-- 2, or 3.


SELECT  DISTINCT works_on.essn
FROM    `works_on`		
WHERE    works_on.pno IN  (1, 2, 3) ;

-- -- Retrieve the names of all employees who do 
-- not have supervisors.
SELECT employee.fname , employee.lname , employee.superssn		
FROM	`employee`		
WHERE	employee.superssn IS  NULL;




