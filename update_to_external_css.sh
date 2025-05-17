#!/bin/bash

# Script to update all HTML files to use an external CSS file
# instead of embedded styles

RESTORED_DIR="/Users/kydroon/Documents/GitHub/mint-4-acme/MINT4ACME/restored"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_DIR="/Users/kydroon/Documents/GitHub/mint-4-acme/MINT4ACME/backups_css_${TIMESTAMP}"

# Create backup directory
mkdir -p "$BACKUP_DIR"
echo "Created backup directory: $BACKUP_DIR"

# Copy all HTML files to backup
cp "$RESTORED_DIR"/*.html "$BACKUP_DIR/"
echo "Backed up all HTML files"

# Process each HTML file
for html_file in "$RESTORED_DIR"/*.html; do
    filename=$(basename "$html_file")
    echo "Processing $filename..."
    
    # Replace the style block with a link to the external CSS
    sed -i '' '/<style>/,/<\/style>/c\
    <link rel="stylesheet" href="css/styles.css">' "$html_file"
    
    echo "Updated $filename to use external CSS"
done

echo "All files have been updated to use the external CSS file."
echo "Original files are backed up in $BACKUP_DIR"