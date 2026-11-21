SQL --> Structured query Language 
Database --> the place where we store our data
It is an organized collection of structured information (data) 

Database systems / Engines ==> MS SQL server (SSMS) , MySQL Workbench, Oracle SQL
DBMS (Database management systems ) --> It is a software that provides an interface between users and databases 

Functions of DBMS
Data Storage
Data retrival
Data Security
Data Integrity --> accuracy and consistency
Concurrent Access
Backup and Recovery

Types Of DBMS
RDBMS * Relational Database management System  ===> Uses tables with rows and columns (structured data)
NOSQL DBMS --> Unstructured Data
Object Oriented DBMS --> Store data as objects
Hierarchical DBMS -> tree like structure


Relational Databases have to maintain ACID Properties 
Atomicity ====== All Operations in a transaction succeed or fail together 
Consistency ==== Database remains in a valid state
Isolation ====== concurrent dont interfere with each other	 
Durability ===== Committed transactions are permanently saved 


# Database files --> 
1. Data files .mdf (primary data file ) -->
2. Transaction log files (.ldf) Records all transactions and data modification 
 ## DATABASE HEIRARCHY

Database
  -- Schemas  ==> Logical Structure that organizes and defines how data is stored 
    ---Tables
    ------Columns
    ------Indexes
    ------Constraints
    
    ---Views
     --stored Procedures
     --Functions
     --Triggers
  
  -- Security
    --Users
    --Roles
 --Service Broker



--> SQL Commands --> DDL , DML , DQL , TCL , DCL

==> DDL >> Data Definition Language --> CREATE, ALTER(Modify database objects), DROP --> Remove database objects

. Create Database sampledb
. USE sampledb
. Create schema schema1 
. drop database sampledb

==> DML >> Data Manipulation Language -->  INSERT --> add new data , UPDATE --> modify existing data , DELETE --> remove data (table/views level)
==> DQL >> Data Query Language --> SELECT 
==> DCL >> Data Control Language --> GRANT-  Give the permission, Revoke:/ Deny 
==> TCL >> Transaction Control Language --> begin transaction , commit , rollback , savepoint

> Begin Transaction
  ==> DO COMMANDS                 ] T-SQL Transaction SQL - variables , control flow statement, error handling
> rollback to previous state
> Commit to save permanent
> savepoint to save data at that point 




### CREATE TABLE
CREATE Table table1 (name char(255),class INT)

## DATA TYPES 
Tiny INT --> 0 to 255 byte
SmallINT  -32768 to 32767 2 bytes 
Int --> -2,147,483,648 to 2,147,483,647 4 bytes 
Big Int --> more big 8 bytes
Float, Decimal (decimal(P,S) 
Date --> DEFAULT FORMAT OF DATA is yyyy/MM/dd
DateTime --> hh:mm:ss
Char(max char) --> if entered char is short then automatically fill with blank rest of char
Varchar(max char) --> it is fixed even if we enter short characters then as well not fill up rest blocks
nchar(max char) -->if going to use unicode




## CONSTRAINTS --> rules that restrict data in a column 
1. not null --> ensures that a column cannot have a null value 
2. Unique --> ensures that all values in a column are different
3. primary Key --> a column which is unique and not null ( helps to identify the unique element )
It does not contain duplicate values and null values
We can only have one primary key in a table


4. Check --> ensures that a value in column satisfies a given condition

CREATE TABLE salesTable(productid int default 001, product_name VARCHAR(255) unique, REGION VARCHAR(255) PRIMARY KEY, price INT CHECK (price<1000))


5. Foreign Key --> It is a column in one table that refers to the primary key in another table
It ensures that the values in the foreign key column must exist in the primary key column of the referenced table

Person Table                 Orders Table
id   name   Age              Orderid    Name   Pid
1                                               3
2                                               2 ---> Foreign Key
3                                               |
------------------------------------------------|

7. Default --> sets a default value for a column if no value is specified
CREATE TABLE EMP2 (COUNTRY VARCHAR(255) DEFAULT 'INDIA')

CREATE TABLE orders (ordered int PRIMARY KEY, orderNo int , pid INT foreign Key references person(id))

6. index --> retrieves data from databases faster

CREATE index firstindex on salestables(product_name)
Indexes in SQL are special database structures that speed up data retrieval by allowing quick access to records instead of scanning the entire table. They act like a lookup system and play an important role in improving query performance and database efficiency.

It speed up queries (SELECT, JOIN, WHERE, ORDER BY).
Reduce disk I/O and improve efficiency in large tables.
Ensure data integrity with unique indexes.

Slower Writes: Every time you INSERT, UPDATE, or DELETE data, the database must also update the corresponding indexes.Storage Space:
Indexes take up additional disk space because they store a copy of the indexed data

Create: CREATE INDEX idx_name ON table_name (column_name);Remove: DROP INDEX idx_name; (Syntax varies by database, e.g., DROP INDEX idx_name ON table_name;

### ALTER TABLE
ALTER table1 ADD COLUMN subjects VARCHAR(255)
ALTER table student ADD COLUMN hobby VARCHAR(255)
ALTER table student DROP COLUMN hobby
ALTER table student RENAME COLUMN oldname TO newname
ALTER table student MODIFY/ALTER COLUMN name VARCHAR(25)
ALTER table student RENAME TO studentNew
ALTER table table_name ADD PRIMARY KEY studentID
ALTER table student ADD CONSTRAINT fk_name  FOREIGN KEY age REFERENCES olderTable(AgeID)
ALTER table student ADD CONSTRAINT NOT NULL salary 
ALTER table student ALTER column salary SET DEFAULT 0;



Bro, let's crack ALL major MS SQL Server `ALTER TABLE` commands from beginner to advanced. This is your practical DDL cheat sheet for modifying tables, columns, constraints, relationships, and storage. 🔥

# 1. ALTER TABLE syntax

```
ALTER TABLE table_name
ADD column_name datatype;
```

General syntax:

```
ALTER TABLE table_name
ADD | ALTER COLUMN | DROP COLUMN
| ADD CONSTRAINT | DROP CONSTRAINT
| SWITCH | REBUILD;
```

# 2. ADD columns

## Add one column

```
ALTER TABLE Students
ADD Email VARCHAR(100);
```

## Add multiple columns

```
ALTER TABLE Students
ADD
    Phone VARCHAR(15),
    DOB DATE,
    Salary DECIMAL(10,2);
```

## Add column with default

```
ALTER TABLE Students
ADD Country VARCHAR(50)
DEFAULT 'India';
```

## Add NOT NULL column

```
ALTER TABLE Students
ADD Status VARCHAR(20) NOT NULL
DEFAULT 'Active';
```

# 3. ALTER COLUMN

## Change datatype

```
ALTER TABLE Students
ALTER COLUMN Name VARCHAR(200);
```

## Change datatype from INT to BIGINT

```
ALTER TABLE Students
ALTER COLUMN StudentID BIGINT;
```

## Make column NOT NULL

```
ALTER TABLE Students
ALTER COLUMN Email VARCHAR(100) NOT NULL;
```

## Make column NULL

```
ALTER TABLE Students
ALTER COLUMN Email VARCHAR(100) NULL;
```

## Change column precision

```
ALTER TABLE Students
ALTER COLUMN Salary DECIMAL(12,2);
```

Important: Existing values must be compatible with the new datatype or nullability.

# 4. DROP COLUMN

## Drop one column

```
ALTER TABLE Students
DROP COLUMN Email;
```

## Drop multiple columns

```
ALTER TABLE Students
DROP COLUMN Phone, DOB;
```

Columns involved in constraints, indexes, or other dependencies may need those dependencies removed first.

# 5. PRIMARY KEY commands

## Add primary key

```
ALTER TABLE Students
ADD CONSTRAINT PK_Students
PRIMARY KEY (StudentID);
```

## Add composite primary key

```
ALTER TABLE Enrollment
ADD CONSTRAINT PK_Enrollment
PRIMARY KEY (StudentID, CourseID);
```

## Drop primary key

```
ALTER TABLE Students
DROP CONSTRAINT PK_Students;
```

## Add clustered primary key

```
ALTER TABLE Students
ADD CONSTRAINT PK_Students
PRIMARY KEY CLUSTERED (StudentID);
```

## Add nonclustered primary key

```
ALTER TABLE Students
ADD CONSTRAINT PK_Students
PRIMARY KEY NONCLUSTERED (StudentID);
```

# 6. FOREIGN KEY commands

## Add foreign key

```
ALTER TABLE Orders
ADD CONSTRAINT FK_Orders_Customers
FOREIGN KEY (CustomerID)
REFERENCES Customers(CustomerID);
```

## Composite foreign key

```
ALTER TABLE ChildTable
ADD CONSTRAINT FK_Child_Parent
FOREIGN KEY (A, B)
REFERENCES ParentTable(A, B);
```

## Foreign key with CASCADE

```
ALTER TABLE Orders
ADD CONSTRAINT FK_Orders_Customers
FOREIGN KEY (CustomerID)
REFERENCES Customers(CustomerID)
ON DELETE CASCADE
ON UPDATE CASCADE;
```

## Drop foreign key

```
ALTER TABLE Orders
DROP CONSTRAINT FK_Orders_Customers;
```

## Disable foreign key

```
ALTER TABLE Orders
NOCHECK CONSTRAINT FK_Orders_Customers;
```

## Enable and validate foreign key

```
ALTER TABLE Orders
WITH CHECK CHECK CONSTRAINT FK_Orders_Customers;
```

## Enable without validating existing data

```
ALTER TABLE Orders
CHECK CONSTRAINT FK_Orders_Customers;
```

# 7. UNIQUE constraints

## Add UNIQUE

```
ALTER TABLE Students
ADD CONSTRAINT UQ_Students_Email
UNIQUE (Email);
```

## Composite UNIQUE

```
ALTER TABLE Enrollment
ADD CONSTRAINT UQ_Student_Course
UNIQUE (StudentID, CourseID);
```

## Drop UNIQUE

```
ALTER TABLE Students
DROP CONSTRAINT UQ_Students_Email;
```

# 8. CHECK constraints

## Add CHECK

```
ALTER TABLE Students
ADD CONSTRAINT CK_Students_Age
CHECK (Age >= 18);
```

## Add salary CHECK

```
ALTER TABLE Employees
ADD CONSTRAINT CK_Employees_Salary
CHECK (Salary > 0);
```

## Drop CHECK

```
ALTER TABLE Students
DROP CONSTRAINT CK_Students_Age;
```

## Disable CHECK

```
ALTER TABLE Students
NOCHECK CONSTRAINT CK_Students_Age;
```

## Enable and validate CHECK

```
ALTER TABLE Students
WITH CHECK CHECK CONSTRAINT CK_Students_Age;
```

# 9. DEFAULT constraints

## Add DEFAULT

```
ALTER TABLE Students
ADD CONSTRAINT DF_Students_City
DEFAULT 'Delhi' FOR City;
```

## Add default for status

```
ALTER TABLE Employees
ADD CONSTRAINT DF_Employees_Status
DEFAULT 'Active' FOR Status;
```

## Drop DEFAULT constraint

```
ALTER TABLE Students
DROP CONSTRAINT DF_Students_City;
```

Note: SQL Server requires the default constraint name when dropping an existing default.


# 12. Indexes associated with tables

## Add index

```
CREATE INDEX IX_Students_Name
ON Students(Name);
```

## Add unique index

```
CREATE UNIQUE INDEX UX_Students_Email
ON Students(Email);
```

## Drop index

```
DROP INDEX IX_Students_Name
ON Students;
```

## Disable index

```
ALTER INDEX IX_Students_Name
ON Students DISABLE;
```

## Rebuild index

```
ALTER INDEX IX_Students_Name
ON Students REBUILD;
```

## Reorganize index

```
ALTER INDEX IX_Students_Name
ON Students REORGANIZE;
```



## 17. Practice lab: complete table modification

```

CREATE DATABASE SQLPractice;
GO

USE SQLPractice;
GO

CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    Name VARCHAR(100),
    Age INT,
    Salary DECIMAL(10,2)
);
GO

-- Add column
ALTER TABLE Employees
ADD Email VARCHAR(100);

-- Modify datatype
ALTER TABLE Employees
ALTER COLUMN Name VARCHAR(200);

-- Add default
ALTER TABLE Employees
ADD CONSTRAINT DF_Employees_Age
DEFAULT 25 FOR Age;

-- Add CHECK
ALTER TABLE Employees
ADD CONSTRAINT CK_Employees_Age
CHECK (Age >= 18);

-- Add UNIQUE
ALTER TABLE Employees
ADD CONSTRAINT UQ_Employees_Email
UNIQUE (Email);

-- Add another column
ALTER TABLE Employees
ADD DepartmentID INT;

-- Drop CHECK
ALTER TABLE Employees
DROP CONSTRAINT CK_Employees_Age;

-- Drop column
ALTER TABLE Employees
DROP COLUMN DepartmentID;

-- Rename column
EXEC sp_rename
    'Employees.Name',
    'EmployeeName',
    'COLUMN';

-- View final structure
EXEC sp_help 'Employees';





























### Alter Table1 drop name 

### DROP table table1


`````

CREATE TABLE student(id int,name varchar(255)), class int,marks int)

INSERT INTO student(## SPECIFY COLUMNS) VALUES(101,'Ram',2,80),(102,'Donald',4,78)
INSERT INTO student(name,class,marks) VALUES('Jack miller',7.99)

UPDATE student set name = 'Biden' WHERE name = 'Donald'
UPDATE student set id = 0 WHERE id is null
UPDATE student set marks = null WHERE marks = 80 and name = 'Ram'

DELETE FROM student where name= 101
DELETE FROM student where name='Ram'

DELETE student --> delete one by one row 
TRUNCATE table student --> delete all table 
delete could also use rollback , where condition , truncate once done is done


SELECT * FROM student  

DELETE VS TRUNCATE VS DROP 
DELETE - delete one by one row / SPECIFIC ROW / Complete DATA 
TRUNCATE - delete all table data 
DROP - delete table structure 


``````


TSQL

````
BEGIN TRANSACTION 
INSERT INTO STUDENT VALUES(101,'Ram',2,80)
COMMIT --> normal and do it 

BEGIN TRANSACTION 
INSERT INTO STUDENT VALUES(101,'Ram',2,80)
SAVEPOINT example --> save a point of time to rollback if needed
 

BEGIN TRANSACTION 
INSERT INTO STUDENT VALUES(101,'Ram',2,80)
ROLLBACK TO SAVEPOINT --> UNDO CHANGES IF SOMETHING GOES WRONG 

`````


GRANT SELECT ON STUDENT TO RISHABH_USERNAME
GRANT CREATE,ALTER,SELECT ON STUDENT TO Jaanvi

REVOKE SELECT ON STUDENT FROM RISHABH

DENY ALL ON STUDENT 

`````


```
SELECT * FROM [dbo] [superstore] WHERE state='Florida'

SELECT distinct order_date FROM [dbo].[superstore] WHERE order_date='2017-04-15'
> Distinct helps to search for unique records

# If I want to aggregate then have to use group by to separate column wise

SELECT oder_date.sum(sales) FROM [dbo].[superstore] group by Order_date

SELECT customer_name,max(sales),Order_date FROM [dbo].[Superstore] WHERE Order_date>'2017-04-15' GROUP BY customer_name,order_date ASC,DESC
# Ascending , Descending

## HAVING is USED after GROUP BY 

##> OPERATORS
1. ARITHMETIC OPERATORS= = +,-,/,*,%
2. Comparison Operators = < , > , = >= , <=
3. Logical Operators -=> they are used to combine two or more conditions (and, or , not)
4. Special Operators => IN , BETWEEN Operator used only in integers, exists check for values , LIKE (wildcard search) -> _ represents a Character
SELECT * FROM EMPL WHERE ID IN (1,2,3)


SELECT Customer_name,SUM(sales) FROM superstore
WHERE region= 'South' or region = 'WEST' or region = 'Central' GROUP BY customer name

SELECT Customer_name, SUM(sales) FROM superstore WHERE customer_name LIKE 'A%' (Checkfing for Capital A)
 
SELECT Customer_name,SUM(sales) FROM superstore WHERE customer_name LIKE '[AEIOU]%' # MEans could be anything FROM range


## SQL command Structure
SELECT FROM WHERE GROUP BY ORDER BY

---- Order of operation / Execution

SELECT --> 5
customer_name, SUM(sales) 
FROM superstore  ----> 1
WHERE region = 'West' ---> 2
GROUP BY customer_name  --> 3
HAVING sum(sales)>100 ---> 4
ORDER BY customer_naem DESC --> 6

1. FROM
2. WHERE
3. GROUP BY
4. AGGREGATION (SUM/COUNT/MAX/MIN/AVG)
4. HAVING --> clause used to apply on aggregated results
5. SELECT
6. ORDER BY



### TOP / LIMIT 
How to get only first 3 record from table
SELECT TOP 3 * FROM Employee
SELECT * FROM Employee LIMIT 3

HOW TO GET 50% OF RECORDS
SELECT * FROM Employee LIMIT (SELECT COUNT(*)/2 FROM Employee)
SELECT TOP 50 PERCENT * FROM EMployees

Write query to get TOP 2 HIGHEST salary of Employees
SELECT * FROM Employee ORDER BY salary DESC LIMIT 2
SELECT TOP 2 * FROM Employee ORDER BY salary DESC


## DISTINCT 
GIVES UNIQUE VALUES
SELECT DISTINCT customer_name FROM superstore



### COALESCE (if you want to deal with null values)

SELECT NAME,COALESCE(PHONE,'Unknown') FROM Employee
# it will replace null values with unknown

CALCULATE Total Compensation(Salary + Bonus)
SELECT salary + COALESCE(bonus,0) FROM Employee

SELECT customer_name, SUM(sales) as TotalSales FROM superstore GROUP BY Customer_name ORDER BY SUM(sales) DESC LIMIT 5

LIMIT ---> limit the number of results
OFFSET --> SKIPS the number of results and show the next one

### CASE STATEMENTS

IF Customer_name LIKE 'S%' then ' name starting with s' else name starting with something else

> Case is followed by atleast one pair of when and then statements
> A statement will always end with end statement

SELECT customer_name,
CASE 
 WHEN customer_name LIKE 'S%' THEN 'Name Starting with s'
 ELSE 'Name Starting with Elese' 
END AS nameflag
FROM superstore
  

# SELECT profit, CASE WHEN profit > 0 then 'Profit' else 'Loss' END as profit_status FROM superstore

# SELECT *,
 CASE WHEN discount >0.5 THEN 'High'
 WHEN discount BETWEEN 0.2 AND 0.5 THEN 'Medium' ELSE 'Low' 
 END AS discount_category
FROM superstore


# SELECT sales, CASE WHEN sales > 500 THEN 'Large'
                     WHEN sales BETWEEN 100 AND 500 THEN 'MEdium'
                     ELSE 'Small' end as SALES_BUCKET
FROM SUperstore

## USING CASE in aggregate FUNCTIONS

SELECT region,
SUM(case WHEN region = 'South' THEN 1
    WHEN region = 'West' Then 1
    ELSE 0
   END) as reioncount
FROM superstore
GROUP by region



## 
SELECT SUM(CASE WHEN region='West' THEN sales else 0 end) as WEST,
       SUM(CASE WHEN region='East' THEN sales else 0 end) as EAST,
       SUM(CASE WHEN region='South' THEN sales else 0 end) as SOUTH
FROM superstore
GROUP by CATEGORY



>>>>> FUNCTIONS 

SELECT SUM(sales), FROM SUPERSTORE
SELECT COUNT(1) FROM SUPERSTORE 
SELECT COUNT(DISTINCT 'ram') FROM SUPERSTORE

SELECT ORDER_ID,LEFT(ORDER_ID,2) AS CountryCode FROM SUPERSTORE
LEFT will retrieve leftish 2 characters from column 

SELECT LEN(customer_name) FROM superstore
will get length of the full name

SELECT RIGHT(CUSTOMER_NAME,4) FROM superstore
IT will retrieve rightish corner of data


SELECT customer_name,CHARINDEX(' ',CUSTOMER_NAME,1)
it will give you the position of specific character..in the above we are getting space position

# SUBSTRING

SELECT customer_name, SUBSTRING(CUSTOMER_NAME,CHARINDEX('',CUSTOMER_NAME,1),LEN(CUSTOMER_NAME)) FROM  SUPERSTORE


SELECT UPPER('donald') --> UpperCase CHaracter
SELECT LOWER('donald') --> lowercase Character


# SQL SERVER
SELECT year(order_date), month(order_date) from superstore

# MYSQL
SELECT EXTRACT (year FROM order_date) FROM superstore

>> DATEADD

SELECT dateadd(month,5,order_date)  FROM SUPERSTORE
> I want to add 5 months to existing add 
# interval - months
# increment - 5 
# to what order_date


SELECT dateadd(year,2,order_date) FROM superstore
IT will add 2 years to current date 

>> Intervals that we can add --> year,quarter,month,day,week,hour,minute


>> DATEDIFF 
SELECT datediff(day,order_date,ship_date) , order_date , ship_date FROM superstore

IF i want to find difference between days , year, week from one date to other date
shipdate - order-date

> IF WANT TO FIND till current today date

SELECT datediff(day,order_date,current_timestamp),order_date FROM superstore
SELECT datediff(day,order_date,getdate), order_date from superstore
SELECT datediff(year,order_date,getdate), order_date FROM superstore



## SELECT datepart(year,order_date) , datename(year,order_date)--> returns char
            ---> order_date FROM superstore


## SELECT datepart(month,order_date) , datename(month,order_date)--> returns char
            ---> order_date FROM superstore


## CAST is used to convert datatype
SELECT cast(order_id as int) FROM superstore

>>>> USER DEFINED FUNCTION

CREATE FUNCTION dbo.squareofanumber(@number int)
returns int
as bengin 
return @number*@number
end

select dbo.squareofnumber(5)



CREATE FUNCTION dbo.getorder_detailofCUstomer(@customerid VARCHAR(255))
returns table
AS
RETURN(SELECT customer_name,ORDER_id, ORDER_DATE FROM superstore WHERE customer_id = @customer_id)


SELECT * from dbo.getorderdetails('DV-13045')


CREATE OR REPLACE FUNCTION calc_age(dob DATE)
RETURNS INT
LANGUAGE SQL
AS $$
    SELECT EXTRACT(YEAR FROM age(current_date, dob))::INT;
$$;
SELECT calc_age('1998-05-10');


CREATE OR REPLACE FUNCTION top_products(n INT)
RETURNS SETOF products
LANGUAGE SQL
AS $$
    SELECT * FROM products
    ORDER BY revenue DESC
    LIMIT n;
$$;
SELECT * FROM top_products(5);






##### WAYS TO COMBINE TABLES

1. JOIN happens on same column
--- 

Inner Join --> only matching rows/records from both tables

LEFT JOIN / LEFT OUTER JOIN--> only left side of the table and only matching record from right table

RIGHT JOIN / RIGHT OUTER JOIN --> only RIGHT JOIN from the table with only matching records from left table

FULL JOIN / FULL OUTER JOIN --> returns all rows from both tables
 
CROSS JOIN --> will multiply cartesian product where it multiplies each element of one table to other table

SELF JOIN --> A table is joining on itself in self join


````````
 SELECT a.*, b.* FROM Customers a INNER JOIN Order2 B ON a.CustomerID = b.CustomerID

 SELECT a.customer_name, b.OrderDate FROM Customers A INNER JOIN orders2 B ON a.CustomerID = b.CustomerID WHERE b.OrderDate= '2023-08-05'

 SELECT a.customer_name, b.OrderDate FROM Customers A LEFT JOIN orders2 B ON a.CustomerID = b.CustomerID 
 SELECT a.customer_name, b.OrderDate FROM Customers A RIGHT JOIN orders2 B ON a.CustomerID = b.CustomerID 

SELECT p.* , od.* FROM prodcuts p FULL JOIN orders od on p.ProductID = od.ProductID

SELECT top 1 p.productNaem, SUM(od.quantity) as TotalQuantity FROM Products P LEFT JOIN orderDetails2 ord on P.ProductID=od.ProductID GROUP BY P.productName ORDER BY SUM(od.quantity) DESC

SELECT e.emp_name, m.emp_name FROM Employees e LEFT JOIN Employees m ON e.manager_id=M.emp_id

>>>> Find the Employees WHO HAVE SALARY MORE THAN THEIR MANAGERS 
SELECT e.emp_name , m.emp_name , e.salary as expSalary, m.salary as mgsalary FROM Employees E LEFT JOIN Employees M ON E.manager_id, emp_id WHERE
e.Salary=m.Salary

################## 



UNION ==> Combine the results FROM two select queries AND removes duplicates 
UNION ALL ==> Combines two results from two select queries but does not remove duplicates
INTERSECT ALL --> returns only common rows from two select queries
EXCEPT --> return rows from the first query that are not in the second query 

---> RULES 
Columns DataTypes should be Same
Column order should be same
column names should be same
Same number of columns in both select statements



SELECT * FROM Employees2
UNION ALL
SELECT emp_id AS Emp_id , emp_name AS Emp_name, department As Department FROM Employees

SELECT * FROM Employees2
INTERSECT
SELECT emp_id as Emp_id.emp_name as EMP_name, Department FROM Employees


SELECT emp_id as Emp_id, emp_name as Emp_name FROM employees
EXCEPT 
SELECT * FROM Employees2


`````
SUBQUERIES
a query used to place inside another query
IT is used to retrive data that will be used by main query 


SELECT emp_name,salary FROM Employees WHERE SALARY > (SALARY AVG(Salary) FROM Employees)

TWO KIND OF SUBQUERIES 

1. Non-correlated --> Outer query is dependant on inner query. (always inner query will run first)
2. Correlated --> Outer Query is independent of inner query. (Outer query will run first) 

Based on the output of subquery
1. Single row subquery
2. multi-row 

SELECT emp_name,department FROM Employees WHERE Department IN (SELECT department FROM Employees GROUP BY Department HAVING COUNT(*) > 1)

``````

## CTE == Common Table Expression 
--> CTE IS A TEMPORARY NAME RESULT SET THAT YOU DEFINE WITHIN THE EXECUTION SCOPE OF SINGLE SELECT , INSERT , UPDATE OR DELETE
-->  It's always written using the keyword 

WITH CTE_NAME AS 
  ( RESULT SET THAT YOU WANT TO SAVE)


WITH AVERAGESALARY AS (SELECT AVG(SALARY) FROM Employees);

SELECT * FROM AVERAGESALARY

>>>> 
WITH AVGSALARY AS ( SELECT AVG(salary) AS SALARY FROM Employees) 
SELECT Emp_name,salary FROM Employees WHERE Salary > AVGSALARY.Salary
 
### 
WITH ITDEPARTMENT AS (SELECT * FROM Employees2 WHERE Department='IT')
INNER JOIN ITDEPARTMENT DEPT ON E.Emp_id = DEPT.EmpID



##### WINDOW FUNCTION 

> CALCULATION YOU want to done by ROW BY ROW 
> Control the data/window size
> Perform row wise comparison 

SYNTAX of WINDOW FUNCTION 

FUNCTION ( COLUMN ) OVER () ==> WINDOWS SIZE IS Entire table

SUM (column) OVER (PARTITION BY column) --> window size is grouped/divided/partitioned according to a column summation


SUM * , SUM(marks) OVER (PARTITION BY subject) as TOTAL_MARKS from table1


### SHOW EACH SALE along with total sales

SELECT sales_amount , SUM(sale_amount) OVER () as totalsales FROM sales_table

### SHOW EACH SALE along with total sales of that each employee


SELECT emp_name, sales_amount, SUM(sales_amount) OVER ( PARTITION BY emp_name) as total_sales_each_employee FROM sales_data

SELECT DISTINCT item, SUM(amount) OVER( PARTITION BY item) as Total_sales FROM Orders


### FOR EACH REGION,give sales and average sales amount in that region 
SELECT region, sales_amount, AVG(sales_amount) OVER(partition by region) FROM sales_data GROUP by region,sales_amount



### Give me cumulative sales Orderd by sales_date( running total sum) 
SELECT *,sum(sale_amount) OVER (order by sale_date asc) as cumlativesales FROM sales_data

### for each employee cumulative sum
SELECT *, SUM(sales_amount) OVER ( PARTITION BY emp_name ORDER BY sales_date ASC) as Cumlative FROM sales_data



#### For each employee give max sales amount along with its actual sales

SELECT emp_name,sale_amount , max(sale_amount) OVER (partition by emp_name) as maxsales FROM sales_data


#### SHOW percentage of total sales of each employee 

SELECT emp_name, sale_amount/SUM(sale_amount) OVER (PARTITION by emp_name)*100 as percent_sales from sales_data
   



>>> RANKING FUNCTION >>>>

RANK --> it will skip if duplicate rank is there
1
1
3
3
5
6
7
8
8
8
11

DENSE RANK --> it will not skip if duplicate is there
1
1
2
3
4
4
5

ROW NUMBER --> gives unique number anyhow irrespective of things
1
2
3
4
5
6
7


### ORDER BY IS COMPULSORY IN OVER in RANK FUNCTIONS
### 2nd highest employee according sales

SELECT emp_name, DENSE_RANK() OVER(ORDER BY sales) FROM sales_data

WITH rankstable as (SELECT emp_name,sales_amount, DENSE_RANK() OVER(ORDER BY sales_amount DESC) AS ranks FROM sales_data)
SELECT * FROM ranktable WHERE rank =2


### FIND top 2 SALES PER employee 
SELECT emp_name ,sale_amount, DENSE_RANK() OVER (PARTITION BY emp_name ORDER BY sale_amount DESC) as ranks from sales_data

SELECT emp_name ,sale_amount, row_number() OVER (PARTITION BY emp_name ORDER BY sale_amount DESC) as ranks from sales_data

SELECT emp_name ,sale_amount, RANK() OVER (PARTITION BY emp_name ORDER BY sale_amount DESC) as ranks from sales_data


#### Rank all sales within each product

SELECT *, ROW_NUMBER() OVER (partition by product order by sales_amount DESC) as Salesrank FROM  sales_data


## Find the 3rd highest salary from employee table
WITH CTE AS(
  SELECT *, ROW_NUMBER() OVER(ORDER BY SALARY DESC) RN FROM Employees
)
SELECT * FROM CTE WHERE RN=3




#### ANALYTICAL FUNCTIONS 
Lead, Lag , First , Last , n_tile


Lag

Temperature    Lag
12.5           null
14             12.5
13             14
15.2           13
16.5           15.2
24             16.5
24.5           24
25.2           24.5
26             25.2
25.5           26
 

# Each day's temperature along previous day's temperature from each city
SELECT *, lag(temperature,1,0) OVER (partition by city order by temperature) as prevtemp from DailyTemperature

LAG(column,what previous value,default if not there)

--> temperature difference from the previous day for each city 
SELECT *, temperature LAG(temperature,1) OVER (partition by city ORDER by tempdate) as difference FROM DailyTemprature


## Identify the days where the temperature dropped compared to previous day for each city

WITH temp AS ( SELECT *, temperature LAG(temperature,1) OVER (partition by city ORDER by tempdate) AS difference FROM dailyTemperature) 
SELECT * FROM temperature WHERE difference < 0


LEAD
NEXT VALUE 

--> each day's temperature along next's temperature for each city 
SELECT *,LEAD(temperature,1) OVER (partition by city order by tempdate) as prevtemp FROM dailyTemp


### Temperature difference from the next dayeach city 
SELECT *,temperature LEAD(temperature,1) OVER (PARTITION BY city ORDER by tempdate) AS differencenext from DailyTemperature

## SHOW FOR EACH CITY WHETHER next day will be warmer, colder or the same COMPARED TO TODAY


SELECT *,
CASE 
  WHEN lead(temperature,1) OVER (PARTITION BY city ORDER BY Tempdate) > TEMPERATURE THEN 'Colder'
  WHEN LEAD(temperature,1) OVER (PARTITION BY City ORDER BY TempDate) < Temperature THEN 'Warmer'
  ELSE 'Same'
END AS nextdaytrend
FROM DailyTemperature
 



``````

VIEWS --> Used for optimization purpose 
virtual tables --> they dont exist physically
# They dont store data as well


CREATE VIEW seattle AS  SELECT * FROM Orders WHERE CITY = 'Seattle'
it will not store data..will store as virtual view


SELECT * FROM seattle

TYPES OF VIew0
1. Simple VIew --> Base on single table , with function or grouping
2. Complex View --> based on multiple tables , joins , aggregation functions
3. Materialised view --> Stores query results physically


Complete view

CREATE VIEW mansal as ( SELECT DISTINCT b.manager_name, a.salary FROM Employees A INNER JOIN Managers B ON  A.department = B.Department) 
SELECT * FROM mansal


#### STORED PROCEDURES
A stored procedure is a precompiled block of sql statement stored in the database
You can call it with parameters ( inputs/outputs) instead of writing the query each time

it can include logic ( IF,WHILE , LOOPS,VARIABLES, error handling) 

Automate Tasks, Business Logic , Batch Operations


CREATE PROCEDURE seattleData_sp
AS
BEGIN
SELECT * FROM TABLE  WHERE city = "seattle'
END;

exec/execute/Call
exec seattleData_sp


--- SP with input paramets
CREATE PROCEDURE
SEATTLEDATA_sp @entercity VARCHAR(255)
AS
BEGIN
SELECT * FROM TABLE
WHERE CITY=@entercity
END;

>> This stored as sql object 


exec citydata_sp @entercity = 'Seattle'
exec citydata_sp @entercity = 'Los Angeles'

---- SP with multiple inputs


CREATE PROCEDURE
city_ship_sp @entercity VARCHAR(255), @entershipmode VARHCAR (255)
AS
BEGIN
SELECT * FROM TABLE
WHERE CITY=@entercity and [ship mode] = @entershipmode
END;

exec city_ship_sp @city='Seattle' and @entershipmode='Second Class'



### TRIGGER 

A trigger in SQL is a special kind of stored procedure that is automatically executed (fired) in the database when
a specified event occurs
It can not be called explicitly by the user

IT react to events lIKE INSERT,UPDATE , DELETE ,CREATE,ALTER,DROP or even LOGON events
IT is mainly used for enforcing business rules,auditing , validation and preventing unwanted actions
No parameters --> event driven only
Less control as stored procedure
Like an automatic alarm system reacting to events


>> Different types of trigger
DML trigger --> They are executed when we insert,update or delete
DDL Trigger --> they are executed when make changes like CREATE , ALTER , DROP
LOGON Trigger --> They are executed when a new user session is started


CREATE TABLE customer2(customerid int , primary key ,name VARCHAR(100), City VARCHAR(50);
CREATE TABLE customerlog(logid int primary key,customer id , action varchar(50), logdate datetime default getdate())


CREATE trigger trg_aftercstomerinsert
ON TABLE1
AFTER INSERT 
AS
BEGIN
INSERT INTO TABLE2 (customerid,action)
SELECT customerid,'Insert' FROM inserted;
END:



CREATE TRIGGER trg_droptable
ON DATABASE
FRO drop_table
AS 
BEGIN
INSERT INTO TABLE(event_data)
VALUES (EVENTDATA());
END;



CREATE TRIGGER trg_blockuserlogin
ON ALL SERVER
FOR LOGON
AS
BEGIN
IF original_login() = 'blocked_user'
BEGIN
ROLLBACK;
END
END:


#### PERFORMANCE QUERY OPTIMIZATION

1. Index --> to navigate to specific row for speed and performance optimization
Clustered index --> Your index is already made if you create primary key

It defines the physical order of rows in a table, when we create an index on a column , sql server rearranges the actual rows
to match the index order
There will be only 1 cluster index per table
It can be created on a column that contains only unique values;

Non Clustered index --> it does not change the physical order of data . It creates separate structure that stored the index of column 

CREATE clustered index rowid_index
ON Order$(row_id)

CREATE NONCLUSTERED index customer_name_index
ON order$(Customer_name)

2. DONT use SELECT * unneccesarily (fetch only relevant columns)
3. USE where clause wisely WHEREVER required.
4. Functions in WHERE caluse should be avoided (breaks index usage)

 X SELECT * FROM Table WHERE year([order_date])=2016
   SELECT * FROM Table WHERE [order_date] >= '2016-01-01' AND [order_date] <='2016-12-31'

5. USE Joins Properly



#### INTERVIEW QUESTIONS

QUERY 1 --> REMOVE DUPLICATE VALUES FROM EMPLOYEE TABLE
SELECT DISTINCT * FROM employee;

QUERY 2 --> WRITE A QUERY TO FIND OUT DUPLICATE VALUES FROM EMPLOYEE
first give row number to each row
then filter out rows with row number > 1
SELECT *, ROW_NUMBER() OVER (PARTITION BY column_name ORDER BY column_name) as row_num
FROM employee
WHERE row_num > 1;

or 
WITH CTE AS (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY column_name ORDER BY column_name) as row_num
  FROM employee
)
SELECT * FROM CTE WHERE row_num = 2;

QUERY 3 --> WRITE A QUERY TO GET TOP 3 LOWEST EARNING EMPLOYEE
SELECT TOP 3 * FROM employee ORDER BY salary ASC;

QUERY 4 --> WRITE A QUERY TO FIND OUT 2nd HIGHEST SALARY EMPLOYEE
SELECT TOP 1 * FROM (SELECT TOP 2 * FROM employee ORDER BY salary DESC) AS temp ORDER BY salary ASC;

OR 

WITH CTE AS (
  SELECT *,row_number() OVER(order by salary desc) rn from employee
)
SELECT * FROM CTE WHERE rn = 2;

QUERY 5 --> WRITE A QUERY TO FIND 2nd LOWEST EARNING EMPLOYEE

WITH CTE AS (
  SELECT * , ROW_NUMBER() OVER(order by salary ASC) rn FROM employee
)
SELECT * FROM CTE WHERE rn = 2;


QUERY --6 -> WRITE A QUERY TO GET 2nd HIGHEST SALARY BASED ON EACH DEPT

WITH CTE AS(
  SELECT *,row_number() OVER(PARTITION BY DEPT ORDER BY SALARY DESC) AS rn FROM emp
)
SELECT * FROM WHERE rn =2

QUERY - 7 --> WRITE a QUERY TO FIND 3rd lowest salary based on each location 

WITH CTE AS (
  SELECT *,row_number() OVER (PARTITION BY location ORDER BY salary ASC) as rn FROM emp
)
SELECT * FROM CTE WHERE rn = 3;


QUERY -8 --> WRITE A QUERY TO GET BOTTOM 2 SALARY BASED ON EACH LOCATION

WITH CTE AS (
  SELECT *,row_number() OVER(PARTITION BY location ORDER BY salary ASC) as rn FROM emp
)
SELECT * FROM CTE WHERE rn <= 2 OR rn in (1,2);





######## RIGROUS 

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







Bro, let's build a proper **SQL Server Intermediate to Advanced Practice Set** 🔥

We'll combine everything into realistic database problems instead of isolated syntax exercises.

# **SQL Practice: Intermediate to Advanced**



100 Questions

SQL Server

Intermediate → Advanced



## **Topics covered**

| Topic             | Skills                                                      |
| ----------------- | ----------------------------------------------------------- |
| JOINs             | INNER, LEFT, RIGHT, FULL, SELF JOIN                         |
| GROUP BY          | Aggregations, multi-column grouping                         |
| HAVING            | Aggregate filtering                                         |
| ORDER BY          | Sorting, ranking, top results                               |
| CTEs              | Simple, recursive, multiple CTEs                            |
| Date functions    | DATEADD, DATEDIFF, DATEPART, EOMONTH                        |
| String functions  | CONCAT, SUBSTRING, CHARINDEX, REPLACE, TRIM                 |
| Numeric functions | ROUND, CEILING, FLOOR, ABS, POWER                           |
| NULL handling     | ISNULL, COALESCE                                            |
| Conversion        | CAST, CONVERT, TRY_CAST, TRY_CONVERT                        |
| Advanced SQL      | CASE, subqueries, window functions, conditional aggregation |

## **Database schema for practice**

Assume these tables are available:

```
Employees(
    EmployeeID, EmployeeName, DepartmentID,
    ManagerID, Salary, JoiningDate, Email
)

Departments(
    DepartmentID, DepartmentName, Location
)

Customers(
    CustomerID, CustomerName, Email,
    City, Country, SignupDate
)

Orders(
    OrderID, CustomerID, EmployeeID,
    OrderDate, Status
)

OrderItems(
    OrderItemID, OrderID, ProductID,
    Quantity, UnitPrice, Discount
)

Products(
    ProductID, ProductName, Category,
    Price, Stock
)

Payments(
    PaymentID, OrderID, PaymentDate,
    Amount, PaymentMethod, PaymentStatus
)
```

# **Section 1: JOINs (Questions 1–15)**

Intermediate

1. Display employee names along with their department names using INNER JOIN.
2. Display all employees, including employees who are not assigned to any department.
3. Display all departments and their employees, including departments without employees.
4. Find employees who do not belong to any department.
5. Find departments that currently have zero employees.
6. Display customer names, order IDs, and order dates for all customers who placed orders.
7. Display all customers and their orders, including customers who never placed an order.
8. Find customers who have never placed an order.
9. Display product names, order IDs, quantities, and unit prices for every ordered product.
10. Calculate total revenue generated by each order using Orders and OrderItems.
11. Display employee names alongside their manager names using SELF JOIN.
12. Find employees earning more than their managers.
13. Display customer names, order IDs, payment amounts, and payment statuses.
14. Find orders that have no payment records.
15. Find products that have never been ordered.

# **Section 2: GROUP BY and HAVING (Questions 16–30)**

Intermediate → Advanced

16. Find the number of employees in each department.
17. Calculate average salary for each department.
18. Find departments having more than five employees.
19. Find departments whose average salary exceeds ₹60,000.
20. Calculate total salary expenditure for each department.
21. Find the number of orders placed by each customer.
22. Find customers who placed more than five orders.
23. Calculate total revenue generated by each customer.
24. Find customers whose total spending exceeds ₹50,000.
25. Calculate total revenue for each product category.
26. Find product categories generating revenue greater than ₹1 lakh.
27. Calculate total quantity sold for each product.
28. Find products sold in quantities greater than 100.
29. Calculate monthly revenue using year and month grouping.
30. Find months where revenue exceeded ₹5 lakh.

# **Section 3: ORDER BY and Filtering (Questions 31–40)**

31. Display the five highest-paid employees.
32. Display the ten most expensive products.
33. Sort employees by department and salary descending.
34. Display customers alphabetically by country and customer name.
35. Find the three customers with the highest total spending.
36. Display the latest ten orders.
37. Find the five most frequently ordered products.
38. Display employees ordered by joining date, oldest first.
39. Display products ordered by category and price descending.
40. Find the top three revenue-generating product categories.

# **Section 4: Date Functions (Questions 41–55)**

Date Function Practice

41. Extract the joining year and month of every employee using YEAR() and MONTH().
42. Display employee names and joining month names using DATENAME().
43. Find employees who joined during the current year using YEAR() and GETDATE().
44. Find employees who joined during the last 12 months using DATEADD().
45. Calculate employee experience in years using DATEDIFF().
46. Find employees who joined in the current month using MONTH() and YEAR().
47. Display order date, quarter, and year using DATEPART().
48. Calculate the number of days between customer signup and their first order.
49. Find orders placed during the previous calendar month.
50. Find orders placed during the last 30 days.
51. Calculate monthly revenue and display the month name.
52. Find the last day of the month for every order using EOMONTH().
53. Find customers who have not placed an order within 90 days of signup.
54. Calculate the number of days between order date and payment date.
55. Find employees who have completed at least three years of service.

# **Section 5: String Functions (Questions 56–65)**

56. Display employee names in uppercase using UPPER().
57. Display customer names in lowercase using LOWER().
58. Remove leading and trailing spaces from employee names using TRIM().
59. Extract email domains using CHARINDEX() and SUBSTRING().
60. Extract the first three characters of every product name using LEFT().
61. Extract the last four characters of every employee email using RIGHT().
62. Replace spaces in product names with hyphens using REPLACE().
63. Display employee full names using CONCAT().
64. Display customer city and country separated by a comma using CONCAT_WS().
65. Find employees whose email contains the word "gmail" using CHARINDEX().

# **Section 6: Numeric Functions (Questions 66–72)**

66. Calculate order revenue and round it to two decimal places using ROUND().
67. Calculate average product prices rounded to the nearest integer.
68. Find the ceiling of average salary for each department using CEILING().
69. Find the floor of average product price using FLOOR().
70. Calculate the absolute difference between product price and average category price using ABS().
71. Calculate squared product prices using POWER().
72. Calculate discounted product prices and round them to two decimal places.

# **Section 7: NULL Handling and Conversion (Questions 73–80)**

73. Display employee bonus as zero whenever Bonus is NULL using ISNULL().
74. Display customer email as 'Not Provided' whenever Email is NULL using COALESCE().
75. Display the first available contact value from Email, Phone, and AlternatePhone using COALESCE().
76. Convert product prices into VARCHAR using CAST().
77. Convert order dates into dd/mm/yyyy format using CONVERT().
78. Convert string values into integers using TRY_CAST(), returning NULL for invalid values.
79. Convert transaction date strings into DATE using TRY_CONVERT().
80. Find records containing invalid numeric data by filtering rows where TRY_CAST() returns NULL.

# **Section 8: CTEs (Questions 81–90)**

Advanced SQL

81\. Create a CTE containing employees earning above ₹50,000 and retrieve their names and salaries.

82\. Create a CTE calculating department-wise average salary, then display departments above the company-wide average salary.

83\. Create a CTE calculating customer-wise total spending, then display customers spending more than ₹1 lakh.

84\. Create a CTE calculating total revenue per product, then display the five highest-revenue products.

85\. Create a CTE calculating monthly revenue, then display months with revenue greater than ₹10 lakh.

86\. Create two CTEs, one calculating department employee counts and another calculating department average salaries. Join them to display both metrics.

87\. Create a CTE that identifies customers with more than three orders, then join it with Customers to retrieve their details.

88\. Create a CTE that calculates employee experience using DATEDIFF(), then categorize employees as:

- Junior: less than 2 years
- Mid-level: 2–5 years
- Senior: more than 5 years

89\. Create a recursive CTE to display the employee hierarchy starting from the CEO, including hierarchy levels.

90\. Create a recursive CTE to generate dates for every day of the current month.

# **Section 9: Advanced Integrated SQL (Questions 91–100)**

Advanced / Interview Level

91\. Find the top three customers by revenue in each country using CTEs, GROUP BY, JOINs, and ranking.

92\. Find employees earning more than the average salary of their own department using a CTE and JOIN.

93\. Calculate monthly revenue growth percentage using LAG() and DATEPART().

94\. Find customers whose spending increased every consecutive month using CTEs and window functions.

95\. Find the second-highest revenue-generating product in each category using ROW_NUMBER() or DENSE_RANK().

96\. Find employees who joined in the same month as their managers using SELF JOIN, MONTH(), and YEAR().

97\. Identify orders where payment amount is less than the calculated order amount using JOINs, GROUP BY, HAVING, and ROUND().

98\. Find products whose revenue is above the average revenue of products in their category using CTEs and aggregation.

99\. Create a monthly sales report showing:

- Year
- Month name
- Total orders
- Total revenue
- Average order value
- Revenue rounded to two decimals
- Previous month's revenue
- Revenue growth percentage

100\. Build a customer analytics report showing:

- Customer name
- Country
- Signup month
- Total orders
- Total spending
- Average order value
- Last order date
- Days since last order
- Customer spending category (Low, Medium, High)
- Rank by revenue within country

