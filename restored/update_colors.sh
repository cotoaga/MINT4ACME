#!/bin/bash

# Script to update CSS in all HTML files in the restored directory
# Changes var(--primary) to var(--dark) for:
# 1. .title-text elements
# 2. h1, h2, h3, h4 elements

DIR="/Users/kydroon/Documents/GitHub/mint-4-acme/MINT4ACME/restored"
BACKUP_DIR="$DIR/backup_$(date +%Y%m%d_%H%M%S)"

# Create backup directory
mkdir -p "$BACKUP_DIR"
echo "Created backup directory: $BACKUP_DIR"

# Process each HTML file
for file in "$DIR"/*.html; do
  filename=$(basename "$file")
  
  # Make a backup
  cp "$file" "$BACKUP_DIR/$filename"
  
  echo "Processing: $filename"
  
  # Replace var(--primary) with var(--dark) for .title-text
  sed -i.bak 's/\.title-text[^}]*color: var(--primary)/\.title-text\n            color: var(--dark)/g' "$file"
  
  # Replace var(--primary) with var(--dark) for h1, h2, h3, h4
  sed -i.bak 's/h1[^}]*color: var(--primary)/h1\n            color: var(--dark)/g' "$file"
  sed -i.bak 's/h2[^}]*color: var(--primary)/h2\n            color: var(--dark)/g' "$file"
  sed -i.bak 's/h3[^}]*color: var(--primary)/h3\n            color: var(--dark)/g' "$file"
  sed -i.bak 's/h4[^}]*color: var(--primary)/h4\n            color: var(--dark)/g' "$file"
  
  # Clean up the .bak files created by sed -i
  rm "$file.bak"
done

echo "Update complete. Backups saved in $BACKUP_DIR"