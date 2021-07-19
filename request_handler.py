# http://localhost:8088/animals
# use this on postman.
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from locations.request import get_all_locations, get_single_location, delete_location, update_location
from employees import get_all_employees, get_single_employee, delete_employee, update_employee
from animals import get_all_animals, get_single_animal, create_animal, delete_animal, update_animal
from customers import get_all_customers,get_single_customer,create_customer, delete_customer, update_customer,get_customers_by_email

# Here's a class. It inherits from another class.
# For now, think of a class as a container for functions that
# work together for a common purpose. In this case, that
# common purpose is to respond to HTTP requests from a client.
class HandleRequests(BaseHTTPRequestHandler):
    '''note that is needed'''
    # def parse_url(self, path):
    #     '''Parse_url function'''
    #     # Just like splitting a string in JavaScript. If the
    #     # path is "/animals/1", the resulting list will
    #     # have "" at index 0, "animals" at index 1, and "1"
    #     # at index 2.
    #     path_params = path.split("/")
    #     resource = path_params[1]
    #     id = None

    #     # Try to get the item at index 2
    #     try:
    #         # Convert the string "1" to the integer 1
    #         # This is the new parseInt()
    #         id = int(path_params[2])
    #     except IndexError:
    #         pass  # No route parameter exists: /animals
    #     except ValueError:
    #         pass  # Request had trailing slash: /animals/

    #     return (resource, id)  # This is a tuple

    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]

        # Check if there is a query string parameter
        if "?" in resource:
            # GIVEN: /customers?email=jenna@solis.com

            param = resource.split("?")[1]  # email=jenna@solis.com
            resource = resource.split("?")[0]  # 'customers'
            pair = param.split("=")  # [ 'email', 'jenna@solis.com' ]
            key = pair[0]  # 'email'
            value = pair[1]  # 'jenna@solis.com'

            return ( resource, key, value )

        # No query string parameter
        else:
            id = None

            try:
                id = int(path_params[2])
            except IndexError:
                pass  # No route parameter exists: /animals
            except ValueError:
                pass  # Request had trailing slash: /animals/

            return (resource, id)

    # Here's a class function
    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        '''do_OPTIONS'''
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    # This is API stuff alot is similar to fetch calls
    # Here's a method on the class that overrides the parent's method.
    # It handles any GET request.
    # def do_GET(self):
    #     '''GET'''
    #     # Set the response code to 'Ok'
    #     self._set_headers(200)
    #     response = {} # default response
    #     # Your new console.log() that outputs to the terminal
    #     (resource, id) = self.parse_url(self.path)

    #     if resource == "animals":
    #         if id is not None:
    #             response = f"{get_single_animal(id)}"
    #         else:
    #             response = get_all_animals()

    #     elif resource == "employees":
    #         if id is not None:
    #             response = f"{get_single_employee(id)}"
    #         else:
    #             response = get_all_employees()

    #     elif resource == "locations":
    #         if id is not None:
    #             response = f"{get_single_location(id)}"
    #         else:
    #             response = get_all_locations()
    #     elif resource == "customers":
    #         if id is not None:
    #             response = f"{get_single_customer(id)}"
    #         else:
    #             response = get_all_customers()

    #     # This weird code sends a response back to the client
    #     self.wfile.write(f"{response}".encode())
    def do_GET(self):
        self._set_headers(200)

        response = {}

        # Parse URL and store entire tuple in a variable
        parsed = self.parse_url(self.path)

        # Response from parse_url() is a tuple with 2
        # items in it, which means the request was for
        # `/animals` or `/animals/2`
        if len(parsed) == 2:
            ( resource, id ) = parsed

            if resource == "animals":
                if id is not None:
                    response = f"{get_single_animal(id)}"
                else:
                    response = f"{get_all_animals()}"
            elif resource == "customers":
                if id is not None:
                    response = f"{get_single_customer(id)}"
                else:
                    response = f"{get_all_customers()}"
            elif resource == "locations":
                if id is not None:
                    response = f"{get_single_location(id)}"
                else:
                    response = f"{get_all_locations()}"
            elif resource == "employees":
                if id is not None:
                    response = f"{get_single_employee(id)}"
                else:
                    response = f"{get_all_employees()}"

        # Response from parse_url() is a tuple with 3
        # items in it, which means the request was for
        # `/resource?parameter=value`
        elif len(parsed) == 3:
            ( resource, key, value ) = parsed

            # Is the resource `customers` and was there a
            # query parameter that specified the customer
            # email as a filtering value?
            if key == "email" and resource == "customers":
                response = get_customers_by_email(value)

        self.wfile.write(response.encode())


    # Here's a method on the class that overrides the parent's method.
    # It handles any POST request.
    def do_POST(self):
        '''Post method'''
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body)

        # Parse the URL
        # put a _ instead of the id so you dont get the orange line
        (resourceFromURL, _) = self.parse_url(self.path)

        # Initialize new animal
        # new_animal = None
        # new_customer = None
        new_item = None

        # Add a new animal to the list. Don't worry about
        # the orange squiggle, you'll define the create_animal
        # function next.
        if resourceFromURL == "animals":
            new_item = create_animal(post_body)
            # self.wfile.write(f"{new_animal}".encode())

        elif resourceFromURL == "customers":
            new_item = create_customer(post_body)
        # Encode the new animal and send in response
            # self.wfile.write(f"{new_customer}".encode())
        self.wfile.write(f"{new_item}".encode())

    def do_DELETE(self):
        '''Delete method'''
    # Set a 204 response code
        self._set_headers(204)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single animal from the list
        if resource == "animals":
            delete_animal(id)

        elif resource == "customers":
            delete_customer(id)

        elif resource == "employees":
            delete_employee(id)

        elif resource == "locations":
            delete_location(id)

        # Encode the new animal and send in response
        self.wfile.write("".encode())


    # Here's a method on the class that overrides the parent's method.
    # It handles any PUT request.

    def do_PUT(self):
        '''PUT'''
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single animal from the list
        if resource == "animals":
            update_animal(id, post_body)

        elif resource == "customers":
            update_customer(id, post_body)

        elif resource == "employees":
            update_employee(id, post_body)

        elif resource == "locations":
            update_location(id, post_body)

        # Encode the new animal and send in response
        self.wfile.write("".encode())
        # self.do_POST()


# This function is not inside the class. It is the starting
# point of this application.
def main():
    '''main'''
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
