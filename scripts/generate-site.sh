#!/bin/bash

# Script to generate static website from markdown documentation
set -e

echo "Generating documentation website..."

# Create output directory if it doesn't exist
mkdir -p 05_DOCUMENTATION/docs/website

# Copy markdown files and convert to HTML
echo "Converting markdown files to HTML..."

# Find all markdown files in documentation directory
find 05_DOCUMENTATION/docs -name "*.md" -type f | while read file; do
  # Get relative path and filename without extension
  relative_path="${file#05_DOCUMENTATION/docs/}"
  filename="${relative_path%.md}"
  
  # Create output directory structure
  output_dir="05_DOCUMENTATION/docs/website/$(dirname "$relative_path")"
  mkdir -p "$output_dir"
  
  # Convert markdown to HTML
  # Using basic conversion - in a real scenario, you might want to use a more sophisticated tool
  # like pandoc or a custom script with proper styling
  title=$(head -n 1 "$file" | sed 's/^# *//')
  if [ -z "$title" ]; then
    title="$filename"
  fi
  
  {
    echo "<!DOCTYPE html>"
    echo "<html lang=\"en\">"
    echo "<head>"
    echo "  <meta charset=\"UTF-8\">"
    echo "  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">"
    echo "  <title>$title</title>"
    echo "  <style>"
    echo "    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji'; max-width: 800px; margin: 0 auto; padding: 20px; line-height: 1.6; color: #333; }"
    echo "    h1, h2, h3 { border-bottom: 1px solid #eaecef; padding-bottom: 0.3em; }"
    echo "    code { background-color: #f6f8fa; padding: 0.2em 0.4em; border-radius: 3px; font-size: 85%; }"
    echo "    pre { background-color: #f6f8fa; padding: 16px; overflow: auto; border-radius: 3px; }"
    echo "    blockquote { margin: 0; padding: 0 1em; color: #6a737d; border-left: 0.25em solid #dfe2e5; }"
    echo "    table { border-collapse: collapse; width: 100%; margin-bottom: 16px; }"
    echo "    th, td { border: 1px solid #dfe2e5; padding: 6px 13px; }"
    echo "    th { background-color: #f6f8fa; }"
    echo "  </style>"
    echo "</head>"
    echo "<body>"
    echo "<nav>"
    echo "  <a href=\"index.html\">Home</a>"
    echo "</nav>"
    echo "<main>"
    
    # Convert markdown to HTML (basic conversion)
    # This is a simple approach - for production use, consider using a proper markdown parser
    sed -e 's/&/\&/g' -e 's/</\</g' -e 's/>/\>/g' "$file" | \
    sed -e 's/^# \(.*\)/<h1>\1<\/h1>/' \
        -e 's/^## \(.*\)/<h2>\1<\/h2>/' \
        -e 's/^### \(.*\)/<h3>\1<\/h3>/' \
        -e 's/^\*\*\(.*\)\*\*/<strong>\1<\/strong>/' \
        -e 's/^\*\(.*\)\*/<em>\1<\/em>/' \
        -e 's/^- \(.*\)/<li>\1<\/li>/' \
        -e 's/`\(.*\)`/<code>\1<\/code>/g' \
        -e 's/^\(.*\)$/  <p>\1<\/p>/'
    
    echo "</main>"
    echo "<footer>"
    echo "  <p>Generated from documentation</p>"
    echo "</footer>"
    echo "</body>"
    echo "</html>"
  } > "05_DOCUMENTATION/docs/website/${filename}.html"
done

# Create index.html
cat > 05_DOCUMENTATION/docs/website/index.html << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Documentation</title>
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji'; max-width: 800px; margin: 0 auto; padding: 20px; line-height: 1.6; color: #333; }
    h1 { border-bottom: 1px solid #eaecef; padding-bottom: 0.3em; }
    ul { list-style-type: none; padding: 0; }
    li { margin: 10px 0; padding: 10px; background-color: #f6f8fa; border-radius: 3px; }
    a { text-decoration: none; color: #0366d6; }
    a:hover { text-decoration: underline; }
  </style>
</head>
<body>
  <h1>Documentation</h1>
  <ul>
    <li><a href="README.html">README</a></li>
  </ul>
</body>
</html>
EOF

echo "Documentation website generated successfully in 05_DOCUMENTATION/docs/website/"