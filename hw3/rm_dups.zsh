#!/bin/zsh

# Directory to process
directory="recup_dir_copy"

# Create a temporary file to store checksums and filenames
tempfile=$(mktemp)

# Generate checksums and list files
find "$directory" -type f -exec sh -c 'md5sum "$1"' _ {} \; | sort > "$tempfile"

# Identify and remove duplicates
awk '{ if (seen[$1]++) print $2 }' "$tempfile" | while read -r file; do
    echo "Removing duplicate file: $file"
    rm "$file"
done

# Clean up temporary file
rm "$tempfile"
