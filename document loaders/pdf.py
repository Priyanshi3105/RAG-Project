from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import CharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
data = PyPDFLoader("document loaders/GRU.pdf")

docs = data.load()

# splitter = CharacterTextSplitter(
splitter = RecursiveCharacterTextSplitter(
    # separator= "",
    chunk_size = 1000,
    chunk_overlap=10
)

chunks  = splitter.split_documents(docs)

# print(docs[14])
# print(len(chunks))

print(chunks[0].page_content)


