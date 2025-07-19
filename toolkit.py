import requests
from bs4 import BeautifulSoup
import config
from utils import parse_financial_data ,parse_cashflow_data
from phi.tools import Toolkit
from phi.utils.log import logger

class CompanyFinanceToolkit(Toolkit):
    """Class for fetching company details of past 4 years , by using company's nse code.

    """
    def __init__(self, company=None):
        """Initializes the class with the nse code of the company
        Args:
         company (str): nse code of the company, 

        """
        super().__init__(name="company_financials")
        self.company = company
        url = f"https://www.screener.in/company/{company}/consolidated/"
        self.company_info = config.company_info_class
        self.finance_class = config.finance_class
        self.pros = config.pros
        self.cons = config.cons
        self.growth_class = config.growth_class
        self.register(self.getBalanceSheet)
        self.register(self.getPnl)
        self.register(self.getCashFlow)
        self.register(self.getCompanyInfo)
        self.register(self.getGrowth)
        self.register(self.getPros)
        self.register(self.getCons)
    


        try:
            response = requests.get(url)
            if response.status_code != 200:
                raise Exception(f"Failed to fetch the details for {company}.")
        except:
            raise Exception(f"Failed to fetch the details for {company}.")
        logger.info(f"Successfully fetched the details for {company}.")
        self.soup = BeautifulSoup(response.text, "html.parser")
        
    
    def getBalanceSheet(self):
        """Returns the balance sheet of the company of past 4 years
        Call the function directly from object without any input parameters
        Args:
            None
        Returns:
            str: balance sheet statement of  the company of previous four years, The  order is from most recent to oldest. The first one is the latest one (This year) and the last one is the oldest
        """
        
        info =self.soup.find_all(class_= self.finance_class)
        if info:
        # Extract all text, including nested elements
            text = info[2].get_text(separator='\n', strip=True)
            parsed_data = parse_financial_data(text)
            quarter = False
            final_response =""
            for field, values in parsed_data.items():
                if field.startswith("Sep"):
                    quarter = True
                if isinstance(values, list):
                    if quarter:
                        values=values[:len(values)-1]
                    if len(values) > 4:
                        values =values[-4:]
                    values.reverse()
                    values = " ".join(values)
                if not(field.startswith("Sep") or field.startswith("Mar")):
                    final_response += f"{field} in Rs Crores: {values}\n"
        else:
            return ""
        return final_response
    
    def getPnl(self):
        """Returns the profit and loss statement of the company of past 4 years
        Call the function directly from object without any input parameters
        Args:
            None
        Returns:
            str: Pnl statement of  the company of previous four years, The  order is from most recent to oldest. The first one is the latest one (This year) and the last one is the oldest.
        """
        info =self.soup.find_all(class_= self.finance_class)
        final_response =""
        quarter = False
        if info:
            text = info[1].get_text(separator='\n', strip=True)
            parsed_data = parse_financial_data(text)
            # # Print the results
            for field, values in parsed_data.items():
                if field.startswith("Sep"):
                    quarter = True
                if isinstance(values, list):
                    if quarter:
                        values=values[:len(values)-1]
                    if len(values) > 4:
                        values =values[-4:]
                    values.reverse()
                    values = " ".join(values)
                if not(field.startswith(("Sep","Mar") )):
                    if not (field.endswith(("%","Rs") )):
                        final_response += f"{field} in Rs Crores: {values}\n"
                    else:
                        final_response += f"{field}: {values}\n"
        
        else:
            return ""
        return final_response
    
    def getCashFlow(self):
        """Returns the cash flow statement of the company of past 4 years. 
         Call the function directly from object without any input parameters
        Args:
            None
        Returns:
            str: cash flow statement of previous four years, The  order is from most recent to oldest. The first one is the latest one (This year) and the last one is the oldest.
        """
        info = self.soup.find_all(class_= self.finance_class)
        # print(info)
        if info:
        # Extract all text, including nested elements
            text = info[3].get_text(separator='\n', strip=True)
            print("text",text)
            parsed_data = parse_cashflow_data(text)
            print("parsed_data",parsed_data)
            quarter = False
            final_response =""
            # # Print the results
            for field, values in parsed_data.items():
                if field.startswith("Sep"):
                    quarter = True
                if isinstance(values, list):
                    if quarter:
                        values=values[:len(values)-1]
                    
                    if(len(values) > 4):
                        values =values[-4:]
                    values.reverse()
                    values = " ".join(values)
                
                final_response += f"{field} in Rs Crores: {values}\n"
            
        else:
            return ""
        return final_response
    
    def getCompanyInfo(self):
        """Returns the  basic information of the company 
        Call the function directly from object without any input parameters
        Args:
            None
        Returns:
            str: basic information of the company
        """
        info =self.soup.find_all(class_= self.company_info)
        if info:
            text = info[0].get_text(separator='\n', strip=True)
        else:
            return ""
        
        text = text.replace('₹', '').replace('\n', ' ')
        text = text.replace('Add ratio to table Edit ratios', '')
        return text
    
    def getGrowth(self):
        """Returns the growth of certain parameters of the company 
        Call the function directly from object without any input parameters
        Args:
            None
        Returns:
            str: growth for certain parameters of the company
        """
        info =self.soup.find_all(class_= self.growth_class)
        final_response =""
        for i in[0,1,3]:
            if  info and info[i]:
                text = info[i].get_text(separator='\n', strip=True)
                text = text.replace("\n"," ")
                text = text.replace("%","%.")
            else :
                text =""
            final_response += f"{text}\n"
        return final_response
    
    def getPros(self):
        """Returns the pros of the company 
        Call the function directly from object without any input parameters
        Args:
            None
        Returns:
            str: pros of the company
        """
        info =self.soup.find_all(class_= self.pros)
        text = info[0].get_text(separator='\n', strip=True)
        text = text.replace("\n",".")
        text = text.replace("Pros","")
        return text
    def getCons(self):
        """Returns the cons of the company 
        Call the function directly from object without any input parameters
        Args:
            None
        Returns:
            str: cons of the company"""
        info =self.soup.find_all(class_= self.cons)
        text = info[0].get_text(separator='\n', strip=True)
        text = text.replace("\n",".")
        text = text.replace("Cons","")
        return text