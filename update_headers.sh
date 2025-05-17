#!/bin/bash

# Directory containing the HTML files
DIRECTORY="/Users/kydroon/Documents/GitHub/mint-4-acme/MINT4ACME/restored"

# CSS for title-text class to add if not present
TITLE_TEXT_CSS=".title-text {
            display: block;
            font-size: 2.2rem;
            font-weight: bold;
            color: var(--primary);
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid var(--border);
        }"

# Process each HTML file in the restored directory
find "$DIRECTORY" -name "*.html" | while read -r file; do
    echo "Processing $file..."
    
    # Check if the file contains an image tag with class="title-image"
    if grep -q 'class="title-image"' "$file"; then
        # Extract the title text from the alt attribute
        title_text=$(grep -o 'alt="[^"]*"' "$file" | grep -v "alt=\"\"" | head -1 | sed 's/alt="//' | sed 's/"//')
        
        if [ -n "$title_text" ]; then
            echo "  Found title: $title_text"
            
            # Create a temporary file
            temp_file=$(mktemp)
            
            # Replace the title image with an h1 header
            sed -E 's|<img src="[^"]*" alt="'"$title_text"'" class="title-image"[^>]*>|<h1 class="title-text">'"$title_text"'</h1>|g' "$file" > "$temp_file"
            
            # Check if the title-text CSS class is already present
            if ! grep -q "title-text" "$file"; then
                # Add the title-text CSS class after the title-image class
                sed -i '' 's|\.title-image {[^}]*}|&\n        '"$TITLE_TEXT_CSS"'|' "$temp_file"
            fi
            
            # Replace the original file with the modified one
            mv "$temp_file" "$file"
            echo "  Updated $file with modern header"
        else
            echo "  No title text found in $file, skipping"
        fi
    else
        echo "  No title image found in $file, skipping"
    fi
done

echo "All files have been processed."