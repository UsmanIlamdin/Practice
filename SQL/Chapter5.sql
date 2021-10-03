SELECT CONCAT(fname , '  ||  ' , minit , '  ||  ' , lname) 
FROM `employee`
WHERE NOT EXISTS(
    SELECT * 
    FROM `dependent`
    WHERE ssn = essn
);


SELECT CONCAT(fname , lname)
FROM `employee`
WHERE dno in (1,2,3);


USE company;

SELECT COUNT(*)
FROM `dept_locations` , `department`;


SELECT *
FROM `department`;



-- Nested QUERY CREATE

-- Select those pnumber in with mr smith work as 
USE company;

SELECT DISTINCT project.pnumber
FROM `project`
WHERE project.pnumber IN (
    SELECT project.pnumber
    FROM `employee` , `project` , `department`
    WHERE employee.ssn = department.mgrssn
    AND
    employee.lname = 'Smith'
    AND
    project.dnum = department.dnumber      
) 
    OR 
    project.pnumber IN (
    SELECT works_on.pno
    FROM `works_on` , `employee`
    WHERE works_on.essn = employee.ssn
    AND employee.lname = 'Smith'
    )
;


-- REtrive the name of all the `employee`
-- who `works_on` on all the projects controlled by 
-- `department` number 5

SELECT employee.fname , employee.lname
FROM `employee` , `works_on` , `project`
WHERE employee.ssn = works_on.essn 
    AND
    works_on.pno = project.pnumber
    AND
    project.dnum = 5; 


-- USEING NESTED form

SELECT employee.fname , employee.lname 
FROM `employee`
WHERE NOT EXISTS
((
    SELECT project.pnumber
    FROM `project`
    WHERE project.dnum = 5)
    EXCEPT
    (SELECT works_on.pno
    FROM `works_on`
    WHERE works_on.essn = employee.ssn   
));


-- select each project number , `project` name and 
-- number of employes `works_on` on it

SELECT project.pname , project.pnumber ,COUNT(*)
FROM `project` , `works_on`
WHERE project.pnumber = works_on.pno
GROUP BY project.pname , project.pnumber;


/*
Retrive all the department in `employee` TABLES
*/
SELECT DISTINCT(dno)      
FROM `employee`;

--this query will run but return only value of SSN
--at the start of count

SELECT employee.dno , AVG(employee.salary) , employee.ssn ,COUNT(*)
FROM `employee`
GROUP BY employee.dno;

/*
Create assertion that whenever salay entered for `employee` 
it should be less than `employee` manger salary
*/

-- CREATE ASSERTION SALARY_CONSTRAINTS
-- CHECK (
--     NOT EXIT( 
--         SELECT *
--         FROM `employee` AS E , `employee` as M , `department` as D
--         WHERE E.salary > M.salary AND D.dnumber = E.dno AND D.mgrssn = M.ssn
--     )
-- );

-- UPDATE `employee`
-- SET employee.salary = "200000.00"
-- WHERE employee.ssn = "666666601";


/*
CREATE A view forwhole employee currently working
*/
CREATE VIEW VIEW1
as  SELECT employee.fname , employee.lname , works_on.hours , project.pname
    FROM `employee` , `works_on` , `project`
    WHERE ssn= essn AND pno = pnumber
    ;

--A view that has the department name, manager name, and manager 
--salary for every department.

CREATE VIEW VIEW2
AS SELECT `employee`.fname , 
           `employee`.lname , 
          `department`.dname ,
          `employee`.salary as manager_salary
    FROM `employee` , `department`
    WHERE `employee`.ssn = `department`.mgrssn ;

SELECT * FROM VIEW2;

-- A view that has the employee name, supervisor name, 
--and employee salary for each employee who works in 
--the ‘Research’ department.
DROP VIEW VIEW3;
CREATE VIEW VIEW3
AS SELECT emp.fname as employees_name,
          emp.salary,
          supervisor.fname as supervisor_name                
    FROM `employee` AS emp,
         `employee` as supervisor,
         `department` as dep
    WHERE emp.dno = dep.dnumber AND
          dep.dname = "Research"
    ;

SELECT * FROM VIEW3;


-- A view that has the project name, controlling department name, 
-- number of employees, and total hours worked per week on the 
-- project for each project.
DROP VIEW VIEW4;
CREATE VIEW VIEW4
AS SELECT `department`.dname ,
          `project`.pname,
          `works_on`.hours,
          COUNT(*) as Total_Employees
    FROM `department` , `project` ,`works_on`
    WHERE `department`.dnumber = `project`.dnum
    AND `project`.pnumber = `works_on`.pno 
    GROUP BY `department`.dname ,`project`.pnumber ;


SELECT * FROM VIEW4;




CREATE VIEW VIEW5
AS SELECT `department`.dname ,
          `project`.pname,
          `works_on`.hours,
          COUNT(*) as Total_Employees
    FROM `department` , `project` ,`works_on`
    WHERE `department`.dnumber = `project`.dnum
    AND `project`.pnumber = `works_on`.pno 
    GROUP BY `department`.dname ,`project`.pnumber
    HAVING COUNT(*)>1;


SELECT * FROM VIEW5;






SELECT Dnumber, COUNT (*) 
FROM DEPARTMENT, EMPLOYEE 
WHERE Dnumber=Dno AND Salary>40000 AND Dno IN(
    SELECT Dno 
    FROM EMPLOYEE 
    GROUP BY Dno 
    HAVING COUNT (*) > 5
    );

SELECT dno , COUNT(ssn)
FROM `employee`
WHERE dno IN (
    SELECT dno 
    FROM `employee` 
    GROUP BY dno
    HAVING COUNT(ssn) > 5 AND salary >40000
);


SELECT *
FROM `employee`
ORDER BY salary DESC
LIMIT 1;

SELECT `department`.dnumber , `employee`.fname,MAX(`employee`.salary)
FROM `department` , `employee`
WHERE `department`.dnumber = `employee`.dno
GROUP BY `department`.dnumber;
