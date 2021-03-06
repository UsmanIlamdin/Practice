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


-- Retrive the distict salary of all `employee`

SElECT DISTINCTROW employee.salary
FROM `employee` ; 

-- Retrive the all salary of all `employee`

SElECT ALL employee.salary
FROM `employee` ; 


-- Retrive all the project number in which 
-- lname = smith work either employess or as an 
-- worker

-- this query retrive all pnumber in which SMith work as an 
-- manager
SELECT DISTINCTROW project.pnumber
FROM `employee` , `department` , `project`
WHERE employee.ssn = department.mgrssn 
AND 
department.dnumber = project.dnum
AND
employee.lname = 'Smith'   

UNION 
-- this query will return all pnumber in which smith work as an worker
SELECT DISTINCTROW project.pnumber
FROM `employee` , `works_on` , `project`
WHERE employee.ssn = works_on.essn 
AND
employee.lname = 'Smith'
AND
project.dnum = works_on.pno 
; 

