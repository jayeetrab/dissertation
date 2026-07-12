import os, re, glob
for f in glob.glob('frontend/src/pages/*.jsx') + ['frontend/src/Components/ScorePanel.jsx']:
    with open(f, 'r') as file:
        content = file.read()
    # Remove delay prop in JSX: delay={...}
    content = re.sub(r'\sdelay=\{[^}]+\}', '', content)
    
    # Remove delay inside transition objects
    # This matches `delay: ` followed by either a Math.min(...) expression, or anything not comma/brace, followed by optional comma
    content = re.sub(r'delay:\s*(?:Math\.min\([^)]+\)|[^,}]+)\s*,?\s*', '', content)
    
    with open(f, 'w') as file:
        file.write(content)
print("Done")
