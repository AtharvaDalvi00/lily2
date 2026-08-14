import React, { useEffect } from 'react';
import { Routes, Route } from 'react-router-dom';
import Lenis from 'lenis';
import 'lenis/dist/lenis.css';
import { Header } from './components/Header';
import { Footer } from './components/Footer';
import { Home } from './pages/Home';
import { FinancialPlanningDetails } from './pages/FinancialPlanningDetails';
import { WealthManagementDetails } from './pages/WealthManagementDetails';
import { InvestmentPortfolioDetails } from './pages/InvestmentPortfolioDetails';
import { MutualFundsDetails } from './pages/MutualFundsDetails';
import { InsurancePlanningDetails } from './pages/InsurancePlanningDetails';
import { RetirementPlanningDetails } from './pages/RetirementPlanningDetails';
import { NRISolutionsDetails } from './pages/NRISolutionsDetails';
import { RiskProfilingDetails } from './pages/RiskProfilingDetails';
import { EstateLegacyDetails } from './pages/EstateLegacyDetails';
import { AuthPortal } from './pages/AuthPortal';

import { ResourcesPage } from './pages/ResourcesPage';
import { CalculatorsPage } from './pages/CalculatorsPage';
import { Chatbot } from './components/Chatbot';

function App() {
  useEffect(() => {
    const lenis = new Lenis({
      duration: 1.2,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)), 
    } as any);

    function raf(time: number) {
      lenis.raf(time);
      requestAnimationFrame(raf);
    }

    requestAnimationFrame(raf);

    return () => {
      lenis.destroy();
    };
  }, []);

  return (
    <div className="bg-brand-light font-sans selection:bg-brand-primary selection:text-white">
      <Header />
      <main>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/auth" element={<AuthPortal />} />
          <Route path="/resources" element={<ResourcesPage />} />
          <Route path="/calculators" element={<CalculatorsPage />} />
          <Route path="/financial-planning" element={<FinancialPlanningDetails />} />
          <Route path="/wealth-management" element={<WealthManagementDetails />} />
          <Route path="/investment-portfolio" element={<InvestmentPortfolioDetails />} />
          <Route path="/mutual-funds" element={<MutualFundsDetails />} />
          <Route path="/insurance-planning" element={<InsurancePlanningDetails />} />
          <Route path="/retirement-planning" element={<RetirementPlanningDetails />} />
          <Route path="/nri-solutions" element={<NRISolutionsDetails />} />
          <Route path="/risk-profiling" element={<RiskProfilingDetails />} />
          <Route path="/estate-legacy" element={<EstateLegacyDetails />} />
        </Routes>
      </main>
      <Footer />
      <Chatbot />
    </div>
  );
}

export default App;