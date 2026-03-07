import os
from dotenv import load_dotenv

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

embedding_model = HuggingFaceEmbeddings(model_name="keepitreal/vietnamese-sbert")
vector_store = Chroma(persist_directory="./chroma_db", embedding_function=embedding_model)

llm = ChatOpenAI(
    model="google/gemma-3-27b-it:free",
    openai_api_base="https://openrouter.ai/api/v1",
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    temperature=0.3,
    max_tokens=2000)

template = '''Bạn là một trợ lý pháp lý chuyên nghiệp tư vấn Luật Dân sự Việt Nam.
Hãy trả lời câu hỏi của người dân một cách lịch sự, căn cứ vào dữ liệu pháp lý được cung cấp dưới đây. 
Nếu thông tin không có trong dữ liệu, hãy nói 'Xin lỗi, dữ liệu hiện tại không đề cập đến vấn đề này', đừng tự ý bịa đặt.
Dữ liệu gốc: {context},
Câu hỏi: {question},
Trả lời (ghi rõ căn cứ vào Điều mấy nếu có):'''

prompt_template = PromptTemplate.from_template(template)

qa_chain = prompt_template | llm | StrOutputParser()

while True:
    question = input("Nhập câu hỏi của bạn (hoặc 'exit' để thoát): ")
    if question.lower() == 'exit':
        break

    relevant_chunks = vector_store.similarity_search(question, k=5)
    context = "\n".join([chunk.page_content for chunk in relevant_chunks])

    answer = qa_chain.invoke({"context": context, "question": question})
    print("Trả lời:")
    print(answer)

