#!/usr/bin/env python3
import os
import re
import glob

# Find all HTML files
html_files = glob.glob('*.html')

print(f"Found {len(html_files)} HTML files to process")

# The archaeology note in the footer that we want to remove
# Specifically looking for the one that appears near the footer or footer-towers
FOOTER_ARCHAEOLOGY_NOTE_PATTERN = r'(<div class="footer(?:-towers)?">.*?</div>.*?)<div class="archaeology-note">.*?</div>'

# Track statistics
modified_count = 0

for file_path in html_files:
    print(f"Processing {file_path}...")
    
    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Look for archaeology notes that appear after the footer-towers div or within footer div
    match = re.search(FOOTER_ARCHAEOLOGY_NOTE_PATTERN, content, re.DOTALL)
    if match:
        # Remove the archaeology note
        new_content = content.replace(match.group(0), match.group(1))
        
        # If content was modified, write it back
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            modified_count += 1
            print(f"  Removed archaeology note from near footer in {file_path}")
        else:
            print(f"  No changes made to {file_path}")
    else:
        print(f"  No archaeology note near footer found in {file_path}")

print(f"\nSummary: Removed archaeology note from near footer in {modified_count} out of {len(html_files)} files")