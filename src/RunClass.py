import LangParser as parser


#Not used to run the main program.  

def run():
    parse = parser.parser
    while True:
        try:
            file = input("Lang>>\nFilename:")
        except EOFError:
            break
        if not file:
            continue
        elif file == "Exit" or file == "exit":
            print("Exit")
            break
        result = parse.parse(file)
        print(result)

run()