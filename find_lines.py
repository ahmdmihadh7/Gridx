with open('index.html', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'islandAvailGen' in l or 'diagHeading' in l or 'bmsThermalBadge' in l:
        print(f"Line {i+1}: {l.strip()[:100]}")
