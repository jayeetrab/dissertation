import os, re, glob
for f in glob.glob('frontend/src/pages/*.jsx') + ['frontend/src/Components/ScorePanel.jsx']:
    with open(f, 'r') as file:
        content = file.read()
    # Replace delay={...} with nothing (we don't even need the prop anymore if it's 0)
    # Wait, if we just remove the delay prop from JSX tags:
    content = re.sub(r'\sdelay=\{[^}]+\}', '', content)
    # Replace delay inside objects: transition={{ delay: ..., duration: ... }}
    content = re.sub(r'delay:\s*[^,{}]+,?', '', content)
    with open(f, 'w') as file:
        file.write(content)
print("Done")
