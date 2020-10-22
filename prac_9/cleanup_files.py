"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import os


def main():
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        # print("Directory:", directory_name)
        # print("\tcontains subdirectories:", subdirectories)
        # print("\tand files:", filenames)
        # print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))

            name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    # could not figure out how to write code which would make all of the files consistent
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


main()

