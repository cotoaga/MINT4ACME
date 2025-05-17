#!/usr/bin/env python3

import os
import re
import shutil
import datetime
from bs4 import BeautifulSoup

# Directory containing the HTML files
directory = "/Users/kydroon/Documents/GitHub/mint-4-acme/MINT4ACME/restored"

# Create backup directory
backup_dir = os.path.join(directory, f"backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}")
os.makedirs(backup_dir, exist_ok=True)
print(f"Created backup directory: {backup_dir}")

# Regular expression to find CSS rules in style tags
def update_css_colors(css_content):
    # Replace all color: var(--primary) with color: var(--dark) in .title-text
    pattern = r'(\.title-text\s*{[^{}]*?)color\s*:\s*var\(--primary\)([^{}]*?})'
    css_content = re.sub(pattern, r'\1color: var(--dark)\2', css_content, flags=re.DOTALL)
    
    # Replace all color: var(--primary) in h1, h2, h3, h4 selectors
    for selector in ['h1', 'h2', 'h3', 'h4']:
        pattern = r'(' + selector + r'\s*{[^{}]*?)color\s*:\s*var\(--primary\)([^{}]*?})'
        css_content = re.sub(pattern, r'\1color: var(--dark)\2', css_content, flags=re.DOTALL)
    
    return css_content

# Process each HTML file
for filename in os.listdir(directory):
    if not filename.endswith('.html'):
        continue
    
    file_path = os.path.join(directory, filename)
    backup_path = os.path.join(backup_dir, filename)
    
    # Create backup
    shutil.copy2(file_path, backup_path)
    
    print(f"Processing: {filename}")
    
    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Create BeautifulSoup object (but don't parse styles with it)
    soup = BeautifulSoup(content, 'html.parser')
    
    # Find all style tags
    style_tags = soup.find_all('style')
    
    # Process each style tag
    changes_made = False
    for style_tag in style_tags:
        original_css = style_tag.string
        if original_css:
            updated_css = update_css_colors(original_css)
            if original_css != updated_css:
                style_tag.string = updated_css
                changes_made = True
    
    # Only write the file if changes were made
    if changes_made:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(str(soup))
        print(f"  Updated CSS in {filename}")
    else:
        print(f"  No changes needed in {filename}")

print(f"Update complete. Backups saved in {backup_dir}")