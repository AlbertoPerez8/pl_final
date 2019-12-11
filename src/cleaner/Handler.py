# This file handles the "cleaner" itself, assuring that the ID called is always defined, and catches error if otherwise.


# returns message if ID not defined when called
def id_not_defined(id):
    return "ID, '" + str(id) + "', is not defined"


# returns message created when the ID is called
def id_saved(id):
    return "'" + str(id) + "' declared successfully"


# displays original string
def string_cleaner(line):
    if isinstance(line, str):
        return line[1:-1]
    return None
