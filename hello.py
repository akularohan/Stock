import requests
from bs4 import BeautifulSoup
import re
import os  

company = "INFY"
url = f"https://www.screener.in/company/{company}/consolidated/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


def parse_financial_data(text) -> dict:
    lines = text.strip().split('\n')
    data = {}
    current_field = None

    for line in lines:
        if not re.match(r'^[\d,.+%]+$', line.strip()):
            current_field = line.strip()
            data[current_field] = []
        else:
            value = line.strip().rstrip('%').replace(',', '')
            if current_field:
                data[current_field].append(value)
    return data


def parse_cashflow_data(text) -> dict:
    lines = text.strip().split('\n')
    data = {}
    current_field = None

    for line in lines:
        if re.match(r'^[A-Za-z\s]+$', line):
            current_field = line.strip()
            data[current_field] = []
        else:
            value = line.strip().rstrip('%').replace(',', '')
            if current_field:
                data[current_field].append(value)
    return data


def get_company_info(soup):
    company_info_class = "company-ratios"
    info = soup.find_all(class_=company_info_class)
    if info:
        text = info[0].get_text(separator='\n', strip=True)
    else:
        print("Couldn't find the specified class.")
        return ""

    text = text.replace('₹', '').replace('\n', ' ')
    text = text.replace('Add ratio to table Edit ratios', '')
    return text


def getPnl(soup):
    Pnl_class = "data-table responsive-text-nowrap"
    info = soup.find_all(class_=Pnl_class)
    final_response = ""
    quarter = False
    if info:
        text = info[1].get_text(separator='\n', strip=True)
        parsed_data = parse_financial_data(text)

        for field, values in parsed_data.items():
            if field.startswith("Sep"):
                quarter = True
            if isinstance(values, list):
                if quarter:
                    values = values[:len(values)-1]
                if len(values) > 4:
                    values = values[-4:]
                values.reverse()
                values = " ".join(values)
            if not (field.startswith(("Sep", "Mar"))):
                if not field.endswith(("%", "Rs")):
                    final_response += f"{field} in Rs Crores: {values}\n"
                else:
                    final_response += f"{field}: {values}\n"
    else:
        print("Couldn't find the specified class.")
    return final_response


def getBalanceSheet(soup):
    BalanceSheet_class = "data-table responsive-text-nowrap"
    info = soup.find_all(class_=BalanceSheet_class)
    final_response = ""
    if info:
        text = info[2].get_text(separator='\n', strip=True)
        parsed_data = parse_financial_data(text)
        quarter = False

        for field, values in parsed_data.items():
            if field.startswith("Sep"):
                quarter = True
            if isinstance(values, list):
                if quarter:
                    values = values[:len(values)-1]
                if len(values) > 4:
                    values = values[-4:]
                values.reverse()
                values = " ".join(values)
            if not (field.startswith("Sep") or field.startswith("Mar")):
                final_response += f"{field} in Rs Crores: {values}\n"
    else:
        print("Couldn't find the specified class.")
    return final_response


def getCashFlow(soup):
    CashFlow_class = "data-table responsive-text-nowrap"
    info = soup.find_all(class_=CashFlow_class)
    final_response = ""
    if info:
        text = info[3].get_text(separator='\n', strip=True)
        parsed_data = parse_cashflow_data(text)
        quarter = False

        for field, values in parsed_data.items():
            if field.startswith("Sep"):
                quarter = True
            if isinstance(values, list):
                if quarter:
                    values = values[:len(values)-1]
                if len(values) > 4:
                    values = values[-4:]
                values.reverse()
                values = " ".join(values)
            final_response += f"{field} in Rs Crores: {values}\n"
    else:
        print("Couldn't find the specified class.")
    return final_response



class1 = "cons"
info = soup.find_all(class_=class1)
if info:
    text = info[0].get_text(separator='\n', strip=True)
    text = text.replace("\n", ".").replace("Pros", "")
    print(text)
else:
    print("Couldn't find the specified class.")


