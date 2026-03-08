import chromadb
from sentence_transformers import SentenceTransformer

class KnowledgeBase:

    def __init__(self):

        self.client = chromadb.Client()
        self.collection = self.client.create_collection("police_incidents")

        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")

    def add_documents(self, docs):

        embeddings = self.embedder.encode(docs).tolist()

        ids = [str(i) for i in range(len(docs))]

        self.collection.add(
            documents=docs,
            embeddings=embeddings,
            ids=ids
        )

    def retrieve(self, query):

        query_embedding = self.embedder.encode([query]).tolist()

        results = self.collection.query(
            query_embeddings=query_embedding,
            n_results=3
        )

        return results["documents"][0]