class Library:

    def __init__(self):
        self.file = open("books.txt", "a+")
        print("Welcome to the Library Management System!\n"
              "This is brought to you by Global AI Hub.\nWhich operation would you like to do today?")

    def __del__(self):
        self.file.close()
        print("Library Management System is closing. Goodbye!")

    def printOptions(self):
        print("*** MENU ***\n1) List books\n2) Add Book\n3) Remove Book\n4) Quit")

    def listBooks(self):
        myList = []
        self.file.seek(0)

        for line in self.file.read().splitlines():
            myList.append(line)

        if len(myList) == 0:
            print("Library Management System does not have any books in its records yet.\n")
            return

        index = 1
        for element in myList:
            firstOccurence = element.find(",")
            secondOccurence = element.find(",", firstOccurence + 1)
            bookTitle = element[:firstOccurence]
            authorName = element[firstOccurence + 1:secondOccurence]
            print(str(index) + " - ", end="")
            print("Book title: " + bookTitle, end="")
            print(", Author name:" + authorName)
            index += 1

    def addBook(self):
        newString = input("Enter the title of the book: ")

        self.file.seek(0)
        for line in self.file.read().splitlines():
            firstOccurence = line.find(",")
            bookNameInFile = line[:firstOccurence]
            if bookNameInFile == newString:
                print("You cannot add this book! It is already in the Library Management System!\n")
                return

        newString += ", "
        newString += input("Enter the author name of the book: ")
        newString += ", "
        newString += input("Enter the first release year of the book: ")
        newString += ", "
        newString += input("Enter the number of pages of the book: ")
        newString += "\n"
        self.file.write(newString)
        return

    def removeBook(self):
        bookNameToRemove = input("Enter the title of the book that you want to remove: ")
        newLines = []
        self.file.seek(0)
        for line in self.file.read().splitlines():
            line += "\n"
            newLines.append(line)

        flag = 0
        for element in newLines:
            firstOccurence = element.find(",")
            bookNameInLine = element[:firstOccurence]
            if bookNameInLine == bookNameToRemove:
                flag = 1
                newLines.remove(element)

        self.file.truncate(0)
        self.file.writelines(newLines)
        if flag == 0:
            print(f"Book with name {bookNameToRemove} was not found in the Library Management System!\n")
        elif flag == 1:
            print(f"Book with name {bookNameToRemove} has been removed from the Library Management System successfully!\n")

    def runProgram(self):
        while True:
            self.printOptions()
            option = input("Enter your option: ")
            if option == "1":
                self.listBooks()
            elif option == "2":
                self.addBook()
            elif option == "3":
                self.removeBook()
            elif option == "4":
                break




lib = Library()
lib.runProgram()