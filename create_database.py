# load pdf
# split chunks
# create the embeddings
#store into croma
#  
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
# from dotenv import load_dotenv
# load_dotenv()

data = PyPDFLoader("document loaders/deeplearning.pdf")

docs = data.load()

splitter = RecursiveCharacterTextSplitter(
    # separator= "",
    chunk_size = 2000,
    chunk_overlap=100
)

chunks  = splitter.split_documents(docs)

# embedding_model = GoogleGenerativeAIEmbeddings(model ="gemini-embedding-2-preview")
embedding_model = HuggingFaceEmbeddings(
model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma.from_documents(
    documents = chunks,
    embedding= embedding_model,
    persist_directory= "chroma-db"
)