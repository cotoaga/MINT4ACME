#!/usr/bin/env python3
import os
import re
import glob

# Directory containing the restored HTML files
restored_dir = "/Users/kydroon/Documents/GitHub/mint-4-acme/MINT4ACME/restored"

# Pages to process - list all numbered section pages
pages_to_process = [
    "1_1.html", "1_2.html", "1_3.html",
    "2_1.html", "2_2.html", "2_3.html", "2_4.html", "2_5.html",
    "3_1.html", "3_2.html",
    "4_1.html", "4_2.html", "4_3.html", "4_4.html", "4_5.html", "4_6.html", "4_7.html", "4_8.html", "4_9.html",
    "5_1.html", "5_2.html", "5_3.html"
]

# Regular expressions for identifying navigation links with GIF icons
back_pattern = re.compile(r'<a href="([^"]+)" class="nav-link">\s*<img src="\.\./original/images/back.gif" alt="Back" width="30" height="24">\s*<span>([^<]+)</span>\s*</a>', re.DOTALL)
forward_pattern = re.compile(r'<a href="([^"]+)" class="nav-link">\s*<img src="\.\./original/images/forward.gif" alt="Forward" width="30" height="24">\s*<span>([^<]+)</span>\s*</a>', re.DOTALL)

# Replacement templates
back_replacement = r'<a href="\1" class="nav-link">\n                    <span class="nav-arrow">⬅️</span>\n                    <span>\2</span>\n                </a>'
forward_replacement = r'<a href="\1" class="nav-link">\n                    <span class="nav-arrow">➡️</span>\n                    <span>\2</span>\n                </a>'

# CSS to add for the new navigation arrows if not present
nav_arrow_css = """
        .nav-arrow {
            font-size: 1.2rem;
            margin-right: 5px;
        }
"""

# Process each page
for page in pages_to_process:
    file_path = os.path.join(restored_dir, page)
    
    # Skip if file doesn't exist
    if not os.path.exists(file_path):
        print(f"Skipping {page} - file not found")
        continue
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Check if already has nav-arrow class
        has_nav_arrow = '.nav-arrow' in content
        
        # Replace back and forward navigation icons
        modified_content = back_pattern.sub(back_replacement, content)
        modified_content = forward_pattern.sub(forward_replacement, modified_content)
        
        # Add the CSS for nav-arrow if needed
        if not has_nav_arrow and 'head' in modified_content:
            css_insert_pattern = re.compile(r'(\.nav-link:hover\s*\{[^\}]*\})')
            modified_content = css_insert_pattern.sub(r'\1\n' + nav_arrow_css, modified_content)
        
        # Write the modified content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(modified_content)
        
        print(f"Updated navigation in {page}")
    
    except Exception as e:
        print(f"Error processing {page}: {e}")

print("\nNavigation icons have been updated with modern Unicode arrows in all HTML files.")