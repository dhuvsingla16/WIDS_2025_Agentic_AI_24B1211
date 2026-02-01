from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.Client(
    chromadb.config.Settings(persist_directory="data/vector_db")
)

collection = client.get_collection("department_data")

def retrieve_context(query, k=3):
    query_embedding = model.encode([query])

    results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=k
    )

    return results["documents"][0]
