from langchain_community.document_loaders import PyPDFLoader 
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

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
      docs = data_load.load(file_path)
      split_docs = splitter.split_documents(docs)
      return split_docs

    except Exception as e:
      print(f"Something went wrong: {e}")


class embeddings_db:
  def __init__(self):
    pass

  def ollama_embedding_db(self, text_documents, ollama_emb_ins):
    """
    This function creates embedding of documents using Ollama.
    """
    try:
      self.vectordb = Chroma.from_documents(text_documents, ollama_emb_ins):
      return self.vectordb
    except Exception as e:
      print(f"Something went wrong: {e}")


class retriever:
  def __init__(self, top_k:int):
    self.k = top_k

  def get_similar_docs(self, query:str):
    """
    This functions retrievs the top_k documents.
    """
    try:
      results = vectordb.similarity_search(query=query, k=self.k)
      return [r.page_content for r in results]
    except Exception as e:
      print(f"Something went wrong: {e}")
