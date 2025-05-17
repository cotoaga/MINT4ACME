#!/usr/bin/env python3
"""
Script to update the copyright footer in all HTML files
"""

import os
import re
import glob
from pathlib import Path

# Directory containing the HTML files
base_dir = "/Users/kydroon/Documents/GitHub/mint-4-acme/MINT4ACME/restored"

# New copyright text
new_copyright = 'Digital Archaeological Restoration | Original © 1997 CSC PLOENZKE AG &amp; &lt;INC.&gt; InterNet Consult GmbH Creator: <a href="https://cotoaga.net" style="color: #666;">Kurt Cotoaga</a>'

# Pattern to match the copyright div
pattern = r'<div style="text-align: center; font-size: 0.8rem; margin-top: 20px; color: #666;">\s*Digital Archaeological Restoration \| Original © 1997[^<]*\s*</div>'

# Get all HTML files
html_files = glob.glob(os.path.join(base_dir, "*.html"))

updated_files = 0

# Process each HTML file
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Skip backup files
    if ".bak" in filepath:
        continue
    
    # Check if we need to update this file
    if re.search(pattern, content):
        # Replace the copyright text
        new_content = re.sub(
            pattern,
            f'<div style="text-align: center; font-size: 0.8rem; margin-top: 20px; color: #666;">\n        {new_copyright}\n    </div>',
            content
        )
        
        # Write the updated content back to the file
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(new_content)
        
        print(f"Updated: {os.path.basename(filepath)}")
        updated_files += 1

print(f"\nTotal files updated: {updated_files}")