#!/usr/bin/env python3
import os
import re
import glob

# Find all HTML files
html_files = glob.glob('*.html')

print(f"Found {len(html_files)} HTML files to process")

# The copyright footer div we want to remove
COPYRIGHT_DIV_PATTERN = r'<div style="text-align: center; font-size: 0.8rem; margin-top: 20px; color: #666;">\s*Digital Archaeological Restoration \| Original © 1997 CSC PLOENZKE AG &amp; INC InterNet Consult GmbH Creator: <a href="https://cotoaga.net" style="color: #666;">Kurt Cotoaga</a>\s*</div>'

# Track statistics
modified_count = 0

for file_path in html_files:
    print(f"Processing {file_path}...")
    
    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Check if the copyright footer exists and remove it
    new_content = re.sub(COPYRIGHT_DIV_PATTERN, '', content)
    
    # If content was modified, write it back
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        modified_count += 1
        print(f"  Removed copyright footer from {file_path}")
    else:
        print(f"  No copyright footer found in {file_path}")

print(f"\nSummary: Removed copyright footer from {modified_count} out of {len(html_files)} files")