SELECT *
FROM `employee`
WHERE `employee`.fname NOT IN  ("Jared","Jon","Justin");




SELECT *
FROM (SELECT *, ROW_NUMBER() OVER() as rn
        FROM `employee`) New_Table
WHERE MOD(New_Table.rn,2)=0;



-- dumb way to remove duplicate in table data

SELECT DISTINCT(`employee`.sex) , DISTINCT(`employee`.fname)
FROM `employee`;



--find Nth highest salary

-- for 2ND highest salary
SELECT MAX(`employee`.salary) as "Highest Salary"
FROM `employee` 
WHERE `employee`.salary NOT IN (
        SELECT MAX(`employee`.salary)
        FROM `employee`
        WHERE `employee`.salary

);


--Using more advance VALUE


SELECT `employee`.salary
FROM `employee`
ORDER BY `employee`.salary DESC;

SELECT E1.fname,E1.salary
FROM `employee` as E1
WHERE 2-1 = (SELECT COUNT(DISTINCT(E2.salary))
        FROM `employee` as E2
        WHERE E2.salary > E1.salary
);



