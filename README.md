# 📚 RAG-Based Question Answering System
 
A Retrieval-Augmented Generation (RAG) application that enables users to query documents using natural language. The system retrieves relevant information from a vector database and generates context-aware responses using a Large Language Model (LLM).
 
## 🚀 Features
 
- Upload and process text documents
- Automatic text chunking
- Vector embeddings generation
- Semantic search using ChromaDB
- Retrieval-Augmented Generation (RAG)
- Interactive Streamlit user interface
- Local LLM inference using Ollama
- Fast and context-aware responses
 
## 🛠️ Tech Stack
 
- **Python**
- **LangChain**
- **Ollama**
- **ChromaDB**
- **HuggingFace Embeddings**
- **Streamlit**
 
## 📂 Project Structure
 
```text
RAG-Project/
│
├── app.py # Streamlit application
├── main.py # Core RAG pipeline
├── requirements.txt # Project dependencies
├── .gitignore
├── README.md
│
├── data/ # Source documents
└── chroma_db/ # Vector database
```
 
## ⚙️ Installation
 
### 1. Clone the Repository
 
```bash
git clone https://github.com/your-username/RAG-Project.git
cd RAG-Project
```
 
### 2. Create a Virtual Environment
 
```bash
python -m venv .venv
```
 
### 3. Activate the Environment
 
```bash
.venv\Scripts\activate
```
 
### 4. Install Dependencies
 
```bash
pip install -r requirements.txt
```
 
## 🤖 Setup Ollama
 
Pull the Llama model:
 
```bash
ollama pull llama3.2
```
 
Verify installation:
 
```bash
ollama list
```
 
## ▶️ Run the Application
 
```bash
streamlit run app.py
```
 
Open your browser and navigate to:
 
```text
http://localhost:8501
```
 
## 🔄 How It Works
 
1. Documents are loaded and preprocessed.
2. Text is split into smaller chunks.
3. Embeddings are generated for each chunk.
4. Chunks are stored in ChromaDB.
5. User queries are converted into embeddings.
6. Relevant chunks are retrieved from the vector database.
7. The LLM generates a response using the retrieved context.
 
## 🎯 Use Cases
 
- Knowledge Base Chatbots
- Document Question Answering
- Research Assistance
- Internal Company Documentation Search
- Educational Content Exploration
 
## 📈 Future Enhancements
 
- PDF and DOCX support
- Multi-document querying
- Conversation memory
- Source citation display
- Hybrid search (keyword + semantic)
- Deployment on cloud platforms
 
## 👩‍💻 Author
 
**Priyanshi Gupta**