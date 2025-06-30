from langchain_community.document_loaders import PyPDFLoader 
from langchain_text_splitters import RecursiveCharacterTextSplitter

FILE_PATH = "/content/drive/MyDrive/Colab/langchain/Data/cv.pdf"

class data_loader:
  def __init__(self):
    pass

  def load_data(self, file_path:str): -> str:
    """
    This function loads the text from the pdf file.
    """
    try:
      loader = PyPDFLoader(file_path)
      data = loader.load()
      return data
    except Exception as e:
      print(f"Something went wrong: {e}")

class data_splitter:
  def __init__(self):
    pass

  def split_documents(self, documents:langchain.documents, file_path:str):
    """
    This function splits the documents into chunks.
    """
    data_load = data_loader()
    try:
      splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=10)
      docs = data_load.load(file_path)
      split_docs = splitter.split_documents(docs)
      return split_docs

    except Exception as e:
      print(f"Something went wrong: {e}")
      














