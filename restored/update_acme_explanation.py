#!/usr/bin/env python3
import os
import re
import glob

# Find all HTML files
html_files = glob.glob('*.html')

print(f"Found {len(html_files)} HTML files to process")

# The text pattern to look for
PATTERN = r'MINT \(Multimedia Information, Negotiation and Transaction\) for ACME was a revolutionary web-based automotive sales application developed in 1997\.'

# The replacement text with ACME explanation
REPLACEMENT = 'MINT (Multimedia Information, Negotiation and Transaction) for ACME (A Car Maker in Europe) was a revolutionary web-based automotive sales application developed in 1997.'

# Track statistics
modified_count = 0

for file_path in html_files:
    print(f"Processing {file_path}...")
    
    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Check if the text exists and replace it
    if PATTERN in content:
        # Replace the text
        new_content = content.replace(PATTERN, REPLACEMENT)
        
        # If content was modified, write it back
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            modified_count += 1
            print(f"  Updated ACME explanation in {file_path}")
        else:
            print(f"  No changes needed in {file_path}")
    else:
        print(f"  Pattern not found in {file_path}")

print(f"\nSummary: Updated ACME explanation in {modified_count} out of {len(html_files)} files")