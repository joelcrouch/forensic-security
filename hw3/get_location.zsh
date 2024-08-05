#!/bin/zsh 


# Set the directory path
dir="output_Mon_Aug__5_10_41_04_2024/"f


# Check if the directory exists
if [[ ! -d "$dir" ]]; then
  echo "Directory $dir does not exist."
  exit 1
fi

# Initialize an array with the .jpg files
files=($dir/*.gif)f

# Check if the array is empty
if [[ ${#files[@]} -eq 0 ]]; then
  echo "No . files found in $dir."
  exit 1
fi

# Process each file
for file in $files; do
  lat=$(exiftool -GPSLatitude -n "$file" | awk -F': ' '{print $2}')
  lon=$(exiftool -GPSLongitude -n "$file" | awk -F': ' '{print $2}')
  if [[ -n "$lat" && -n "$lon" ]]; then
    if (( $(echo "$lat > 41.5 && $lat < 42.0 && $lon > -88.0 && $lon < -87.0" | bc -l) )); then
      echo "$file was taken around Chicago"
    fi
  fi
done
