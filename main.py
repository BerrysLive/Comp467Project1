import csv
import os

# Project 1 Pseudocode

xytech_dir = "Xytech.txt"
baselight_dir = "Baselight_export.txt"


# Step 1: Open the Baselight export file and read its contents.

# Step 2: Go through each line in the Baselight export file.

#For each line in the file
    # Step 3: Check for errors and handle them if any.
    #If you find "<null>" or "<err>"
        #Fix the error or skip the line

    # Step 4: Parse the line to extract frame information and store it.
    #Extract the location and frame details
    #Save them in a list

# Repeat similar steps for the Xytech.txt file to extract Producer, Operator, and Job details.

# Step 5: Combine the information from both files.
#Create a new list for the CSV content
#Add the details from both files to the list

# Step 6: Make sure frames and frame ranges are in order and not mixed.

# Step 7: Write the combined list to a new CSV file.
#Open a new CSV file for writing
#For each item in the list
    #Write the item to the CSV file, with each piece of information separated by a slash (/)



# Define the filename
filename = "export.csv"

# Check if the file already exists in the current working directory
if not os.path.isfile(filename):
    # If the file does not exist, create it
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        # You can add column headers or initial data here if necessary
        # Example: writer.writerow(['Column1', 'Column2', 'Column3'])
    print(f"'{filename}' has been created.")
else:
    print(f"'{filename}' already exists.")


