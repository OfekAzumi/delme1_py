from clear import *
import json




if __name__ == "__main__":
    cls() #clears terminal
    fName = input("Enter First Name: ")
    lName = input("Enter Last Name: ")
    lst= {
        "fname" : fName,
        "lname" : lName
    }

    # add dictionary to JSON file
    with open('db.json', 'w') as json_file: 
        json.dump(lst, json_file)


    # open the JSON file for reading
    with open('db.json', 'r') as json_file:
        data = json.load(json_file)
    
    print(data)
    COLOR_RED = '\x1b[31m'
    COLOR_GREEN = '\x1b[32m'
    COLOR_YELLOW = '\x1b[33m'
    COLOR_RESET = '\x1b[0m'  # Reset to default color

    # Print colored text
    # print(COLOR_RED + "This text is red." + COLOR_RESET)
    print(COLOR_GREEN + "This text is green.")
    # print(COLOR_YELLOW + "This text is yellow." + COLOR_RESET)
    print("still green?")
    print(COLOR_RESET)


   