CONTEXT_WINDOW=1000
ANSWER_BUDGET=300

paragraph=(
    "Rag lets a model anser questions using your own",
    "documents instead of only what is memorized during training"
)

def estimate_tokens(text):
    #~4 characters per token
    return max(1,len(text)//4)

per_paragraph=estimate_tokens(paragraph)
prompt_budget=CONTEXT_WINDOW-ANSWER_BUDGET
max_paragraphs=prompt_budget//per_paragraph

print("Context window  :",CONTEXT_WINDOW,"tokens(prompt+answer)")
print("Reserve for answer :",ANSWER_BUDGET,"tokens")
print("Left for the prompt :",prompt_budget,"tokens")
print("Tokens per paragraph :",per_paragraph)
print()
