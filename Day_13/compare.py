from sentence_transformers import SentenceTransformer,util
DOCS=[
    "A car is a four wheeled vechile for the road",
    "An automobile takes you from place to place",
    "The chef cooked a delicious pasta dinner",
    "Photosynthesis lets plants make food from light."
  
]
QUERY="How does a motor vechile work?"
def main():
    model=SentenceTransformer("all-MiniLM-L6-v2")
    query_vec=model.encode(QUERY)
    docs_vec=model.encode(DOCS)
    scores=util.cos_sim(query_vec,docs_vec)[0]
    print(scores)

if __name__ == "__main__":
    main()