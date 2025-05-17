#!/usr/bin/env python3
import os
import glob

# The copyright footer we're looking for
COPYRIGHT_TEXT = "Digital Archaeological Restoration | Original © 1997 CSC PLOENZKE AG"

# Find all HTML files
html_files = glob.glob('*.html')

print(f"Found {len(html_files)} HTML files to process")

# Files with missing copyright
missing_copyright = []

# Files that have copyright but in archaeology note
has_archaeology_note = []

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Check if file has the copyright text
    if COPYRIGHT_TEXT not in content:
        missing_copyright.append(file_path)
    
    # Check if file has archaeology note
    if '<div class="archaeology-note">' in content:
        has_archaeology_note.append(file_path)

print("\nFiles missing copyright text:")
for file in missing_copyright:
    print(f"  {file}")

print("\nFiles with archaeology note:")
for file in has_archaeology_note:
    print(f"  {file}")

print(f"\nSummary: {len(missing_copyright)} files missing copyright, {len(has_archaeology_note)} files have archaeology note")