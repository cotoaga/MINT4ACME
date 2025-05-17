#!/bin/bash

# Script to completely remove the copyright footer from all HTML files
# This addresses the issue of redundant copyright information

# Show what we're doing
echo "Removing copyright footer from all HTML files..."

# Find all HTML files and process them
for file in $(find . -name "*.html"); do
    echo "Processing $file..."
    
    # Remove the standalone copyright div in the index file
    if [[ "$file" == "./index.html" ]]; then
        sed -i '' -e '/<div class="copyright">/,/<\/div>/d' "$file"
    fi
    
    # Remove the footer div at the bottom of content pages
    sed -i '' -e '/<div style="text-align: center; font-size: 0.8rem; margin-top: 20px; color: #666;">/,/<\/div>/d' "$file"
done

echo "Footer removal complete!"