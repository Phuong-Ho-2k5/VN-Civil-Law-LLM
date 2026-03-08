from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

pdf_path = "data/raw/91_2015_QH13_296215.pdf"

loader = PyPDFLoader(pdf_path)
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_documents(documents)

embedding_model = HuggingFaceEmbeddings(model_name="keepitreal/vietnamese-sbert")

vector_store = Chroma.from_documents(
    documents=chunks, 
    embedding=embedding_model,
    persist_directory="./chroma_db")
