import vertexai
from langchain.llms import VertexAI
from langchain.embeddings import VertexAIEmbeddings

from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.vectorstores import DocArrayInMemorySearch

def GCP_Embedding(input_text,query):
    vertexai.init(project="personalized-learning-340207", location="us-central1")

    llm = VertexAI(
        model_name="text-bison@001",
        max_output_tokens=256,
        temperature=0.1,
        top_p=0.8,
        top_k=40,
        verbose=True,)

    embeddings = VertexAIEmbeddings()
    print("--indexing---")
    loader = TextLoader(input_text, encoding='utf-8')

    index = VectorstoreIndexCreator(vectorstore_cls=DocArrayInMemorySearch,
              embedding=embeddings).from_loaders([loader])
    response = index.query(query,llm=llm)
    return response