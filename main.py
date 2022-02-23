"""This script will represent a study of the random library's randint method. How random does it really generate
an integer?

Here we'll be using integers 0-9.

This script will prompt a user to enter several attributes about the study they would like to execute. First, the
script will prompt the user for a sample size, that is to say, how many random integers they want generated at a time.
Next, how many times to repeat the test at that sample size. This will be roughly equal to the number of rows in
the Excel file (less one for the column headers). Finally, the name of the Excel file where the user would like to
export the findings of the study.

Once the calculations finish, the program will open the designated Excel file and overwrite any pre-existing content.
The intention is then that the file be opened in a dataframe for further analysis.

Example:
    Sample size: 10, Repeated: 2, Excel File: 'study.xlsx'

    Output to study.xlsx:
    ['Keys',    0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ['round 1', 2, 3, 3, 2, 0, 0, 0, 0, 0, 0]
    ['round 2', 0, 0, 1, 2, 0, 0, 2, 0, 0, 5]
    """


def see_instructions(str):

    pass


def run_study():
    pass


def create_export_file(filename):
    pass


def confirm_export():
    pass


def export_finding(destination):
    pass


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
