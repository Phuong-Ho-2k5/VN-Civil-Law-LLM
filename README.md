# ⚖️ VN-Civil-Law-LLM: Vietnamese Legal AI Assistant

Hệ thống hỏi đáp pháp lý thông minh chuyên biệt cho **Bộ luật Dân sự Việt Nam 2015** dựa trên kiến trúc **Retrieval-Augmented Generation (RAG)**.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/LangChain-Framework-green?logo=chainlink" alt="LangChain">
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi" alt="FastAPI">
  <img src="https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?logo=streamlit" alt="Streamlit">
  <img src="https://img.shields.io/badge/VectorDB-Chroma-orange" alt="VectorDB">
  <img src="https://img.shields.io/badge/LLM-OpenRouter-purple" alt="LLM">
</p>

---

## 🚀 Giới thiệu

**VN-Civil-Law-LLM** là một dự án nghiên cứu ứng dụng AI trong lĩnh vực **Legal-Tech**. Hệ thống giúp người dùng tra cứu các quy định pháp luật dân sự một cách tự nhiên, chính xác và có căn cứ dẫn chiếu trực tiếp từ văn bản luật gốc.

### Quy trình cốt lõi:
1.  **Ingestion:** Chuyển đổi văn bản luật (PDF) thành các đoạn văn bản nhỏ (Chunks).
2.  **Retrieval:** Sử dụng **Vietnamese SBERT** để tìm kiếm ngữ nghĩa, trích xuất các điều luật liên quan nhất từ **ChromaDB**.
3.  **Augmentation:** Kết hợp câu hỏi của người dùng với ngữ cảnh pháp lý và lịch sử trò chuyện.
4.  **Generation:** LLM (thông qua **OpenRouter**) sinh câu trả lời chuyên nghiệp, ghi rõ căn cứ vào Điều mấy của Bộ luật.

---

## 🧠 Kiến trúc hệ thống

Dự án được thiết kế theo mô hình **Decoupled Architecture** (Tách biệt hoàn toàn Backend và Frontend):



* **AI Engine (LangChain):** Điều phối luồng dữ liệu giữa Vector Database và LLM.
* **Backend (FastAPI):** Cung cấp RESTful API hiệu năng cao, quản lý logic xử lý và session người dùng.
* **Frontend (Streamlit):** Giao diện Chatbot thân thiện, hỗ trợ quản lý ID người dùng và hiển thị lịch sử hội thoại.
* **Storage:** Sử dụng **ChromaDB** cho dữ liệu vector và **JSON** cho việc lưu trữ lịch sử chat bền vững.

---

## ✨ Tính năng nổi bật

* ✅ **Semantic Search:** Hiểu ý nghĩa câu hỏi ngay cả khi người dùng không dùng chính xác thuật ngữ chuyên môn.
* ✅ **Multi-turn Conversation:** Duy trì ngữ cảnh cuộc trò chuyện thông qua hệ thống lưu trữ lịch sử theo `user_id`.
* ✅ **Fact-Grounded:** Giảm thiểu tối đa hiện tượng "ảo giác" của AI bằng cách buộc mô hình chỉ trả lời dựa trên dữ liệu luật cung cấp.
* ✅ **Professional UI:** Giao diện thanh bên (Sidebar) cho phép cá nhân hóa người dùng và quản lý phiên làm việc.

---

## 📂 Cấu trúc dự án

```text
VN-Civil-Law-LLM/
├── app/
│   ├── main.py              # Backend API (FastAPI)
│   └── streamlit_ui.py      # Frontend Chatbot Interface (Streamlit)
├── scripts/
│   ├── ingest.py            # Quy trình xử lý dữ liệu PDF -> Vector DB
│   └── legal_bot.py         # Logic RAG và cấu hình LangChain
├── data/
│   ├── raw/                 # Chứa file PDF Luật Dân sự gốc
│   └── history/             # Lưu trữ lịch sử trò chuyện (.json)
├── chroma_db/               # Cơ sở dữ liệu Vector đã lưu trữ
├── .env                     # Lưu trữ API Key (Không upload lên GitHub)
└── requirements.txt         # Danh sách các thư viện cần thiết
```

## ⚙️ Cài đặt & Sử dụng

1.  **Chuẩn bị môi trường**
```bash
    git clone https://github.com/Phuong-Ho-2k5/VN-Civil-Law-LLM.git
    cd VN-Civil-Law-LLM
    python -m venv venv
    ./venv/Scripts/activate  # Windows
    pip install -r requirements.txt
```

2. **Cấu hình API Key**

   Tạo file `.env` tại thư mục gốc và dán key của bạn vào:
```text
   OPENROUTER_API_KEY=your_openrouter_key_here
```

3. **Khởi chạy hệ thống (Cần mở 2 Terminal)**

   - **Khởi tạo dữ liệu** (Chỉ chạy lần đầu):
```bash
     python scripts/ingest.py
```

   - **Terminal 1 - Chạy Backend API:**
```bash
     python -m app.main
```

   - **Terminal 2 - Chạy Frontend UI:**
```bash
     streamlit run app/streamlit_ui.py
```

## 📊 Đánh giá & Kiểm thử

Hệ thống được kiểm thử qua bộ Benchmark gồm 50+ câu hỏi thuộc các nhóm:

- **Tra cứu trực tiếp**: Định nghĩa, thời hiệu, phân loại tài sản.
- **Phân tích tình huống**: Thừa kế, hợp đồng vô hiệu, năng lực hành vi.
- **Lọc ngoài phạm vi**: Từ chối các câu hỏi không thuộc phạm vi Luật Dân sự (ví dụ: Luật Hình sự).

---

### ⚠️ Lưu ý

Dự án này được xây dựng cho mục đích nghiên cứu và tham khảo công nghệ. Các câu trả lời của AI **không có giá trị thay thế** cho tư vấn pháp lý từ các chuyên gia hoặc luật sư có chuyên môn.

---

### 👨‍💻 Tác giả

Phát triển bởi **Phuong (Phuong-Ho-2k5)**.

Dự án thể hiện kỹ năng về AI Engineering, Backend Development và RAG Optimization.