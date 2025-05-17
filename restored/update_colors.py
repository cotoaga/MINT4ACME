#!/usr/bin/env python3

import os
import re
import shutil
import datetime

# Directory containing the HTML files
directory = "/Users/kydroon/Documents/GitHub/mint-4-acme/MINT4ACME/restored"

# Create backup directory
backup_dir = os.path.join(directory, f"backup_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}")
os.makedirs(backup_dir, exist_ok=True)
print(f"Created backup directory: {backup_dir}")

# Patterns to match CSS rules
title_text_pattern = re.compile(r'(\.title-text\s*\{[^}]*color\s*:\s*)var\(--primary\)([^}]*\})', re.DOTALL)
h1_pattern = re.compile(r'(h1\s*\{[^}]*color\s*:\s*)var\(--primary\)([^}]*\})', re.DOTALL)
h2_pattern = re.compile(r'(h2\s*\{[^}]*color\s*:\s*)var\(--primary\)([^}]*\})', re.DOTALL)
h3_pattern = re.compile(r'(h3\s*\{[^}]*color\s*:\s*)var\(--primary\)([^}]*\})', re.DOTALL)
h4_pattern = re.compile(r'(h4\s*\{[^}]*color\s*:\s*)var\(--primary\)([^}]*\})', re.DOTALL)

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
    
    # Replace var(--primary) with var(--dark)
    modified_content = title_text_pattern.sub(r'\1var(--dark)\2', content)
    modified_content = h1_pattern.sub(r'\1var(--dark)\2', modified_content)
    modified_content = h2_pattern.sub(r'\1var(--dark)\2', modified_content)
    modified_content = h3_pattern.sub(r'\1var(--dark)\2', modified_content)
    modified_content = h4_pattern.sub(r'\1var(--dark)\2', modified_content)
    
    # Write the modified content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(modified_content)

print(f"Update complete. Backups saved in {backup_dir}")