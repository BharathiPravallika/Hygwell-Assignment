from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text: str) -> np.ndarray:
    return model.encode([text])[0]

def find_most_relevant_section(content: str, content_embedding: np.ndarray, question_embedding: np.ndarray) -> str:
    similarity = np.dot(content_embedding, question_embedding) / (np.linalg.norm(content_embedding) * np.linalg.norm(question_embedding))
    # Here lets assume a simple case where the entire content is returned if it's sufficiently similar.
    if similarity > 0.8:
        return content
    return "Sorry, I couldn't find a relevant section."
