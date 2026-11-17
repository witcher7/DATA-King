



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

