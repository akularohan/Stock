from ai_utils import create_index_vars,create_index,get_summary
from finance import CompanyFinance








def llm_summary(company_code):
    try:
        Company = CompanyFinance(company_code)
        balancesheet = Company.getBalanceSheet()
        cashflow = Company.getCashFlow()
        companyInfo = Company.getCompanyInfo()
        growth = Company.getGrowth()
        Pnl = Company.getPnl()
        pros = Company.getPros()
        cons = Company.getCons()
        print(cashflow)
    except Exception as e:
        raise ValueError(f"Error in getting company details:{str(e)}")
    try:
        doc,splitter,response_synthesizer,llm = create_index_vars(balancesheet , cashflow , Pnl , companyInfo , growth,pros,cons)

        vector_index = create_index(doc,splitter,response_synthesizer,llm)

        summary = get_summary(vector_index,doc)
        return summary
    except Exception as e:
        raise ValueError("Error in llm inference. Please try after sometime")
    
# print(llm_summary("500209"))


