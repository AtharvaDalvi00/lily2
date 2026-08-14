import re
import os

files = [
    'components/TenureIncreaseCalculator.tsx'
]

for file in files:
    with open(file, 'r') as f:
        content = f.read()

    # Find where the Header starts
    header_idx = content.find('{/* Header */}')
    if header_idx == -1:
        print(f"Header not found in {file}")
        continue
    
    next_section_idx = content.find('{/* Split Panels */}', header_idx)
        
    if next_section_idx == -1:
        print(f"Could not find end of header in {file}")
        continue
        
    old_header = content[header_idx:next_section_idx]
    
    # Find Title
    title_match = re.search(r'<h[23][^>]*>(.*?)</h[23]>', old_header)
    title = title_match.group(1) if title_match else "Calculator"
    
    # Find Subtitle
    sub_match = re.search(r'<p[^>]*text-[a-z]+-100[^>]*>(.*?)</p>', old_header)
    if not sub_match:
        sub_match = re.search(r'<p[^>]*text-slate-[0-9]+[^>]*>(.*?)</p>', old_header)
    if not sub_match:
        sub_match = re.search(r'<p[^>]*text-[a-z]+-200[^>]*>(.*?)</p>', old_header)
    if not sub_match:
        sub_match = re.search(r'<p[^>]*text-sky-[0-9]+[^>]*>(.*?)</p>', old_header)
        
    subtitle = sub_match.group(1) if sub_match else "Interactive Planner"
    
    # Find Icon
    icon_match = re.search(r'<([A-Z][a-zA-Z]+) className="w-6 h-6"', old_header)
    icon = icon_match.group(1) if icon_match else "Calculator"
    
    export_fn = "exportToExcel()"
        
    # Check if LeadFormModal is imported
    if "LeadFormModal" not in content:
        content = content.replace("import { motion } from 'motion/react';", "import { motion } from 'motion/react';\nimport { LeadFormModal } from './LeadFormModal';")

    if "import { LeadFormModal }" not in content:
        if "import React" in content:
            content = content.replace("import React", "import { LeadFormModal } from './LeadFormModal';\nimport React")

    # Make sure we have isFormOpened and isFormModalOpen state
    if "isFormOpened" not in content:
        content = content.replace("const [", "const [isFormOpened, setIsFormOpened] = useState(false);\n  const [isFormModalOpen, setIsFormModalOpen] = useState(false);\n  const [", 1)

    # Check for Download import
    if "Download" not in content[:500]:
        content = content.replace("import { X,", "import { X, Download,")
        content = content.replace("import { Landmark, X", "import { Landmark, X, Download")
    
    # Remove old download buttons from the file
    content = re.sub(r'<button[^>]*onClick=\{[^}]*?download[^}]*?\}[^>]*>.*?</button>', '', content, flags=re.DOTALL)
    content = re.sub(r'<button[^>]*onClick=\{[^}]*?export[^}]*?\}[^>]*>.*?</button>', '', content, flags=re.DOTALL)
    content = re.sub(r'<LeadFormModal[^>]*/>', '', content, flags=re.DOTALL)
    
    new_header = f"""{{/* Header */}}
        <div className="flex flex-wrap items-center justify-between p-6 bg-brand-primary text-white border-b border-white/20 gap-4 shrink-0">
          <div className="flex items-center gap-3">
            <div className="bg-white/20 p-2.5 rounded-xl">
              <{icon} className="w-6 h-6" />
            </div>
            <div>
              <h2 className="text-xl font-bold tracking-tight">{title}</h2>
              <p className="text-xs text-blue-100">{subtitle}</p>
            </div>
          </div>
          <div className="flex items-center gap-3 ml-auto">
            <button
              onClick={{() => {{
                if (!isFormOpened) {{
                  setIsFormModalOpen(true);
                }} else {{
                  {export_fn};
                }}
              }}}}
              className={{`flex items-center gap-2 ${{isFormOpened ? 'bg-sky-600 hover:bg-sky-700' : 'bg-[#3B82F6] hover:bg-[#1D4ED8]'}} text-white px-4 py-2 rounded-xl transition-colors font-semibold text-sm shadow-sm`}}
            >
              <Download className="w-4 h-4" />
              {{isFormOpened ? 'Download Excel Sheet' : 'Fill Form & Download'}}
            </button>
            <LeadFormModal
              isOpen={{isFormModalOpen}}
              onClose={{() => setIsFormModalOpen(false)}}
              onSubmitAndDownload={{() => {{
                setIsFormOpened(true);
                setIsFormModalOpen(false);
                {export_fn};
              }}}}
            />
            <button onClick={{onClose}} className="p-2.5 bg-white/10 hover:bg-white/20 rounded-xl transition-colors text-white">
              <X className="w-5 h-5" />
            </button>
          </div>
        </div>
        """
        
    content = content.replace(old_header, new_header)
    
    with open(file, 'w') as f:
        f.write(content)
    print(f"Updated {file}")
