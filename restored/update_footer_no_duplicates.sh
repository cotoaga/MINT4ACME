#!/bin/bash

# Script to update the copyright footer on all HTML files
# Removes redundant MINT for ACME footer while keeping only navigation and single copyright line

# Find all HTML files in the current directory
HTML_FILES=$(find . -maxdepth 1 -name "*.html")

# Loop through each HTML file
for file in $HTML_FILES; do
    echo "Updating footer in $file..."
    
    # Create a backup of the original file
    cp "$file" "${file}.bak"
    
    # Check if the file has both footers (the footer div within content-container and the copyright line)
    if grep -q '<div class="footer">' "$file" && grep -q '<div style="text-align: center; font-size: 0.8rem;' "$file"; then
        # Remove the redundant MINT footer content from within the .footer div
        sed -i '' -E '/<div class="footer">/,/<\/div>/ {
            /<p>MINT for ACME Digital Archaeology Project<\/p>/d
            /<p>Original © 1997 CSC PLOENZKE AG and INC\. InterNet Consult GmbH<\/p>/d
            /<p>Restoration © 2025<\/p>/d
        }' "$file"
    fi
    
    echo "Updated $file"
done

echo "All files updated."