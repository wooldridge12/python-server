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


def get_all_employees():

    return EMPLOYEES


# Function with a single parameter
def get_single_employee(id):
    # Variable to hold the found animal, if it exists
    requested_employee = None

    # Iterate the EMPLOYEES list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee


def delete_employee(id):
  #comments of sections in animals request.py
    employee_index = -1

    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            employee_index = index

    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)


def update_employee(id, new_employee):
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break
