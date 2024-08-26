import os
from dotenv import load_dotenv
from langchain_astradb import AstraDBVectorStore
from langchain_openai import OpenAIEmbeddings

load_dotenv()

astra_bd_api_endpoint = os.getenv("ASTRA_DB_API_ENDPOINT")
astra_db_token = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
app_name = os.getenv("ASTRA_DB_KEYSPACE")

def create_vector_store(namespace):
    embe = OpenAIEmbeddings()
    vstore = AstraDBVectorStore(
        embedding=embe,
        collection_name="astra_vector_demo",
        api_endpoint=astra_bd_api_endpoint,
        token=astra_db_token,
        namespace=namespace,
    )
    return vstore

vectorstore = create_vector_store("marquise")
