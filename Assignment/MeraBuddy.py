import json
import os
from urllib.parse import quote_plus
import streamlit as st
from dotenv import load_dotenv
from groq import Groq
from pypdf import PdfReader

load_dotenv()

st.set_page_config(page_title="Resume Analyzer", page_icon="👍🤞")
@st.cache_resource
def get_groq_client():
    if not os.getenv("GROQ_API_KEY"):
        return None
    return Groq()

client=get_groq_client()

st.title("RESUME ANALYZER AND JOB FINDER (●'◡'●)")

st.sidebar.header("Settings")
model = st.sidebar.selectbox(
    "Model",
    ["llama-3.1-8b-instant", "llama-3.3-70b-versatile"],
)
if st.sidebar.button("Start over"):
    st.session_state.clear()
 
if client is None:
    st.error(
        "No GROQ_API_KEY found. Create a .env file with GROQ_API_KEY=your_key_here, "
        "then restart the app."
    )
    st.stop()

def extract_text_from_pdf(uploaded_file)->str:
    """Read every page of the uploaded PDF and join their text together"""
    reader=PdfReader(uploaded_file)
    pages_text=[]
    for page in reader.pages:
        pages_text.append(page.extract_text() or "")
    return "\n".join(pages_text)

uploaded_file=st.file_uploader("Upload your RESUME (PDF only)", type=["pdf"])

ANALYSIS_SYSTEM_PROMPT="""You are a strict but fair resume reviewer.
Read the resume text the user gives you and respond with ONLY a JSON object, no markdown fences,no extra commentary,in exactly this shape:

{  
  "score": <integer 0-100>,
  "strengths":["...","..."],
   "weaknesses": ["...", "..."],
  "suggestions": ["...", "..."],
  "suggested_job_titles": ["...", "..."]
  }
 Keep each list to 3-5 short,specific items.Suggested_job_titles should be realistic job titles this resume is  good fit for right now."""

def analyze_resume(resume_text:str) ->dict:
    response=client.chat.completions.create(
        model=model,
        messages=[
            {"role":"system","content":ANALYSIS_SYSTEM_PROMPT},
            {"role":"user","content":resume_text},

        ],
        temperature=0.2,
    )
    raw_reply=response.choices[0].message.content
    cleaned = (
    raw_reply.strip()
    .removeprefix("```json")
    .removeprefix("```")
    .removesuffix("```")
    .strip()
)
    return json.loads(cleaned)


def build_job_links(job_title: str) -> dict:
    query = quote_plus(job_title)
    return {
        "LinkedIn": f"https://www.linkedin.com/jobs/search/?keywords={query}",
        "Naukri": f"https://www.naukri.com/{quote_plus(job_title.replace(' ', '-'))}-jobs",
        "Indeed": f"https://www.indeed.com/jobs?q={query}",
    }
if uploaded_file is not None:
    
    if st.session_state.get("analyzed_filename") != uploaded_file.name:
        with st.spinner("Reading and analyzing your resume..."):
            resume_text = extract_text_from_pdf(uploaded_file)
            analysis = analyze_resume(resume_text)
 
        st.session_state.analyzed_filename = uploaded_file.name
        st.session_state.resume_text = resume_text
        st.session_state.analysis = analysis
        st.session_state.messages = []  
 
    analysis = st.session_state.analysis

    st.subheader("Your Score")
    st.metric("Resume Score", f"{analysis['score']} / 100")
 
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Strengths**")
        for item in analysis["strengths"]:
            st.markdown(f"- {item}")
    with col2:
        st.markdown("**Weaknesses**")
        for item in analysis["weaknesses"]:
            st.markdown(f"- {item}")
 
    st.markdown("**Suggestions to improve**")
    for item in analysis["suggestions"]:
        st.markdown(f"- {item}")

    st.subheader("Matching Job Titles")
    for title in analysis["suggested_job_titles"]:
        links = build_job_links(title)
        link_line = " | ".join(f"[{portal}]({url})" for portal, url in links.items())
        st.markdown(f"**{title}** — {link_line}")
 
    st.divider()
    st.subheader("Ask follow-up questions")
 
    if "messages" not in st.session_state:
        st.session_state.messages = []
 
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
 
    user_text = st.chat_input("e.g. How do I improve my skills section?")
 
    if user_text:
        st.session_state.messages.append({"role": "user", "content": user_text})
        with st.chat_message("user"):
            st.write(user_text)
 
        with st.chat_message("assistant"):
           
            grounded_system_prompt = (
                "You are a helpful resume coach. Answer the user's questions "
                "about the resume below, using the earlier analysis as context.\n\n"
                f"Resume text:\n{st.session_state.resume_text}\n\n"
                f"Earlier analysis:\n{json.dumps(st.session_state.analysis)}"
            )
            messages_to_send = [{"role": "system", "content": grounded_system_prompt}]
            messages_to_send.extend(st.session_state.messages)
 
            stream = client.chat.completions.create(
                model=model,
                messages=messages_to_send,
                temperature=0.4,
                stream=True,
            )
 
            def token_generator():
                for chunk in stream:
                    piece = chunk.choices[0].delta.content
                    if piece:
                        yield piece
 
            reply = st.write_stream(token_generator())
 
        st.session_state.messages.append({"role": "assistant", "content": reply})
else:
    st.info("Upload a PDF resume above to get started.")
 