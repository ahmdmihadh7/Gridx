import re

with open('index.html', encoding='utf-8') as f:
    text = f.read()

ids = re.findall(r'id=[\'"]([^\'"]+)[\'"]', text)
print("Matching IDs:")
for i in ids:
    if any(k in i.lower() for k in ['diag', 'balance', 'status', 'power', 'bms', 'ai', 'health', 'island']):
        print(' -', i)
