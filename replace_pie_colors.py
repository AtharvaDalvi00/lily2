import re

filepath = 'components/ComprehensivePortfolio.tsx'
with open(filepath, 'r') as f:
    content = f.read()

replacements = {
    '#6ab11e': '#0284C7',
    '#ffb330': '#3B82F6',
    '#578bbd': '#0EA5E9',
    '#8c6d59': '#60A5FA',
    '#f2ab35': '#1D4ED8',
    '#649ed9': '#38BDF8',
    '#996ba5': '#1E3A8A',
    '#d8a45e': '#7DD3FC',
    '#ee302a': '#2563EB',
    '#848484': '#94A3B8'
}

for old, new in replacements.items():
    pattern = re.compile(re.escape(old), re.IGNORECASE)
    content = pattern.sub(new, content)

with open(filepath, 'w') as f:
    f.write(content)
