import fs from 'fs';
import path from 'path';

const images = {
  'FinancialPlanningDetails.tsx': 'https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?w=1600&q=80',
  'WealthManagementDetails.tsx': 'https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?w=1600&q=80',
  'InvestmentPortfolioDetails.tsx': 'https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=1600&q=80',
  'MutualFundsDetails.tsx': 'https://images.unsplash.com/photo-1579532537598-459ecdaf39cc?w=1600&q=80',
  'TaxOptimizationDetails.tsx': 'https://images.unsplash.com/photo-1586486855514-8c633cc1fd29?w=1600&q=80',
  'RetirementPlanningDetails.tsx': 'https://images.unsplash.com/photo-1473186578172-c141e6798cf4?w=1600&q=80',
  'NRISolutionsDetails.tsx': 'https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=1600&q=80',
  'EstateLegacyDetails.tsx': 'https://images.unsplash.com/photo-1521791136064-7986c2920216?w=1600&q=80',
  'RiskProfilingDetails.tsx': 'https://images.unsplash.com/photo-1633158829585-23ba8f7c8caf?w=1600&q=80',
  'InsurancePlanningDetails.tsx': 'https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=1600&q=80',
};

const pagesDir = path.join(process.cwd(), 'pages');
const files = fs.readdirSync(pagesDir);

for (const file of files) {
  if (images[file]) {
    const filePath = path.join(pagesDir, file);
    let content = fs.readFileSync(filePath, 'utf8');

    // Add image if not already added
    if (!content.includes('<img src="https://images.unsplash.com')) {
      const regex = /(className="py-20 bg-brand-light relative overflow-hidden"(\s*)>\s*)(<div className="absolute top-0)/g;
      
      const insert = `$1<div className="absolute inset-0 z-0">\n          <img src="${images[file]}" alt="Background" className="w-full h-full object-cover opacity-[0.06] mix-blend-multiply" />\n        </div>\n        $3`;
      
      content = content.replace(regex, insert);
      fs.writeFileSync(filePath, content, 'utf8');
      console.log(`Updated ${file}`);
    }
  }
}
