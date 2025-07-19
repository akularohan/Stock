from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from inference import llm_summary
from nse_data import company_list, get_company_code
from datetime import datetime
import re

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def format_financial_text(text):
    # Clean markdown symbols
    text = re.sub(r'[_*]+', '', text)
    text = re.sub(r'(\d)\.\s+(\d)', r'\1.\2', text)
    text = re.sub(r'\s*\n\s*', ' ', text)

    # Format known section headers
    headers = [
        "Financial Trends Summary",
        "Overall Financial Health",
        "Investment Recommendations",
        "Additional Insights"
    ]
    for header in headers:
        text = re.sub(fr'\s*{header}:?', f'\n\n__**{header.upper()}:**__\n', text)

    # Remove a), b), c)
    text = re.sub(r'\s*[a-c]\)\s+', ' ', text)

    # Newline before risk indicators
    text = re.sub(r'(?<!\n)(\b(?:Low|Medium|High) Risk:)', r'\n\1', text)

    # Sentence breaks
    text = re.sub(r'(?<!\d)\.(?=\s+[A-Z])', r'.\n', text)

    lines = [line.strip() for line in text.split('\n') if line.strip()]
    return '\n'.join(lines)

@app.get("/api/stocks")
async def get_stocks():
    return {"stocks": company_list}

@app.get("/get_inference/")
def get_inference(company: str):
    company_code = get_company_code(company)
    if company_code is None:
        return {"error": "Company not found"}

    try:
        summary = llm_summary(company_code)
        summary = re.sub(r'\*+', '', summary)
        formatted_summary = format_financial_text(summary)

        print("\n====== MODEL INFERENCE ======")
        for line in formatted_summary.split('\n'):
            print(line)
        print("====== END ======\n")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return {
            "MODEL RESPONSE": formatted_summary,
            "timestamp": timestamp
        }

    except Exception as e:
        return JSONResponse(status_code=200, content={"error": str(e)})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
