import pandas as pd


def merge_csv_files():
    # Create an empty list to store files for merging.
    filePaths = []

    # Start loop to prompt user to enter file paths for CSVs to merge:
    while True:
        filePath = input("Please copy the file path and hit enter. When finished, type 'done': \n").strip()
        if filePath.lower() == 'done':
            break
        filePath = filePath.strip('"')
        filePaths.append(filePath)

    # Determine if any CSVs were imported:

    if not filePaths:
        print("No CSVs provided to merge. Exiting script")
        return

    # Create list to store data frames for Pandas to store and merge information:

    dataFrames = []

    # Read and write input from filePaths list into dataFrames list:

    for filePath in filePaths:
        try:
            dataFrameInput = pd.read_csv(filePath)
            dataFrames.append(dataFrameInput)
        except Exception as error:
            print(f"Error reading {filePath}: {error}.\n")  # Error catching, handling, and explanation.

        continue

    # Merge dataframes into a single file:

    if dataFrames:
        # Concatenate data into a single file:
        mergedDF = pd.concat(dataFrames, ignore_index=True)
        print("Files have been merged successfully.")
        # If any lines imported as duplicates remove them from the dataframe:
        mergedDF.drop_duplicates(inplace=True)
        print("Successfully dropped duplicate rows.")

        outputFilePath = input(f"Please enter the file path, including filename, to export merged CSV File: \n").strip()
        # Strip quotation marks if they are included in pasted file path
        outputFilePath = outputFilePath.strip('"')

        # Attempt to save the file to user-specified file path:

        try:
            mergedDF.to_csv(outputFilePath, index=False)
            print(f"The file has been saved as: {outputFilePath}.\n")
        except Exception as errors:
            print(f"Error saving merged CSV file: {errors}.\n")
    else:
        print("Completed. No more CSV files to print.\n")


# Call function to run code:

merge_csv_files()
