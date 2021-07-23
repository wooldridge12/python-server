import sqlite3
import json
from models import Employee

EMPLOYEES = [
    {
        "id": 1,
        "name": "Richard",
        "locationId": 2
    },
    {
      "id": 2,
      "name": "Davey Jones",
      "locationId": 2
    },
    {
      "id": 3,
      "name": "John Basalone",
      "locationId": 1
    },
    {
      "id": 4,
      "name": "Lisa Rigdon",
      "locationId": 1
    },
    {
      "name": "Isabelle",
      "locationId": 1,
      "id": 5
    },
    {
      "name": "Hello World",
      "locationId": 3,
      "id": 6
    }
  ]


# def get_all_employees():

#     return EMPLOYEES

def get_all_employees():
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
          SELECT
              e.id,
              e.name,
              e.location_id
          FROM employee e
          """)

        employees = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['location_id'])

            employees.append(employee.__dict__)

        return json.dumps(employees)

def get_single_employee(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.location_Id
        FROM employee e
        WHERE e.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()


        employee = Employee(data['id'], data['name'], data['location_Id'])

    return json.dumps(employee.__dict__)

def delete_employee(id):
  #comments of sections in animals request.py
    employee_index = -1

    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            employee_index = index

    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)


def update_employee(id, new_employee):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE employee
            SET
                name = ?,
                location_id = ?
        WHERE id = ?
        """, (new_employee['name'], new_employee['location_id'], id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True

def get_employees_by_location(location_id):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.location_id
        FROM Employee e
        WHERE e.location_id = ?
        """, ( location_id, ))

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['location_id'])
            employees.append(employee.__dict__)

    return json.dumps(employees)
    