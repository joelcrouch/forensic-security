import os
import subprocess

# Path to the output file
output_file = '/home/joel/ktunes_jpginfo.txt'
# Directory containing JPG files
directory = '/home/joel/mfb/Pictures'

# Function to extract metadata from a single file using exiftool
def extract_metadata(file_path):
    try:
        # Run exiftool command to get metadata
        result = subprocess.run(
            ['exiftool', '-GPSLatitude', '-GPSLongitude', '-DateTimeOriginal', file_path],
            capture_output=True, text=True
        )
        
        # Check if exiftool command was successful
        if result.returncode == 0:
            output = result.stdout
            
            # Extract GPS and Date/Time information
            gps_latitude = next((line.split(': ')[1] for line in output.splitlines() if 'GPS Latitude' in line), 'N/A')
            gps_longitude = next((line.split(': ')[1] for line in output.splitlines() if 'GPS Longitude' in line), 'N/A')
            datetime_original = next((line.split(': ')[1] for line in output.splitlines() if 'Date/Time Original' in line), 'N/A')
            
            # Write to output file
            with open(output_file, 'a') as f:
                f.write(f"Metadata for {file_path}:\n")
                f.write(f"GPS Latitude: {gps_latitude}\n")
                f.write(f"GPS Longitude: {gps_longitude}\n")
                f.write(f"Date/Time Original: {datetime_original}\n\n")
        else:
            with open(output_file, 'a') as f:
                f.write(f"Error occurred while processing {file_path}.\n")
                
    except Exception as e:
        with open(output_file, 'a') as f:
            f.write(f"Exception occurred: {e}\n")

# Ensure the output file is empty or created
with open(output_file, 'w') as f:
    pass

# Check if directory exists
if not os.path.isdir(directory):
    with open(output_file, 'a') as f:
        f.write(f"Directory {directory} does not exist.\n")
else:
    # Process each JPG file in the directory
    for file_name in os.listdir(directory):
        if file_name.lower().endswith('.jpg'):
            file_path = os.path.join(directory, file_name)
            extract_metadata(file_path)
