from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.vectordb.lancedb import LanceDb, SearchType
from agno.embedder.ollama import OllamaEmbedder
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Optional: Print a message confirming environment is loaded



# Define the agent
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),

    description="You are an expert Indian tax advisor for individuals and businesses.",
    
    instructions=[
        "Only answer questions related to Indian taxation, including income tax, GST, deductions, forms, and filing procedures.",
        "If the question is not tax-related, politely say you can only help with Indian tax queries.",
        "Use your own reasoning and knowledge **first** to respond.",
        "If needed, consult the PDF-based knowledge base to provide more detail or clarification.",
        "If the answer is still unclear, use DuckDuckGo to search for updates or additional info.",
        "Start your response with a short greeting like 'Hello!' or 'Hi there!' **only** if the query is general or not specific.",
        "Respond in a helpful, friendly tone — like a qualified tax consultant."
    ],

    knowledge=PDFKnowledgeBase(
        path=r"C:\upsala\tex_chat\Text.pdf",
        vector_db=LanceDb(
            uri="tmp/lancedb",
            table_name="tax_faq",
            search_type=SearchType.hybrid,
            embedder=OllamaEmbedder()
        ),
    ),
    
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True
)

    
    

TAX_KEYWORDS = [
    "tax", "gst", "income tax", "itr", "deduction", "form", "refund", 
    "audit", "tds", "filing", "assessment", "advance tax", "80c", "80d", "home loan", "gstr"
]

def run_agent(query: str) -> str:
    query_lower = query.lower()

    if not any(keyword in query_lower for keyword in TAX_KEYWORDS):
        return "I'm designed to help only with Indian taxation-related queries. Please ask me something about tax."

    response = agent.run(query)

    if hasattr(response, "content"):
        return response.content
    elif hasattr(response, "text"):
        return response.text
    else:
        return str(response)


