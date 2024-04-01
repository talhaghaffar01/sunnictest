import pandas as pd
import os
from glob import glob
from datetime import datetime

def process_files(input_dir, output_dir):
    # Define the patterns to match the files needed
    file_pattern = "_1000.csv"
    exclusion_pattern = "_summe"
    enerparc_pattern = "Enerparc*"
    sunnic_extern_pattern = "sunnic_extern*"

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get all matching files for Enerparc and sunnic_extern that do not end with _summe
    enerparc_files = [f for f in glob(os.path.join(input_dir, enerparc_pattern + file_pattern)) if exclusion_pattern not in f]
    sunnic_extern_files = [f for f in glob(os.path.join(input_dir, sunnic_extern_pattern + file_pattern)) if exclusion_pattern not in f]

    # Ensure we process matched pairs of files
    files_to_process = list(zip(enerparc_files, sunnic_extern_files))
    
    for enerparc_file, sunnic_file in files_to_process:
        # Extract the timestamp from the filenames
        date_str = os.path.basename(enerparc_file).split('_')[1]

        # Read the files
        enerparc_df = pd.read_csv(enerparc_file, delimiter=';', usecols=lambda col: "Leistung" in col or "Datum" in col)
        sunnic_df = pd.read_csv(sunnic_file, delimiter=';', usecols=lambda col: "Leistung" in col or "Datum" in col)

        # Rename columns as required
        enerparc_df.rename(columns=lambda x: x.replace("Meteocontrol_PV_Leistung ", "").replace("Datum [Europe/Berlin]", "dt_start"), inplace=True)
        sunnic_df.rename(columns=lambda x: x.replace("Meteocontrol_PV_Leistung ", "").replace("Datum [Europe/Berlin]", "dt_start"), inplace=True)

        # Combine the dataframes column-wise
        combined_df = pd.concat([enerparc_df, sunnic_df.drop(columns="dt_start")], axis=1)

        # Generate the current timestamp for the output filename
        current_timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        output_filename = f"combined_{current_timestamp}.csv"
        combined_df.to_csv(os.path.join(output_dir, output_filename), index=False)
        print(f"Saved combined file: {output_filename}")

def main():
    input_dir = 'data/input'
    output_dir = 'data/output'
    process_files(input_dir, output_dir)

if __name__ == "__main__":
    main()
