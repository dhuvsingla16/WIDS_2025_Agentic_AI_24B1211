from sentence_transformers import SentenceTransformer
import chromadb
import os

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_vector_store(chunks):
    os.makedirs("data/vector_db", exist_ok=True)

    client = chromadb.Client(
        chromadb.config.Settings(persist_directory="data/vector_db")
    )

    collection = client.get_or_create_collection("department_data")

    embeddings = model.encode(chunks)

    collection.add(
        documents=chunks,
        embeddings=embeddings.tolist(),
        ids=[str(i) for i in range(len(chunks))]
    )

    client.persist()
