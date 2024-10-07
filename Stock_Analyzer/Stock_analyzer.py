# python Stock_Analyzer\Stock_analyzer.py
import os
import pandas as pd


from .select_sector.news_researcher import SectorNewsResearcher
from .select_sector.data_engineer import SectorDataEngineer
from .select_sector.data_scientist import SectorDataScientist
from .select_sector.frontend_developer import SectorFrontendDeveloper
from .select_sector.backend_developer import SectorBackendDeveloper
from .select_sector.quantitative_analyst import SectorQuantitativeAnalyst

from .select_company.news_researcher import CompanyNewsResearcher
from .select_company.data_engineer import CompanyDataEngineer
from .select_company.data_scientist import CompanyDataScientist
from .select_company.frontend_developer import CompanyFrontendDeveloper
from .select_company.backend_developer import CompanyBackendDeveloper
from .select_company.quantitative_analyst import CompanyQuantitativeAnalyst

from .overall_next_day.news_researcher import OverallNewsResearcher
from .overall_next_day.data_engineer import OverallDataEngineer
from .overall_next_day.data_scientist import OverallDataScientist
from .overall_next_day.frontend_developer import OverallFrontendDeveloper
from .overall_next_day.backend_developer import OverallBackendDeveloper
from .overall_next_day.quantitative_analyst import OverallQuantitativeAnalyst

from .ipo.news_researcher import IPO_NewsResearcher
from .ipo.data_engineer import IPO_DataEngineer
from .ipo.data_scientist import IPO_DataScientist
from .ipo.frontend_developer import IPO_FrontendDeveloper
from .ipo.backend_developer import IPO_BackendDeveloper
from .ipo.quantitative_analyst import IPO_QuantitativeAnalyst

from .historical.data_scientist import HistoricalDataScientist
from .historical.frontend_developer import HistoricalFrontendDeveloper
from .historical.backend_developer import HistoricalBackendDeveloper
from .historical.quantitative_analyst import HistoricalQuantitativeAnalyst


# # Importing sector analysis modules
# from select_sector.news_researcher import SectorNewsResearcher
# from select_sector.data_engineer import SectorDataEngineer
# from select_sector.data_scientist import SectorDataScientist
# from select_sector.frontend_developer import SectorFrontendDeveloper
# from select_sector.backend_developer import SectorBackendDeveloper
# from select_sector.quantitative_analyst import SectorQuantitativeAnalyst

# # Importing company analysis modules
# from select_company.news_researcher import CompanyNewsResearcher
# from select_company.data_engineer import CompanyDataEngineer
# from select_company.data_scientist import CompanyDataScientist
# from select_company.frontend_developer import CompanyFrontendDeveloper
# from select_company.backend_developer import CompanyBackendDeveloper
# from select_company.quantitative_analyst import CompanyQuantitativeAnalyst

# # Importing overall next-day analysis modules
# from overall_next_day.news_researcher import OverallNewsResearcher
# from overall_next_day.data_engineer import OverallDataEngineer
# from overall_next_day.data_scientist import OverallDataScientist
# from overall_next_day.frontend_developer import OverallFrontendDeveloper
# from overall_next_day.backend_developer import OverallBackendDeveloper
# from overall_next_day.quantitative_analyst import OverallQuantitativeAnalyst

# # Importing IPO analysis modules
# from ipo.news_researcher import IPO_NewsResearcher
# from ipo.data_engineer import IPO_DataEngineer
# from ipo.data_scientist import IPO_DataScientist
# from ipo.frontend_developer import IPO_FrontendDeveloper
# from ipo.backend_developer import IPO_BackendDeveloper
# from ipo.quantitative_analyst import IPO_QuantitativeAnalyst

# # Importing historical data analysis modules
# from historical.data_scientist import HistoricalDataScientist
# from historical.frontend_developer import HistoricalFrontendDeveloper
# from historical.backend_developer import HistoricalBackendDeveloper
# from historical.quantitative_analyst import HistoricalQuantitativeAnalyst

class StockAnalyzer:
    def __init__(self):
        self.sector_analysis_data = None
        self.company_analysis_data = None
        self.ipo_analysis_data = None
        self.historical_data = None

    def sector_analysis(self, sector):
        print(f"Starting sector analysis for: {sector}")
        
        # Step 1: News Researcher
        news_researcher = SectorNewsResearcher(sector)
        self.sector_analysis_data = news_researcher.collect_news_and_sentiment()
        
        # Step 2: Data Engineer
        data_engineer = SectorDataEngineer(self.sector_analysis_data)
        filtered_data = data_engineer.collect_historical_data()
        
        # Step 3: Data Scientist
        data_scientist = SectorDataScientist(filtered_data)
        predictions = data_scientist.predict_top_stocks()
        
        # Step 4: Frontend Developer
        frontend = SectorFrontendDeveloper(predictions)
        frontend.visualize_predictions()
        
        # Step 5: Backend Developer
        backend = SectorBackendDeveloper(predictions)
        backend.manage_alerts()
        
        # Step 6: Quantitative Analyst
        quantitative_analyst = SectorQuantitativeAnalyst(predictions)
        quantitative_analyst.perform_risk_analysis()
    
    # def company_analysis(self, company_name):
    #     print(f"Starting company analysis for: {company_name}")
        
    #     # Step 1: News Researcher
    #     news_researcher = CompanyNewsResearcher(company_name)
    #     self.news_researcher = CompanyNewsResearcher()
    #     self.company_analysis_data = news_researcher.collect_news_and_sentiment()
    #     self.company_analysis_data = self.news_researcher.collect_news_and_sentiment(company_name)

    def company_analysis(self, company_name):
        print(f"Starting company analysis for: {company_name}")
        # Collect news and sentiment
        self.company_analysis_data = self.news_researcher.collect_news_and_sentiment(company_name)
        # Continue with further analysis after collecting news and sentiment
        print(f"News and sentiment data: {self.company_analysis_data}")

        
        # Step 2: Data Engineer
        data_engineer = CompanyDataEngineer(self.company_analysis_data)
        historical_data = data_engineer.collect_historical_data()
        
        # Step 3: Data Scientist
        data_scientist = CompanyDataScientist(historical_data)
        predictions = data_scientist.predict_stock_movement()
        
        # Step 4: Frontend Developer
        frontend = CompanyFrontendDeveloper(predictions)
        frontend.visualize_predictions()
        
        # Step 5: Backend Developer
        backend = CompanyBackendDeveloper(predictions)
        backend.manage_alerts()
        
        # Step 6: Quantitative Analyst
        quantitative_analyst = CompanyQuantitativeAnalyst(predictions)
        quantitative_analyst.perform_risk_analysis()
    
    def overall_next_day_analysis(self):
        print("Starting overall next day analysis...")
        
        # Step 1: News Researcher
        news_researcher = OverallNewsResearcher()
        news_data = news_researcher.collect_top_news()
        
        # Step 2: Data Engineer
        data_engineer = OverallDataEngineer(news_data)
        top_companies = data_engineer.select_top_companies()
        
        # Step 3: Data Scientist
        data_scientist = OverallDataScientist(top_companies)
        predictions = data_scientist.predict_top_stocks()
        
        # Step 4: Frontend Developer
        frontend = OverallFrontendDeveloper(predictions)
        frontend.visualize_predictions()
        
        # Step 5: Backend Developer
        backend = OverallBackendDeveloper(predictions)
        backend.manage_alerts()
        
        # Step 6: Quantitative Analyst
        quantitative_analyst = OverallQuantitativeAnalyst(predictions)
        quantitative_analyst.perform_risk_analysis()
    
    def ipo_analysis(self):
        print("Starting IPO analysis...")
        
        # Step 1: News Researcher
        news_researcher = IPO_NewsResearcher()
        self.ipo_analysis_data = news_researcher.collect_news_and_sentiment()
        
        # Step 2: Data Engineer
        data_engineer = IPO_DataEngineer(self.ipo_analysis_data)
        ipo_data = data_engineer.collect_historical_data()
        
        # Step 3: Data Scientist
        data_scientist = IPO_DataScientist(ipo_data)
        predictions = data_scientist.predict_stock_movement()
        
        # Step 4: Frontend Developer
        frontend = IPO_FrontendDeveloper(predictions)
        frontend.visualize_predictions()
        
        # Step 5: Backend Developer
        backend = IPO_BackendDeveloper(predictions)
        backend.manage_alerts()
        
        # Step 6: Quantitative Analyst
        quantitative_analyst = IPO_QuantitativeAnalyst(predictions)
        quantitative_analyst.perform_risk_analysis()
    
    def historical_analysis(self, historical_data):
        print("Starting historical data analysis...")
        
        # Step 1: Data Scientist
        data_scientist = HistoricalDataScientist(historical_data)
        rated_stocks = data_scientist.feature_engineering()
        
        # Step 2: Frontend Developer
        frontend = HistoricalFrontendDeveloper(rated_stocks)
        frontend.visualize_stock_performance()
        
        # Step 3: Backend Developer
        backend = HistoricalBackendDeveloper(rated_stocks)
        backend.set_alerts()
        
        # Step 4: Quantitative Analyst
        analyst = HistoricalQuantitativeAnalyst(rated_stocks)
        analyst.conduct_risk_analysis()


if __name__ == "__main__":
    stock_analyzer = StockAnalyzer()
    
    # Example of usage:
    # stock_analyzer.sector_analysis("Technology")
    # stock_analyzer.company_analysis("Tata Steel")
    # stock_analyzer.overall_next_day_analysis()
    # stock_analyzer.ipo_analysis()
    
    # For historical analysis, you would need to load historical data
    # historical_data = pd.read_csv('historical_stock_data.csv')
    # stock_analyzer.historical_analysis(historical_data)
