import streamlit as st
import newspaper
import nltk
from PIL import Image

# Download necessary nltk datasets
nltk.download('punkt')

# Set page configuration with custom title and favicon
st.set_page_config(page_title="Keyword Extractor & Article Scraper", page_icon="📰", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    /* Main header style */
    .main-header {
        font-family: 'Helvetica', sans-serif;
        color: #FF6F61;
        font-weight: bold;
        text-align: center;
        font-size: 3em;
    }
    
    /* Subheader and general text style */
    .subheader {
        font-family: 'Arial', sans-serif;
        color: #333;
        text-align: left;
    }
    
    /* Keywords section styling */
    .keyword-box {
        background-color: #f0f8ff;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #ddd;
        font-size: 1.2em;
        color: #4B8BFF;
        margin-top: 10px;
    }

    /* Author styling */
    .author-box {
        background-color: #ffe4e1;
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #f0a0a0;
        font-size: 1.1em;
        color: #D84315;
    }

    /* Tabs text alignment */
    .tab-text {
        font-family: 'Verdana', sans-serif;
        text-align: justify;
        color: #2E8B57;
        line-height: 1.6;
    }

    /* Full Text and Summary Tab styling */
    .full-text, .summary {
        background-color: #FAFAFA;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    }

    /* Footer styling */
    .footer {
        text-align: center;
        font-size: 1em;
        font-family: 'sans-serif', monospace;
        color: #grey;
        margin-top: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# Main title
st.markdown("<h1 class='main-header'>📰 Keyword Extractor & Article Scraper</h1>", unsafe_allow_html=True)

# Input section
st.markdown("### 🌐 Paste an article URL below to extract keywords and a summary:")

# User input for URL
url = st.text_input('', placeholder='Enter article URL and hit Enter!', help="The app will scrape content from the article.")

if url:
    # Layout with columns for better organization
    col1, col2 = st.columns([4, 2])

    # Scrape the article
    article = newspaper.Article(url)
    article.download()
    article.parse()
    article.nlp()

    # Display Authors
    authors = article.authors
    with col1:
        st.markdown("### ✍️ **Author(s):**")
        if authors:
            st.markdown(f"<div class='author-box'>{', '.join(authors)}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<p style='color: #FF4B4B;'>No authors found.</p>", unsafe_allow_html=True)

    # Display Keywords
    st.markdown("")
    with col1:
        st.subheader("🔑 **Extracted Keywords:**")
        key = article.keywords
        if key:
            st.markdown(f"<div class='keyword-box'>{', '.join(key)}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<p style='color: #FF4B4B;'>No keywords extracted.</p>", unsafe_allow_html=True)

    # Create Tabs for Full Text and Summary
    st.markdown("---")
    tab1, tab2 = st.tabs(["📃 Full Text", "📜 Summary"])

    with tab1:
        st.markdown("### 📃 **Full Text:**")
        st.markdown(f"<div class='full-text tab-text'>{article.text}</div>", unsafe_allow_html=True)

    with tab2:
        st.markdown("### 📜 **Summary:**")
        st.markdown(f"<div class='summary tab-text'>{article.summary}</div>", unsafe_allow_html=True)

    # Footer Section
    st.markdown("<div class='footer'>🔗 App Developed by Farrukh Noor Khan</div>", unsafe_allow_html=True)

