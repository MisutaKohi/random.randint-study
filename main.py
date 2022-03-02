
"""This script will represent a study of the random library's randint method. How random does it really generate
an integer?

The program will prompt the user to enter several parameters about the study they'd like to run, and then export
the results of the study to a CSV file. The intention is that this CSV file will not only be opened as a dataframe in
Jupyter Notebook for further analysis, but also then exported to an Excel file for data visualization purposes.

The user will be prompted to enter:
1) the desired sample size
2) the desired number of iterations
3) the desired file where the program will export the results

Once the user enters the desired parameters of the study, this script will then generate x number of random numbers,
equivalent to the sample size. It will then repeat this process based upon the desired number of iterations. Finally,
what gets exported to the Excel file will essentially be a list of numbers. The first list will be the column headers,
and each subsequent row will represent a different 'round' in the study.

Example:
    Sample size: 10, Iterations: 2, CSV File: 'study.csv'

    Output to study.xlsx:
    [['Keys',   0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    ['round 1', 2, 3, 3, 2, 0, 0, 0, 0, 0, 0],
    ['round 2', 0, 0, 1, 2, 0, 0, 2, 0, 0, 5]]
    """

import csv
import random


def see_instructions(str):
    """This function will display the instructions for using this script as well as what each piece of user
     input will be used for."""

    pass


def run_study(sample_size, iterations):
    """This function will run the bulk of the mathematical operations for the study. It returns a list of CSV lists,
    ready for export."""

    # list of CSV strings
    export_lists = [['keys', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']]

    # counter to keep track of which round random values belong to
    round_number = 0

    # handles executing rounds for given number of iterations
    for num in range(0, iterations):

        study_tally = {'round':0, 0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

        round_number += 1

        # handles random number generations for a particular round/iteration
        for num in range(0, sample_size):

            rand_num = random.randint(0,9)

            study_tally[rand_num] += 1

        # updates 'round' key with appropriate round number
        study_tally['round'] = "round " + str(round_number)

        export_lists.append(list(study_tally.values()))

    return export_lists

#print(run_study(10, 10))



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

    filename_as_excel = filename_no_extension[0] + '.csv'

    return filename_as_excel


def confirm_export(filename):
    '''This function will prompt the user to verify that the given filename is the correct destination to which
    to export the results of the study. Function returns True/False based upon user input.'''

    print("Are you sure that '{}' is correct?".format(filename))
    correct = input('This will overwrite and erase existing content if file already exists. (y/n) ')

    # return true where first letter of user response is 'y'
    if (correct[0].lower() == 'y'):
        return True
    else:
        return False

    return correct


def export_finding(destination, export_data):
    '''This function takes 2 parameters: an export destination as well as a list of strings to export.'''

    with open(destination, 'w') as f_out:

        writer = csv.writer(f_out)

        writer.writerows(export_data)

'''
def main():

    while (True):
        yes_or_no = input('Welcome! Would you like to see the instructions? (y/n) ')

        if (yes_or_no[0].lower() == 'y' or yes_or_no[0].lower() == 'n'):
            see_instructions(yes_or_no)
            break

    sample_size = input("Please enter desired sample size: ")
    num_iterations = input("How many iterations: ")
    export_destination = input("Export destination (as CSV file): ")

    # cleans given file destination and adds appropriate file extension (CSV)
    export_file = create_export_file(export_destination)

    # prompts user to reconfirm that the given file destination is correct
    confirm = confirm_export(export_file)

    while (confirm != True):
        export_destination = input("Reenter export destination (as CSV file): ")
        export_file = create_export_file(export_destination)
        confirm = confirm_export()

    # creates a list of CSV lists
    export_data = run_study(sample_size, num_iterations)

    export_finding(export_file, export_data)

    print('Operation successful!')


if __name__ == "__main__":
    main()'''