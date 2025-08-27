# Importing necessary libraries
import os
import asyncio
import streamlit as st
from dotenv import load_dotenv

# LangChain imports
from langchain_groq import ChatGroq
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Load environment variables from .env
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# ------------------- Custom CSS -------------------
st.markdown(
    """
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .stChatMessage {
        border-radius: 18px;
        padding: 12px;
        margin: 8px 0;
        font-size: 16px;
        line-height: 1.5;
    }
    .user-msg {
        background-color: #DCF8C6;
        color: black;
        text-align: right;
    }
    .bot-msg {
        background-color: #ffffff;
        color: #333333;
        border: 1px solid #e6e6e6;
    }
    .stButton>button {
        border-radius: 12px;
        background: linear-gradient(90deg, #6a11cb 0%, #2575fc 100%);
        color: white;
        padding: 0.6em 1.2em;
        border: none;
        font-weight: 600;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #2575fc 0%, #6a11cb 100%);
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit App Title
st.markdown("<h1 style='text-align: center;'>📄 Chat with PDF using Gemma 💁</h1>", unsafe_allow_html=True)
st.write("Ask questions from your PDF documents in a conversational way!")

# Initialize the LLM
llm = ChatGroq(groq_api_key=groq_api_key, model_name="gemma2-9b-it")

# Prompt template
prompt = ChatPromptTemplate.from_template("""
Answer the question based only on the provided context.
<context>
{context}
</context>

Question: {input}
""")

# Function to create vector DB
def vector_embedding():
    if "embeddings" not in st.session_state:
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        except RuntimeError:
            loop = asyncio.get_event_loop()
        st.session_state.embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001", 
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )

    if "vectors" not in st.session_state:
        st.session_state.loader = PyPDFDirectoryLoader("./pdf")
        st.session_state.docs = st.session_state.loader.load()
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=300)
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs)
        st.session_state.vector_store = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)
        st.session_state.vectors = True  

# Button to create the vector store
if st.button("📂 Create Vector Store"):
    vector_embedding()
    st.success("✅ Vector store DB is ready!")

# ------------------- Chat Section -------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    role = "user" if msg["role"] == "user" else "assistant"
    css_class = "user-msg" if role == "user" else "bot-msg"
    st.markdown(f"<div class='stChatMessage {css_class}'>{msg['content']}</div>", unsafe_allow_html=True)

# User input box (chat style)
if prompt1 := st.chat_input("Type your question here..."):
    # Save user message
    st.session_state.messages.append({"role": "user", "content": prompt1})
    
    if "vector_store" in st.session_state:
        document_chain = create_stuff_documents_chain(llm=llm, prompt=prompt)
        retriever = st.session_state.vector_store.as_retriever()
        retrieval_chain = create_retrieval_chain(retriever, document_chain)

        with st.spinner("🤔 Thinking..."):
            response = retrieval_chain.invoke({"input": prompt1})
            answer = response["answer"]

        # Save bot response
        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.rerun()
    else:
        st.warning("⚠️ Please create the vector store first.")

