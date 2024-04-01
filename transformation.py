import pandas as pd
import os
from glob import glob
from datetime import datetime
import time

def task1(input_dir, output_dir):
    time_slot = '1000'
    process_files(input_dir, output_dir, time_slot)

def task2(input_dir, output_dir):
    time_slot = '1030'
    process_files(input_dir, output_dir, time_slot)

def process_files(input_dir, output_dir, time_slot):
    # Define the patterns to match the files needed
    file_pattern = f"_{time_slot}.csv"
    exclusion_pattern = "_summe"
    enerparc_pattern = "Enerparc*"
    sunnic_extern_pattern = "sunnic_extern*"

    # Get all matching files for Enerparc and sunnic_extern that do not end with _summe
    enerparc_files = [f for f in glob(os.path.join(input_dir, enerparc_pattern + file_pattern)) if exclusion_pattern not in f]
    sunnic_extern_files = [f for f in glob(os.path.join(input_dir, sunnic_extern_pattern + file_pattern)) if exclusion_pattern not in f]

    # Ensure we process matched pairs of files
    files_to_process = list(zip(enerparc_files, sunnic_extern_files))

    if not files_to_process:
        print(f"No files found for time slot {time_slot}")
        return

    combined_output_filename = f"combined_{datetime.now().strftime('%Y%m%d')}_{time_slot}.csv"
    output_path = os.path.join(output_dir, combined_output_filename)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if os.path.exists(output_path):
        # Read the existing combined file
        combined_df = pd.read_csv(output_path)
    else:
        # Create an empty DataFrame if the combined file does not exist yet
        combined_df = pd.DataFrame()

    for enerparc_file, sunnic_file in files_to_process:
        # Read the files
        enerparc_df = pd.read_csv(enerparc_file, delimiter=';', usecols=lambda col: "Leistung" in col or "Datum" in col)
        sunnic_df = pd.read_csv(sunnic_file, delimiter=';', usecols=lambda col: "Leistung" in col or "Datum" in col)

        # Rename columns as required and remove "Leistung" prefix
        enerparc_df.rename(columns=lambda x: x.replace("Leistung ", "").replace("Datum [Europe/Berlin]", "dt_start"), inplace=True)
        sunnic_df.rename(columns=lambda x: x.replace("Leistung ", "").replace("Datum [Europe/Berlin]", "dt_start"), inplace=True)

        # Combine the dataframes column-wise
        combined_df = pd.concat([combined_df, enerparc_df, sunnic_df.drop(columns="dt_start")], axis=0, ignore_index=True)

    # Overwrite the existing combined file with updated data
    combined_df.to_csv(output_path, index=False)
    print(f"Saved combined file: {combined_output_filename}")

def main():
    input_dir = 'data/input'
    output_dir = 'data/output'

    choice = input("Enter 1 for task 1 or 2 for task 2: ")
    if choice == '1':
        task1(input_dir, output_dir)
    elif choice == '2':
        while True:
            task2(input_dir, output_dir)
            # Sleep for 1 minutes before processing files again (enabled for demo purpose)
            time.sleep(1 * 60)
            # Sleep for 30 minutes before processing files again
            #time.sleep(30 * 60)
    else:
        print("Invalid choice. Please enter either 1 or 2.")

if __name__ == "__main__":
    main()
