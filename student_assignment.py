from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    loader = PyPDFLoader(file_path='OpenSourceLicenses.pdf')
    docs = loader.load()

    return docs[(len(docs)-1)]



def hw02_2(q2_pdf):
    pass
