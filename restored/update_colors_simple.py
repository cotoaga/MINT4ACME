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
    
    # Track if any changes were made
    original_content = content
    
    # Find the style section
    style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
    if style_match:
        style_content = style_match.group(1)
        
        # Update .title-text color
        updated_style = re.sub(
            r'(\.title-text\s*\{[^{}]*?)color\s*:\s*var\(--primary\)([^{}]*?\})',
            r'\1color: var(--dark)\2',
            style_content,
            flags=re.DOTALL
        )
        
        # Update h1, h2, h3, h4 colors
        for tag in ['h1', 'h2', 'h3', 'h4']:
            updated_style = re.sub(
                r'(' + tag + r'\s*\{[^{}]*?)color\s*:\s*var\(--primary\)([^{}]*?\})',
                r'\1color: var(--dark)\2',
                updated_style,
                flags=re.DOTALL
            )
        
        # Replace the style section in the full content
        content = content.replace(style_match.group(1), updated_style)
    
    # Only write if changes were made
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"  Updated CSS in {filename}")
    else:
        print(f"  No changes needed in {filename}")

print(f"Update complete. Backups saved in {backup_dir}")