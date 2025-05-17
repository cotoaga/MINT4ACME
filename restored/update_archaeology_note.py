#!/usr/bin/env python3
import os
import re
import glob

# Updated archaeology note text
NEW_ARCHAEOLOGY_NOTE = """<div class="archaeology-note">
    <strong>Digital Archaeology Note:</strong> This is a modern restoration of a 1997 web application. 
    The original used Flash animations, auto-playing WAV files, frames, and obsolete web technologies. 
    These have been replaced with HTML5 equivalents while preserving the original look and navigation structure. 
    Background images are now more visible, and redundant copyright footers have been removed.
</div>"""

# Find all HTML files
html_files = glob.glob('*.html')

print(f"Found {len(html_files)} HTML files to process")

for file_path in html_files:
    print(f"Processing {file_path}...")
    
    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace existing archaeology notes with the new one
    if '<div class="archaeology-note">' in content:
        # Replace the existing archaeology note
        content = re.sub(
            r'<div class="archaeology-note">.*?</div>',
            NEW_ARCHAEOLOGY_NOTE,
            content,
            flags=re.DOTALL
        )
    elif '<hr>' in content and '</div>' in content:
        # Add archaeology note before the last <hr> in the content div
        match = re.search(r'(.*<div class="content">.*?)(</div>\s*<hr>)', content, re.DOTALL)
        if match:
            content = content.replace(
                match.group(0),
                f"{match.group(1)}\n        {NEW_ARCHAEOLOGY_NOTE}\n    {match.group(2)}"
            )
    
    # Write the modified content back
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

print("Archaeology note update complete!")