"""
Make two files, cats.txt and dogs.txt. Store at least three
names of cats in the first file and three names of dogs in the second file. Write
a program that tries to read these files and print the contents of the file to the
screen. Wrap your code in a try-except block to catch the FileNotFound error,
and print a friendly message if a file is missing. Move one of the files to a dif-
ferent location on your system, and make sure the code in the except block
executes properly."""

def read_contents(filename: list) -> str:
    try:
        with open(filename) as file_object:
            contents = file_object.readlines()
            print(file_object.name)
            print('Contents')
            for content in contents:
                print(f'- {content.strip()}')
            print('\n')
    except FileNotFoundError:
        print(f"File not found: {filename}")

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    read_contents(filename)
