from Functionality import Server


if __name__ == '__main__':
    s = Server()

    #For creating server functions, write code here.

    #This code is a running sample
    s.create_server("server", 5000)
    s.update_variables("data", '{}')
    s.update_variables("data2", '{"name": "Juana", "lastName": "Petraca"}')
    s.add_route("server", "/app/send", "send")
    s.create_data("send", "data")
    
    s.add_route("server", "/app/get", "get")
    s.read_data("get", "data")
    s.update_variables("home_text", '{"Hello":"world"}')
    s.add_route("server", '/', "home")
    s.read_data("home", "home_text")

    s.update_variables("test", s.http_get("https://reqres.in/api/users?page=2"))
    s.add_route("server", '/test', "test_route")
    s.read_data("test_route", "test")

    s.print_object("test")
    s.print_object("data2")

    s.read_data(s.add_route("server", "/empty"), "data2")
    s.start_server("server")