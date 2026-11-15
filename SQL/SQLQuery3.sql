CREATE TABLE Employee (
    employee_id INT ,
    employee_name VARCHAR(50),
    department_id INT,
    position VARCHAR(50),
    salary DECIMAL(10, 2)
);


INSERT INTO Employee (employee_id, employee_name, department_id, position, salary)
VALUES 
(1, 'Alice Johnson', 101, 'Software Engineer', 70000),
(2, 'Bob Smith', 102, 'Data Scientist', 80000),
(3, 'Carol White', 103, 'Project Manager', 75000),
(4, 'David Brown', 104, 'Quality Assurance', 60000),
(5, 'Eva Green', 105, 'HR Specialist', 55000),
(6, 'Frank Martin', 101, 'Software Engineer', 70000),
(3, 'Carol White', 103, 'Project Manager', 75000),
(4, 'David Brown', 104, 'Quality Assurance', 60000)

select * from employee

--query 1. Remove duplicate values from employee table 
select distinct * from employee

-- query 2. write a query to find out duplicate values from employee 
with cte as(
select *, row_number() over(partition by employee_id order by employee_id ) as rn from employee
)
select * from cte where rn=2
-- query 3. write a query to find out highest earning employee based on each position 
select max(salary), position from employee group by position 

--query 4. write a query to get top 3 highest earning employee 
select top 3 * from employee order by salary desc 

with cte as(
select distinct * from employee)
select top 3* from cte order by salary desc

-- query 5 write a query to get top 3 lowest earning employee 

with cte as(
select distinct * from employee)
select top 3 * from cte order by salary asc 




CREATE TABLE Emp (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10, 2),
    location VARCHAR(50)
);

INSERT INTO Emp (employee_id, employee_name, department, salary, location)
VALUES 
(1, 'Alice Johnson', 'Engineering', 75000, 'New York'),
(2, 'Bob Smith', 'Data Science', 85000, 'San Francisco'),
(3, 'Carol White', 'Human Resources', 65000, 'Chicago'),
(4, 'David Brown', 'Engineering', 78000, 'Austin'),
(5, 'Eva Green', 'Marketing', 70000, 'Seattle'),
(6, 'Frank Martin', 'Data Science', 82000, 'New York'),
(7, 'Grace Lee', 'Finance', 90000, 'Los Angeles'),
(8, 'Harry Clark', 'Sales', 72000, 'Chicago'),
(9, 'Ivy Baker', 'Human Resources', 67000, 'Austin'),
(10, 'Jack Wilson', 'Marketing', 71000, 'San Francisco'),
(11, 'Karen Evans', 'Engineering', 76000, 'Seattle'),
(12, 'Leo Adams', 'Data Science', 84000, 'New York'),
(13, 'Mona Scott', 'Finance', 88000, 'Los Angeles'),
(14, 'Nate Perry', 'Sales', 74000, 'Chicago'),
(15, 'Olivia Cooper', 'Engineering', 78000, 'Austin');

select *from emp

--query 5 write a query to find out 2nd highest salary employee

with cte as(
select * , row_number() over(order by salary desc) rn from emp
)
select * from cte where rn=3

--query 6 write a query to get 2nd lowest earning employee 
with cte as(
select * , row_number() over(order by salary asc) rn from emp
)
select * from cte where rn=2

--query 7 write a query to get 2nd highest salary based on each department 

with cte as(
select * , row_number() over(partition by department order by salary desc) as rn from emp
)
select * from cte where rn=2

--query 8 write query to get 3rd lowest salary based on each location 
with cte as(
select * , row_number() over(partition by location order by salary asc) as rn from emp
)
select * from cte where rn=3
--query 9 write a query to get bottom 2 salary based on each location 

with cte as(
select * ,row_number() over(partition by location order by salary asc) as rn from emp
)
select * from cte where rn in (1,2)

--query 10 write a query to get top 2 salary based on each department 

with cte as(
select * ,row_number() over(partition by location order by salary desc) rn from emp
)
select * from cte where rn in (1,2)


---join related que

create table table1  (id int) 
Insert into table1 values(1),(1),(1),(1),(1)

create table table2 (id int)
Insert into table2 values(1),(1),(1),(1),(1),(null)


select * from table1
select * from table2

--query1. how many rows will you get when you will perform inner join 

select * from table1 join table2 on table1.id=table2.id

--query1. how many rows will you get when you will perform left join 
select * from table1 left join table2 on table1.id=table2.id

--query1. how many rows will you get when you will perform right join 

select * from table1 right join table2 on table1.id=table2.id
--query1. how many rows will you get when you will perform full join 

select * from table1 full join table2 on table1.id=table2.id


insert into table1 values(null)


--------
select * from employee
select * from table3
select * from table4

--query : write a query to create new table with same schema as employee table (only schema)
select * into table3 from employee where 1=2
--query 2: create new table same like employee table (data + schema) 
select * into table4 from employee where 1=1
--query 3 : write a query where employee_name starts with letter A
select * from employee where employee_name like 'A%'
--query 4 : write a query where department_id starts letter and ends letter is same 
select * from employee where left(department_id,1)=right(department_id,1)

--query 5 : write a query to get records in xml format 
select * from employee for xml auto

--query 6 : how to get current date 
select getdate()
select CURRENT_TIMESTAMP

--query 7: query to get cuurent month 
select month(getdate())

--query 8: query to get current year \

select year(getdate())




---question 1 . difference betwwn Union and Union all

UNION: Combines the results of two queries and removes duplicate rows.
UNION ALL: Combines the results of two queries without removing duplicate

--question 2 . primary key vs union difference 
primary key - Used to serve as a unique identifier for each row in a table.
Cannot accept NULL values.
Only one primary key

UNIQUE KEY- Uniquely determines a row that isn�t the primary key.
Can accept NULL values.
More than one unique key

emp_id  primary key     mobile nmber unique




--question difference between rank and dense rank 
RANK(): Skips ranks if there are ties.
DENSE_RANK(): Does not skip ranks, even if there are ties.

rank      dense rank     salary 
1          1             100000
2          2              70000
2          2              70000
4           3             50000


--questiuon 4 . delete vs drop vs truncate 

The TRUNCATE command helps us delete the complete records from an existing table

The DROP command drops the existing table from the database. It only requires the name of the table to be dropped.

The SQL DELETE command is a DML (Data Manipulation Language) command that deletes existing
records from the table in the database. It can delete one or more rows from the table
depending on the condition given with the WHERE clause

--question 5. what are different windows function 

Window functions perform calculations across a set of table rows related to the current row. Examples include:

ROW_NUMBER()
RANK()
DENSE_RANK()
AVG() OVER()

--question 6 . where and having clause difference
WHERE: Filters rows before grouping (GROUP BY).
HAVING: Filters groups created by GROUP BY.

--question 7. how to handle null values in sql 
Use functions like:
IS NULL or IS NOT NULL to filter records.
COALESCE(column, default_value) to replace NULL with a default value.




---important employee manager related sql question 

CREATE TABLE Emp4 (
    EmpID INT PRIMARY KEY,
    EmpName VARCHAR(50),
    ManagerID INT,
    Department VARCHAR(50)
);

INSERT INTO Emp4 (EmpID, EmpName, ManagerID, Department)
VALUES 
    (1, 'John', NULL, 'HR'),        -- John is the top-level manager
    (2, 'Alice', 1, 'Finance'),    -- Alice reports to John
    (3, 'Bob', 1, 'IT'),           -- Bob reports to John
    (4, 'Charlie', 2, 'Finance'),  -- Charlie reports to Alice
    (5, 'Eve', 3, 'IT');         

select * from emp4
-- Find out the employees manager details from employee table

select a.empname, b.empname as manager_name , a.department from emp4 a left join emp4 b 
on a.managerid=b.empid

-- query : write a query to find out cumulative sum of salary
select * from employee

select * , sum(salary) over(order by employee_id) as rn from employee


--- Fill null value with previous values 

CREATE TABLE Chocolate_Brands (
    chocolate_name VARCHAR(50),
    brand_name VARCHAR(50)
);

INSERT INTO Chocolate_Brands (chocolate_name, brand_name) VALUES
('KitKat', 'Nestle'),
('Perk', NULL),
('Munch', NULL),
('Dairy Milk', 'Cadbury'),
('5 Star', NULL),
('Silk', NULL);

select * from chocolate_brands


with cte as(
select * , row_number() over(order by (select null)) rn ,
case when brand_name is null then 0 else 1 end rn1
from chocolate_brands
)
,cte1 as(
select * , sum(rn1) over(order by rn) roll_sum from cte
)
select chocolate_name, brand_name , 
max(brand_name) over(partition by roll_sum) as new_brand_name from cte1


-- find new and repeated customer 

create table customer_orders (
order_id integer,
customer_id integer,
order_date date,
order_amount integer
);

insert into customer_orders values(1,100,cast('2022-01-01' as date),2000),(2,200,cast('2022-01-01' as date),2500),(3,300,cast('2022-01-01' as date),2100)
,(4,100,cast('2022-01-02' as date),2000),(5,400,cast('2022-01-02' as date),2200),(6,500,cast('2022-01-02' as date),2700)
,(7,100,cast('2022-01-03' as date),3000),(8,400,cast('2022-01-03' as date),1000),(9,600,cast('2022-01-03' as date),3000)


-- find new and repeated customer on each date 
select * from customer_orders



with first_visit_date as (
select customer_id , min(order_date) first_order from customer_orders
group by customer_id
),
final as(
select a.* , b.first_order ,case when order_date=first_order then 1 else 0 end new_customer,
case when order_date!=first_order then 1 else 0 end repeated_customer
from customer_orders a join first_visit_date b 
on a.customer_id=b.customer_id 
)
select sum(new_customer) new , sum(repeated_customer) as repeated , order_date from final
group by order_date

select * from first_visit_date



Bro, let's turn these SQL Server functions into a proper **hands-on SQL practice guide**. 🔥

I'll use SQL Server syntax and show **5 examples for every function**, including:

- Syntax
- Example query
- Expected output
- Practical explanation

## **1. Date Functions**

## **GETDATE()**

Returns the current database system date and time.

```
SELECT GETDATE() AS CurrentDateTime;
```

5 Examples

```
-- Example 1: Current date and time
SELECT GETDATE() AS CurrentDateTime;

-- Example 2: Current year
SELECT YEAR(GETDATE()) AS CurrentYear;

-- Example 3: Current month
SELECT MONTH(GETDATE()) AS CurrentMonth;

-- Example 4: Current day
SELECT DAY(GETDATE()) AS CurrentDay;

-- Example 5: Current date in dd/mm/yyyy format
SELECT CONVERT(VARCHAR(10), GETDATE(), 103)
       AS FormattedDate;
```

Example output for Example 5:

```
16/11/2026
```

## **YEAR(), MONTH(), DAY()**

Extract year, month, and day from a date.

```
SELECT
    YEAR('2026-11-16') AS YearValue,
    MONTH('2026-11-16') AS MonthValue,
    DAY('2026-11-16') AS DayValue;
```

Output:

| YearValue | MonthValue | DayValue |
| --------- | ---------- | -------- |
| 2026      | 11         | 16       |

5 Examples

```
-- Example 1
SELECT YEAR('2025-03-15') AS YearValue;
-- 2025

-- Example 2
SELECT MONTH('2025-03-15') AS MonthValue;
-- 3

-- Example 3
SELECT DAY('2025-03-15') AS DayValue;
-- 15

-- Example 4
SELECT YEAR('2024-12-31') AS YearValue,
       MONTH('2024-12-31') AS MonthValue,
       DAY('2024-12-31') AS DayValue;
-- 2024, 12, 31

-- Example 5: Extract birth year
SELECT YEAR('2003-08-21') AS BirthYear;
-- 2003
```

## **DATEPART()**

Returns a specific date component as an integer.

```
SELECT DATEPART(quarter, '2026-11-16') AS QuarterValue;
```

Output: `4`

5 Examples

```
-- Example 1: Year
SELECT DATEPART(year, '2026-11-16');
-- 2026

-- Example 2: Month
SELECT DATEPART(month, '2026-11-16');
-- 11

-- Example 3: Quarter
SELECT DATEPART(quarter, '2026-11-16');
-- 4

-- Example 4: Day of year
SELECT DATEPART(dayofyear, '2026-11-16');
-- 320

-- Example 5: Week number
SELECT DATEPART(week, '2026-11-16');
-- 47 (depends on DATEFIRST setting)
```

Common date parts:

| Date part | Meaning                |
| --------- | ---------------------- |
| year      | Year                   |
| month     | Month                  |
| day       | Day                    |
| quarter   | Quarter                |
| week      | Week number            |
| weekday   | Day of week            |
| hour      | Hour                   |
| minute    | Minute                 |
| second    | Second                 |
| dayofyear | Day number within year |

## **DATENAME()**

Returns the name of a date component as text.

```
SELECT DATENAME(month, '2026-11-16') AS MonthName;
```

Output: `November`

5 Examples

```
-- Example 1: Month name
SELECT DATENAME(month, '2026-11-16');
-- November

-- Example 2: Weekday name
SELECT DATENAME(weekday, '2026-11-16');
-- Monday

-- Example 3: Year as text
SELECT DATENAME(year, '2026-11-16');
-- 2026

-- Example 4: Quarter as text
SELECT DATENAME(quarter, '2026-11-16');
-- 4

-- Example 5: Day name
SELECT DATENAME(day, '2026-11-16');
-- 16
```

## **DATEADD()**

Adds or subtracts an interval from a date.

```
SELECT DATEADD(day, 7, '2026-11-16') AS FutureDate;
```

Output: `2026-11-23`

5 Examples

```
-- Example 1: Add 7 days
SELECT DATEADD(day, 7, '2026-11-16');
-- 2026-11-23

-- Example 2: Subtract 10 days
SELECT DATEADD(day, -10, '2026-11-16');
-- 2026-11-06

-- Example 3: Add 3 months
SELECT DATEADD(month, 3, '2026-11-16');
-- 2027-02-16

-- Example 4: Add 2 years
SELECT DATEADD(year, 2, '2026-11-16');
-- 2028-11-16

-- Example 5: Add 5 hours
SELECT DATEADD(hour, 5, '2026-11-16 10:00:00');
-- 2026-11-16 15:00:00
```

## **DATEDIFF()**

Counts the number of date boundaries crossed between two dates.

```
SELECT DATEDIFF(day, '2026-11-01', '2026-11-16')
       AS Difference;
```

Output: `15`

5 Examples

```
-- Example 1: Difference in days
SELECT DATEDIFF(day, '2026-11-01', '2026-11-16');
-- 15

-- Example 2: Difference in months
SELECT DATEDIFF(month, '2026-01-01', '2026-06-01');
-- 5

-- Example 3: Difference in years
SELECT DATEDIFF(year, '2020-01-01', '2026-01-01');
-- 6

-- Example 4: Difference in hours
SELECT DATEDIFF(hour,
    '2026-11-16 10:00:00',
    '2026-11-16 15:00:00');
-- 5

-- Example 5: Employee experience
SELECT DATEDIFF(year,
    '2020-05-10',
    '2026-11-16') AS ExperienceYears;
-- 6
```

**Important:** `DATEDIFF(year,...)` counts year boundaries, not completed anniversaries. For exact age or completed experience, extra logic may be needed.

## **EOMONTH()**

Returns the last day of a month.

```
SELECT EOMONTH('2026-11-16') AS MonthEnd;
```

Output: `2026-11-30`

5 Examples

```
-- Example 1: End of current month
SELECT EOMONTH('2026-11-16');
-- 2026-11-30

-- Example 2: End of previous month
SELECT EOMONTH('2026-11-16', -1);
-- 2026-10-31

-- Example 3: End of next month
SELECT EOMONTH('2026-11-16', 1);
-- 2026-12-31

-- Example 4: End of February in leap year
SELECT EOMONTH('2024-02-10');
-- 2024-02-29

-- Example 5: End of December
SELECT EOMONTH('2026-12-05');
-- 2026-12-31
```

# **2. String Functions**

## **CONCAT()**

Combines multiple strings. NULL values are treated as empty strings.

```
-- Example 1
SELECT CONCAT('SQL', ' Server');
-- SQL Server

-- Example 2
SELECT CONCAT('Hello', ' ', 'World');
-- Hello World

-- Example 3
SELECT CONCAT('Student', 101);
-- Student101

-- Example 4
SELECT CONCAT('Price: ', 500);
-- Price: 500

-- Example 5
SELECT CONCAT('A', NULL, 'B');
-- AB
```

## **CONCAT_WS()**

Combines strings using a specified separator. NULL values are skipped.

```
-- Example 1
SELECT CONCAT_WS('-', '2026', '11', '16');
-- 2026-11-16

-- Example 2
SELECT CONCAT_WS(' ', 'John', 'Doe');
-- John Doe

-- Example 3
SELECT CONCAT_WS(',', 'SQL', 'Python', 'Java');
-- SQL,Python,Java

-- Example 4
SELECT CONCAT_WS('-', 'India', NULL, 'Delhi');
-- India-Delhi

-- Example 5
SELECT CONCAT_WS('/', '10', '20', '30');
-- 10/20/30
```

## **SUBSTRING()**

Extracts characters from a specified position.

Syntax:

```
SUBSTRING(expression, start, length)
```

```
-- Example 1
SELECT SUBSTRING('Database', 1, 4);
-- Data

-- Example 2
SELECT SUBSTRING('Database', 5, 4);
-- base

-- Example 3
SELECT SUBSTRING('SQL Server', 1, 3);
-- SQL

-- Example 4
SELECT SUBSTRING('Programming', 4, 3);
-- gra

-- Example 5
SELECT SUBSTRING('ABCDEFGHIJ', 3, 5);
-- CDEFG
```

## **LEFT()**

Extracts characters from the beginning of a string.

```
-- Example 1
SELECT LEFT('SQL Server', 3);
-- SQL

-- Example 2
SELECT LEFT('Database', 4);
-- Data

-- Example 3
SELECT LEFT('Programming', 6);
-- Progra

-- Example 4
SELECT LEFT('India', 2);
-- In

-- Example 5
SELECT LEFT('BlackForge', 5);
-- Black
```

## **RIGHT()**

Extracts characters from the end of a string.

```
-- Example 1
SELECT RIGHT('SQL Server', 6);
-- Server

-- Example 2
SELECT RIGHT('Database', 4);
-- base

-- Example 3
SELECT RIGHT('Programming', 4);
-- ming

-- Example 4
SELECT RIGHT('India', 3);
-- dia

-- Example 5
SELECT RIGHT('BlackForge', 5);
-- Forge
```

## **TRIM()**

Removes leading and trailing spaces.

```
-- Example 1
SELECT TRIM('  Hello  ');
-- Hello

-- Example 2
SELECT TRIM('   SQL Server   ');
-- SQL Server

-- Example 3
SELECT TRIM('  Database  ');
-- Database

-- Example 4
SELECT TRIM('   India   ');
-- India

-- Example 5
SELECT TRIM('   Python   ');
-- Python
```

## **REPLACE()**

Replaces all occurrences of a substring.

```
-- Example 1
SELECT REPLACE('2026/11/16', '/', '-');
-- 2026-11-16

-- Example 2
SELECT REPLACE('SQL Server', 'Server', 'Database');
-- SQL Database

-- Example 3
SELECT REPLACE('banana', 'a', 'o');
-- bonono

-- Example 4
SELECT REPLACE('Hello World', 'World', 'SQL');
-- Hello SQL

-- Example 5
SELECT REPLACE('100-200-300', '-', '/');
-- 100/200/300
```

## **LEN()**

Returns the number of characters, excluding trailing spaces.

```
-- Example 1
SELECT LEN('SQL');
-- 3

-- Example 2
SELECT LEN('Database');
-- 8

-- Example 3
SELECT LEN('Programming');
-- 11

-- Example 4
SELECT LEN('Hello World');
-- 11

-- Example 5
SELECT LEN('SQL   ');
-- 3
```

## **UPPER()**

Converts text to uppercase.

```
-- Example 1
SELECT UPPER('sql');
-- SQL

-- Example 2
SELECT UPPER('database');
-- DATABASE

-- Example 3
SELECT UPPER('hello world');
-- HELLO WORLD

-- Example 4
SELECT UPPER('india');
-- INDIA

-- Example 5
SELECT UPPER('blackforge labs');
-- BLACKFORGE LABS
```

## **LOWER()**

Converts text to lowercase.

```
-- Example 1
SELECT LOWER('SQL');
-- sql

-- Example 2
SELECT LOWER('DATABASE');
-- database

-- Example 3
SELECT LOWER('HELLO WORLD');
-- hello world

-- Example 4
SELECT LOWER('INDIA');
-- india

-- Example 5
SELECT LOWER('BlackForge Labs');
-- blackforge labs
```

## **CHARINDEX()**

Finds the position of a substring.

```
-- Example 1
SELECT CHARINDEX('a', 'Database');
-- 2

-- Example 2
SELECT CHARINDEX('SQL', 'Learn SQL Server');
-- 7

-- Example 3
SELECT CHARINDEX('@', 'user@mail.com');
-- 5

-- Example 4
SELECT CHARINDEX('World', 'Hello World');
-- 7

-- Example 5
SELECT CHARINDEX('xyz', 'SQL Server');
-- 0
```

# **3. Numeric & Math Functions**

## **ROUND()**

Rounds a number to a specified decimal position.

```
-- Example 1
SELECT ROUND(15.678, 2);
-- 15.68

-- Example 2
SELECT ROUND(15.678, 1);
-- 15.7

-- Example 3
SELECT ROUND(15.678, 0);
-- 16

-- Example 4: Round to tens
SELECT ROUND(157.8, -1);
-- 160

-- Example 5: Truncate instead of rounding
SELECT ROUND(15.678, 2, 1);
-- 15.67
```

## **CEILING()**

Rounds upward to the nearest integer.

```
-- Example 1
SELECT CEILING(4.1);
-- 5

-- Example 2
SELECT CEILING(7.8);
-- 8

-- Example 3
SELECT CEILING(10.0);
-- 10

-- Example 4
SELECT CEILING(-4.1);
-- -4

-- Example 5
SELECT CEILING(99.01);
-- 100
```

## **FLOOR()**

Rounds downward to the nearest integer.

```
-- Example 1
SELECT FLOOR(4.9);
-- 4

-- Example 2
SELECT FLOOR(7.1);
-- 7

-- Example 3
SELECT FLOOR(10.0);
-- 10

-- Example 4
SELECT FLOOR(-4.1);
-- -5

-- Example 5
SELECT FLOOR(99.99);
-- 99
```

## **ABS()**

Returns the absolute value.

```
-- Example 1
SELECT ABS(-15);
-- 15

-- Example 2
SELECT ABS(25);
-- 25

-- Example 3
SELECT ABS(-99.50);
-- 99.50

-- Example 4
SELECT ABS(-1000);
-- 1000

-- Example 5
SELECT ABS(0);
-- 0
```

## **POWER()**

Raises a number to a specified power.

```
-- Example 1
SELECT POWER(2, 3);
-- 8

-- Example 2
SELECT POWER(5, 2);
-- 25

-- Example 3
SELECT POWER(10, 3);
-- 1000

-- Example 4
SELECT POWER(3, 4);
-- 81

-- Example 5
SELECT POWER(4, 0);
-- 1
```

# **4. Conversion & NULL-Handling Functions**

## **ISNULL()**

Replaces NULL with a specified value.

```
-- Example 1
SELECT ISNULL(NULL, 0);
-- 0

-- Example 2
SELECT ISNULL(NULL, 'Unknown');
-- Unknown

-- Example 3
SELECT ISNULL(500, 0);
-- 500

-- Example 4
SELECT ISNULL(NULL, 'India');
-- India

-- Example 5
SELECT ISNULL(NULL, 1000);
-- 1000
```

### **Practical table example**

```
CREATE TABLE Employees (
    EmployeeID INT,
    EmployeeName VARCHAR(50),
    Bonus INT
);

INSERT INTO Employees VALUES
(1, 'Aman', 5000),
(2, 'Rahul', NULL),
(3, 'Priya', 3000);
```

```
SELECT EmployeeName,
       ISNULL(Bonus, 0) AS Bonus
FROM Employees;
```

Output:

| EmployeeName | Bonus |
| ------------ | ----- |
| Aman         | 5000  |
| Rahul        | 0     |
| Priya        | 3000  |

## **COALESCE()**

Returns the first non-NULL value.

```
-- Example 1
SELECT COALESCE(NULL, NULL, 100);
-- 100

-- Example 2
SELECT COALESCE(NULL, 'India', 'USA');
-- India

-- Example 3
SELECT COALESCE(NULL, NULL, NULL, 500);
-- 500

-- Example 4
SELECT COALESCE('SQL', NULL, 'Python');
-- SQL

-- Example 5
SELECT COALESCE(NULL, NULL, 'Unknown');
-- Unknown
```

### **Practical example**

```
SELECT COALESCE(NULL, NULL, 'No Data')
       AS Result;
```

Output:

| Result  |
| ------- |
| No Data |

## **CAST()**

Converts one data type into another.

```
-- Example 1
SELECT CAST(123 AS VARCHAR(10));
-- 123 (text)

-- Example 2
SELECT CAST('100' AS INT);
-- 100

-- Example 3
SELECT CAST(25.75 AS INT);
-- 25

-- Example 4
SELECT CAST('2026-11-16' AS DATE);
-- 2026-11-16

-- Example 5
SELECT CAST(100 AS DECIMAL(10,2));
-- 100.00
```

## **CONVERT()**

Converts data types and supports formatting styles.

```
-- Example 1
SELECT CONVERT(INT, '100');
-- 100

-- Example 2
SELECT CONVERT(VARCHAR(10), 123);
-- 123

-- Example 3
SELECT CONVERT(VARCHAR(10),
       GETDATE(), 103);
-- 16/11/2026

-- Example 4
SELECT CONVERT(VARCHAR(10),
       GETDATE(), 105);
-- 16-11-2026

-- Example 5
SELECT CONVERT(VARCHAR(10),
       GETDATE(), 110);
-- 11-16-2026
```

### **Important date styles**

| Style | Format              |
| ----- | ------------------- |
| 103   | dd/mm/yyyy          |
| 104   | dd.mm.yyyy          |
| 105   | dd-mm-yyyy          |
| 110   | mm-dd-yyyy          |
| 111   | yyyy/mm/dd          |
| 112   | yyyymmdd            |
| 120   | yyyy-mm-dd hh:mi:ss |

## **TRY_CAST()**

Attempts conversion. If conversion fails, returns NULL instead of an error.

```
-- Example 1
SELECT TRY_CAST('100' AS INT);
-- 100

-- Example 2
SELECT TRY_CAST('ABC' AS INT);
-- NULL

-- Example 3
SELECT TRY_CAST('25.50' AS DECIMAL(10,2));
-- 25.50

-- Example 4
SELECT TRY_CAST('2026-11-16' AS DATE);
-- 2026-11-16

-- Example 5
SELECT TRY_CAST('Hello' AS DATE);
-- NULL
```

## **TRY_CONVERT()**

Attempts conversion using CONVERT syntax but safely returns NULL when conversion fails.

```
-- Example 1
SELECT TRY_CONVERT(INT, '100');
-- 100

-- Example 2
SELECT TRY_CONVERT(INT, 'ABC');
-- NULL

-- Example 3
SELECT TRY_CONVERT(DATE, '2026-11-16');
-- 2026-11-16

-- Example 4
SELECT TRY_CONVERT(DECIMAL(10,2), '99.50');
-- 99.50

-- Example 5
SELECT TRY_CONVERT(DATE, 'InvalidDate');
-- NULL
```

# **5. Bonus: Real SQL Practice Using These Functions**

Let's combine multiple functions in realistic SQL queries.

### **Example 1: Extract employee joining year**

```
SELECT EmployeeName,
       YEAR(JoiningDate) AS JoiningYear
FROM Employees;
```

### **Example 2: Calculate employee tenure**

```
SELECT EmployeeName,
       DATEDIFF(year, JoiningDate, GETDATE())
       AS YearsWorked
FROM Employees;
```

Note: This counts year boundaries, not necessarily completed years of service.

### **Example 3: Display employee email domain**

```
SELECT Email,
       SUBSTRING(
           Email,
           CHARINDEX('@', Email) + 1,
           LEN(Email)
       ) AS Domain
FROM Employees;
```

### **Example 4: Handle NULL salary**

```
SELECT EmployeeName,
       ISNULL(Salary, 0) AS Salary
FROM Employees;
```

### **Example 5: Calculate discounted product price**

```
SELECT ProductName,
       Price,
       ROUND(Price * 0.90, 2) AS DiscountedPrice
FROM Products;
```

### **Example 6: Find employees joining this month**

```
SELECT *
FROM Employees
WHERE MONTH(JoiningDate) = MONTH(GETDATE())
  AND YEAR(JoiningDate) = YEAR(GETDATE());
```

### **Example 7: Find transactions from the last 30 days**

```
SELECT *
FROM Transactions
WHERE TransactionDate >= DATEADD(day, -30, GETDATE());
```

### **Example 8: Display month name**

```
SELECT EmployeeName,
       DATENAME(month, JoiningDate) AS JoiningMonth
FROM Employees;
```

### **Example 9: Clean employee names**

```
SELECT UPPER(TRIM(EmployeeName)) AS CleanName
FROM Employees;
```

### **Example 10: Convert invalid numeric data safely**

```
SELECT TRY_CAST('2500' AS INT) AS Amount1,
       TRY_CAST('ABC' AS INT) AS Amount2;
```

Output:

| Amount1 | Amount2 |
| ------- | ------- |
| 2500    | NULL    |

## **Quick Revision Cheat Sheet**

| Function    | Main purpose                       |
| ----------- | ---------------------------------- |
| GETDATE     | Current date/time                  |
| YEAR        | Extract year                       |
| MONTH       | Extract month                      |
| DAY         | Extract day                        |
| DATEPART    | Extract numeric date part          |
| DATENAME    | Extract textual date part          |
| DATEADD     | Add/subtract date interval         |
| DATEDIFF    | Calculate date boundary difference |
| EOMONTH     | Last day of month                  |
| CONCAT      | Combine strings                    |
| CONCAT_WS   | Combine with separator             |
| SUBSTRING   | Extract middle characters          |
| LEFT        | Extract beginning characters       |
| RIGHT       | Extract ending characters          |
| TRIM        | Remove leading/trailing spaces     |
| REPLACE     | Replace text                       |
| LEN         | Count characters                   |
| UPPER       | Uppercase                          |
| LOWER       | Lowercase                          |
| CHARINDEX   | Find substring position            |
| ROUND       | Round numbers                      |
| CEILING     | Round upward                       |
| FLOOR       | Round downward                     |
| ABS         | Absolute value                     |
| POWER       | Exponentiation                     |
| ISNULL      | Replace NULL                       |
| COALESCE    | First non-NULL value               |
| CAST        | Type conversion                    |
| CONVERT     | Type conversion + formatting       |
| TRY_CAST    | Safe type conversion               |
| TRY_CONVERT | Safe conversion + formatting       |

If you want, next we can do **100 SQL practice questions covering all these functions, from beginner to interview-level, with an Employees, Products, Orders, and Customers database.** 🔥









