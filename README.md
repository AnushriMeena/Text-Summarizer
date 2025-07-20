# Text Summarizer

A simple and elegant web app to summarize text using OpenAI's GPT-4o model. Paste your text or upload a `.txt` file, and get concise bullet-point summaries instantly.

## Features
- Summarize any text or uploaded `.txt` file
- Clean, modern UI with custom styling
- Uses OpenAI GPT-4o for high-quality summaries
- Bullet-point output for clarity

## Demo
![Screenshot](screenshot.png) <!-- Add a screenshot if available -->

## Getting Started

### Prerequisites
- Python 3.7+
- [pip](https://pip.pypa.io/en/stable/)
- An OpenAI API key ([get one here](https://platform.openai.com/account/api-keys))

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/text-summarizer.git
   cd text-summarizer
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up your OpenAI API key:**
   - Create a `.env` file in the project root:
     ```env
     OPENAI_API_KEY=your_openai_api_key_here
     ```

### Running the App
```bash
streamlit run updatedTS.py
```

- Open the provided local URL in your browser.
- Enter text or upload a `.txt` file, then click **Summarize**.

## File Structure
- `updatedTS.py` – Main Streamlit app
- `textsummarizer.py` – (Legacy/alternate script)
- `.env` – Your OpenAI API key (not included in repo)

## Deployment
You can deploy this app on [Streamlit Cloud](https://streamlit.io/cloud) or any platform that supports Streamlit.

## License
[MIT](LICENSE)

## Acknowledgments
- [OpenAI](https://openai.com/)
- [Streamlit](https://streamlit.io/) 