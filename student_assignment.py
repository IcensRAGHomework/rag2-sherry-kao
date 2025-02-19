from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    loader = PyPDFLoader(q1_pdf)
    docs = loader.load()

    return docs[(len(docs)-1)]



def hw02_2(q2_pdf):
    loader = PyPDFLoader(q2_pdf)
    pdf_text = loader.load()
    
    pdf_text_combined = " ".join([doc.page_content for doc in pdf_text])
    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=10,  # 每個 chunk 的最大字符數
    chunk_overlap=0,  # 每個 chunk 之間的重疊字符數
    separators=[r"第\s+.*\s+章\s+", r"第\s+.*\s+條\s+",],
    is_separator_regex=True
    )
    chapter_chunks = text_splitter.split_text(pdf_text_combined)
    
    return len(chapter_chunks)
