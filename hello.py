import requests
from bs4 import BeautifulSoup

company = "INFY"

url = f"https://www.screener.in/company/{company}/consolidated/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


def parse_financial_data(text) -> dict:
    # Split the text into lines
    lines = text.strip().split('\n')
    
    data = {}
    current_field = None
    
    for line in lines:
        # Check if this line is a field name
        if not re.match(r'^[\d,.+%]+$', line.strip()): # change this condition to (if re.match(r'^[A-Za-z\s]+$', line)) forcashflowe
            current_field = line.strip()
            data[current_field] = []
        else:
            # This line contains a value
            value = line.strip().rstrip('%')  # Remove % sign if present
            value = value.replace(',', '')  # Remove commas
            
            # Convert to float if possible, otherwise keep as string
            # try:
            #     value = float(value)
            # except ValueError:
            #     pass
            
            if current_field:
                data[current_field].append(value)
    
    return data
def parse_cashflow_data(text) -> dict:
    # Split the text into lines
    lines = text.strip().split('\n')
    
    data = {}
    current_field = None
    
    for line in lines:
        # Check if this line is a field name
        if  re.match(r'^[A-Za-z\s]+$', line): 
            current_field = line.strip()
            data[current_field] = []
        else:
            # This line contains a value
            value = line.strip().rstrip('%')  # Remove % sign if present
            value = value.replace(',', '')  # Remove commas
            
            # Convert to float if possible, otherwise keep as string
            # try:
            #     value = float(value)
            # except ValueError:
            #     pass
            
            if current_field:
                data[current_field].append(value)
    
    return data
class1 ="company-ratios"
class2="data-table responsive-text-nowrap"
class3 ="responsive-holder fill-card-width" # info[1]
balancesheet ="data-table responsive-text-nowrap" # info[2]
cashflow="data-table responsive-text-nowrap" # info[3]
pros="pros"
huggingfacetoken="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"
llamahf="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"

info =soup.find_all(class_=pros)
import re
if info:
    # Extract all text, including nested elements
    text = info[0].get_text(separator='\n', strip=True)
    
    # Replace multiple spaces with a single space
    # text = re.sub(r'\s+', ' ', text)
    

    
    
else:
    print("Couldn't find the specified class.")


def get_company_info(soup):
    company_info_class ="company-ratios"
    info =soup.find_all(class_=company_info_class)
    if info:
    # Extract all text, including nested elements
        text = info[0].get_text(separator='\n', strip=True)
    
    else:
        print("Couldn't find the specified class.")


    text = text.replace('₹', '').replace('\n', ' ')
    text = text.replace('Add ratio to table Edit ratios', '')
    return text

def getPnl(soup):
    Pnl_class ="data-table responsive-text-nowrap"
    info =soup.find_all(class_= Pnl_class)
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
        print("Couldn't find the specified class.")
    return final_response
        

def getBalanceSheet(soup):
    BalanceSheet_class ="data-table responsive-text-nowrap"
    info =soup.find_all(class_= BalanceSheet_class)
    if info:
    # Extract all text, including nested elements
        text = info[2].get_text(separator='\n', strip=True)
        parsed_data = parse_financial_data(text)
        quarter = False
        final_response =""
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
            if not(field.startswith("Sep") or field.startswith("Mar")):
                final_response += f"{field} in Rs Crores: {values}\n"
    else:
        print("Couldn't find the specified class.")
    return final_response




def getCashFlow(soup):
    CashFlow_class ="data-table responsive-text-nowrap"
    info =soup.find_all(class_= CashFlow_class)
    if info:
    # Extract all text, including nested elements
        text = info[3].get_text(separator='\n', strip=True)
        parsed_data = parse_cashflow_data(text)
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
        print("Couldn't find the specified class.")
    return final_response

class1="cons"
info =soup.find_all(class_= class1)
text = info[0].get_text(separator='\n', strip=True)
text = text.replace("\n",".")
text = text.replace("Pros","")

print(text)






# get_company_info(soup)
# getPnl(soup)
# getCashFlow(soup)
# getBalanceSheet(soup)

