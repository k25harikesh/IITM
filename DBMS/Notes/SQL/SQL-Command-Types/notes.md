### Basic SQL

#### Introduction to SQL
SQL (Structured Query Language) is the standard language for relational database management systems.

#### Data Definition Language (DDL)
Commands to define the database structure.

- **CREATE**: Create a new table or database.
    ```sql
    CREATE TABLE Students (
      StudentID INT PRIMARY KEY,
      Name VARCHAR(50),
      Age INT,
      Major VARCHAR(50)
    );
    ```

- **ALTER**: Modify an existing database object.
    ```sql
    ALTER TABLE Students ADD COLUMN Email VARCHAR(50);
    ```

- **DROP**: Delete a table or database.
    ```sql
    DROP TABLE Students;
    ```

#### Data Manipulation Language (DML)
Commands to manipulate data in the database.

- **INSERT**: Add new records to a table.
    ```sql
    INSERT INTO Students (StudentID, Name, Age, Major) VALUES (1, 'Alice', 20, 'Computer Science');
    ```

- **SELECT**: Retrieve data from the database.
    ```sql
    SELECT * FROM Students;
    ```

- **UPDATE**: Modify existing records.
    ```sql
    UPDATE Students SET Age = 21 WHERE StudentID = 1;
    ```

- **DELETE**: Remove records from a table.
    ```sql
    DELETE FROM Students WHERE StudentID = 1;
    ```

#### Data Control Language (DCL)
DCL is a subset of SQL used to control access to data in a database. It primarily deals with permissions and access control.

**Key DCL Commands**

- **GRANT**: Gives users access privileges to the database objects.
    ```sql
    GRANT privilege_type ON object TO user;
    GRANT SELECT, INSERT ON Employees TO User1;
    ```

- **REVOKE**: Removes access privileges from users.
    ```sql
    REVOKE privilege_type ON object FROM user;
    REVOKE SELECT, INSERT ON Employees FROM User1;
    ```

**Privilege Types**

- **ALL PRIVILEGES**: Grants all privileges.
- **SELECT**: Allows users to read data.
- **INSERT**: Allows users to insert new data.
- **UPDATE**: Allows users to modify existing data.
- **DELETE**: Allows users to delete data.
- **EXECUTE**: Allows users to execute stored procedures or functions.

#### Transaction Control Language (TCL)
TCL commands are used to manage transactions in the database. Transactions are sequences of operations performed as a single logical unit of work.

**Key TCL Commands**

- **COMMIT**: Saves all changes made in the current transaction to the database.
    ```sql
    COMMIT;
    -- Example
    INSERT INTO Employees (FirstName, LastName, Email) VALUES ('John', 'Doe', 'john.doe@example.com');
    COMMIT;
    ```

- **ROLLBACK**: Undoes all changes made in the current transaction.
    ```sql
    ROLLBACK;
    -- Example
    DELETE FROM Employees WHERE EmployeeID = 5;
    ROLLBACK;
    ```

- **SAVEPOINT**: Sets a savepoint within a transaction to which you can later roll back.
    ```sql
    SAVEPOINT savepoint_name;
    -- Example
    SAVEPOINT sp1;
    UPDATE Employees SET Email = 'john.doe@newdomain.com' WHERE EmployeeID = 1;
    ROLLBACK TO sp1;
    ```

- **SET TRANSACTION**: Specifies the characteristics of the transaction.
    ```sql
    SET TRANSACTION [READ WRITE | READ ONLY];
    -- Example
    SET TRANSACTION READ ONLY;
    ```

