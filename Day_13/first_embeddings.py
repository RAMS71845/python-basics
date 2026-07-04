#pip install sentence-transformers numpy
from sentence_transformers import SentenceTransformer
def main():
    model=SentenceTransformer("all-MiniLM-L6-v2")
    sentence="I LOVE AI"
    vector=model.encode(sentence)
    print(vector)

    sentences=[
        "The cat sat on the mat",
        "A feline rested on the ruf",
        "Interest rates rose this quarter"
    ]
    vectors=model.encode(sentences)
    print(vectors)
if __name__=="__main__":
    main()