#!/usr/bin/env python3
import os
import re
import glob

# The copyright footer we want to restore
COPYRIGHT_FOOTER = """<div style="text-align: center; font-size: 0.8rem; margin-top: 20px; color: #666;">
        Digital Archaeological Restoration | Original © 1997 CSC PLOENZKE AG &amp; INC InterNet Consult GmbH Creator: <a href="https://cotoaga.net" style="color: #666;">Kurt Cotoaga</a>
    </div>"""

# Find all HTML files
html_files = glob.glob('*.html')

print(f"Found {len(html_files)} HTML files to process")

for file_path in html_files:
    print(f"Processing {file_path}...")
    
    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Skip files that already have the copyright footer
    if 'Digital Archaeological Restoration | Original © 1997 CSC PLOENZKE AG' in content:
        print(f"  Skipping {file_path} - already has copyright footer")
        continue
    
    # Keep the archaeology note, but add the copyright footer before the closing body tag
    if '</body>' in content:
        content = content.replace('</body>', f"{COPYRIGHT_FOOTER}\n</body>")
    
    # Write the modified content back
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

print("Copyright footer restoration complete!")