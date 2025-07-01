from langchain_community.document_loaders import PyPDFLoader 
from langchain_text_splitters import RecursiveCharacterTextSplitter

FILE_PATH = "/content/drive/MyDrive/Colab/langchain/Data/cv.pdf"

class data_loader:
  def __init__(self):
    pass

  def load_data(self, file_path:str):
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
      docs = data_load.load_data(file_path)
      split_docs = splitter.split_documents(docs)
      return split_docs

    except Exception as e:
      print(f"Something went wrong: {e}")

class create_embeddings:
  def __init__(self):
    pass

  def get_embedding_model(self):
    pass

  def get_embeddings(self, text:str):
    """
    This function create embeddings for the given text
    """
    pass

class database_operations:
  def __init__(self):
    pass

  def load_db(self,config=None):
    """
    Load the database client.
    """
    pass

  def read_data(self):
    """
    Loads the data.
    """
    pass

  def load_data_into_db(self):
    """
    Upload the data into DB.
    """
    pass

  def delete(self):
    """
    Deletes data.
    """
    pass








