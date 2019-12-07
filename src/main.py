from Functionality import Server

# Basically a big tester for server creation and server manipulation. Will test functionality here.
if __name__ == '__main__':
    s = Server()

    # Beginning Test. Creates Server, updates variables, adds routes, reads data, etc.
    s.create_server("server", 5000)
    s.update_variables("data", '{}')
    s.update_variables("data2", '{"name": "Juana", "lastName": "Petraca"}')
    s.add_route("server", "/app/send", "send")
    s.create_data("send", "data")
    # s.create_data("send", "data2")
    s.add_route("server", "/app/get", "get")
    s.read_data("get", "data")
    s.update_variables("home_text", '{"Hello":"world"}')
    s.add_route("server", '/', "home")
    s.read_data("home", "home_text")
    # s.add_endpoints("server", '/', lambda : 'Hello, World')#placeholder, necessary for execution


