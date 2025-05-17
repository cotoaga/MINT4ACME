#!/bin/bash
# Script to add title animations to all HTML files in the restored directory

# Path to the restored directory
RESTORED_DIR="/Users/kydroon/Documents/GitHub/mint-4-acme/MINT4ACME/restored"

# Create js directory if it doesn't exist
mkdir -p "$RESTORED_DIR/js"

# Backup the original files
echo "Creating backup of HTML files..."
mkdir -p "$RESTORED_DIR/backup_$(date +%Y%m%d)"
cp "$RESTORED_DIR"/*.html "$RESTORED_DIR/backup_$(date +%Y%m%d)/"

# Update all HTML files to include the animation CSS and JS
echo "Updating HTML files to include animation references..."
for html_file in "$RESTORED_DIR"/*.html; do
  # Skip if it's a backup file
  if [[ "$html_file" == *".bak"* ]]; then
    continue
  fi
  
  # Add animation CSS and JS to head section
  sed -i.bak 's/<link rel="stylesheet" href="css\/styles.css">/<link rel="stylesheet" href="css\/styles.css">\n    <link rel="stylesheet" href="css\/title-animation.css">\n    <script src="js\/title-animation.js" defer><\/script>/g' "$html_file"
  
  echo "Updated: $html_file"
done

echo "Animation updates complete!"
echo "The original Flash title animations have been replaced with modern CSS/JS animations."
echo "Check any page with a title-text class to see the animation."