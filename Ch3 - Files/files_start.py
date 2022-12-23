#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#


def main():
    # Open a file for writing and create it if it doesn't exist
    # myfile = open("textfile.txt", 'w+')

    # # Open the file for appending text to the end
    # myfile = open("textfile.txt", 'a+')

    # # write some lines of data to the file
    # text = input("Type your text:")
    # myfile.write(text)

    # # close the file when done
    # myfile.close()


    # Open the file back up and read the contents
    myfile = open("textfile.txt", 'r')
    if myfile.mode == 'r':
        fl = myfile.readlines()
        for item in fl:
            print(item + '\n')

        # contents = myfile.read()
        # print(contents)

if __name__ == "__main__":
        main()
