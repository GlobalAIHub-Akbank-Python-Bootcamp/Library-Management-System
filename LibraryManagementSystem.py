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
        bookContent = self.file.read()

        for line in bookContent.splitlines():
            myList.append(line)

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
        return