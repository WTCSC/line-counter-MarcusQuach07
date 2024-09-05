# Import a python built in module to help go through the information
import argparse
#Defines line count
def line_count():
    # Opens file.txt into read mode as a file
    with open('file.txt', 'r') as file:
        # Adds 1 to the line each time it iterates(Repeats itself) in file.txt
        line_counter = sum(1 for line in file)

        # Defines main as a new section
        def main():
            # Goes through the folder and parses the amount of lines and gives a description
            parser = argparse.ArgumentParser(description='Count lines in a file.')
            # Goes to a file and adds a argument to it through parser
            parser.add_argument('filename', help='The file to count lines from')
            # Defines args as a parser argument and assigns no value to it
            args = parser.parse_args()
            # Activates line counter and takes the file to count the lines
            count = line_counter(args.filename)

            # Prints the file name and the number of lines
            print(f"The file {args.filename} has {count} lines.")
            # If __name__ is equal to __main__ then it processes into the command line and continues next
            if __name__ == '__main__':
                # Lets the process imput into the command line and calls for line_counter to function with a certain file name
                main()
        # Returns the line count
        return line_counter