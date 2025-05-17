#!/bin/bash

# Script to standardize the copyright footer format across all HTML files

# Find all HTML files in the current directory
HTML_FILES=$(find . -maxdepth 1 -name "*.html")

# Loop through each HTML file
for file in $HTML_FILES; do
    echo "Standardizing footer in $file..."
    
    # Create a backup of the original file
    cp "$file" "${file}.bak"
    
    # Update the footer content
    sed -i '' -E 's|<div style="text-align: center; font-size: 0.8rem; margin-top: 20px; color: #666;">.*Digital Archaeological Restoration \| Original © 1997 CSC PLOENZKE AG.*<\/div>|<div style="text-align: center; font-size: 0.8rem; margin-top: 20px; padding-top: 10px; color: #666; border-top: 1px solid #eee;">\n        Digital Archaeological Restoration \| Original © 1997 CSC PLOENZKE AG \&amp; INC Creator: <a href="https:\/\/cotoaga.net" style="color: #666;">Kurt Cotoaga<\/a>\n    <\/div>|g' "$file"
    
    # Fix any broken &lt;INC.&gt; or similar issues
    sed -i '' -E 's|CSC PLOENZKE AG &amp;amp; &amp;lt;INC.&amp;gt;|CSC PLOENZKE AG \&amp; INC|g' "$file"
    sed -i '' -E 's|CSC PLOENZKE AG &amp;amp; &lt;INC.&gt;|CSC PLOENZKE AG \&amp; INC|g' "$file"
    sed -i '' -E 's|CSC PLOENZKE AG &amp; &lt;INC.&gt;|CSC PLOENZKE AG \&amp; INC|g' "$file"
    
    echo "Updated $file"
done

echo "All footers standardized."