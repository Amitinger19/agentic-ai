from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_chroma import Chroma
from google.colab import userdata

GOOGLE_API_KEY = userdata.get('GOOGLE_API_KEY')
LANGCHAIN_API_KEY = userdata.get('LANGCHAIN_API_KEY')
LANGCHAIN_PROJECT = userdata.get('LANGCHAIN_PROJECT')
LANGCHAIN_TRACING_V2 = "true"

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.1,
    google_api_key=GOOGLE_API_KEY
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that answers questions strictly from the context given to you.\n*******CONTEXT*******\n{context}"
        ),
        ("human", "{input}"),
    ]
)

query = "Expertise of Amit?"
results = vectordb.similarity_search(query=query, k=5)
context = "\n".join([r.page_content for r in results])
output = StrOutputParser()

chain = prompt | llm | output


response = chain.invoke(
    {
        "context": context,
        "input": query
    }
)

print(response)