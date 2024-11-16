# Student-Recording-System

This document outlines the implementation of a simple records management system using Python for the user interface (front-end) and MySQL for the database (back-end).

## Specification
**Data Set**: The system manages student records with the following fields 
- <mark>StudentID</mark> (varchar(10), not null, primary key)
- <mark>Surname</mark> (varchar(20), not null)
- <mark>Firstname</mark> (varchar(20), not null)
- <mark>Birthdate</mark> (date, not null)
- <mark>Gender</mark> (char, not null)
- <mark>Address</mark> (varchar(50), not null)

**Functions**: The system provides this functionalities:
- **Add**: Add new student records.
- **Edit**: Modify existing student records.
- **Delete**: Remove student records.
- **View**: Display all student records.
- **Sort**: Sort student records based on specific criteria.
## Prerequisites
- **XAMPP**: Ensure that XAMPP is installed on your system.

## **Setup Instructions**
1. **Start Apache and MySQL Modules**
* Open the XAMPP Control Panel.
* Start both the Apache and MySQL modules.
2. **Create a Database**
* Click on the "Admin" button of the MySQL module in the XAMPP Control Panel
* In the "Databases" section, enter the name "record_schema" and click "Create".

3. **Create a Table**
*  Go to the newly created database and open MySQL client in PhpMyAdmin.
* Connect to the "record_schema" database.
* Execute the following SQL query to create a table named "records_table":
```sql
CREATE TABLE records_table (
    stud_id VARCHAR(10) NOT NULL,
    surname VARCHAR(20) NOT NULL,
    firstname VARCHAR(20) NOT NULL,
    birthdate DATE NOT NULL,
    gender CHAR NOT NULL,
    address VARCHAR(50) NOT NULL,
    PRIMARY KEY (stud_id)
);
```
4. **Configure Python File**
- Open Python File you will use for the front-end
- Set the following variables
   * <mark>DATABASENAME = 'record_schema'</mark> (Your Database Name)
   * <mark>TABLENAME = 'records_table'</mark> (Your Database Table)

5. **Install Python**
- Open the command prompt (cmd).
- Check if python is installed by running the command:
```bash
python -V
``` 
- If python is not installed, download it from the official website: <https://www.python.org/downloads/> 

6. **Install MySQL Connector and Prettytable:**
- Install the MySQL Connector for Python using the following command:
```bash
pip install mysql-connector-python
```
- Install the Prettytable library for formatting table output:
```bash
pip install prettytable
```
7. **Locate Python file and Open cmd**
- Locate the directory where your Python file is saved.
- Type "cmd" in the search bar to open a command prompt in that directory.

8. **Run the Python file:**
- In the command prompt, run the Python file using the command:

```bash
python main.py
```
## Functionality

1. **Adding Data**
- The program will connect to the MySQL database.
- If no records exist, it will display a prompt to add a new record.
- Enter the student's details as prompted:
  - Student_ID (e.g., 21-1-00781)
  - FirstName (e.g., John)
  - Surname (e.g., Doe)
  - Birthdate (e.g., 2002-11-06)
  - Gender (e.g., M)
  - Address (e.g., Baybay City, Leyte)
- The program will insert the new record into the database.
- The updated table with the newly added record will be displayed.
2. **Updating Data**
- The program will display the existing student records.
- Enter the stud_id of the record you want to update.
- The program will prompt you to enter the attribute you want to change (e.g., <mark>firstname</mark>).
- Enter the new value for the attribute (e.g., <mark>John</mark>).
- The program will update the record in the database.
- The updated table with the modified record will be displayed.

3.  **Deleting Data**
- The program will display the existing student records.
- Enter the <mark>stud_id</mark> of the record you want to delete.
- The program will delete the record from the database.
- The updated table without the deleted record will be displayed.
