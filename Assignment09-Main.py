# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# AArevalo, 3.9.2021, Modified code to complete assignment 9
# ------------------------------------------------------------------------ #

if __name__ == "__main__":
    import ProcessingClasses as P            # Processing classes
    import IOClasses as IO                   # Input/Output
    from DataClasses import Employee as Emp  # Data structure for Employee
else:
    raise Exception("This file was not created to be imported")

# Loading the Data
lstFileData = P.FileProcessor.read_data_from_file("EmployeeData.txt")
lstTable = []
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2].strip()))

while True:
    # Print Menu Items
    IO.EmployeeIO.print_current_list_items(lstTable)
    IO.EmployeeIO.print_menu_items()
    choice = IO.EmployeeIO.input_menu_options()

    if choice == '1':       # Print the current list
        IO.EmployeeIO.print_current_list_items(lstTable)
        continue

    elif choice == '2':     # Add new data to the list
        lstTable.append(IO.EmployeeIO.input_employee_data())
        continue

    elif choice == '3':     # Save the data
        lstFileData = P.FileProcessor.save_data_to_file("EmployeeData.txt", lstTable)
        continue

    elif choice == '4':     # Exit the program
        break
