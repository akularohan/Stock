from phi.agent import Agent
from phi.model.groq import Groq
from finance import CompanyFinance
from dotenv import load_dotenv
from phi.tools.csv_tools import CsvTools
from toolkit import CompanyFinanceToolkit

load_dotenv()

company_code = CsvTools("companies.csv")
agent  = Agent(
    model=Groq(id="llama3-70b-8192"),
    tools=[company_code],
    instructions=[" get the  nse code name  of the comapny","get the repective Company code of the company"],
    show_tool_calls=True,
    markdown=True
)
agent2 = Agent(
     model=Groq(id="llama3-70b-8192"),
    tools=[CompanyFinanceToolkit()],
    instructions=[" get the  nse code name  of the comapny","get the respective finanical details of that company"],
    show_tool_calls=True,
    markdown=True
)
agent2.print_response("Which company fundamentls are good , hdfc bank or icici bank, which one is good for long term", stream=True)