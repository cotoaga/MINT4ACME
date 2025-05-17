#!/usr/bin/env python3
import os
import re
import glob

# Find all HTML files
html_files = glob.glob('*.html')

print(f"Found {len(html_files)} HTML files to process")

for file_path in html_files:
    print(f"Processing {file_path}...")
    
    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove copyright footer from regular content pages
    content = re.sub(
        r'<div style="text-align: center; font-size: 0\.8rem; margin-top: 20px; color: #666;">.*?Digital Archaeological Restoration.*?<\/div>',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Remove copyright div from index.html 
    if file_path == 'index.html':
        content = re.sub(
            r'<div class="copyright">.*?Digital Archaeological Restoration.*?<\/div>',
            '',
            content,
            flags=re.DOTALL
        )
    
    # Write the modified content back
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

print("Footer removal complete!")