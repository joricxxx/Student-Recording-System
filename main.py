import mysql.connector
from mysql.connector import Error
import prettytable
import os
import re
from datetime import datetime

connection = None
TABLENAME= 'tbl_students'    # Your Database Table 
DATABASENAME='dbstudentrecord'

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',  # Default XAMPP MySQL username
        password='',  # Default XAMPP MySQL password (usually empty)
        database=DATABASENAME  # Your database name
    )
    print("Connection to MySQL DB successful")
except Error as e:
    print(f"The error '{e}' occurred")


def execute_query(query):
    """ Execute any query """
    cursor=connection.cursor(dictionary=True)
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed sucessfully")
    except Error as error:
        print(f"Error: {error}")
def get_all_data():
    query = f"SELECT * FROM {TABLENAME}" # Use dictionary=True to get results as dictionaries
    cursor=connection.cursor(dictionary=True)
    cursor.execute(query)
    results = cursor.fetchall()  # Fetch all results
    cursor.close()
    return results
def insert_query():
    studentID=input("Student_ID[00-0-00000]: ")
    firstname=input("FirstName[String]: ")
    surname=input("Surname[String]: ")
    birthdate=input("Birthdate[YYYY-MM-DD]: ")
    gender=input("Gender[M/F]: ")
    if(validate_inputs(studentID, firstname, surname, birthdate, gender) == True):
        query = f"""
        INSERT INTO {TABLENAME} (stud_id, surname, firstname, birthdate, gender)
        VALUES ('{studentID}', '{surname}', '{firstname}', '{birthdate}', '{gender}')
        """
        print(query)
        execute_query(query)
    else:
        print("Validation Error")
    input("Press Enter to continue...")

def delete_query():
    data = get_all_data()
    sID = input("Student ID: ")
    index = -1
    for i, student in enumerate(data):
        if student['stud_id'] == sID:
            index = i
    if index != -1:
        query=f"""
        DELETE FROM {TABLENAME}
        WHERE stud_id = '{sID}'
        """
        print(query)
        execute_query(query)
    input("Press Enter to continue...")
def validate_inputs(studentID, firstname, surname, birthdate, gender):
    if validate_input("stud_id",studentID) == False:
        return False;
    if validate_input("firstname",firstname) == False:
        return False;
    if validate_input("surname",surname) == False:
        return False;
    if validate_input("birthdate",birthdate) == False:
        return False;
    if validate_input("gender",gender) == False:
        return False;
    return True

def validate_input(attribute_name, attribute_value):
    match attribute_name:
        case "stud_id": 
            ID_PATTERN = r'^\d{2}-\d{1}-\d{5}$'
            if re.match(ID_PATTERN, attribute_value) is None:
                print("ID error")
                return False 
        case "firstname":
            if not isinstance(attribute_value, str) or len(attribute_value.strip()) == 0:
                print("Firstname error")
                return False
        case "surname":
            if not isinstance(attribute_value, str) or len(attribute_value.strip()) == 0:
                print("Surname error")
                return False
        case "gender":
            if attribute_value not in ['M', 'F']:
                print("Gender error")
                return False
        case "birthdate":
            try:
                datetime.strptime(attribute_value, '%Y-%m-%d')  # Check if the date is in the correct format
            except ValueError:
                print("Birthdate error")
                return False
    return True
    
def update_query():
    data = get_all_data()
    sID = input("stud_id: ")
    index = -1
    for i, student in enumerate(data):
        if student['stud_id'] == sID:
            index = i
    if index != -1:
        # print(f"index: {index}")
        # print(data[index])
        print_table(get_all_data())
        print("Student Attribute:")
        for keys in data[0].keys():
            print(keys)
        print("")
        atrbs=input("Attribute: ")
        atrbs_value=input("value: ")
        if validate_input(atrbs, atrbs_value) == True:
            query=f"""
            UPDATE {TABLENAME}
            SET {atrbs} ='{atrbs_value}'
            WHERE stud_id = '{sID}'
            """
            print(query)
            execute_query(query)
        else:
            print("Validation Error")
    else:
        print("Student_ID not found")
    input("Press Enter to continue...")
        
def print_table(data):
    """ Print data as a formatted table """
    if not data:
        print("No data to display.")
        return

    # Create a PrettyTable object
    table = prettytable.PrettyTable()

    # Set the column names
    table.field_names = data[0].keys()

    # Add rows to the table
    for row in data:
        table.add_row(row.values())

    # Print the table
    os.system('cls')
    print(f"Database: {DATABASENAME}")
    print(f"Table: {TABLENAME}\n")
    print(table)
if __name__ == "__main__":
    running = True
    while(running):
        print_table(get_all_data())
        print("\t\t[U]pdate [D]elete [A]dd [E]xit")
        user_input = input().upper()
        match user_input:
            case 'E':
                running = False
            case 'A': 
                insert_query()
            case 'D':
                delete_query()
            case 'U':
                update_query()
                


    # Close the connection
    if connection:
        connection.close()
