from llama_index.core import get_response_synthesizer,DocumentSummaryIndex
from llama_index.core import Settings,PromptHelper,Document
from  llama_index.core.node_parser import SentenceSplitter
from llm import embedding_model,inference_model,groq_llm
from prompt import get_prompt



def create_index_vars(balancesheet , cashflow , PnL , companyInfo , growth,pros,cons):
    llm = groq_llm
    
    Settings.chunk_size=128
    Settings.chunk_overlap=50
    Settings.num_output=2048
    Settings.embed_model=embedding_model

    prompt = PromptHelper(num_output=300)
    splitter = SentenceSplitter(chunk_size=128, chunk_overlap=50)
    response_synthesizer = get_response_synthesizer(response_mode="tree_summarize",use_async=True,
                                                    llm=llm)
    doc = Document(text=f"""CompanyInfo :{companyInfo} \nPast 4 years BalanceSheet : {balancesheet} \n Past 4 yearsCashFlow Statement : {cashflow} \nPast 4 years PnL statement : {PnL} \nGrowth Rates : {growth} \n Pros : {pros} \nCons : {cons} """)
    return doc,splitter,response_synthesizer,llm


def create_index(doc,splitter,response_synthesizer,llm):
    prompt = get_prompt()
    index = DocumentSummaryIndex.from_documents([doc],transformations=[splitter],
                                                summary_query=prompt,response_synthesizer=response_synthesizer,llm=llm)
    return index

def create_query_response(index,query):
    query_engine = index.as_query_engine(response_mode="tree_summarize",use_async=True)
    response = query_engine.query(query)
    return response

def get_summary(doc_summary_index ,doc):
    return doc_summary_index.get_document_summary(doc.doc_id)