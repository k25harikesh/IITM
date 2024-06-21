---

### SQL Commands

#### Filtering Records

- **WHERE**: Filter results based on conditions.
    ```sql
    SELECT * FROM Students WHERE Age > 20;
    ```

#### Logical Operators

- **AND**: Combine multiple conditions where all must be true.
    ```sql
    SELECT * FROM Students WHERE Age > 20 AND Major = 'Computer Science';
    ```

- **OR**: Combine multiple conditions where at least one must be true.
    ```sql
    SELECT * FROM Students WHERE Age > 20 OR Major = 'Mathematics';
    ```

- **NOT**: Negate a condition.
    ```sql
    SELECT * FROM Students WHERE NOT Age = 20;
    ```

#### Sorting Results

- **ORDER BY**: Sort the result set by one or more columns.
    ```sql
    SELECT * FROM Students ORDER BY Age DESC;
    ```

#### Aliases

Temporary names for tables or columns to make queries easier to read and write.

- **Syntax**:
    ```sql
    SELECT column_name AS alias_name
    FROM table_name AS alias_name;
    ```

- **Example**:
    ```sql
    SELECT e.FirstName AS First, e.LastName AS Last
    FROM Employees AS e;
    ```

#### JOINs

Combine rows from two or more tables based on a related column.

**Types of JOINs**:

- **INNER JOIN**: Returns rows that have matching values in both tables.
    ```sql
    SELECT Employees.Name, Departments.DepartmentName
    FROM Employees
    INNER JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID;
    ```

- **LEFT JOIN (or LEFT OUTER JOIN)**: Returns all rows from the left table and matched rows from the right table. If no match, NULL values are returned for columns from the right table.
    ```sql
    SELECT Employees.Name, Departments.DepartmentName
    FROM Employees
    LEFT JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID;
    ```

- **RIGHT JOIN (or RIGHT OUTER JOIN)**: Returns all rows from the right table and matched rows from the left table. If no match, NULL values are returned for columns from the left table.
    ```sql
    SELECT Employees.Name, Departments.DepartmentName
    FROM Employees
    RIGHT JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID;
    ```

- **FULL JOIN (or FULL OUTER JOIN)**: Returns rows when there is a match in one of the tables. If there is no match, the result is NULL on the side that does not have a match.
    ```sql
    SELECT Employees.Name, Departments.DepartmentName
    FROM Employees
    FULL OUTER JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID;
    ```

#### UNION and UNION ALL

Combines the result sets of two or more SELECT statements.

- **UNION**: Removes duplicate records.
    ```sql
    SELECT Name FROM Employees
    UNION
    SELECT Name FROM Customers;
    ```

- **UNION ALL**: Includes duplicate records.
    ```sql
    SELECT Name FROM Employees
    UNION ALL
    SELECT Name FROM Customers;
    ```

#### Subqueries

A query within another query, used to perform operations that depend on the results of another query.

- **Example**:
    ```sql
    SELECT Name FROM Employees
    WHERE Salary > (SELECT AVG(Salary) FROM Employees);
    ```

#### GROUP BY and HAVING

- **GROUP BY**: Groups rows that have the same values into summary rows, like "find the number of employees in each department."
    ```sql
    SELECT DepartmentID, COUNT(*) AS EmployeeCount
    FROM Employees
    GROUP BY DepartmentID;
    ```

- **HAVING**: Filters records that work on summarized GROUP BY results.
    ```sql
    SELECT DepartmentID, COUNT(*) AS EmployeeCount
    FROM Employees
    GROUP BY DepartmentID
    HAVING COUNT(*) > 5;
    ```

---
