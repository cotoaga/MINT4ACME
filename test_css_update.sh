#!/bin/bash

# Test script for updating a single file to use external CSS

RESTORED_DIR="/Users/kydroon/Documents/GitHub/mint-4-acme/MINT4ACME/restored"
TEST_FILE="$RESTORED_DIR/1_1.html"
BACKUP_FILE="$RESTORED_DIR/1_1.html.bak"

# Create backup
cp "$TEST_FILE" "$BACKUP_FILE"
echo "Created backup: $BACKUP_FILE"

# Replace the style block with a link to the external CSS
sed -i '' '/<style>/,/<\/style>/c\
    <link rel="stylesheet" href="css/styles.css">' "$TEST_FILE"

echo "Updated test file to use external CSS"
echo "Original file is backed up as $BACKUP_FILE"
echo "You can check the result and then run the full script if it looks good."