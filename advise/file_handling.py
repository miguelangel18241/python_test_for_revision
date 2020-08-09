def navigation():
    print("File Manager")
    print("1: Create and write some text to text file")
    print("2: Read the text from the given file name")
    print("3: Edit file")
    print("4: Quit")
    while True:
        try:
            answer = input("Choose the action what you wanna do: ")
            int(answer)
            break
        except ValueError:
            print("Unsupported input")
    if int(answer) == 1:
        write_to_file()
    if int(answer) == 2:
        read_from_file()
    if int(answer) == 3:
        edit_file()


def write_to_file():
    texts = input("Enter the text you want to save: ")
    while True:
        try:
            filename = input("Enter the Name of the file you want to save as: ")
            file = open(filename+".txt", "x")
            file.write(texts)
            file.close()
            print("Done")
            break
        except FileExistsError:
            print("That name already exists")
    navigation()


def read_from_file():
    filename = input("Enter the file name: ")
    try:
        file = open(filename+".txt", "r")
        print("\n"+file.read()+"\n")
        file.close()
    except FileNotFoundError:
        print("Couldn't find a file with that name.")
        navigation()
    navigation()


def edit_file():
    filename = input("Enter the file name you want to read: ")
    file = None
    try:
        file = open(filename + ".txt", "w")
    except FileNotFoundError:
        print("Couldn't find a file with that name.")
        navigation()
    texts = input("Enter the texts you want to save: ")
    file.write(texts)
    file.close()
    navigation()


navigation()
