# ⚖️ VN-Civil-Law-LLM

### 🇻🇳 Hệ thống AI tư vấn **Luật Dân sự Việt Nam** sử dụng RAG

<p align="center">
Hệ thống hỏi đáp pháp lý sử dụng <b>Retrieval-Augmented Generation (RAG)</b>, <b>Vector Database</b> và <b>Large Language Models</b> để hỗ trợ tra cứu Luật Dân sự Việt Nam.
</p>

---

# 📌 Badges

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![VectorDB](https://img.shields.io/badge/VectorDB-Chroma-orange)
![LLM](https://img.shields.io/badge/LLM-OpenRouter-purple)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

</p>

---

# 🚀 Giới thiệu

**VN-Civil-Law-LLM** là hệ thống **AI hỗ trợ tư vấn pháp lý cho Luật Dân sự Việt Nam**.

Hệ thống cho phép người dùng đặt câu hỏi về luật, sau đó:

1️⃣ Truy xuất thông tin liên quan từ văn bản luật

2️⃣ Cung cấp ngữ cảnh cho mô hình ngôn ngữ lớn (LLM)

3️⃣ Sinh câu trả lời có **căn cứ pháp lý**

Công nghệ chính được sử dụng:

* **Retrieval-Augmented Generation (RAG)**
* **Vector Search**
* **Large Language Model (LLM)**

---

# 🧠 Kiến trúc hệ thống

```id="f1x4ph"
                ┌─────────────────────┐
                │  Văn bản Luật (PDF) │
                └──────────┬──────────┘
                           │
                           ▼
                 ┌─────────────────┐
                 │ Document Loader │
                 └────────┬────────┘
                          │
                          ▼
                ┌─────────────────────┐
                │ Text Splitter       │
                │ (Chunking)          │
                └──────────┬──────────┘
                           │
                           ▼
               ┌─────────────────────────┐
               │ Embedding Model         │
               │ Vietnamese SBERT        │
               └──────────┬──────────────┘
                          │
                          ▼
               ┌─────────────────────────┐
               │ Vector Database         │
               │ ChromaDB                │
               └──────────┬──────────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Retriever       │
                 └────────┬────────┘
                          │
                          ▼
                ┌─────────────────────┐
                │ LLM (OpenRouter)    │
                │ GPT-OSS             │
                └──────────┬──────────┘
                           │
                           ▼
                 ⚖️ Câu trả lời pháp lý
```

---

# 📂 Cấu trúc dự án

```id="wra41u"
VN-Civil-Law-LLM
│
├── chroma_db/              # Vector database lưu embeddings
│   ├── chroma.sqlite3
│   └── <collection_id>
│
├── data/
│   ├── raw/                # Dữ liệu gốc (PDF luật)
│   │   └── 91_2015_QH13_296215.pdf
│   │
│   └── processed/          # Dữ liệu sau xử lý (tuỳ chọn)
│
├── scripts/
│   ├── ingest.py           # Tạo embeddings và lưu vào ChromaDB
│   └── legal_bot.py        # Chatbot hỏi đáp luật
│
├── .env                    # API key
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ✨ Tính năng

✅ Hỏi đáp **Luật Dân sự Việt Nam**

✅ Truy xuất văn bản luật bằng **vector search**

✅ Sinh câu trả lời bằng **LLM**

✅ Embedding tiếng Việt bằng **Vietnamese SBERT**

✅ Chatbot chạy trực tiếp trên **CLI**

---

# ⚙️ Cài đặt

Clone repository:

```bash id="a69a1k"
git clone https://github.com/your-username/VN-Civil-Law-LLM.git
cd VN-Civil-Law-LLM
```

Cài đặt thư viện:

```bash id="mrm8gb"
pip install -r requirements.txt
```

---

# 🔑 Cấu hình API Key

Tạo file `.env`

```id="3r5rsv"
OPENROUTER_API_KEY=your_api_key_here
```

Lấy API key tại:

https://openrouter.ai

---

# 📚 Chuẩn bị dữ liệu pháp lý

Đặt file **PDF luật** vào thư mục:

```id="qxt8n9"
data/raw/
```

Ví dụ:

```id="vnb6t5"
data/raw/91_2015_QH13_296215.pdf
```

---

# 🧩 Tạo Vector Database

Chạy script ingest:

```bash id="yn2qhe"
python scripts/ingest.py
```

Script sẽ:

* Load PDF luật
* Chia văn bản thành các đoạn nhỏ
* Tạo embeddings
* Lưu vào **ChromaDB**

---

# 💬 Chạy chatbot tư vấn luật

Chạy chương trình:

```bash id="r5g68d"
python scripts/legal_bot.py
```

Ví dụ:

```id="ddkr55"
Nhập câu hỏi của bạn:
Quyền sở hữu tài sản là gì?
```

Kết quả:

```id="fg0k73"
Theo Điều ... của Bộ luật Dân sự 2015,
quyền sở hữu bao gồm quyền chiếm hữu,
quyền sử dụng và quyền định đoạt tài sản.
```

---

# 🔮 Hướng phát triển

Một số cải tiến trong tương lai:

* 🌐 Web UI (Streamlit / Gradio)
* 🔎 Hybrid search (BM25 + Vector)
* 📚 Hỗ trợ nhiều bộ luật
* 📄 Trích dẫn chính xác Điều / Khoản
* 🇻🇳 Fine-tune Legal LLM cho tiếng Việt

---

# ⚠️ Lưu ý

Dự án chỉ mang tính **nghiên cứu và tham khảo**.
Kết quả từ hệ thống **không thay thế tư vấn pháp lý chuyên nghiệp**.

---

# 👨‍💻 Tác giả

Dự án nghiên cứu về:

**Legal AI + Retrieval-Augmented Generation cho hệ thống pháp luật Việt Nam**

