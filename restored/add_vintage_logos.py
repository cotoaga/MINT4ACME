#!/usr/bin/env python3
import re

# The file to update
file_path = "index.html"

# The list of logos to add
logos = [
    "fastcup.gif",
    "cosmoplayer.gif",
    "get_shockwave.gif",
    "ie_spotlight.gif",
    "ie_standardanimated.gif",
    "netnow4.gif",
    "optimized.gif",
    "qtlogo2.gif",
    "quicktimelogo.gif",
    "shockwave_flash.gif",
    "tuneup.gif"
]

# Create HTML for the logos section
logos_html = '''
        <div class="vintage-logos">
            <p>Original required plugins and browsers:</p>
            <div class="logo-grid">
'''

for logo in logos:
    logos_html += f'                <img src="../original/images/{logo}" alt="{logo.replace(".gif", "")}" class="vintage-logo">\n'

logos_html += '''            </div>
        </div>
'''

# Read the file
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Find the position to insert the logos - after the original application text and before the button
pattern = r'(        <p>This version preserves the original navigation structure, images, and content while replacing obsolete technologies\.</p>\s+        <p class="note">Original © 1997 CSC PLOENZKE AG and INC\. InterNet Consult GmbH</p>)'

# Insert the logos HTML
modified_content = re.sub(pattern, r'\1' + logos_html, content)

# Write the modified file
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(modified_content)

print(f"Added vintage logos to {file_path}")

# Now add the CSS to style the logos
css_file_path = "css/styles.css"

with open(css_file_path, 'r', encoding='utf-8') as file:
    css_content = file.read()

# CSS to add
logo_css = '''
/* Vintage logos in disclaimer */
.vintage-logos {
    margin: 20px 0;
    text-align: center;
}

.logo-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 15px;
    margin-top: 10px;
}

.vintage-logo {
    max-height: 40px;
    margin: 5px;
}
'''

# Append the CSS
if ".vintage-logos" not in css_content:
    with open(css_file_path, 'a', encoding='utf-8') as file:
        file.write(logo_css)
    print(f"Added CSS for vintage logos to {css_file_path}")
else:
    print(f"CSS for vintage logos already exists in {css_file_path}")

print("Done!")