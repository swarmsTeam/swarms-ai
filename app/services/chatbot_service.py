import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import JSONLoader
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Set up the environment for the API key
load_dotenv()
if "GOOGLE_API_KEY" not in os.environ:
    raise EnvironmentError("GOOGLE_API_KEY environment variable not found!")

# Load the pre-trained model for the chatbot
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# Load event data
loader = JSONLoader(file_path="data/events.json", jq_schema='.[] | {event_name, date, location, description}', text_content=False)
documents = loader.load()

# Set up the vector store with embeddings
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vector_store = FAISS.from_documents(documents, embeddings)
retriever = vector_store.as_retriever()

# System message to guide the chatbot
system_message = (
    "You are the EVNTO chatbot, and your role is to assist users with event information. "
    "EVNTO is an app that helps Mansoura University students and others find events and connect with volunteer teams. "
    "You can answer questions about events happening in the university and other locations."
)

# Chain setup for the chatbot to perform question answering
qa_chain = RetrievalQA.from_chain_type(llm=model, retriever=retriever)

def process_chatbot_query(query: str) -> str:
    """
    Processes the query for the chatbot.
    """
    full_query = f"{system_message} {query}"
    result = qa_chain.invoke(full_query)
    return result['result']