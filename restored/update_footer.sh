#!/bin/bash

# Script to update the copyright footer on all HTML files
# Moves it below the navigation links and updates the format

# Find all HTML files in the current directory
HTML_FILES=$(find . -maxdepth 1 -name "*.html")

# Loop through each HTML file
for file in $HTML_FILES; do
    echo "Updating footer in $file..."
    
    # Create a backup of the original file
    cp "$file" "${file}.bak"
    
    # Replace the existing copyright footer line with updated format
    sed -i '' -E 's|<div style="text-align: center; font-size: 0.8rem; margin-top: 20px; color: #666;">.*Digital Archaeological Restoration \| Original © 1997 CSC PLOENZKE AG.*<\/div>|<div style="text-align: center; font-size: 0.8rem; margin-top: 20px; padding-top: 10px; color: #666; border-top: 1px solid #eee;">\n        Digital Archaeological Restoration \| Original © 1997 CSC PLOENZKE AG \&amp; INC Creator: <a href="https:\/\/cotoaga.net" style="color: #666;">Kurt Cotoaga<\/a>\n    <\/div>|g' "$file"
    
    # If the file didn't have the footer, add it before the </body> tag
    if ! grep -q "Digital Archaeological Restoration" "$file"; then
        sed -i '' -E 's|<\/body>|    <div style="text-align: center; font-size: 0.8rem; margin-top: 20px; padding-top: 10px; color: #666; border-top: 1px solid #eee;">\n        Digital Archaeological Restoration \| Original © 1997 CSC PLOENZKE AG \&amp; INC Creator: <a href="https:\/\/cotoaga.net" style="color: #666;">Kurt Cotoaga<\/a>\n    <\/div>\n<\/body>|g' "$file"
    fi
    
    echo "Updated $file"
done

echo "All files updated."