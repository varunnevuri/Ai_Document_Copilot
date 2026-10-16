import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Document Chatbot", page_icon="🤖", layout="centered")

# --- Custom CSS ---
st.markdown("""
<style>
    /* Main background - light lavender */
    .stApp {
        background: linear-gradient(135deg, #f0f4ff, #e8eaff, #f5f0ff);
        color: #1e1b3a;
    }

    /* Title */
    h1 {
        text-align: center;
        color: #5b21b6;
        font-size: 2.5rem;
        margin-bottom: 0.2rem;
    }

    /* Headers */
    h2, h3 {
        color: #6d28d9;
    }

    /* Caption / subtext */
    .stMarkdown p, .stCaption {
        color: #4b5563;
    }

    /* Login card */
    .login-box {
        background: rgba(255,255,255,0.75);
        border: 1px solid rgba(109,40,217,0.25);
        border-radius: 16px;
        padding: 2rem;
        margin-top: 2rem;
        box-shadow: 0 4px 20px rgba(109,40,217,0.1);
    }

    /* Input fields */
    .stTextInput > div > div > input {
        background-color: #ffffff;
        color: #1e1b3a;
        border: 1.5px solid #7c3aed;
        border-radius: 8px;
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(90deg, #7c3aed, #a78bfa);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        font-weight: 600;
        transition: 0.2s;
        width: 100%;
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #6d28d9, #8b5cf6);
        transform: scale(1.02);
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #ede9fe, #ddd6fe);
        border-right: 1px solid rgba(109,40,217,0.2);
    }
    section[data-testid="stSidebar"] * {
        color: #3b0764 !important;
    }

    /* Chat messages - light bubbles */
    .stChatMessage {
        background: rgba(255, 255, 255, 0.85) !important;
        border-radius: 12px !important;
        border: 1px solid rgba(109,40,217,0.15) !important;
        margin-bottom: 0.5rem;
        box-shadow: 0 2px 8px rgba(109,40,217,0.08);
        color: #1e1b3a !important;
    }

    /* Make all text inside chat messages dark */
    .stChatMessage p, .stChatMessage div, .stChatMessage span {
        color: #1e1b3a !important;
    }

    /* Chat input */
    .stChatInputContainer textarea {
        background-color: #ffffff !important;
        color: #1e1b3a !important;
        border: 1.5px solid #7c3aed !important;
        border-radius: 8px !important;
    }

    /* Spinner */
    .stSpinner > div {
        border-top-color: #7c3aed !important;
    }
</style>
""", unsafe_allow_html=True)

# --- Session State ---
if "user_id" not in st.session_state:
    st.session_state.user_id = None
if "username" not in st.session_state:
    st.session_state.username = None
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- App ---
st.title("🤖 Document Chatbot")

if st.session_state.user_id is None:
    st.markdown("<br>", unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        st.subheader("👋 Welcome! Please login to continue")
        username = st.text_input("Enter your Username:", key="login_username")
        if st.button("Login / Signup", key="login_button"):
            if username:
                try:
                    res = requests.post(f"{API_URL}/get_or_create_user", json={"username": username})
                    res.raise_for_status()
                    data = res.json()
                    st.session_state.user_id = data["user_id"]
                    st.session_state.username = data["username"]

                    res_hist = requests.post(f"{API_URL}/get_history", json={"user_id": data["user_id"]})
                    st.session_state.messages = res_hist.json()["history"]
                    st.rerun()
                except Exception as e:
                    st.error(f"Error: {e}")
            else:
                st.warning("Please enter a username.")
        st.markdown('</div>', unsafe_allow_html=True)

else:
    st.sidebar.markdown(f"### 👤 {st.session_state.username}")
    st.sidebar.markdown("---")
    st.sidebar.markdown("📚 **Knowledge Base**")
    st.sidebar.markdown("- webscraping.txt")
    st.sidebar.markdown("- oops_java.pdf")
    st.sidebar.markdown("---")
    if st.sidebar.button("🚪 Logout", key="logout_button"):
        st.session_state.user_id = None
        st.session_state.username = None
        st.session_state.messages = []
        st.rerun()

    st.subheader("💬 Chat Interface")
    st.caption("Ask anything about your documents")

    for chat in st.session_state.messages:
        with st.chat_message(chat["role"]):
            st.markdown(chat["content"])

    if prompt := st.chat_input("Ask me anything ..."):
        st.session_state.messages.append({"role": "human", "content": prompt})
        with st.chat_message("human"):
            st.markdown(prompt)

        with st.chat_message("ai"):
            with st.spinner("Thinking ..."):
                try:
                    res = requests.post(f"{API_URL}/query", json={"user_id": st.session_state.user_id, "text": prompt})
                    res.raise_for_status()
                    answer = res.json()["answer"]
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "ai", "content": answer})
                except Exception as e:
                    st.error(f"Error: {e}")
