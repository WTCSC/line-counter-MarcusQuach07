def line_count():
        with open('file.txt', 'r') as file:
        # Opens file.txt into read mode as a file
            line_counter = sum(1 for line in file)
            # adds 1 to the line each time it iterates(Repeats itself) in file.txt
        return line_counter
        # returns the line count