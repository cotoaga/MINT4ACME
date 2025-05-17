#!/usr/bin/env python3
import os
import re
import glob

# Find all HTML files
html_files = glob.glob('*.html')

print(f"Found {len(html_files)} HTML files to process")

# The current footer that's outside the content container
COPYRIGHT_FOOTER = """<div style="text-align: center; font-size: 0.8rem; margin-top: 20px; color: #666;">
        Digital Archaeological Restoration | Original © 1997 CSC PLOENZKE AG &amp; INC InterNet Consult GmbH Creator: <a href="https://cotoaga.net" style="color: #666;">Kurt Cotoaga</a>
    </div>"""

# Path to the home page which gets special handling
HOME_PAGE = "home.html"
BLANK_PAGE = "blank.html"
INDEX_PAGE = "index.html"

for file_path in html_files:
    print(f"Processing {file_path}...")
    
    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Check if the copyright footer exists outside the content container
    if COPYRIGHT_FOOTER in content:
        # Remove the footer from outside the container
        content = content.replace(COPYRIGHT_FOOTER, "")
        
        # Special handling for home.html (append to .footer div)
        if file_path == HOME_PAGE:
            # Find the footer div
            footer_div = re.search(r'<div class="footer">\s*</div>', content)
            if footer_div:
                # Replace empty footer div with footer div containing copyright
                content = content.replace(
                    footer_div.group(0),
                    f'<div class="footer">\n        {COPYRIGHT_FOOTER}\n    </div>'
                )
        # Special handling for blank.html (append after the message div)
        elif file_path == BLANK_PAGE:
            # Insert after the message div and before the archaeology note
            content = re.sub(
                r'(</div>)(\s*<div class="archaeology-note">)',
                r'\1\n    ' + COPYRIGHT_FOOTER + r'\2',
                content
            )
        # Special handling for index.html (append to the footer section)
        elif file_path == INDEX_PAGE:
            # Find the footer div's closing tag
            footer_div_close = re.search(r'(<div class="archaeology-note">.*?</div>)\s*</div>', content, re.DOTALL)
            if footer_div_close:
                # Insert after the archaeology note but inside the footer div
                content = content.replace(
                    footer_div_close.group(0),
                    f'{footer_div_close.group(1)}\n            {COPYRIGHT_FOOTER}\n        </div>'
                )
        # For regular content pages, add before the closing </div> of content-container
        else:
            # Use regex to find the closing tag of content-container div
            content_container_close = re.search(r'</div>\s*</div>\s*\n\s*(<script|</body>)', content)
            if content_container_close:
                # Insert before the closing div tag
                content = content.replace(
                    content_container_close.group(0),
                    f"\n    {COPYRIGHT_FOOTER}\n</div>\n</div>\n\n    {content_container_close.group(1)}"
                )
        
        # Write the modified content back
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

print("Copyright footer repositioning complete!")