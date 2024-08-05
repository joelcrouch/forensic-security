#!/bin/zsh

# List of directories to process
directories=("recup_dir.3" "recup_dir.4" "recup_dir.5" "recup_dir.6" "recup_dir.7" "recup_dir.8" "recup_dir.9" "recup_dir.10" "recup_dir.11")

# Directory to copy files to
destination="recup_dir_copy"

# Create the destination directory if it does not exist
mkdir -p "$destination"

# Iterate over each directory
for dir in "${directories[@]}"; do
    # Check if the directory exists
    if [[ -d "$dir" ]]; then
        # Find and copy files with specified extensions
        find "$dir" -type f \( -iname "*.jpg" -o -iname "*.png" -o -iname "*.gif" \) -exec cp {} "$destination" \;
    else
        echo "Directory $dir does not exist."
    fi
done
