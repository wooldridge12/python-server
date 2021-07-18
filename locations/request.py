LOCATIONS = [
    {
      "id": 1,
      "name": "Nashville North",
      "address": "8422 Johnson Pike"
    },
    {
      "id": 2,
      "name": "Nashville South",
      "address": "209 Emory Drive"
    },
    {
      "name": "shepherdsville",
      "address": "757 Benson Drive, apt 13",
      "id": 3
    },
    {
      "name": "shepherdsville",
      "address": "757 Benson Drive, apt 13",
      "id": 4
    },
    {
      "name": "richmond",
      "address": "757 Benson Drive, apt 13",
      "id": 5
    }
  ]

def get_all_locations():
    return LOCATIONS


    # Function with a single parameter
def get_single_location(id):
    # Variable to hold the found animal, if it exists
    requested_location = None

    # Iterate the LOCATIONS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for location in LOCATIONS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if location["id"] == id:
            requested_location = location

    return requested_location


def delete_location(id):
    location_index = -1

    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            location_index = index

    if location_index >= 0:
        LOCATIONS.pop(location_index)
        


def update_location(id, new_location):
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            LOCATIONS[index] = new_location
            break
