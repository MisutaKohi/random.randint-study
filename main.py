
"""This script will represent a study of the random library's randint method. How random does it really generate
an integer?

The program will prompt the user to enter several parameters about the study they'd like to run, and then export
the results of the study to an Excel file for further data analysis.

The user will be prompted to enter:
1) the desired sample size
2) the desired number of iterations
3) the desired file where the program will export the results

Once the user enters the desired parameters of the study, this script will then generate x number of random numbers,
equivalent to the sample size. It will then repeat this process based upon the desired number of iterations. Finally,
what gets exported to the Excel file will essentially be a list of numbers. The first list will be the column headers,
and each subsequent row will represent a different 'round' in the study.

Example:
    Sample size: 10, Iterations: 2, Excel File: 'study.xlsx'

    Output to study.xlsx:
    ['Keys',    0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ['round 1', 2, 3, 3, 2, 0, 0, 0, 0, 0, 0]
    ['round 2', 0, 0, 1, 2, 0, 0, 2, 0, 0, 5]
    """


def see_instructions(str):
    """This function will display the instructions for using this script as well as what each piece of user
     input will be used for."""

    pass


def run_study(sample_size, iterations):
    """This function will run the bulk of the mathematical operations for the study."""
    pass


def create_export_file(filename):
    '''This function will take a given filename with or without a file extension. It will split the filename at
    the '.' and replace any given file extension with '.xlsx'.

    If the filename contains any symbols apart from '-' or '_', they will be removed.'''

    filename_as_list = list(filename)

    symbols_removed = ""

    # cleans given filename of all non-valid chars
    for char in filename_as_list:
        if (char.isalnum()):
            symbols_removed += char
        if (char in ['-', '_', '.']):
            symbols_removed += char

    # multiple periods in filename will cause bugs
    filename_no_extension = symbols_removed.split('.')

    filename_as_excel = filename_no_extension[0] + '.xlsx'

    return filename_as_excel


def confirm_export():

    return True


def export_finding(destination):
    pass




'''
def main():
    yes_or_no = ''

    while (True):
        yes_or_no = input('Welcome! Would you like to see the instructions? (y/n) ')

        if (yes_or_no.lower() == 'y' or yes_or_no.lower() == 'n'):
            see_instructions(yes_or_no)
            break

    sample_size = input("Please enter desired sample size: ")
    repeat = input("Repeat how many times: ")
    export_destination = input("Excel file export destination: ")

    export_file = create_export_file(export_destination)

    confirm = confirm_export()
    export_file = ''

    while (confirm != True):
        export_destination = input("Excel file export destination: ")
        export_file = create_export_file(export_destination)
        confirm = confirm_export()


    run_study(sample_size, repeat)

    export_finding(export_file)

    print('Operation successful!')


if __name__ == "__main__":
    main()
'''