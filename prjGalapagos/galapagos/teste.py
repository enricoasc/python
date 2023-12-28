## zipfile.ZipFile
import zipfile

def main():
    with zipfile.ZipFile('/home/enrico/Downloads/teste.zip') as file:

        # ZipFile.infolist() returns a list containing all the members of an archive file
        print(file.infolist())

        # ZipFile.namelist() returns a list containing all the members with names of an archive file
        print(file.namelist())

        # ZipFile.getinfo(path = filepath) returns the information about a member of Zip file.
        # It raises a KeyError if it doesn't contain the mentioned file
        print(file.getinfo(file.namelist()[-1]))

        # ZipFile.open(path = filepath, mode = mode_type, pwd = password) opens the members of an archive file
        # 'pwd' is optional -> if it has password mention otherwise leave it
        text_file = file.open(name = file.namelist()[-1], mode = 'r')

        # 'read()' method of the file prints all the content of the file. You see this method in file handling.
        print(text_file.read())

        # You must close the file if you don't open a file using 'with' keyword
        # 'close()' method is used to close the file
        text_file.close()

        # ZipFile.extractall(path = filepath, pwd = password) extracts all the files to current directory
        file.extractall()
        # after executing check the directory to see extracted files


if __name__ == '__main__': main()