from flask import Flask
from flask import request as req
import json
import logging

#Removes log msgs when disabled == true, Server started msg is still there
log = logging.getLogger('werkzeug')
log.disabled = False

#Defines a Route_id obj
#attributes:
#   route: the assigned route string 
#   server_id: Server_ID attached to Route_ID
class Route_ID():
    def __init__(self, route, server_id):
        self.route = route
        self.server_id = server_id
    
#Defines a Server_ID obj
#attributes:
#   flask_instance: flask server instance 
#   port: por where flask is running
class Server_ID():
    def __init__(self, flask_instance, port):
        self.flask_instance = flask_instance
        self.port = port

#Defines Server Functionality
#attributes:
#   variables: all variables made in code 
#   used_ports: ports in use by app
class Server():
    def __init__(self, variables = {}):
        self.variables = variables  #parser stores id's here
        self.used_ports = []

    def update_variables(self, var_id, object):
        try:
            parsed = json.loads(object)
        except:
            self.variables[var_id] = str(object)
            return

        try:
            for key in parsed:
                if parsed[key] in self.variables:
                    parsed[key] = self.variables[parsed[key]]
            self.variables[var_id] = parsed
        except:
            self.variables[var_id] = parsed
        
    def add_route(self, server_id, route, route_id, action):
        if(not route_id):
            route_id = server_id + route
        self.variables[route_id] = Route_ID(route, server_id)

        return route_id

    def add_endpoints(self, server_id, route_endpoint, action):
        app = self.variables[server_id].flask_instance
        try: 
            app.add_url_rule(route_endpoint, str(route_endpoint), action)
            return "Action added"
        except:
            return "Cannot assign more than one acton to the same route"

    def create_data(self, route_id, object_id):
        endpoint = self.variables[route_id]
        
        def create_action():
            self.variables[object_id] = request.get_json()
            return str(self.variables[object_id])
        
        return self.add_endpoints(endpoint.server_id, str(endpoint.route), create_action)

    

