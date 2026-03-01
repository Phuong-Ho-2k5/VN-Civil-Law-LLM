from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate

# Load the Chroma vector store
embedding_model = HuggingFaceEmbeddings(model_name="keepitreal/vietnamese-sbert")
vector_store = Chroma(persist_directory="./chroma_db", embedding_function=embedding_model)

# Define a prompt template for question answering
template = '''Bạn là một trợ lý pháp lý chuyên nghiệp. Hãy sử dụng thông tin dưới đây để giải đáp thắc mắc.
Nếu thông tin không có trong dữ liệu, hãy nói rằng bạn không chắc chắn, đừng tự ý bịa đặt.
Dữ liệu gốc: {context},
Câu hỏi: {question},
Trả lời:'''

prompt_template = PromptTemplate.from_template(template)

while True:
    question = input("Nhập câu hỏi của bạn (hoặc 'exit' để thoát): ")
    if question.lower() == 'exit':
        break

    # Retrieve relevant chunks from the vector store
    relevant_chunks = vector_store.similarity_search(question, k=5)

    # Combine the retrieved chunks into a single context
    context = "\n".join([chunk.page_content for chunk in relevant_chunks])

    # Format the prompt with the context and question
    prompt = prompt_template.format(context=context, question=question)
    print("Prompt đã tạo:")
    print(prompt)

    # Here you would typically pass the prompt to a language model for generating an answer
    