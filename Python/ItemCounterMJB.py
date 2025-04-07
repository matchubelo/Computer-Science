# Assume that a file containing a series of names (as strings) is named names.txt and exists
# on the computer’s disk. Write a program that displays the number of names that are stored
# in the file. (Hint: Open the file and read every string stored in it. Use a variable to keep a
# count of the number of items that are read from the file.)

def count_names_in_file(filename):
    try:
        with open(filename, 'r') as file:
            names = file.readlines()
            count = len(names)
            print(f"The number of names in the file is: {count}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

# Call the function with the filename
# Ensure the file exists in the same directory or provide the full path to the file
count_names_in_file('/Users/mattb/Documents/School (local)/Computer Science/Python/names.txt')