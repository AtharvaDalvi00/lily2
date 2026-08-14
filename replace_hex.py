import os
import re

replacements = {
    # Emerald/Teal to Sky
    '#059669': '#0284C7',
    '#10B981': '#0EA5E9',
    '#047857': '#0369A1',
    '#ECFDF5': '#F0F9FF',
    '#A7F3D0': '#BAE6FD',
    '#D1FAE5': '#E0F2FE',
    '#065F46': '#075985',
    # Rose to Blue
    '#BE123C': '#1D4ED8',
    '#E11D48': '#3B82F6',
    '#FDA4AF': '#BFDBFE',
    '#FFF1F2': '#EFF6FF',
    '#FFE4E6': '#DBEAFE',
    '#DC2626': '#2563EB',
    # Indigo to Blue
    '#4F46E5': '#2563EB',
    '#6366F1': '#3B82F6',
    '#4338CA': '#1D4ED8',
    '#EEF2FF': '#EFF6FF',
    '#C7D2FE': '#BFDBFE',
    '#E0E7FF': '#DBEAFE',
    # Orange to Sky
    '#EA580C': '#0284C7',
}

def replace_in_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
        
    for old, new in replacements.items():
        # Case insensitive replacement for hex codes
        pattern = re.compile(re.escape(old), re.IGNORECASE)
        content = pattern.sub(new, content)
        
    with open(filepath, 'w') as f:
        f.write(content)

for filename in os.listdir('components'):
    if filename.endswith('.tsx'):
        replace_in_file(os.path.join('components', filename))

