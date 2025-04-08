import streamlit as st
from newspaper import Article
import re
from transformers import pipeline

# Initialize the  pipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

import requests
from bs4 import BeautifulSoup


def fetch_article(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")

        # For BBC articles
        paragraphs = soup.find_all("p")
        article_text = " ".join(p.get_text() for p in paragraphs)

        return article_text
    except Exception as e:
        st.error(f"Error fetching article from URL: {e}")
        return None


model_name = "sshleifer/distilbart-cnn-12-6"
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")


# CSS 
st.markdown("""
    <style>
    .title span {
        display: inline-block;
        opacity: 0;
        color: #2e86de; 
        animation: fadeIn 1s ease-in forwards;
        animation-delay: 0s;
    }
    .title .space {
        margin-right: 10px; 
    }


    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateX(-10px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }

    
    .title span:nth-child(1) { animation-delay: 0s; }
    .title span:nth-child(2) { animation-delay: 0.1s; }
    .title span:nth-child(3) { animation-delay: 0.2s; }
    .title span:nth-child(4) { animation-delay: 0.3s; }
    .title .space:nth-child(5) { animation-delay: 0.4s; }
    .title span:nth-child(6) { animation-delay: 0.5s; }
    .title span:nth-child(7) { animation-delay: 0.6s; }
    .title span:nth-child(8) { animation-delay: 0.7s; }
    .title .space:nth-child(9) { animation-delay: 0.8s; }
    .title span:nth-child(10) { animation-delay: 0.9s; }
    .title span:nth-child(11) { animation-delay: 1.0s; }
    .title span:nth-child(12) { animation-delay: 1.1s; }
    .title span:nth-child(13) { animation-delay: 1.2s; }
    .title span:nth-child(14) { animation-delay: 1.3s; }
    .title span:nth-child(15) { animation-delay: 1.4s; }
    .title span:nth-child(16) { animation-delay: 1.5s; }
    .title span:nth-child(17) { animation-delay: 1.6s; }
    .title span:nth-child(18) { animation-delay: 1.7s; }
    .title span:nth-child(19) { animation-delay: 1.8s; }
    .title span:nth-child(20) { animation-delay: 1.9s; }
    .title span:nth-child(21) { animation-delay: 2.0s; }

    
    @keyframes cycle {
        0%, 100% { opacity: 1; } 
        50% { opacity: 0; } 
    }

   
    .title {
        animation: fadeIn 4s ease-out infinite, pauseAfterCycle 4.5s ease-in-out infinite;
    }

    
    @keyframes pauseAfterCycle {
        0% { opacity: 1; }
        50% { opacity: 1; }
        100% { opacity: 0; } 
    }
    </style>
    <h1 class="title">
        <span>📰</span><span>A</span><span>I</span><span class="space"> </span><span>N</span><span>e</span><span>w</span><span>s</span><span class="space"> </span><span>S</span><span>u</span><span>m</span><span>m</span><span>a</span><span>r</span><span>i</span><span>z</span><span>e</span><span>r</span>
    </h1>
    """, unsafe_allow_html=True)

# Fetch article text from URL
def fetch_article(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        st.error(f"Error fetching article from URL: {e}")
        return None

# Summarization function using Hugging Face
def huggingface(text):
    try:
        summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        st.error(f"Error with Hugging Face API: {e}")
        return "Summary could not be generated."

# Main function
def main():
    st.write("Enter a news article as text or URL to get a concise summary.")

    # Options in the sidebar
    st.sidebar.title("Options")
    option = st.sidebar.selectbox("Choose input type:", ["Text", "URL"])

    # Display input field
    if option == "Text":
        news_text = st.text_area("✍️ Enter the news text here", height=300)
    elif option == "URL":
        news_url = st.text_input("🔗 Enter the URL of the news article")
        news_text = fetch_article(news_url) if news_url else None

    if option == "URL" and news_text:
        st.write("**Fetched Article Preview:**")
        st.write(news_text[:500] + ("..." if len(news_text) > 500 else ""))  
    # Summarize button
    if st.button("💡 Summarize"):
        if news_text:
            cleaned_text = re.sub(r"\s+", " ", news_text.strip())[:3000]  
            with st.spinner("Summarizing... Please wait."):
                summary = huggingface(cleaned_text)

            st.subheader("Summary")
            st.write(summary)
        else:
            st.warning("Please enter some text or a URL.")

if __name__ == "__main__":
    main()
