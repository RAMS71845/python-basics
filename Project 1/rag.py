from config import SYSTEM_PROMPT
def build_context_block(matches:list)->str:
    if not matches:
        return("No documents retrieved")
    print(matches)
    print (matches[0])
    lines=[]
    for i,match in enumerate(matches,start=1):
        lines.append(
            f"[Source {i} | file:{match['source']}]"
            f"relevance: {match['similarity']:.2f}\n{match['document']}"
        )
    return "\n\n".join(lines)
def build_messages(question:str,matches:list,history:list)->list:
    context_block = build_context_block(matches)
    messages=[{"role":"system","content":SYSTEM_PROMPT}]
    messages.extend(history)
    
    messages.append({
        "role":"user",
        "content":(
            f"Context from user's docs: \n{context_block}\n\n"
            f"question:{question}"
        )
    })
    return messages