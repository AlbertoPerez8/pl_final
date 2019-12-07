import LangParser as parser


# Focuses on running the application appropriately
def run():
    parse = parser.parser
    while True:
        try:
            s = input('ViSe >> ')
        except EOFError:
            break
        if not s:
            continue
        elif s == "Exit" or s == "exit":
            break
        result = parse.parse(s)
        print(result)


run()
