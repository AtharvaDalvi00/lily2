with open("pages/CalculatorsPage.tsx", "r") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if line.strip() == "{":
        if len(new_lines) > 0 and new_lines[-1].strip() == "import { EarlyLoanClosureLumpSumCalculator } from '../components/EarlyLoanClosureLumpSumCalculator';":
            new_lines.append("import { FileSpreadsheet, Zap, HeartHandshake, ArrowRightLeft, Landmark, TrendingUp, Calculator } from 'lucide-react';\n")
            new_lines.append("\nconst calculators = [\n")
            # skip the `{` and `iconColor: ... }` part because it's dangling
            continue
    if line.strip() == "iconColor: 'text-blue-600',":
        if len(new_lines) > 0 and new_lines[-1].strip() == "const calculators = [":
            continue
    if line.strip() == "},":
        if len(new_lines) > 0 and new_lines[-1].strip() == "const calculators = [":
            continue

    new_lines.append(line)

with open("pages/CalculatorsPage.tsx", "w") as f:
    f.writelines(new_lines)
