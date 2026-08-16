from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

# 1) Browser tab title
s = re.sub(r'<title>.*?</title>', '<title>JEREMIE Studio</title>', s, count=1, flags=re.S)

# Remove any prior safe patch blocks before re-applying.
s = re.sub(r'\n?  /\* JEREMIE SAFE PATCH START \*/.*?/\* JEREMIE SAFE PATCH END \*/\n?', '\n', s, flags=re.S)
s = re.sub(r'\n?<script id="jeremie-safe-patch">.*?</script>\n?', '\n', s, flags=re.S)
s