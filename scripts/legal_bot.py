import os
import json
from dotenv import load_dotenv

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.messages import message_to_dict, messages_from_dict

HISTORY_DIR = "./data/history"

load_dotenv()

embedding_model = HuggingFaceEmbeddings(model_name="keepitreal/vietnamese-sbert")
vector_store = Chroma(persist_directory="./chroma_db", embedding_function=embedding_model)

llm = ChatOpenAI(
    model="openai/gpt-oss-120b:free",
    base_url="https://openrouter.ai/api/v1",
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    temperature=0.3,
    max_tokens=2000,
    default_headers={
        "HTTP-Referer": "http://localhost:3000",
        "X-Title": "VN-Civil-Law-LLM",
    })

def get_history_by_id(history_id):
    history_path = os.path.join(HISTORY_DIR, f"{history_id}.json")
    history = ChatMessageHistory()
    
    if os.path.exists(history_path):
        with open(history_path, "r", encoding="utf-8") as f:
            try:
                history_data = json.load(f)
                messages = messages_from_dict(history_data)
                history.add_messages(messages)
            except Exception as e:
                print(f"Lỗi khi load lịch sử: {e}")
                
    return history

def save_history(history_id, history):
    file_path = os.path.join(HISTORY_DIR, f"{history_id}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump([message_to_dict(m) for m in history.messages], f, ensure_ascii=False, indent=4)

template = '''Bạn là một trợ lý pháp lý chuyên nghiệp tư vấn Luật Dân sự Việt Nam.
Hãy trả lời câu hỏi của người dân một cách lịch sự, căn cứ vào dữ liệu pháp lý được cung cấp dưới đây. 
Nếu thông tin không có trong dữ liệu, hãy nói 'Xin lỗi, dữ liệu hiện tại không đề cập đến vấn đề này', đừng tự ý bịa đặt.
Lịch sử trò chuyện: {history}
Dữ liệu gốc: {context},
Câu hỏi: {question},
Trả lời (ghi rõ căn cứ vào Điều mấy nếu có):'''

prompt_template = PromptTemplate.from_template(template)

qa_chain = prompt_template | llm | StrOutputParser()

current_session = input("Nhập ID người dùng (ví dụ: user_01): ") or "default_user"

def get_answer(user_id, question):
    if question.lower() == "exit":
        return "Kết thúc trò chuyện."
    
    if not os.path.exists(HISTORY_DIR):
        os.makedirs(HISTORY_DIR)
        
    history = get_history_by_id(user_id)
    relevant_chunks = vector_store.similarity_search(question, k=5)
    context = "\n".join([chunk.page_content for chunk in relevant_chunks])

    answer = qa_chain.invoke({
        "context": context, 
        "question": question, 
        "history": [msg.content for msg in history.messages] 
    })

    history.add_user_message(question)
    history.add_ai_message(answer)
    save_history(user_id, history)
    
    return answer

