import streamlit as st
import requests

st.set_page_config(page_title="VN Civil Law Chatbot", page_icon="⚖️")

with st.sidebar:
    st.title("Settings")
    user_id = st.text_input("Nhập User ID của bạn:", value="default_user")
    st.info("Hệ thống sẽ dựa vào ID này để lưu lại lịch sử trò chuyện của bạn.")
    
    if st.button("Xóa lịch sử chat hiện tại"):
        st.session_state.messages = []
        st.rerun()

st.title("⚖️ VN-Civil-Law AI Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Hỏi tôi về Luật Dân sự..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Đang tra cứu luật..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/chat",
                    json={
                        "user_id": user_id,
                        "question": prompt
                    }
                )
                if response.status_code == 200:
                    answer = response.json()["answer"]
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                else:
                    st.error(f"Lỗi từ Backend: {response.text}")
            except Exception as e:
                st.error(f"Không thể kết nối đến Server: {e}")