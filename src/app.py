import streamlit as st

from transcript import get_transcript
from chunking import  create_chunks
from embedding import create_embeddings
from vector_store import create_index
from youtube_utils import extract_video_id

# -----------------------------
# Streamlit Page Configuration
# -----------------------------
st.set_page_config(
    page_title="YouTube Video Analyzer",
    page_icon="🎥",
    layout="wide"
)

# -----------------------------
# Session State
# -----------------------------
if "video_loaded" not in st.session_state:
    st.session_state.video_loaded = False

if "chunks" not in st.session_state:
    st.session_state.chunks = None

if "index" not in st.session_state:
    st.session_state.index = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.title("🎥 Video Analyzer")

    st.markdown("---")

    st.info(
        """
        This application uses

        ✅ Transcript Extraction

        ✅ Semantic Chunking

        ✅ Sentence Transformer

        ✅ FAISS Vector Search

        ✅ Gemini LLM
        """
    )

# -----------------------------
# Main Title
# -----------------------------
st.title("🎥 YouTube Video Analyzer")

st.caption("Ask anything from any YouTube video using RAG.")

st.divider()

# -----------------------------
# URL Input
# -----------------------------
video_url = st.text_input(
    "Paste YouTube URL"
)

analyze_btn = st.button(
    "Analyze Video",
    use_container_width=True
)

# -----------------------------
# Analyze Video
# -----------------------------
if analyze_btn:

    if video_url.strip() == "":

        st.warning("Please enter a YouTube URL.")

        st.stop()

    progress = st.progress(0)

    status = st.empty()

    # -------------------------
    # Transcript
    # -------------------------
    status.info("📄 Fetching transcript...")

    video_id = extract_video_id(video_url)

    transcript = get_transcript(video_id)

    progress.progress(25)

    # -------------------------
    # Chunking
    # -------------------------
    status.info("✂️ Creating chunks...")

    

    chunks = create_chunks(transcript)

    progress.progress(50)

    # -------------------------
    # Embeddings
    # -------------------------
    status.info("🧠 Creating embeddings...")

    embeddings = create_embeddings(chunks)

    progress.progress(75)

    # -------------------------
    # FAISS
    # -------------------------
    status.info("⚡ Building Vector Index...")

    index = create_index(embeddings)

    progress.progress(100)

    status.success("✅ Video Ready!")

    st.session_state.video_loaded = True
    st.session_state.chunks = chunks
    st.session_state.index = index

    st.success("You can now ask questions.")

# -----------------------------
# Video Statistics
# -----------------------------
if st.session_state.video_loaded:

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Chunks",
            len(st.session_state.chunks)
        )

    with col2:

        st.metric(
            "Embedding Dimension",
            384
        )

    st.divider()
from embedding import create_query_embedding
from retriever import retrieve_chunks
from llm import generate_answer

# ----------------------------------------
# Chat Interface
# ----------------------------------------

if st.session_state.video_loaded:

    st.header("💬 Ask Questions About This Video")

    question = st.chat_input(
        "Ask anything about this video..."
    )

    if question:

        # User Message
        st.session_state.chat_history.append(
            ("user", question)
        )

        with st.spinner("Searching video..."):

            # -------------------------
            # Query Embedding
            # -------------------------
            query_embedding = create_query_embedding(
                question
            )

            # -------------------------
            # Retrieve Context
            # -------------------------
            context = retrieve_chunks(
                index=st.session_state.index,
                query_embedding=query_embedding,
                chunks=st.session_state.chunks,
                top_k=3
            )

            # -------------------------
            # Gemini Response
            # -------------------------
            answer = generate_answer(
                question,
                context
            )

        st.session_state.chat_history.append(
            ("assistant", answer)
        )

# ----------------------------------------
# Display Chat History
# ----------------------------------------

for role, message in st.session_state.chat_history:

    with st.chat_message(role):

        st.markdown(message)
# ----------------------------------------
# Sidebar Statistics
# ----------------------------------------

if st.session_state.video_loaded:

    st.sidebar.markdown("---")
    st.sidebar.subheader("📊 Video Statistics")

    st.sidebar.metric(
        "Chunks",
        len(st.session_state.chunks)
    )

    st.sidebar.metric(
        "Embedding Dimension",
        384
    )

    st.sidebar.success("FAISS Index Ready")

# ----------------------------------------
# Clear Chat
# ----------------------------------------

st.sidebar.markdown("---")

if st.sidebar.button(
    "🗑 Clear Chat",
    use_container_width=True
):

    st.session_state.chat_history = []

    st.rerun()

# ----------------------------------------
# Analyze Another Video
# ----------------------------------------

if st.sidebar.button(
    "🔄 Analyze Another Video",
    use_container_width=True
):

    st.session_state.video_loaded = False
    st.session_state.index = None
    st.session_state.chunks = None
    st.session_state.chat_history = []

    st.rerun()

# ----------------------------------------
# Footer
# ----------------------------------------

st.markdown("---")

st.markdown(
    """
<div style='text-align:center'>

### 🎥 YouTube Video Analyzer

Built using

✅ Streamlit

✅ Sentence Transformers

✅ FAISS

✅ Gemini API

Made by Sanskar 🚀

</div>
""",
unsafe_allow_html=True
)