import streamlit as st
from newspaper import Article
import re
from transformers import pipeline

# initialize pipeline
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# CSS
st.markdown("""
    <style>
    .main {
        background-color: #f4f4f8;
        color: #333333;
    }
    h1 {
        color: #2e86de;
    }
    </style>
    """, unsafe_allow_html=True)

# fetch article text from URL
def fetch_article(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        st.error(f"Error fetching article from URL: {e}")
        return None

def huggingface(text):
    try:
        summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        st.error(f"Error with Hugging Face API: {e}")
        return "Summary could not be generated."

# main function
def main():
    st.title("📰 AI News Summarizer")
    st.write("Enter a news article as text or URL to get a concise summary.")

    # option
    st.sidebar.title("Options")
    option = st.sidebar.selectbox("Choose input type:", ["Text", "URL"])

    # display input field
    if option == "Text":
        news_text = st.text_area("✍️ Enter the news text here", height=300)
    elif option == "URL":
        news_url = st.text_input("🔗 Enter the URL of the news article")
        news_text = fetch_article(news_url) if news_url else None

    if option == "URL" and news_text:
        st.write("**Fetched Article Preview:**")
        st.write(news_text[:500] + ("..." if len(news_text) > 500 else ""))  # Display first 500 characters of the article

    # button
    if st.button("💡 Summarize"):
        cleaned_text = re.sub(r"\s+", " ", news_text.strip())[:3000]  # clean and truncate text to 3000 characters
        with st.spinner("Summarizing... Please wait."):
            summary = huggingface(cleaned_text)
                
        st.subheader("Summary")
        st.write(summary)

if __name__ == "__main__":
    main()
