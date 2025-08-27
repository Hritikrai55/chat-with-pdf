# 📄 Chat with PDF using Gemma 💁

A Streamlit-based application that allows users to interact with PDF documents through natural language queries using advanced AI models and vector embeddings.

## 🚀 Features

- **PDF Document Processing**: Automatically loads and processes all PDF files from a designated directory
- **Intelligent Text Splitting**: Uses RecursiveCharacterTextSplitter for optimal document chunking
- **Vector Embeddings**: Leverages Google Generative AI embeddings for semantic search
- **FAISS Vector Store**: Efficient similarity search and retrieval of relevant document chunks
- **AI-Powered Q&A**: Uses Groq's Gemma2-9b-it model for accurate question answering
- **Interactive Web Interface**: Clean and user-friendly Streamlit interface

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI Models**: 
  - Groq Gemma2-9b-it (LLM)
  - Google Generative AI Embeddings (models/embedding-001)
- **Vector Database**: FAISS
- **Document Processing**: PyPDF2, pypdf
- **Framework**: LangChain
- **Environment Management**: python-dotenv

## 📋 Prerequisites

- Python 3.7+
- Groq API Key
- Google API Key

## 🔧 Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd chat-with-pdf
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the root directory and add your API keys:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   GOOGLE_API_KEY=your_google_api_key_here
   ```

4. **Prepare PDF documents**:
   - Create a `pdf/` directory in the project root
   - Place your PDF files in the `pdf/` directory

## 🚀 Usage

1. **Start the application**:
   ```bash
   streamlit run app.py
   ```

2. **Access the web interface**:
   - Open your browser and navigate to `http://localhost:8501`

3. **Create Vector Store**:
   - Click the "Create Vector Store" button to process and embed your PDF documents
   - Wait for the success message confirming the vector store is ready

4. **Ask Questions**:
   - Enter your question in the text input field
   - The AI will search through your documents and provide contextual answers

## 📁 Project Structure

```
chat-with-pdf/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (not tracked)
├── .gitignore         # Git ignore rules
├── pdf/               # Directory for PDF documents
│   └── *.pdf         # Your PDF files
└── README.md          # This file
```

## 🔍 How It Works

1. **Document Loading**: The application loads all PDF files from the `pdf/` directory using PyPDFDirectoryLoader
2. **Text Splitting**: Documents are split into chunks of 1000 characters with 300 character overlap for better context retention
3. **Embedding Generation**: Each chunk is converted to vector embeddings using Google's Generative AI model
4. **Vector Storage**: Embeddings are stored in a FAISS vector database for efficient retrieval
5. **Query Processing**: User questions are embedded and matched against document chunks
6. **Answer Generation**: Relevant chunks are passed to the Gemma2-9b-it model to generate contextual answers

## 🔑 API Keys Setup

### Groq API Key
1. Visit [Groq Console](https://console.groq.com/)
2. Sign up/Login and create an API key
3. Add it to your `.env` file

### Google API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Add it to your `.env` file

## ⚙️ Configuration

- **Chunk Size**: 1000 characters (configurable in `app.py` line 48)
- **Chunk Overlap**: 300 characters (configurable in `app.py` line 48)
- **Model**: Gemma2-9b-it (configurable in `app.py` line 25)
- **Embedding Model**: models/embedding-001 (configurable in `app.py` line 41)

## 🤝 Dependencies

All required packages are listed in `requirements.txt`:
- `faiss-cpu` - Vector similarity search
- `groq` - Groq API client
- `langchain-groq` - LangChain Groq integration
- `PyPDF2` & `pypdf` - PDF processing
- `langchain_google_genai` - Google AI integration
- `langchain` - LangChain framework
- `streamlit` - Web interface
- `langchain_community` - Community integrations
- `python-dotenv` - Environment variable management

## 🚨 Important Notes

- Ensure your PDF files are in the `pdf/` directory before creating the vector store
- The `.env` file is ignored by git for security reasons
- Vector store creation may take time depending on the size and number of PDF documents
- The application uses session state to maintain vector store across interactions

## 🔒 Security

- API keys are stored in environment variables and not committed to version control
- The `.gitignore` file excludes the `.env` file from git tracking

## 🐛 Troubleshooting

- **"Please create the vector store first"**: Click the "Create Vector Store" button before asking questions
- **API Key errors**: Verify your API keys are correctly set in the `.env` file
- **No PDFs found**: Ensure PDF files are placed in the `pdf/` directory
- **Memory issues**: Consider reducing chunk size or processing fewer documents at once

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 👨‍💻 Author

**Hritik Rai**
- GitHub: [@Hritikrai55](https://github.com/Hritikrai55)
- LinkedIn: [Hritik Rai](https://www.linkedin.com/in/hritik-rai-)
- Email Address: hritikrai55@gmail.com

