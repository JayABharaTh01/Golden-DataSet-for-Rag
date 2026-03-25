# from config import CHUNK_SIZE, CHUNK_OVERLAP

# def chunk_text(text):
#     words = text.split()
#     chunks = []

#     for i in range(0, len(words), CHUNK_SIZE - CHUNK_OVERLAP):
#         chunk = " ".join(words[i:i + CHUNK_SIZE])
#         chunks.append(chunk)

#     return chunks

def chunk_text(text, size=300, overlap=50):
    words = text.split()
    chunks = []

    for i in range(0, len(words), size - overlap):
        chunk = " ".join(words[i:i+size])
        chunks.append(chunk)

    return chunks