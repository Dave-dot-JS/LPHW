from sys import argv

script, filename = argv
# opens the specific file for later use
txt = open(filename)
# reads the designated file
print(f"Here's your file {filename}:")
print(txt.read())
# re-takes input for file name to open
print("Type the filename again:")
file_again = input("> ")
# opens new file
txt_again = open(file_again)
#reads new file
print(txt_again.read())
