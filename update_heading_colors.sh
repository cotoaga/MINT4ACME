#!/bin/bash

# Create a backup directory with timestamp
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_DIR="/Users/kydroon/Documents/GitHub/mint-4-acme/MINT4ACME/backups_$TIMESTAMP"
RESTORED_DIR="/Users/kydroon/Documents/GitHub/mint-4-acme/MINT4ACME/restored"

# Create backup directory
mkdir -p "$BACKUP_DIR"
echo "Created backup directory: $BACKUP_DIR"

# Copy all HTML files to backup
cp "$RESTORED_DIR"/*.html "$BACKUP_DIR/"
echo "Backed up all HTML files"

# Update .title-text CSS in all HTML files
echo "Updating .title-text in all HTML files..."
find "$RESTORED_DIR" -name "*.html" -exec sed -i '' 's/\.title-text {[^}]*color: var(--primary);/\.title-text {\n            display: block;\n            font-size: 2.2rem;\n            font-weight: bold;\n            color: var(--dark);\n            margin-bottom: 20px;\n            padding-bottom: 10px;\n            border-bottom: 2px solid var(--border);/g' {} \;

# Update h3 headings in content sections (like .problem-section h3)
echo "Updating h3 headings in content sections..."
find "$RESTORED_DIR" -name "*.html" -exec sed -i '' 's/\..*section h3 {[^}]*color: var(--primary);/\.problem-section h3 {\n            color: var(--dark);\n            margin-top: 0;\n            margin-bottom: 10px;/g' {} \;
find "$RESTORED_DIR" -name "*.html" -exec sed -i '' 's/\..*-item h3 {[^}]*color: var(--primary);/\.benefit-item h3 {\n            color: var(--dark);\n            margin-top: 0;\n            margin-bottom: 10px;/g' {} \;
find "$RESTORED_DIR" -name "*.html" -exec sed -i '' 's/\..*-description h3 {[^}]*color: var(--primary);/\.component-description h3 {\n            color: var(--dark);\n            margin-top: 0;\n            margin-bottom: 15px;\n            border-bottom: 1px solid #ddd;\n            padding-bottom: 5px;/g' {} \;
find "$RESTORED_DIR" -name "*.html" -exec sed -i '' 's/\.tech-stack h3 {[^}]*color: var(--primary);/\.tech-stack h3 {\n            color: var(--dark);\n            margin-top: 0;\n            margin-bottom: 15px;\n            border-bottom: 1px solid #ddd;\n            padding-bottom: 5px;/g' {} \;

echo "Done updating all heading colors to use var(--dark) instead of var(--primary)"