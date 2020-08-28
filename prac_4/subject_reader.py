"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data"


def main():
    data = get_data()
    print_data(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data.append(parts)
    input_file.close()
    return data


def print_data(data):
    line_number = 0
    for i in data:
        print(f"{data[line_number][0]} is taught by {data[line_number][1]} and has {data[line_number][2]} students")
        line_number += 1


main()
