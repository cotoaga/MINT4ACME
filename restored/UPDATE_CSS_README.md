# CSS Update Tools for MINT4ACME Restored HTML Files

This directory contains scripts to update the CSS color variables in the HTML files from `var(--primary)` to `var(--dark)` for:
1. `.title-text` elements
2. Heading elements (h1, h2, h3, h4)

## Available Scripts

Three different approaches are provided:

### 1. Shell Script (update_colors.sh)

```bash
./update_colors.sh
```

Uses `sed` to perform the replacements. Simple but may have limitations with complex HTML/CSS.

### 2. Python Script with External Dependencies (update_colors_safe.py)

```bash
# Install dependencies first
pip install -r requirements.txt

# Then run the script
python update_colors_safe.py
```

Uses BeautifulSoup to properly parse the HTML and make targeted changes to the CSS. Most reliable but requires installing dependencies.

### 3. Simple Python Script (update_colors_simple.py)

```bash
python update_colors_simple.py
```

Uses Python's built-in regex module to find and replace CSS patterns. No external dependencies required.

## Backup

All scripts will automatically create a backup directory with timestamps before making any changes.

## Verification

After running any of the scripts, you should:

1. Check that all `.title-text` elements now use `var(--dark)` instead of `var(--primary)`
2. Check that all heading elements (h1, h2, h3, h4) now use `var(--dark)` instead of `var(--primary)`
3. View the pages in a browser to ensure they look correct