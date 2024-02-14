class Library:
    def __init__(self):
        open("books.txt", "a+")
        print("Welcome to the Library Management System!\nThis is brought to you by Global AI Hub.\nWhich operation would you like to do today?")
    def __del__(self):
        print("Library Management System is closing. Goodbye!")
    def printOptions(self):
        print("*** MENU ***\n1) List books\n2) Add Book\n3) Remove Book\n4) Quit")