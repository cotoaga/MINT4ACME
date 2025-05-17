#!/bin/bash

# Script to update heading colors from --primary (red) to --dark (black)
# in the restored HTML files

RESTORED_DIR="/Users/kydroon/Documents/GitHub/mint-4-acme/MINT4ACME/restored"

echo "Updating heading colors from --primary to --dark in restored HTML files..."

# Find all HTML files and update heading styles
find "$RESTORED_DIR" -name "*.html" -type f | while read -r file; do
    echo "Processing $file"
    
    # 1. Update title-text class (main heading)
    sed -i '' 's/color: var(--primary);/color: var(--dark);/g' "$file"
    
    # 2. Update h1, h2, h3 elements if they exist with primary color
    sed -i '' 's/h1 {.*color: var(--primary);/h1 { color: var(--dark);/g' "$file"
    sed -i '' 's/h2 {.*color: var(--primary);/h2 { color: var(--dark);/g' "$file"
    sed -i '' 's/h3 {.*color: var(--primary);/h3 { color: var(--dark);/g' "$file"
    
    # 3. Update tower h4 elements (in index.html and similar templates)
    sed -i '' 's/\.tower h4 {.*color: var(--primary);/.tower h4 { color: var(--dark);/g' "$file"
    
    # 4. Update .disclaimer h1 (in index.html)
    sed -i '' 's/\.disclaimer h1 {.*color: var(--primary);/.disclaimer h1 { color: var(--dark);/g' "$file"
    
    # 5. Update key-points h3 (in some content pages)
    sed -i '' 's/\.key-points h3 {.*color: var(--primary);/.key-points h3 { color: var(--dark);/g' "$file"
done

echo "Heading colors updated successfully!"