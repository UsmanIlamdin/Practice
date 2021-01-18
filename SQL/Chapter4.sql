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

