import AboutPage from './AboutPage';
import ClimateIntelligencePage from './ClimateIntelligencePage';
import ContactPage from './ContactPage';
import CybersecurityPage from './CybersecurityPage';
import DigitalTransformationPage from './DigitalTransformationPage';
import EnterpriseAiPage from './EnterpriseAiPage';
import HomePage from './HomePage';
import IndustriesBankingFinancialServicesPage from './IndustriesBankingFinancialServicesPage';
import IndustriesEnergyPage from './IndustriesEnergyPage';
import IndustriesGovernmentPublicSectorPage from './IndustriesGovernmentPublicSectorPage';
import IndustriesHealthcarePage from './IndustriesHealthcarePage';
import IndustriesInfrastructurePage from './IndustriesInfrastructurePage';
import IndustriesManufacturingPage from './IndustriesManufacturingPage';
import IndustriesProfessionalServicesPage from './IndustriesProfessionalServicesPage';
import IndustriesRealEstatePage from './IndustriesRealEstatePage';
import IndustriesTechnologyPage from './IndustriesTechnologyPage';
import IndustriesPage from './IndustriesPage';
import InsightsAiGovernanceForBoardsPage from './InsightsAiGovernanceForBoardsPage';
import InsightsClimateRiskManagementBankingPage from './InsightsClimateRiskManagementBankingPage';
import InsightsCyberResilienceStrategyPage from './InsightsCyberResilienceStrategyPage';
import InsightsIntegratedRiskManagementPage from './InsightsIntegratedRiskManagementPage';
import InsightsPage from './InsightsPage';
import RiskDecisionIntelligencePage from './RiskDecisionIntelligencePage';

export const pages = [
  { path: "\/about", Component: AboutPage, meta: AboutPage.meta },
  { path: "\/climate-intelligence", Component: ClimateIntelligencePage, meta: ClimateIntelligencePage.meta },
  { path: "\/contact", Component: ContactPage, meta: ContactPage.meta },
  { path: "\/cybersecurity", Component: CybersecurityPage, meta: CybersecurityPage.meta },
  { path: "\/digital-transformation", Component: DigitalTransformationPage, meta: DigitalTransformationPage.meta },
  { path: "\/enterprise-ai", Component: EnterpriseAiPage, meta: EnterpriseAiPage.meta },
  { path: "\/", Component: HomePage, meta: HomePage.meta },
  { path: "\/industries-banking-financial-services", Component: IndustriesBankingFinancialServicesPage, meta: IndustriesBankingFinancialServicesPage.meta },
  { path: "\/industries-energy", Component: IndustriesEnergyPage, meta: IndustriesEnergyPage.meta },
  { path: "\/industries-government-public-sector", Component: IndustriesGovernmentPublicSectorPage, meta: IndustriesGovernmentPublicSectorPage.meta },
  { path: "\/industries-healthcare", Component: IndustriesHealthcarePage, meta: IndustriesHealthcarePage.meta },
  { path: "\/industries-infrastructure", Component: IndustriesInfrastructurePage, meta: IndustriesInfrastructurePage.meta },
  { path: "\/industries-manufacturing", Component: IndustriesManufacturingPage, meta: IndustriesManufacturingPage.meta },
  { path: "\/industries-professional-services", Component: IndustriesProfessionalServicesPage, meta: IndustriesProfessionalServicesPage.meta },
  { path: "\/industries-real-estate", Component: IndustriesRealEstatePage, meta: IndustriesRealEstatePage.meta },
  { path: "\/industries-technology", Component: IndustriesTechnologyPage, meta: IndustriesTechnologyPage.meta },
  { path: "\/industries", Component: IndustriesPage, meta: IndustriesPage.meta },
  { path: "\/insights\/ai-governance-for-boards", Component: InsightsAiGovernanceForBoardsPage, meta: InsightsAiGovernanceForBoardsPage.meta },
  { path: "\/insights\/climate-risk-management-banking", Component: InsightsClimateRiskManagementBankingPage, meta: InsightsClimateRiskManagementBankingPage.meta },
  { path: "\/insights\/cyber-resilience-strategy", Component: InsightsCyberResilienceStrategyPage, meta: InsightsCyberResilienceStrategyPage.meta },
  { path: "\/insights\/integrated-risk-management", Component: InsightsIntegratedRiskManagementPage, meta: InsightsIntegratedRiskManagementPage.meta },
  { path: "\/insights", Component: InsightsPage, meta: InsightsPage.meta },
  { path: "\/risk-decision-intelligence", Component: RiskDecisionIntelligencePage, meta: RiskDecisionIntelligencePage.meta },
];
