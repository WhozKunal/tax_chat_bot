from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.lancedb import LanceDb, SearchType
from dotenv import load_dotenv
from agno.embedder.huggingface import HuggingfaceCustomEmbedder
from agno.embedder.ollama import OllamaEmbedder



load_dotenv()
print(load_dotenv())

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),

    description="You are an expert in Indian taxation.",
    instructions=[
        "Use your knowledge base to answer Indian taxation questions like income tax, GST, deductions, forms.",
        "Use DuckDuckGo to supplement if you cannot answer from documents.",
        "Give priority to the knowledge base over tool-based info."
    ],
    # knowledge=PDFUrlKnowledgeBase(
        
        
        
    #     urls=[
    #         "https://example.com/Indian_Taxation_FAQ.pdf"
    #     ],
        
        
        
    #     vector_db=LanceDb(
    #         uri="tmp/lancedb",
    #         table_name="tax_faq",
    #         search_type=SearchType.hybrid,
    #         embedder=OllamaEmbedder()
    #     ),
    # ),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True
)

# Ensure knowledge base is loaded
if agent.knowledge is not None:
    agent.knowledge.load()
    
    
def run_agent(query: str) -> str:
    response = agent.run(query)
    
    # This handles cases where the response is wrapped in a RunResponse object
    if hasattr(response, "content"):
        return response.content
    elif hasattr(response, "text"):
        return response.text
    else:
        return str(response)



