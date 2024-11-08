 AI News Summarizer

An AI-powered news summarizer that uses the Gemini API to summarize articles. The application processes the text from news articles and generates concise summaries for the user to read quickly and efficiently.

 Features
- Summarizes news articles using advanced AI techniques.
- Displays summarized content in an easy-to-read format.
- Built using Python, Streamlit, and the Gemini API.

 Installation

Follow these steps to get the application up and running on your local machine:

 Prerequisites
- Python 3.10 or higher.
- pip (Python's package installer).

 Step 1: Clone the repository
```bash
git clone https://github.com/Mani1515/AI-News-Summarizer.git
```

Step 2: Navigate into the project directory
```bash
cd AI-News-Summarizer
```

 Step 3: Set up a virtual environment (optional but recommended)
```bash
python -m venv venv
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate
```

 Step 4: Install dependencies
```bash
pip install -r requirements.txt
```

 Step 5: Run the app
```bash
streamlit run app.py
```

The application should now be running locally. You can access it through your browser at `http://localhost:8501`.

 Dependencies
This project uses the following libraries:
- `newspaper3k`: To extract articles from news websites.
- `lxml`: XML parsing library, required by `newspaper3k`.
- `streamlit`: A framework for building web applications.

You can find all dependencies in the `requirements.txt` file.

License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

