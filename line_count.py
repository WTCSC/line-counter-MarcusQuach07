import argparse

def line_count():
    # Opens file.txt into read mode as a file
    with open('file.txt', 'r') as file:
        # adds 1 to the line each time it iterates(Repeats itself) in file.txt
        line_counter = sum(1 for line in file)

        # Defines main as a new section
        def main():
            # goes through the folder and parses the amount of lines and gives a description
            parser = argparse.ArgumentParser(description='Count lines in a file.')
            # goes to a file and adds a argument to it through parser
            parser.add_argument('filename', help='The file to count lines from')
            # defines args as a parser argument and assigns no value to it
            args = parser.parse_args()
            # activates line counter and takes the file to count the lines
            count = line_counter(args.filename)

            # Prints the file name and the number of lines
            print(f"The file {args.filename} has {count} lines.")
            # If __name__ is equal to __main__ then it processes into the command line and continues next
            if __name__ == '__main__':
                # Lets the process imput into the command line and calls for line_counter to function with a certain file name
                main()
        # returns the line count
        return line_counter