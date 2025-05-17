#!/bin/bash

# Directory containing the HTML files
DIRECTORY="/Users/kydroon/Documents/GitHub/mint-4-acme/MINT4ACME/restored"

# List of files to modify
FILES=(
    "4_3.html"
    "4_2.html"
    "4_1.html"
    "3_2.html"
    "3_1.html"
    "4_6.html"
    "4_5.html"
    "2_2.html"
    "4_4.html"
    "examples.html"
    "examples_multimedia.html"
    "examples_internet.html"
    "examples_automotive.html"
    "info.html"
    "help.html"
)

# New attribution to add before </body>
NEW_ATTRIBUTION='<div style="text-align: center; font-size: 0.8rem; margin-top: 20px; color: #666;">
    Digital Archaeological Restoration | Original © 1997 CSC PLOENZKE AG & INC Creator: <a href="https://cotoaga.net" style="color: #666;">Kurt Cotoaga</a>
</div>'

# Process each file
for file in "${FILES[@]}"; do
    filepath="$DIRECTORY/$file"
    
    # Check if file exists
    if [ -f "$filepath" ]; then
        echo "Processing $file..."
        
        # Create a temporary file
        temp_file=$(mktemp)
        
        # Remove the copyright div section
        sed '/<div class="copyright">/,/<\/div>/d' "$filepath" > "$temp_file"
        
        # Add new attribution before </body>
        sed -i '' "s|</body>|$NEW_ATTRIBUTION\n</body>|" "$temp_file"
        
        # Replace the original file with the modified one
        mv "$temp_file" "$filepath"
        
        echo "$file updated successfully"
    else
        echo "Warning: $file not found in $DIRECTORY"
    fi
done

echo "All files have been processed."