# from dotenv import load_dotenv
# from langchain.chat_models import init_chat_model
# # from langchain_community.document_loaders import TextLoader
# from langchain_community.document_loaders import PyPDFLoader
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_community.document_loaders import RecursiveCharacterTextSplitter

# load_dotenv()

# # data = TextLoader("document loaders/notes.txt")
# # data = PyPDFLoader("document loaders/GRU.pdf")
# data = PyPDFLoader("document loaders/deeplearning.pdf")

# docs = data.load()

# splitter = RecursiveCharacterTextSplitter(
#     # separator= "",
#     chunk_size = 1000,
#     chunk_overlap=200
# )

# chunks  = splitter.split_documents(docs)

# template=ChatPromptTemplate.from_messages(
#     [("system","you are a AI that summarizes the text"),
#     #  ("human",docs[0].page_content)]
#      ("human",docs[0].page_content)]

# )

# model=init_chat_model("google_genai:gemini-2.5-flash-lite")

# # promt = template.format_messages(data= docs[0].page_content)

# promt = template.format_messages(data= docs)


# result=model.invoke(promt)

# print(result.content)

from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

embedding_model = HuggingFaceEmbeddings(
model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma(
persist_directory="chroma-db",
embedding_function=embedding_model
)

retriever = vectorstore.as_retriever(
    search_type = "mmr",
    search_kwargs = {
        "k" : 4,
        "fetch_k":10,
        "lambda_mult" :0.5
    }
)

llm = ChatOllama(
model="llama3.2"
)



#prompt template 
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a helpful AI assistant.

Use ONLY the provided context to answer the question.

If the answer is not present in the context,
say: "I could not find the answer in the document."
"""
        ),
        (
            "human",
            """Context:
{context}

Question:
{question}
"""
        )
    ]
)

print("Rag system created ")

print("press 0 to exit ")

while True:
    query = input("You : ")
    if query == "0":
        break 
    
    docs = retriever.invoke(query)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )
    
    final_prompt = prompt.invoke({
        "context" :context,
        "question": query
    })
    
    response = llm.invoke(final_prompt)

    print(f"\n AI: {response.content}")
    